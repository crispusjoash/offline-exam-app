import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const dataDir = path.join(__dirname, '../src/data');

async function extract() {
  const files = fs.readdirSync(dataDir).filter(f => f.endsWith('.js') && f !== 'pastPapers.js' && f !== 'pastPapersMeta.js');
  
  const metadata = {
    KPSEA: [],
    KJSEA: []
  };

  const fileMap = {};

  for (const file of files) {
    const filePath = path.join(dataDir, file);
    try {
      const module = await import(`file://${filePath}`);
      const exportName = Object.keys(module)[0];
      const paper = module[exportName];
      
      const meta = {
        id: paper.id,
        title: paper.title,
        subject: paper.subject,
        year: paper.year,
        isSubPaper: paper.isSubPaper || false,
        isParentPaper: paper.isParentPaper || false,
        durationMinutes: paper.durationMinutes,
        timeAllowed: paper.timeAllowed,
        exportName,
        fileName: file
      };
      
      if (file.startsWith('kpsea')) {
        metadata.KPSEA.push(meta);
      } else if (file.startsWith('kjsea')) {
        metadata.KJSEA.push(meta);
      }
      
      fileMap[paper.id] = { fileName: file, exportName };
    } catch (e) {
      console.error(`Error processing ${file}:`, e);
    }
  }

  // Sort them generally so order remains consistent
  const sortFn = (a, b) => a.id.localeCompare(b.id);
  metadata.KPSEA.sort(sortFn);
  metadata.KJSEA.sort(sortFn);

  const outFile = path.join(dataDir, 'pastPapersMeta.js');
  const code = `// GENERATED FILE - DO NOT EDIT MANUALLY
export const PAST_PAPERS_META = ${JSON.stringify(metadata, null, 2)};

export const PAPER_FILE_MAP = ${JSON.stringify(fileMap, null, 2)};
`;
  
  fs.writeFileSync(outFile, code);
  console.log('Successfully generated pastPapersMeta.js');
}

extract();
