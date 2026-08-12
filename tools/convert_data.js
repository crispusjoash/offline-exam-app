import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SRC_DATA_DIR = path.join(__dirname, '../src/data');
const OUT_DATA_DIR = path.join(__dirname, '../public/data');

async function main() {
  await fs.mkdir(OUT_DATA_DIR, { recursive: true });

  const files = await fs.readdir(SRC_DATA_DIR);
  
  for (const file of files) {
    if (file.endsWith('.js') && !file.includes('pastPapers') && !file.includes('pastPapersMeta')) {
      const filePath = path.join(SRC_DATA_DIR, file);
      
      try {
        // Dynamic import
        const module = await import(`file://${filePath}`);
        
        // Find the exported object (it's the only key usually)
        const exportKeys = Object.keys(module);
        if (exportKeys.length === 0) continue;
        
        const data = module[exportKeys[0]];
        const jsonContent = JSON.stringify(data, null, 2);
        
        const outFileName = file.replace('.js', '.json');
        const outFilePath = path.join(OUT_DATA_DIR, outFileName);
        
        await fs.writeFile(outFilePath, jsonContent, 'utf-8');
        console.log(`Converted ${file} -> ${outFileName}`);
      } catch (err) {
        console.error(`Failed to convert ${file}:`, err);
      }
    }
  }
}

main().catch(console.error);
