'use strict';
const path = require('path');
const compareVersions = require('compare-versions');
const chalk = require('chalk');

/**
 * @typedef {import('../../types').CompatStatement} CompatStatement
 * @typedef {import('../../types').Identifier} Identifier
 * @typedef {import('../../types').IdentifierMeta} IdentifierMeta
 * @typedef {import('../../types').PrimaryIdentifier} PrimaryIdentifier
 * @typedef {import('../../types').SimpleSupportStatement} SimpleSupportStatement
 * @typedef {import('../../types').SupportStatement} SupportStatement
 * @typedef {import('../../types').VersionValue} VersionValue
 *
 * @typedef {'unsupported' | 'support_unknown' | 'subfeature_earlier_implementation'} ErrorType
 *
 * @typedef {object} ConsistencyError
 * @property {string} feature
 * @property {string[]} path
 * @property {FeatureError[]} errors
 *
 * @typedef {object} FeatureError
 * @property {ErrorType} errortype
 * @property {string} browser
 * @property {VersionValue} parent_value
 * @property {[string, VersionValue][]} subfeatures
 */

/**
 * Consistency check.
 *
 * This checker aims at improving data quality
 * by detecting inconsistent information.
 */
class ConsistencyChecker {
  /**
   * @param {Identifier} data
   * @return {ConsistencyError[]}
   */
  check(data) {
    return this.checkSubfeatures(data);
  }

  /**
   * @param {Identifier} data
   * @param {string[]} [path]
   * @return {ConsistencyError[]}
   */
  checkSubfeatures(data, path = []) {
    /** @type {ConsistencyError[]} */
    let allErrors = [];

    // Check this feature.
    if (this.isFeature(data)) {
      const feature = path.length ? path[path.length - 1] : 'ROOT';

      const errors = this.checkFeature(data);

      if (errors.length) {
        allErrors.push({
          feature,
          path,
          errors,
        });
      }
    }

    // Check sub-features.
    const keys = Object.keys(data).filter(key => key != '__compat');
    keys.forEach(key => {
      allErrors = [
        ...allErrors,
        ...this.checkSubfeatures(data[key], [...path, key]),
      ];
    });

    return allErrors;
  }

  /**
   * @param {PrimaryIdentifier & Required<IdentifierMeta>} data
   * @return {FeatureError[]}
   */
  checkFeature(data) {
    /** @type {FeatureError[]} */
    let errors = [];

    const subfeatures = Object.keys(data).filter(key =>
      this.isFeature(data[key]),
    );

    // Test whether sub-features are supported when basic support is not implemented
    // For all unsupported browsers (basic support == false), sub-features should be set to false
    const unsupportedInParent = this.extractUnsupportedBrowsers(data.__compat);
    /** @type {Partial<Record<string, [string, VersionValue][]>>} */
    var inconsistentSubfeaturesByBrowser = {};

    subfeatures.forEach(subfeature => {
      const unsupportedInChild = this.extractUnsupportedBrowsers(
        data[subfeature].__compat,
      );

      const browsers = unsupportedInParent.filter(
        x => !unsupportedInChild.includes(x),
      );

      browsers.forEach(browser => {
        inconsistentSubfeaturesByBrowser[browser] =
          inconsistentSubfeaturesByBrowser[browser] || [];
        const subfeature_value =
          data[subfeature].__compat.support[browser].version_added;
        inconsistentSubfeaturesByBrowser[browser].push([
          subfeature,
          subfeature_value,
        ]);
      });
    });

    // Add errors
    Object.keys(inconsistentSubfeaturesByBrowser).forEach(browser => {
      const subfeatures = inconsistentSubfeaturesByBrowser[browser];
      const errortype = 'unsupported';
      const parent_value = data.__compat.support[browser].version_added;

      errors.push({
        errortype,
        browser,
        parent_value,
        subfeatures,
      });
    });

    // Test whether sub-features are supported when basic support is not implemented
    // For all unsupported browsers (basic support == false), sub-features should be set to false
    const supportUnknownInParent = this.extractSupportUnknownBrowsers(
      data.__compat,
    );
    inconsistentSubfeaturesByBrowser = {};

    subfeatures.forEach(subfeature => {
      const supportUnknownInChild = this.extractSupportNotTrueBrowsers(
        data[subfeature].__compat,
      );

      const browsers = supportUnknownInParent.filter(
        x => !supportUnknownInChild.includes(x),
      );

      browsers.forEach(browser => {
        inconsistentSubfeaturesByBrowser[browser] =
          inconsistentSubfeaturesByBrowser[browser] || [];
        const subfeature_value =
          data[subfeature].__compat.support[browser].version_added;
        inconsistentSubfeaturesByBrowser[browser].push([
          subfeature,
          subfeature_value,
        ]);
      });
    });

    // Add errors
    Object.keys(inconsistentSubfeaturesByBrowser).forEach(browser => {
      const subfeatures = inconsistentSubfeaturesByBrowser[browser];
      const errortype = 'support_unknown';
      const parent_value = data.__compat.support[browser].version_added;

      errors.push({
        errortype,
        browser,
        parent_value,
        subfeatures,
      });
    });

    // Test whether sub-features are supported at an earlier version than basic support
    const supportInParent = this.extractSupportedBrowsersWithVersion(
      data.__compat,
    );
    inconsistentSubfeaturesByBrowser = {};

    subfeatures.forEach(subfeature => {
      supportInParent.forEach(browser => {
        if (
          data[subfeature].__compat.support[browser] != undefined &&
          this.isVersionAddedGreater(
            data[subfeature].__compat.support[browser],
            data.__compat.support[browser],
          )
        ) {
          inconsistentSubfeaturesByBrowser[browser] =
            inconsistentSubfeaturesByBrowser[browser] || [];
          const subfeature_value =
            data[subfeature].__compat.support[browser].version_added;
          inconsistentSubfeaturesByBrowser[browser].push([
            subfeature,
            subfeature_value,
          ]);
        }
      });
    });

    // Add errors
    Object.keys(inconsistentSubfeaturesByBrowser).forEach(browser => {
      const subfeatures = inconsistentSubfeaturesByBrowser[browser];
      const errortype = 'subfeature_earlier_implementation';
      const parent_value = data.__compat.support[browser].version_added;

      errors.push({
        errortype,
        browser,
        parent_value,
        subfeatures,
      });
    });

    return errors;
  }

