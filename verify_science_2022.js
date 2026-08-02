import { kpseaScience2022 } from './src/data/kpsea-science-2022.js';

if (kpseaScience2022 && kpseaScience2022.sectionA.length === 40) {
    console.log('Syntax is valid and exactly 40 questions were found!');
} else {
    console.error('Invalid structure or missing questions!');
}
