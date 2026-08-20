import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('electronAPI', {
  getExamPaper: (fileName: string) => ipcRenderer.invoke('get-exam-paper', fileName),
  // Window controls
  minimize: () => ipcRenderer.invoke('window-minimize'),
  maximize: () => ipcRenderer.invoke('window-maximize'),
  close: () => ipcRenderer.invoke('window-close'),
  isMaximized: () => ipcRenderer.invoke('window-is-maximized'),
  onMaximizeChange: (cb: (isMax: boolean) => void) => {
    ipcRenderer.on('window-maximized', (_e, isMax) => cb(isMax));
  },
});
