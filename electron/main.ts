import { app, ipcMain, BrowserWindow, Menu, session } from 'electron';
import { createCapacitorElectronApp, defineConfig } from '@capawesome/capacitor-electron';
import path from 'path';
import fs from 'fs';

// Remove the default application menu (File, Edit, View, Window)
Menu.setApplicationMenu(null);

// ─── CRITICAL: Register preload BEFORE createCapacitorElectronApp ───
// app.on('ready', ...) fires synchronously during the ready event,
// before the Promise-based app.whenReady().then() microtasks.
// This guarantees our preload.js is injected BEFORE the window is created.
app.on('ready', () => {
  const existing = session.defaultSession.getPreloads();
  session.defaultSession.setPreloads([
    ...existing,
    path.join(__dirname, 'preload.js'),
  ]);
});

// IPC: exam paper loader
ipcMain.handle('get-exam-paper', async (_event, fileName: string) => {
  const filePath = path.join(app.getAppPath(), 'app', 'data', fileName);
  try {
    const rawJsonString = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(rawJsonString);
  } catch (err) {
    console.error('File Read Error:', err);
    throw err;
  }
});

// IPC: window controls
ipcMain.handle('window-minimize', (_event) => {
  BrowserWindow.fromWebContents(_event.sender)?.minimize();
});

ipcMain.handle('window-maximize', (_event) => {
  const win = BrowserWindow.fromWebContents(_event.sender);
  if (!win) return false;
  if (win.isMaximized()) {
    win.unmaximize();
    return false;
  } else {
    win.maximize();
    return true;
  }
});

ipcMain.handle('window-close', (_event) => {
  BrowserWindow.fromWebContents(_event.sender)?.close();
});

ipcMain.handle('window-is-maximized', (_event) => {
  return BrowserWindow.fromWebContents(_event.sender)?.isMaximized() ?? false;
});

// Create the Capacitor Electron app — called AFTER app.on('ready', ...) is registered
createCapacitorElectronApp(defineConfig({
  window: {
    width: 1280,
    height: 800,
    minWidth: 1024,
    minHeight: 700,
    show: false,
    frame: false,
    titleBarStyle: 'hidden',
  } as any,
  hooks: {
    onWindowCreated: async (win) => {
      win.setMenuBarVisibility(false);
      win.setAutoHideMenuBar(true);
      win.maximize();
      win.show();
      win.on('maximize', () => win.webContents.send('window-maximized', true));
      win.on('unmaximize', () => win.webContents.send('window-maximized', false));
    },
  },
}));
