import { Capacitor } from '@capacitor/core';

export const NativeEngine = {
  async getExamPaper(paperId, fileName) {
    const platform = Capacitor.getPlatform();
    
    // Convert .js filename to .json (only if it actually ends with .js — not .json which contains .js)
    const jsonFileName = fileName.endsWith('.json') ? fileName : fileName.replace(/\.js$/, '.json');
    
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

    // Web Fallback with full debug logging
    try {
      const ts = Date.now();
      const url = `/data/${jsonFileName}?t=${ts}`;
      console.log('[NativeEngine] Fetching URL:', url);
      console.log('[NativeEngine] window.location.href:', window.location.href);
      const response = await fetch(url);
      console.log('[NativeEngine] Response status:', response.status);
      console.log('[NativeEngine] Content-Type:', response.headers.get('content-type'));
      const text = await response.text();
      console.log('[NativeEngine] Response body (first 200 chars):', text.substring(0, 200));
      if (!response.ok) throw new Error(`HTTP ${response.status} for ${url}`);
      try {
        return JSON.parse(text);
      } catch(parseErr) {
        throw new Error(`JSON parse failed for ${url}: ${parseErr.message}. Body starts with: ${text.substring(0, 80)}`);
      }
    } catch (error) {
      console.error('[NativeEngine] Web Fallback Error:', error);
      throw error;
    }
  }
};
