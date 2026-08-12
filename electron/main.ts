import { app, ipcMain, session } from 'electron';
import { createCapacitorElectronApp } from '@capawesome/capacitor-electron';
import path from 'path';

import config from './capacitor.electron.config';

// Load the C++ Addon (will fail gracefully if not compiled yet)
let dataEngine;
try {
  dataEngine = require('./build/Release/data_engine.node');
} catch (e) {
  console.warn("C++ Data Engine addon not found. Did you run node-gyp rebuild?");
}

app.whenReady().then(() => {
  // Inject our custom preload script for IPC alongside Capacitor's
  session.defaultSession.setPreloads([
    path.join(__dirname, 'preload.js')
  ]);

  // Register IPC handler to call C++ engine
  ipcMain.handle('get-exam-paper', async (event, fileName) => {
    if (!dataEngine) {
      throw new Error("Native C++ engine is not compiled. Please install VS Build Tools.");
    }
    const filePath = path.join(app.getAppPath(), 'app', 'data', fileName);
    try {
      const rawJsonString = dataEngine.getExamPaper(filePath);
      return JSON.parse(rawJsonString);
    } catch (err) {
      console.error("C++ Engine Error:", err);
      throw err;
    }
  });

  createCapacitorElectronApp(config);
});
