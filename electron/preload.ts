import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('electronAPI', {
  getExamPaper: (fileName) => ipcRenderer.invoke('get-exam-paper', fileName)
});
