const assert = require('assert');
const path = require('path');
const { cleanPath } = require(path.join(__dirname, '../OpenInFinder.popclipext/open_finder.js'));

const tests = [
  ['/Users/sunda/Documents/POPCLIP/', '/Users/sunda/Documents/POPCLIP/'],
  ['"/Users/sunda/Documents/POPCLIP/"', '/Users/sunda/Documents/POPCLIP/'],
  ["'~/Documents/POPCLIP/'", '~/Documents/POPCLIP/'],
  ['file:///Users/sunda/Documents/POPCLIP/', '/Users/sunda/Documents/POPCLIP/'],
  ['~/Downloads', '~/Downloads'],
  ['/Library/Application\\ Support/PopClip', '/Library/Application Support/PopClip'],
  ['/Users/sunda/Documents/POPCLIP/.', '/Users/sunda/Documents/POPCLIP/.'],
  ['/Users/sunda/Documents/POPCLIP/,', '/Users/sunda/Documents/POPCLIP/'],
  ['“/Users/sunda/Documents/POPCLIP/”', '/Users/sunda/Documents/POPCLIP/'],
  ['<~/Documents/POPCLIP>', '~/Documents/POPCLIP'],
  ['`~/Documents/POPCLIP`', '~/Documents/POPCLIP']
];

for (const [input, expected] of tests) {
  const result = cleanPath(input);
  assert.strictEqual(result, expected, `Failed for input: ${input}`);
}

console.log(`All ${tests.length} JavaScript cleanPath tests passed!`);
