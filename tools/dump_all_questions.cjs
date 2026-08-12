const fs = require('fs');
const path = require('path');

const files = [
  'src/data/kpsea-science-2023.js',
  'src/data/kpsea-english-2023.js',
  'src/data/kpsea-kiswahili-2023.js',
  'src/data/kpsea-sst-parta-2023.js',
  'src/data/kpsea-sst-cre-2023.js',
  'src/data/kpsea-sst-ire-2023.js',
  'src/data/kpsea-sst-hre-2023.js',
];

const result = {};

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  // Remove "export const kpsea... = "
  const eqIdx = content.indexOf('=');
  const jsonText = content.substring(eqIdx + 1).trim().replace(/;$/, '');
  
  // Use eval or Function to get the JS object
  try {
    const data = eval('(' + jsonText + ')');
    result[data.id] = data;
    console.log(`Loaded ${data.id}: ${data.sectionA ? data.sectionA.length : 0} questions`);
  } catch (e) {
    console.error(`Error parsing ${file}:`, e.message);
  }
});

fs.writeFileSync('all_non_math_questions.json', JSON.stringify(result, null, 2));
console.log('Saved all questions to all_non_math_questions.json');
