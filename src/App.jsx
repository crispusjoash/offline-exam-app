import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { MainPortal } from './views/MainPortal';
import { YearSelector } from './views/YearSelector';
import { PaperSelector } from './views/PaperSelector';
import { ExamSession } from './views/ExamSession';
import { SectionAReview } from './views/SectionAReview';
import { SectionBRunner } from './views/SectionBRunner';
import { FinalResults } from './views/FinalResults';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPortal />} />
        <Route path="/papers/:portal" element={<YearSelector />} />
        <Route path="/papers/:portal/:year" element={<PaperSelector />} />
        <Route path="/exam/:portal/:paperId" element={<ExamSession />} />
        <Route path="/exam/:portal/:paperId/sectionAReview" element={<SectionAReview />} />
        <Route path="/exam/:portal/:paperId/sectionB" element={<SectionBRunner />} />
        <Route path="/exam/:portal/:paperId/results" element={<FinalResults />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
