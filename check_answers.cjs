const fs = require('fs');

const content = fs.readFileSync('src/data/pastPapers.js', 'utf8');

// Match all question objects roughly.
const qMatches = content.match(/id:\s*"q\d+".*?options:\s*\[.*?\]/gs);

const correctAnswersScheme = {
  1: 'C', 2: 'B', 3: 'C', 4: 'D', 5: 'D',
  6: 'C', 7: 'A', 8: 'D', 9: 'B', 10: 'D',
  11: 'A', 12: 'D', 13: 'A', 14: 'B', 15: 'C',
  16: 'A', 17: 'A', 18: 'C', 19: 'C', 20: 'A',
  21: 'D', 22: 'C', 23: 'D', 24: 'D', 25: 'C',
  26: 'C', 27: 'B', 28: 'A', 29: 'C', 30: 'D'
};

const letters = ['A', 'B', 'C', 'D'];
let mismatches = [];

if (qMatches) {
  qMatches.forEach(qBlock => {
    const idMatch = qBlock.match(/id:\s*"q(\d+)"/);
    if (!idMatch) return;
    const qNum = parseInt(idMatch[1]);
    
    // Extract options array content
    const optionsMatch = qBlock.match(/options:\s*\[(.*?)\]/s);
    if (!optionsMatch) return;
    const optionsStr = optionsMatch[1];
    
    // Find options with isCorrect
    const optionLines = optionsStr.split('}').filter(l => l.includes('text:'));
    let correctIdx = -1;
    optionLines.forEach((line, idx) => {
      if (line.includes('isCorrect: true')) {
        correctIdx = idx;
      }
    });
    
    if (correctIdx !== -1) {
      const actualLetter = letters[correctIdx];
      const expectedLetter = correctAnswersScheme[qNum];
      if (actualLetter !== expectedLetter) {
        mismatches.push(`Q${qNum}: Expected ${expectedLetter}, but got ${actualLetter}`);
      }
    }
  });
}

if (mismatches.length === 0) {
  console.log("All answers match the marking scheme perfectly!");
} else {
  console.log("Mismatches found:");
  mismatches.forEach(m => console.log(m));
}
