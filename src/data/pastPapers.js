import { PAST_PAPERS_META, PAPER_FILE_MAP } from './pastPapersMeta.js';
import { NativeEngine } from '../services/NativeEngine.js';

export const PAST_PAPERS = PAST_PAPERS_META;

export async function loadPaper(paperId) {
  const mapEntry = PAPER_FILE_MAP[paperId];
  if (!mapEntry) {
    throw new Error(`Paper ID ${paperId} not found in metadata.`);
  }
  
  const { fileName } = mapEntry;
  
  try {
    const data = await NativeEngine.getExamPaper(paperId, fileName);
    return data;
  } catch (error) {
    console.error(`Error loading paper via NativeEngine: ${fileName}`, error);
    throw error;
  }
}