  /**
   * @param {Identifier} data
   * @return {data is Required<IdentifierMeta>}
   */
  isFeature(data) {
    return '__compat' in data;
  }

  /**
   * @param {CompatStatement} compatData
   * @return {string[]}
   */
  extractUnsupportedBrowsers(compatData) {
    return this.extractBrowsers(
      compatData,
      data =>
        data.version_added === false ||
        (typeof data.version_removed !== 'undefined' &&
          data.version_removed !== false),
    );
  }

  /**
   * @param {CompatStatement} compatData
   * @return {string[]}
   */
  extractSupportUnknownBrowsers(compatData) {
    return this.extractBrowsers(
      compatData,
      data => data.version_added === null,
    );
  }

  /**
   * @param {CompatStatement} compatData
   * @return {string[]}
   */
  extractSupportNotTrueBrowsers(compatData) {
    return this.extractBrowsers(
      compatData,
      data =>
        data.version_added === false ||
        data.version_added === null ||
        (typeof data.version_removed !== 'undefined' &&
          data.version_removed !== false),
    );
  }
  /**
   * @param {CompatStatement} compatData
   * @return {string[]}
   */
  extractSupportedBrowsersWithVersion(compatData) {
    return this.extractBrowsers(
      compatData,
      data => typeof data.version_added === 'string',
    );
  }

  /**
   * @param {SupportStatement} compatData
   * @return {string | null}
   */
  getVersionAdded(compatData) {
    /** @type {string | null} */
    var version_added = null;

    if (typeof compatData.version_added === 'string')
      return compatData.version_added;

    if (compatData.constructor === Array) {
      for (var i = compatData.length - 1; i >= 0; i--) {
        var va = compatData[i].version_added;
        if (
          typeof va === 'string' &&
          (version_added == null ||
            (typeof version_added === 'string' &&
              compareVersions.compare(
                version_added.replace('≤', ''),
                va.replace('≤', ''),
                '>',
              )))
        ) {
          version_added = va;
        }
      }
    }

    return version_added;
  }

  /**
   * @param {SupportStatement} a
   * @param {SupportStatement} b
   * @return {boolean}
   */
  isVersionAddedGreater(a, b) {
    var a_version_added = this.getVersionAdded(a);
    var b_version_added = this.getVersionAdded(b);

    if (
      typeof a_version_added === 'string' &&
      typeof b_version_added === 'string'
    ) {
      if (a_version_added.startsWith('≤') || b_version_added.startsWith('≤')) {
        return false;
      }
      return compareVersions.compare(a_version_added, b_version_added, '<');
    }

    return false;
  }

  /**
   *
   * @param {CompatStatement} compatData
   * @param {(browserData: SimpleSupportStatement) => boolean} callback
   * @return {string[]}
   */
  extractBrowsers(compatData, callback) {
    return Object.keys(compatData.support).filter(browser => {
      const browserData = compatData.support[browser];

      if (Array.isArray(browserData)) {
        return browserData.every(callback);
      } else if (typeof browserData === 'object') {
        return callback(browserData);
      } else {
        return false;
      }
    });
  }
}

/**
 * @param {string} filename
 */
function testConsistency(filename) {
  /** @type {Identifier} */
  let data = require(filename);

  const checker = new ConsistencyChecker();
  const errors = checker.check(data);

  if (errors.length) {
    console.error(
      chalk`{red   Consistency - {bold ${errors.length} }${
        errors.length === 1 ? 'error' : 'errors'
      }:}`,
    );
    errors.forEach(({ feature, path, errors }) => {
      console.error(
        chalk`{red   → {bold ${errors.length}} × {bold ${feature}} [${path.join(
          '.',
        )}]: }`,
      );
      errors.forEach(({ errortype, browser, parent_value, subfeatures }) => {
        if (errortype == 'unsupported') {
          console.error(
            chalk`{red     → No support in {bold ${browser}}, but support is declared in the following sub-feature(s):}`,
          );
        } else if (errortype == 'support_unknown') {
          console.error(
            chalk`{red     → Unknown support in parent for {bold ${browser}}, but support is declared in the following sub-feature(s):}`,
          );
        } else if (errortype == 'subfeature_earlier_implementation') {
          console.error(
            chalk`{red     → Basic support in {bold ${browser}} was declared implemented in a later version ({bold ${parent_value}}) than the following sub-feature(s):}`,
          );
        }

        subfeatures.forEach(subfeature => {
          console.error(
            chalk`{red       → {bold ${path.join('.')}.${subfeature[0]}}: ${
              subfeature[1] === undefined ? '[Array]' : subfeature[1]
            }}`,
          );
        });
      });
    });
    return true;
  }
  return false;
}

module.exports = testConsistency;
