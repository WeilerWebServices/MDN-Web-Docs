const path = require("path");

const sanitizeFilename = require("sanitize-filename");

function slugToFoldername(slug) {
  return (
    slug
      // We have slugs with these special characters that would be
      // removed by the sanitizeFilename() function. What might then
      // happen is that it leads to two *different slugs* becoming
      // *same* folder name.
      .replace(/\*/g, "_star_")
      .replace(/:/g, "_colon_")
      .replace(/\?/g, "_question_")

      .toLowerCase()
      .split("/")
      .map(sanitizeFilename)
      .join(path.sep)
  );
}

module.exports = {
  slugToFoldername,
};
