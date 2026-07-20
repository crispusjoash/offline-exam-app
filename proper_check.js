import { PAST_PAPERS } from './src/data/pastPapers.js';

const correctAnswersScheme = {
  1: 'C', 2: 'B', 3: 'C', 4: 'D', 5: 'D',
  6: 'C', 7: 'A', 8: 'D', 9: 'B', 10: 'D',
  11: 'A', 12: 'D', 13: 'A', 14: 'B', 15: 'C',
  16: 'A', 17: 'A', 18: 'C', 19: 'C', 20: 'A',
  21: 'D', 22: 'C', 23: 'D', 24: 'D', 25: 'C',
  26: 'C', 27: 'B', 28: 'A', 29: 'C', 30: 'D'
};

const letters = ['A', 'B', 'C', 'D'];
const paper = PAST_PAPERS.KPSEA[0]; // First paper
let mismatches = [];

paper.sectionA.forEach(q => {
  const correctIdx = q.options.findIndex(opt => opt.isCorrect);
  const actualLetter = letters[correctIdx];
  const expectedLetter = correctAnswersScheme[q.questionNumber];
  
  if (actualLetter !== expectedLetter) {
    mismatches.push(`Q${q.questionNumber}: Expected ${expectedLetter}, but got ${actualLetter}`);
  }
});

if (mismatches.length === 0) {
  console.log("SUCCESS: All 30 answers match the marking scheme perfectly!");
} else {
  console.log("MISMATCHES FOUND:");
  mismatches.forEach(m => console.log(m));
}
