let re = /[0-9]+/g;
let str = '2016-01-02|2019-03-07';
let result = re[Symbol.matchAll](str);

console.log(Array.from(result, x => x[0]));
// expected output: Array ["2016", "01", "02", "2019", "03", "07"]
