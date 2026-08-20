/**
 * db.js — Smart storage abstraction
 *
 * On web (browser / dev server):  uses localStorage — fast, simple, no WASM issues
 * On native (Android / Electron): uses @capacitor-community/sqlite via Java/C++
 *
 * This is the recommended Capacitor pattern: gracefully degrade to localStorage
 * on web so the dev experience stays smooth, and enjoy native SQLite on device.
 */

import { Capacitor } from '@capacitor/core';

// ─── Web fallback (localStorage) ────────────────────────────────────────────

const webSave = (table, paperId, data) => {
  try {
    localStorage.setItem(`${table}_${paperId}`, JSON.stringify(data));
  } catch (e) {
    console.warn('[db.js] localStorage write failed:', e);
  }
};

const webLoad = (table, paperId) => {
  try {
    const raw = localStorage.getItem(`${table}_${paperId}`);
    return raw ? JSON.parse(raw) : null;
  } catch (e) {
    return null;
  }
};

// ─── Native SQLite (Android / Electron) ─────────────────────────────────────

let db = null;
let sqliteModule = null;

const initNativeDB = async () => {
  if (db) return db;
  try {
    const { CapacitorSQLite, SQLiteConnection } = await import('@capacitor-community/sqlite');
    sqliteModule = new SQLiteConnection(CapacitorSQLite);

    const ret = await sqliteModule.checkConnectionsConsistency();
    const isConn = (await sqliteModule.isConnection('cbc_offline_db', false)).result;

    if (ret.result && isConn) {
      db = await sqliteModule.retrieveConnection('cbc_offline_db', false);
    } else {
      db = await sqliteModule.createConnection('cbc_offline_db', false, 'no-encryption', 1, false);
    }

    await db.open();

    await db.execute(`
      CREATE TABLE IF NOT EXISTS exam_sessions (
        paperId TEXT PRIMARY KEY,
        sessionData TEXT NOT NULL
      );
      CREATE TABLE IF NOT EXISTS sectionb_sessions (
        paperId TEXT PRIMARY KEY,
        sessionData TEXT NOT NULL
      );
    `);

    console.log('[db.js] Native SQLite ready');
    return db;
  } catch (e) {
    console.error('[db.js] Native SQLite init error:', e);
    throw e;
  }
};

// ─── Public API ──────────────────────────────────────────────────────────────

export const initDB = async () => {
  const platform = Capacitor.getPlatform();
  console.log('[db.js] Platform:', platform);

  // On web AND electron: use localStorage (SQLite plugin not wired on Electron)
  if (platform === 'web' || platform === 'electron') {
    console.log('[db.js] Using localStorage for platform:', platform);
    return 'localStorage';
  }

  return initNativeDB();
};

export const saveSession = async (table, paperId, data) => {
  const platform = Capacitor.getPlatform();
  if (platform === 'web' || platform === 'electron' || !db) {
    webSave(table, paperId, data);
    return;
  }
  try {
    await db.run(
      `INSERT OR REPLACE INTO ${table} (paperId, sessionData) VALUES (?, ?)`,
      [paperId, JSON.stringify(data)]
    );
  } catch (e) {
    console.error('[db.js] saveSession error:', e);
    // Fallback
    webSave(table, paperId, data);
  }
};

export const loadSession = async (table, paperId) => {
  const platform = Capacitor.getPlatform();
  if (platform === 'web' || platform === 'electron' || !db) {
    return webLoad(table, paperId);
  }
  try {
    const res = await db.query(
      `SELECT sessionData FROM ${table} WHERE paperId = ?`,
      [paperId]
    );
    if (res.values && res.values.length > 0) {
      return JSON.parse(res.values[0].sessionData);
    }
  } catch (e) {
    console.error('[db.js] loadSession error:', e);
    return webLoad(table, paperId);
  }
  return null;
};
