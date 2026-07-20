import fs from 'fs';
import { PAST_PAPERS } from './src/data/pastPapers.js';

let imports = '';
let arrayItems = '';

for (const paper of PAST_PAPERS.KPSEA) {
  const id = paper.id;
  // create variable name, e.g., kpsea-kiswahili-2023 -> kpseaKiswahili2023
  const varName = id.replace(/-([a-z0-9])/g, g => g[1].toUpperCase());
  
  const content = `export const ${varName} = ${JSON.stringify(paper, null, 2)};`;
  fs.writeFileSync(`./src/data/${id}.js`, content, 'utf8');
  
  imports += `import { ${varName} } from './${id}.js';\n`;
  arrayItems += `    ${varName},\n`;
}

const mainContent = `${imports}
export const PAST_PAPERS = {
  KPSEA: [
${arrayItems}  ]
};
`;

fs.writeFileSync('./src/data/pastPapers.js', mainContent, 'utf8');
console.log('Split complete!');
