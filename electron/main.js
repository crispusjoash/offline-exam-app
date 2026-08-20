"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const electron_1 = require("electron");
const capacitor_electron_1 = require("@capawesome/capacitor-electron");
const path_1 = __importDefault(require("path"));
const capacitor_electron_config_1 = __importDefault(require("./capacitor.electron.config"));
const fs_1 = __importDefault(require("fs"));
electron_1.app.whenReady().then(() => {
    // Inject our custom preload script for IPC alongside Capacitor's
    electron_1.session.defaultSession.setPreloads([
        path_1.default.join(__dirname, 'preload.js')
    ]);
    // Register IPC handler to call native JS file system
    electron_1.ipcMain.handle('get-exam-paper', async (event, fileName) => {
        const filePath = path_1.default.join(electron_1.app.getAppPath(), 'app', 'data', fileName);
        try {
            const rawJsonString = fs_1.default.readFileSync(filePath, 'utf-8');
            return JSON.parse(rawJsonString);
        }
        catch (err) {
            console.error("File Read Error:", err);
            throw err;
        }
    });
});
(0, capacitor_electron_1.createCapacitorElectronApp)(capacitor_electron_config_1.default);
