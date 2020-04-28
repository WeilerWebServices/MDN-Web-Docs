
function render(dataOrString, renderer, configuration) {

    /* Convert a string to the BCD data */
    let data = undefined;
    if (typeof dataOrString === 'string' || dataOrString instanceof String) {
        const dataParts = dataOrString.split('.');
        data = require('mdn-browser-compat-data');
        dataParts.forEach((elem) => {
            if (!data.hasOwnProperty(elem)) {
                throw new Error(`Unable to find data for "${dataOrString}" at "${elem}".`);
            }
            data = data[elem];
        });
    } else {
        data = dataOrString;
    }
    return renderer(data, configuration);
}

function usage() {
    const usageString = `Render a feature as an HTML table.

Usage:
 npm run render <featurePath> [depth] [aggregateMode]

Options:

 featurePath: Dotted path to feature
 depth: Traversal depth

Examples:

 npm run render webextensions.api.alarms
 npm run --silent render webextensions.api.alarms > test.html
 npm run render http.status.404
 npm run render webextensions.api.alarms 3
`;
    console.log(usageString);
}


function main() {
    const renderers = require('../src/renderers/index.js');
    const query = process.argv[2];
    const depth = process.argv[3] || 1;

    if (query === undefined) {
        usage();
        process.exit(0);
    }

    const html = render(
        query,
        renderers.mdnFeatureTable,
        {
            'query': query,
            'depth': depth,
        });
    console.log(html);
}

module.exports = render;
if (require.main === module) main();
