import React, { useEffect } from 'react';
import { HashRouter, Routes, Route, Navigate, useNavigate, useLocation } from 'react-router-dom';
import { App as CapacitorApp } from '@capacitor/app';
import { Dialog } from '@capacitor/dialog';
import { AppShell } from './components/AppShell';
import { MainPortal } from './views/MainPortal';
import { YearSelector } from './views/YearSelector';
import { PaperSelector } from './views/PaperSelector';
import { ExamSession } from './views/ExamSession';
import { SectionAReview } from './views/SectionAReview';
import { SectionBRunner } from './views/SectionBRunner';
import { FinalResults } from './views/FinalResults';

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
  return (
    <HashRouter>
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
        <Route path="/exam/:portal/:paperId" element={<ExamSession />} />
        <Route path="/exam/:portal/:paperId/sectionAReview" element={<SectionAReview />} />
        <Route path="/exam/:portal/:paperId/sectionB" element={<SectionBRunner />} />
        <Route path="/exam/:portal/:paperId/results" element={<FinalResults />} />

        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </HashRouter>
  );
}

export default App;
