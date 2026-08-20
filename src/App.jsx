import React, { useEffect, createContext, useContext, useState } from 'react';
import { HashRouter, Routes, Route, Navigate, useNavigate, useLocation } from 'react-router-dom';
import { App as CapacitorApp } from '@capacitor/app';
import { Capacitor } from '@capacitor/core';
import { Dialog } from '@capacitor/dialog';
import { AppShell } from './components/AppShell';
import { MainPortal } from './views/MainPortal';
import { YearSelector } from './views/YearSelector';
import { PaperSelector } from './views/PaperSelector';
import { initDB } from './services/db';
import { ActivationLocker } from './components/ActivationLocker';
import { ElectronTitleBar } from './components/ElectronTitleBar';

const ExamSession = React.lazy(() => import('./views/ExamSession').then(m => ({ default: m.ExamSession })));
const SectionAReview = React.lazy(() => import('./views/SectionAReview').then(m => ({ default: m.SectionAReview })));
const SectionBRunner = React.lazy(() => import('./views/SectionBRunner').then(m => ({ default: m.SectionBRunner })));
const FinalResults = React.lazy(() => import('./views/FinalResults').then(m => ({ default: m.FinalResults })));

// ── Theme Context ─────────────────────────────────────────────────────────────
export const ThemeContext = createContext({ dark: false, toggleDark: () => {} });
export const useTheme = () => useContext(ThemeContext);

const ThemeProvider = ({ children }) => {
  const [dark, setDark] = useState(() => {
    try { return localStorage.getItem('cbc-theme') === 'dark'; }
    catch { return false; }
  });

  useEffect(() => {
    const root = document.documentElement;
    if (dark) {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
    try { localStorage.setItem('cbc-theme', dark ? 'dark' : 'light'); }
    catch { /* ignore */ }
  }, [dark]);

  const toggleDark = () => setDark(d => !d);

  return (
    <ThemeContext.Provider value={{ dark, toggleDark }}>
      {children}
    </ThemeContext.Provider>
  );
};

const BackButtonHandler = () => {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const listener = CapacitorApp.addListener('backButton', async () => {
      if (location.pathname === '/') {
        const { value } = await Dialog.confirm({
          title: 'Exit Application',
          message: 'Are you sure you want to exit the app?',
          okButtonTitle: 'Exit',
          cancelButtonTitle: 'Cancel'
        });
        if (value) {
          CapacitorApp.exitApp();
        }
      } else {
        navigate(-1);
      }
    });

    return () => {
      listener.then(l => l.remove());
    };
  }, [location, navigate]);

  return null;
};

function App() {
  const [dbReady, setDbReady] = React.useState(false);
  const [dbError, setDbError] = React.useState(null);

  useEffect(() => {
    initDB()
      .then(() => setDbReady(true))
      .catch(e => {
        console.error(e);
        setDbError(e.message || String(e));
      });
  }, []);

  if (dbError) return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', justifyContent: 'center', alignItems: 'center', fontFamily: 'Outfit, sans-serif', padding: '2rem', textAlign: 'center' }}>
      <h2 style={{ color: 'red' }}>Database Initialization Failed</h2>
      <p style={{ maxWidth: '600px', background: '#fee2e2', padding: '1rem', borderRadius: '8px', wordWrap: 'break-word' }}>{dbError}</p>
    </div>
  );

  if (!dbReady) return <div style={{ display: 'flex', height: '100vh', justifyContent: 'center', alignItems: 'center', fontFamily: 'Outfit, sans-serif' }}>Initializing System...</div>;

  const isElectron = Capacitor.getPlatform() === 'electron' || (typeof window !== 'undefined' && Boolean(window.electronAPI));

  return (
    <ThemeProvider>
      <HashRouter>
        <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
          {/* Custom premium title bar with sticky back button — only on Electron desktop (position:fixed) */}
          {isElectron && <ElectronTitleBar />}

          {/* App content — push down 40px on Electron to clear the fixed title bar */}
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', paddingTop: isElectron ? '40px' : '0' }}>
            <ActivationLocker>
              <BackButtonHandler />
              <Routes>
                {/* ── Browsing routes: wrapped in AppShell (sidebar visible) ── */}
                <Route
                  path="/"
                  element={
                    <AppShell>
                      <MainPortal />
                    </AppShell>
                  }
                />
                <Route
                  path="/papers/:portal"
                  element={
                    <AppShell>
                      <YearSelector />
                    </AppShell>
                  }
                />
                <Route
                  path="/papers/:portal/:year"
                  element={
                    <AppShell>
                      <PaperSelector />
                    </AppShell>
                  }
                />

                {/* ── Exam routes: full-screen, no sidebar ── */}
                <Route path="/exam/:portal/:paperId" element={<React.Suspense fallback={<div style={{ display: 'flex', height: '100vh', justifyContent: 'center', alignItems: 'center' }}>Loading...</div>}><ExamSession /></React.Suspense>} />
                <Route path="/exam/:portal/:paperId/sectionAReview" element={<React.Suspense fallback={<div style={{ display: 'flex', height: '100vh', justifyContent: 'center', alignItems: 'center' }}>Loading...</div>}><SectionAReview /></React.Suspense>} />
                <Route path="/exam/:portal/:paperId/sectionB" element={<React.Suspense fallback={<div style={{ display: 'flex', height: '100vh', justifyContent: 'center', alignItems: 'center' }}>Loading...</div>}><SectionBRunner /></React.Suspense>} />
                <Route path="/exam/:portal/:paperId/results" element={<React.Suspense fallback={<div style={{ display: 'flex', height: '100vh', justifyContent: 'center', alignItems: 'center' }}>Loading...</div>}><FinalResults /></React.Suspense>} />

                <Route path="*" element={<Navigate to="/" replace />} />
              </Routes>
            </ActivationLocker>
          </div>
        </div>
      </HashRouter>
    </ThemeProvider>
  );
}

export default App;
