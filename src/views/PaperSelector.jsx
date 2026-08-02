import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { PAST_PAPERS } from '../data/pastPapers';
import { 
  ArrowLeft,
  Clock, 
  FileText, 
  Play, 
  Hash, 
  BookOpen, 
  ChevronRight, 
  X, 
  Calculator, 
  Languages, 
  Atom, 
  Globe2, 
  Sparkles,
  CheckCircle2
} from 'lucide-react';

export const PaperSelector = () => {
  const { portal, year } = useParams();
  const navigate = useNavigate();
  const allPortalPapers = PAST_PAPERS[portal] || [];
  
  // Filter out sub-papers so they only appear inside the customized parent selector
  const papers = allPortalPapers.filter(p => String(p.year) === String(year) && !p.isSubPaper);
  
  const isKPSEA = portal === 'KPSEA';
  const accentColor = isKPSEA ? '#2563eb' : '#7c3aed';
  const gradient = isKPSEA
    ? 'linear-gradient(135deg, #2563eb, #3b82f6)'
    : 'linear-gradient(135deg, #7c3aed, #db2777)';

  // Selection overlay modal states
  const [selectedParent, setSelectedParent] = React.useState(null);
  const [religionStep, setReligionStep] = React.useState(false);

  const handleSelectPaper = (paper) => {
    if (paper.isParentPaper) {
      setSelectedParent(paper);
      setReligionStep(false);
    } else {
      navigate(`/exam/${portal}/${paper.id}`);
    }
  };

  return (
    <div style={{ width: '100%', boxSizing: 'border-box' }}>
      <style>{`
        @keyframes modalSlideUp {
          from {
            opacity: 0;
            transform: translateY(20px) scale(0.98);
          }
          to {
            opacity: 1;
            transform: translateY(0) scale(1);
          }
        }
      `}</style>

      {/* ── Main Content Container ── */}
      <div style={{ padding: '1.5rem 1.75rem 3rem', maxWidth: '1100px', width: '100%', boxSizing: 'border-box' }}>

        {/* ── Compact Banner Header ── */}
        <div style={{
          background: isKPSEA 
            ? 'linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%)' 
            : 'linear-gradient(135deg, #4c1d95 0%, #7c3aed 100%)',
          borderRadius: '1.25rem',
          padding: '1.75rem 2rem',
          color: '#ffffff',
          position: 'relative',
          overflow: 'hidden',
          marginBottom: '2rem',
          boxShadow: `0 16px 36px -10px ${accentColor}40`,
        }}>
          <div style={{ position: 'relative', zIndex: 2 }}>
            <span style={{ 
              fontSize: '0.72rem', 
              fontWeight: '800', 
              letterSpacing: '0.1em', 
              textTransform: 'uppercase', 
              background: 'rgba(255, 255, 255, 0.15)',
              padding: '0.25rem 0.75rem',
              borderRadius: '9999px',
              border: '1px solid rgba(255, 255, 255, 0.25)',
              marginBottom: '0.65rem',
              display: 'inline-block',
            }}>
              {year} National Exam Papers
            </span>

            <h1 style={{ fontFamily: 'Outfit, sans-serif', fontSize: 'clamp(1.75rem, 3.5vw, 2.3rem)', fontWeight: '900', color: '#ffffff', marginBottom: '0.35rem' }}>
              Select Examination Subject
            </h1>

            <p style={{ color: 'rgba(255,255,255,0.85)', fontSize: '0.9rem', maxWidth: '540px' }}>
              Choose a subject below to start your timed practice exam with auto-grading.
            </p>
          </div>
        </div>

        {/* ── Subject Cards Grid ── */}
        {papers.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '4rem 1rem', background: '#ffffff', borderRadius: '1.25rem', border: '1px dashed #cbd5e1' }}>
            <BookOpen size={44} style={{ color: '#94a3b8', marginBottom: '0.75rem' }} />
            <h3 style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '700', fontSize: '1.1rem', color: '#0f172a' }}>No papers found</h3>
            <p style={{ fontSize: '0.85rem', color: '#64748b', marginTop: '0.25rem' }}>No past papers are listed for {portal} {year}.</p>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(290px, 1fr))', gap: '1.25rem' }}>
            {papers.map(paper => (
              <PaperCard
                key={paper.id}
                paper={paper}
                portal={portal}
                accentColor={accentColor}
                gradient={gradient}
                onSelect={() => handleSelectPaper(paper)}
              />
            ))}
          </div>
        )}
      </div>

      {/* ── Section Choice Overlay Modal ── */}
      {selectedParent && (
        <div style={{
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
          background: 'rgba(15, 23, 42, 0.55)',
          backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          zIndex: 100, padding: '1rem',
        }}>
          <div style={{
            background: '#ffffff',
            width: '100%', maxWidth: '520px',
            borderRadius: '1.5rem',
            boxShadow: '0 25px 50px -12px rgba(15, 23, 42, 0.25)',
            overflow: 'hidden',
            animation: 'modalSlideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards',
          }}>
            {/* Modal Header */}
            <div style={{
              padding: '1.25rem 1.5rem',
              background: '#f8fafc',
              borderBottom: '1px solid #e2e8f0',
              display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            }}>
              <div>
                <h2 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.2rem', fontWeight: '800', margin: 0, color: '#0f172a' }}>
                  {religionStep ? 'Select Religion Option' : 'Select Paper Section'}
                </h2>
                <p style={{ fontSize: '0.78rem', color: '#64748b', margin: '0.15rem 0 0 0', fontWeight: '500' }}>
                  {religionStep ? 'Choose your specific religious education paper' : 'This exam has core & optional religious sections.'}
                </p>
              </div>
              <button
                onClick={() => setSelectedParent(null)}
                style={{
                  background: '#e2e8f0', border: 'none',
                  width: '32px', height: '32px', borderRadius: '50%',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  cursor: 'pointer', color: '#475569',
                }}
              >
                <X size={16} />
              </button>
            </div>

            {/* Modal Content Options */}
            <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
              {!religionStep ? (
                <>
                  <SelectorOption
                    title="Part A: Social Studies & Creative Arts"
                    badgeText="Core Section"
                    badgeBg="#eff6ff"
                    badgeColor="#2563eb"
                    description="Covers geography, history, civics, and creative arts. Questions 1 to 35."
                    duration="100 min"
                    qsCount="35 Qs"
                    onClick={() => {
                      setSelectedParent(null);
                      navigate(`/exam/${portal}/kpsea-sst-parta-${selectedParent.year || '2023'}`);
                    }}
                  />

                  <SelectorOption
                    title="Part B: Religious Education"
                    badgeText="Optional Section"
                    badgeBg="#ecfdf5"
                    badgeColor="#059669"
                    description="Choose your religious education option (CRE, IRE, or HRE). Questions 36 to 50."
                    duration="30 min"
                    qsCount="15 Qs"
                    onClick={() => setReligionStep(true)}
                  />
                </>
              ) : (
                <>
                  <button
                    onClick={() => setReligionStep(false)}
                    style={{
                      display: 'inline-flex', alignItems: 'center', gap: '0.4rem',
                      background: 'none', border: 'none', color: '#2563eb',
                      cursor: 'pointer', fontSize: '0.85rem', fontWeight: '700',
                      alignSelf: 'flex-start', padding: '0.2rem 0',
                    }}
                  >
                    <ArrowLeft size={14} /> Back to paper sections
                  </button>

                  <SubSelectorOption
                    title="Christian Religious Education (CRE)"
                    subtitle="Part B · Questions 36 to 50"
                    onClick={() => {
                      setSelectedParent(null);
                      navigate(`/exam/${portal}/kpsea-sst-cre-${selectedParent.year || '2023'}`);
                    }}
                  />

                  <SubSelectorOption
                    title="Islamic Religious Education (IRE)"
                    subtitle="Part B · Questions 36 to 50"
                    onClick={() => {
                      setSelectedParent(null);
                      navigate(`/exam/${portal}/kpsea-sst-ire-${selectedParent.year || '2023'}`);
                    }}
                  />

                  <SubSelectorOption
                    title="Hindu Religious Education (HRE)"
                    subtitle="Part B · Questions 36 to 50"
                    onClick={() => {
                      setSelectedParent(null);
                      navigate(`/exam/${portal}/kpsea-sst-hre-${selectedParent.year || '2023'}`);
                    }}
                  />
                </>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

/* ── Custom Interactive Card Options for Modal ── */
const SelectorOption = ({ title, badgeText, badgeBg, badgeColor, description, duration, qsCount, onClick }) => {
  const [hov, setHov] = React.useState(false);
  return (
    <div
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      onClick={onClick}
      style={{
        border: `1.5px solid ${hov ? '#2563eb' : '#e2e8f0'}`,
        background: hov ? '#eff6ff50' : '#ffffff',
        borderRadius: '1rem', padding: '1.15rem',
        cursor: 'pointer', transition: 'all 0.2s ease',
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
      }}
    >
      <div style={{ flex: 1, paddingRight: '1rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.35rem', flexWrap: 'wrap' }}>
          {badgeText && (
            <span style={{ background: badgeBg, color: badgeColor, fontSize: '0.68rem', fontWeight: '800', padding: '0.15rem 0.45rem', borderRadius: '0.35rem', textTransform: 'uppercase' }}>{badgeText}</span>
          )}
          <h4 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1rem', fontWeight: '800', margin: 0, color: '#0f172a' }}>{title}</h4>
        </div>
        <p style={{ fontSize: '0.78rem', color: '#64748b', margin: 0, lineHeight: 1.4, fontWeight: '500' }}>
          {description}
        </p>
        <div style={{ display: 'flex', gap: '0.75rem', marginTop: '0.65rem', fontSize: '0.72rem', color: '#64748b', fontWeight: '600' }}>
          {duration && <span style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}><Clock size={12} /> {duration}</span>}
          {qsCount && <span style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}><Hash size={12} /> {qsCount}</span>}
        </div>
      </div>
      <ChevronRight size={18} color={hov ? '#2563eb' : '#94a3b8'} />
    </div>
  );
};

const SubSelectorOption = ({ title, subtitle, onClick }) => {
  const [hov, setHov] = React.useState(false);
  return (
    <div
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      onClick={onClick}
      style={{
        border: `1.5px solid ${hov ? '#2563eb' : '#e2e8f0'}`,
        background: hov ? '#eff6ff50' : '#ffffff',
        borderRadius: '0.75rem', padding: '0.85rem 1.15rem',
        cursor: 'pointer', transition: 'all 0.2s ease',
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
      }}
    >
      <div>
        <h5 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '0.95rem', fontWeight: '800', margin: 0, color: '#0f172a' }}>{title}</h5>
        <p style={{ fontSize: '0.75rem', color: '#64748b', margin: '0.15rem 0 0 0', fontWeight: '500' }}>{subtitle}</p>
      </div>
      <ChevronRight size={16} color={hov ? '#2563eb' : '#94a3b8'} />
    </div>
  );
};

