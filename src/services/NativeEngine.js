import { Capacitor } from '@capacitor/core';

export const NativeEngine = {
  async getExamPaper(paperId, fileName) {
    const platform = Capacitor.getPlatform();
    
    // Convert .js filename to .json
    const jsonFileName = fileName.replace('.js', '.json');
    
    // In actual app we'll implement Android/Electron bridges, but for now we'll rely on fetch for web
    // Note: window.electronAPI would be the IPC bridge for electron
    
    if (window.electronAPI) {
        // C++ IPC logic goes here
        try {
            return await window.electronAPI.getExamPaper(jsonFileName);
        } catch(e) {
            console.error("Electron IPC failed", e);
            throw e;
        }
    } else if (platform === 'android') {
        // Java plugin logic goes here
        try {
            const { NativeData } = Capacitor.Plugins;
            const { data } = await NativeData.getPaper({ file: jsonFileName });
            return JSON.parse(data);
        } catch(e) {
            console.error("Capacitor Java Plugin failed", e);
            throw e;
        }
    }

    // Web Fallback
    try {
      const response = await fetch(`/data/${jsonFileName}`);
      if (!response.ok) throw new Error(`Failed to fetch /data/${jsonFileName}`);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Web Fallback Error:', error);
      throw error;
    }
  }
};