/* ── Standard Subject Card Component ── */
const PaperCard = ({ paper, portal, accentColor, gradient, onSelect }) => {
  const [hov, setHov] = React.useState(false);
  const isKPSEA = portal === 'KPSEA';

  // Calculate length based on sectionA content if not a parent paper
  const questionCount = paper.isParentPaper ? 50 : (paper.sectionA?.length || 0);

  // Pick appropriate icon based on subject
  const getSubjectIcon = (subName) => {
    const s = (subName || '').toLowerCase();
    if (s.includes('math')) return <Calculator size={22} />;
    if (s.includes('kiswahili') || s.includes('english')) return <Languages size={22} />;
    if (s.includes('science')) return <Atom size={22} />;
    if (s.includes('social')) return <Globe2 size={22} />;
    return <FileText size={22} />;
  };

  return (
    <div
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{
        background: '#ffffff',
        border: `1.5px solid ${hov ? accentColor : '#e2e8f0'}`,
        borderRadius: '1.25rem',
        overflow: 'hidden',
        boxShadow: hov ? `0 12px 30px -4px ${accentColor}25` : '0 4px 16px -2px rgba(15, 23, 42, 0.05)',
        transform: hov ? 'translateY(-3px)' : 'translateY(0)',
        transition: 'all 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
        display: 'flex', 
        flexDirection: 'column',
        cursor: 'pointer',
      }}
      onClick={onSelect}
    >
      <div style={{ height: '5px', background: gradient }} />

      <div style={{ padding: '1.5rem', flex: 1, display: 'flex', flexDirection: 'column' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
          <div style={{
            width: '44px', 
            height: '44px', 
            borderRadius: '0.85rem',
            background: `${accentColor}12`, 
            color: accentColor,
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center',
          }}>
            {getSubjectIcon(paper.subject)}
          </div>

          <span style={{
            background: `${accentColor}12`, 
            border: `1px solid ${accentColor}25`,
            borderRadius: '9999px', 
            padding: '0.2rem 0.65rem',
            fontSize: '0.7rem', 
            fontWeight: '800', 
            color: accentColor,
            textTransform: 'uppercase',
          }}>
            {paper.year} Exam
          </span>
        </div>

        <h3 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.25rem', fontWeight: '800', color: '#0f172a', lineHeight: 1.25, marginBottom: '0.75rem' }}>
          {paper.subject}
        </h3>

        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap', marginBottom: '1.25rem', marginTop: 'auto' }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.3rem', background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '0.5rem', padding: '0.25rem 0.6rem', fontSize: '0.74rem', color: '#475569', fontWeight: '600' }}>
            <Clock size={12} /> {paper.durationMinutes} min
          </span>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.3rem', background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '0.5rem', padding: '0.25rem 0.6rem', fontSize: '0.74rem', color: '#475569', fontWeight: '600' }}>
            <Hash size={12} /> {questionCount} {isKPSEA ? 'Questions' : 'MCQs'}
          </span>
        </div>

        <button
          onClick={(e) => { e.stopPropagation(); onSelect(); }}
          style={{
            width: '100%', 
            padding: '0.75rem',
            background: hov ? gradient : '#f8fafc',
            border: `1.5px solid ${hov ? 'transparent' : '#cbd5e1'}`,
            borderRadius: '0.75rem',
            color: hov ? '#ffffff' : '#0f172a',
            fontWeight: '700', 
            fontSize: '0.88rem', 
            cursor: 'pointer',
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center', 
            gap: '0.5rem',
            boxShadow: hov ? `0 6px 20px ${accentColor}35` : 'none',
            transition: 'all 0.2s ease',
          }}
        >
          <Play size={14} fill={hov ? '#ffffff' : 'none'} /> Start Practice Exam
        </button>
      </div>
    </div>
  );
};
