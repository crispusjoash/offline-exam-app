import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { PAST_PAPERS } from '../data/pastPapers';
import { ArrowLeft, Clock, FileText, Play, Hash, BookOpen, ChevronRight, X } from 'lucide-react';

export const PaperSelector = () => {
  const { portal, year } = useParams();
  const navigate = useNavigate();
  const allPortalPapers = PAST_PAPERS[portal] || [];
  
  // Filter out sub-papers so they only appear inside the customized parent selector
  const papers = allPortalPapers.filter(p => String(p.year) === String(year) && !p.isSubPaper);
  
  const isKPSEA = portal === 'KPSEA';
  const accentColor = isKPSEA ? '#2563eb' : '#7c3aed';
  const gradient = isKPSEA
    ? 'linear-gradient(135deg, #2563eb, #7c3aed)'
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
    <div style={{ minHeight: '100vh', background: 'var(--bg)', color: 'var(--text)' }}>
      {/* CSS Animation Keyframes for Modal Entrance */}
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

      {/* ── Header ── */}
      <header style={{
        background: 'rgba(255,255,255,0.8)',
        backdropFilter: 'blur(12px)',
        WebkitBackdropFilter: 'blur(12px)',
        borderBottom: '1px solid var(--border)',
        padding: '0 1.5rem',
        height: '64px',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        position: 'sticky', top: 0, zIndex: 20,
      }}>
        <button
          onClick={() => navigate(`/papers/${portal}`)}
          style={{
            display: 'inline-flex', alignItems: 'center', gap: '0.5rem',
            background: 'none', border: 'none', color: 'var(--text-muted)',
            cursor: 'pointer', fontSize: '0.85rem', fontWeight: '600',
            padding: '0.4rem 0.75rem', borderRadius: '0.5rem',
          }}
        >
          <ArrowLeft size={15} /> Back
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
          <div style={{
            width: '30px', height: '30px', borderRadius: '0.5rem',
            background: gradient, display: 'flex', alignItems: 'center', justifyContent: 'center',
            boxShadow: `0 3px 10px ${accentColor}30`,
          }}>
            <BookOpen size={15} color="#fff" strokeWidth={2.5} />
          </div>
          <div>
            <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', fontSize: '1rem', color: 'var(--text)', lineHeight: 1 }}>{portal} {year}</div>
            <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', lineHeight: 1, marginTop: '0.15rem' }}>Past Papers</div>
          </div>
        </div>

        <div style={{ width: '80px' }} /> {/* spacer */}
      </header>

      {/* ── Hero banner ── */}
      <div style={{
        background: gradient,
        padding: '2.5rem 1.5rem',
        textAlign: 'center',
        position: 'relative',
        overflow: 'hidden',
      }}>
        {/* decorative blobs */}
        <div style={{ position: 'absolute', top: '-40px', right: '-40px', width: '200px', height: '200px', borderRadius: '50%', background: 'rgba(255,255,255,0.08)' }} />
        <div style={{ position: 'absolute', bottom: '-60px', left: '-30px', width: '160px', height: '160px', borderRadius: '50%', background: 'rgba(255,255,255,0.06)' }} />

        <p style={{ fontSize: '0.72rem', fontWeight: '700', color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase', letterSpacing: '0.15em', marginBottom: '0.5rem' }}>
          {isKPSEA ? 'Grade 6' : 'Grade 9'} · {year} Assessment
        </p>
        <h1 style={{ fontFamily: 'Outfit, sans-serif', fontSize: 'clamp(1.8rem, 5vw, 2.6rem)', fontWeight: '900', color: '#ffffff', marginBottom: '0.5rem', letterSpacing: '-0.02em' }}>
          {portal} {year} Papers
        </h1>
        <p style={{ color: 'rgba(255,255,255,0.8)', fontSize: '0.9rem', fontWeight: '500' }}>
          Select a subject to begin your practice session
        </p>
      </div>

      {/* ── Cards ── */}
      <div style={{ maxWidth: '960px', margin: '0 auto', padding: '2rem 1.25rem' }}>
        {papers.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '5rem 0', color: 'var(--text-muted)' }}>
            <BookOpen size={48} style={{ opacity: 0.3, marginBottom: '1rem' }} />
            <p>No papers available yet for {portal}.</p>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '1.25rem' }}>
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

      {/* ── Overlay Modal ── */}
      {selectedParent && (
        <div style={{
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
          background: 'rgba(15, 23, 42, 0.45)',
          backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          zIndex: 100, padding: '1rem',
        }}>
          <div style={{
            background: '#ffffff',
            width: '100%', maxWidth: '540px',
            borderRadius: '1.5rem',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.15), 0 0 0 1px rgba(0,0,0,0.05)',
            overflow: 'hidden',
            animation: 'modalSlideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards',
          }}>
            {/* Modal Header */}
            <div style={{
              padding: '1.5rem',
              background: 'var(--bg-muted)',
              borderBottom: '1px solid var(--border)',
              display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            }}>
              <div>
                <h2 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.3rem', fontWeight: '800', margin: 0, color: 'var(--text)', letterSpacing: '-0.01em' }}>
                  {religionStep ? 'Select Religion Option' : 'Select Paper Section'}
                </h2>
                <p style={{ fontSize: '0.78rem', color: 'var(--text-muted)', margin: '0.2rem 0 0 0', fontWeight: '500' }}>
                  {religionStep ? 'Choose your specific religious education option' : 'This paper is divided into core & religious sections.'}
                </p>
              </div>
              <button
                onClick={() => setSelectedParent(null)}
                style={{
                  background: '#f1f5f9', border: 'none',
                  width: '32px', height: '32px', borderRadius: '50%',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  cursor: 'pointer', color: 'var(--text-muted)',
                  transition: 'background 0.2s',
                }}
                onMouseEnter={(e) => e.target.style.background = '#e2e8f0'}
                onMouseLeave={(e) => e.target.style.background = '#f1f5f9'}
              >
                <X size={16} />
              </button>
            </div>

            {/* Modal Content */}
            <div style={{ padding: '1.5rem', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {!religionStep ? (
                <>
                  <SelectorOption
                    title="Part A: Social Studies & Creative Arts"
                    badgeText="Core Section"
                    badgeBg="#ebf5ff"
                    badgeColor="#2563eb"
                    description="Covers geography, history, civics, and creative arts. Compulsory questions 1 to 35."
                    duration="60 min"
                    qsCount="35 Qs"
                    onClick={() => {
                      setSelectedParent(null);
                      navigate(`/exam/${portal}/kpsea-sst-parta-2023`);
                    }}
                  />

                  <SelectorOption
                    title="Part B: Religious Education"
                    badgeText="Optional Section"
                    badgeBg="#f0fdf4"
                    badgeColor="#10b981"
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
                    <ArrowLeft size={14} /> Back to main sections
                  </button>

                  <SubSelectorOption
                    title="Christian Religious Education (CRE)"
                    subtitle="Part B · Questions 36 to 50"
                    onClick={() => {
                      setSelectedParent(null);
                      navigate(`/exam/${portal}/kpsea-sst-cre-2023`);
                    }}
                  />

                  <SubSelectorOption
                    title="Islamic Religious Education (IRE)"
                    subtitle="Part B · Questions 36 to 50"
                    onClick={() => {
                      setSelectedParent(null);
                      navigate(`/exam/${portal}/kpsea-sst-ire-2023`);
                    }}
                  />

                  <SubSelectorOption
                    title="Hindu Religious Education (HRE)"
                    subtitle="Part B · Questions 36 to 50"
                    onClick={() => {
                      setSelectedParent(null);
                      navigate(`/exam/${portal}/kpsea-sst-hre-2023`);
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
        border: `1.5px solid ${hov ? '#2563eb' : 'var(--border)'}`,
        background: hov ? '#2563eb05' : '#ffffff',
        borderRadius: '1rem', padding: '1.25rem',
        cursor: 'pointer', transition: 'all 0.2s ease',
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        boxShadow: hov ? '0 8px 24px rgba(37,99,235,0.06)' : 'var(--shadow-sm)',
      }}
    >
      <div style={{ flex: 1, paddingRight: '1rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.4rem', flexWrap: 'wrap' }}>
          {badgeText && (
            <span style={{ background: badgeBg, color: badgeColor, fontSize: '0.68rem', fontWeight: '800', padding: '0.15rem 0.45rem', borderRadius: '0.35rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>{badgeText}</span>
          )}
          <h4 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.05rem', fontWeight: '800', margin: 0, color: 'var(--text)' }}>{title}</h4>
        </div>
        <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)', margin: 0, lineHeight: 1.4, fontWeight: '500' }}>
          {description}
        </p>
        <div style={{ display: 'flex', gap: '0.75rem', marginTop: '0.75rem', fontSize: '0.72rem', color: 'var(--text-muted)', fontWeight: '600' }}>
          {duration && <span style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}><Clock size={12} /> {duration}</span>}
          {qsCount && <span style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}><Hash size={12} /> {qsCount}</span>}
        </div>
      </div>
      <ChevronRight size={20} color={hov ? '#2563eb' : 'var(--text-muted)'} style={{ transform: hov ? 'translateX(2px)' : 'translateX(0)', transition: 'transform 0.2s' }} />
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
        border: `1.5px solid ${hov ? '#2563eb' : 'var(--border)'}`,
        background: hov ? '#2563eb05' : '#ffffff',
        borderRadius: '0.75rem', padding: '1rem 1.25rem',
        cursor: 'pointer', transition: 'all 0.2s ease',
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        boxShadow: hov ? '0 8px 24px rgba(37,99,235,0.06)' : 'var(--shadow-sm)',
      }}
    >
      <div>
        <h5 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1rem', fontWeight: '800', margin: 0, color: 'var(--text)' }}>{title}</h5>
        <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', margin: '0.15rem 0 0 0', fontWeight: '500' }}>{subtitle}</p>
      </div>
      <ChevronRight size={18} color={hov ? '#2563eb' : 'var(--text-muted)'} style={{ transform: hov ? 'translateX(2px)' : 'translateX(0)', transition: 'transform 0.2s' }} />
    </div>
  );
};

/* ── Standard Subject Card Component ── */
const PaperCard = ({ paper, portal, accentColor, gradient, onSelect }) => {
  const [hov, setHov] = React.useState(false);
  const isKPSEA = portal === 'KPSEA';

  // Calculate length based on sectionA content if not a parent paper
  const questionCount = paper.isParentPaper ? 50 : (paper.sectionA?.length || 0);

  return (
    <div
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{
        background: '#ffffff',
        border: `1.5px solid ${hov ? accentColor + '50' : 'var(--border)'}`,
        borderRadius: '1.25rem',
        overflow: 'hidden',
        boxShadow: hov ? `0 16px 40px ${accentColor}18, var(--shadow-md)` : 'var(--shadow-sm)',
        transform: hov ? 'translateY(-4px)' : 'translateY(0)',
        transition: 'all 0.3s ease',
        display: 'flex', flexDirection: 'column',
        cursor: 'pointer',
      }}
      onClick={onSelect}
    >
      <div style={{ height: '4px', background: gradient }} />

      <div style={{ padding: '1.5rem', flex: 1, display: 'flex', flexDirection: 'column' }}>
        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', marginBottom: '1rem' }}>
          <span style={{
            background: `${accentColor}12`, border: `1px solid ${accentColor}25`,
            borderRadius: '0.4rem', padding: '0.2rem 0.6rem',
            fontSize: '0.7rem', fontWeight: '800', color: accentColor,
            textTransform: 'uppercase', letterSpacing: '0.1em',
          }}>
            {paper.year}
          </span>
          <div style={{
            width: '36px', height: '36px', borderRadius: '0.6rem',
            background: `${accentColor}12`, border: `1px solid ${accentColor}25`,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>
            <FileText size={17} color={accentColor} />
          </div>
        </div>

        <h3 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.25rem', fontWeight: '800', color: 'var(--text)', lineHeight: 1.2, marginBottom: '1rem' }}>
          {paper.subject}
        </h3>

        <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap', marginBottom: '1.25rem', marginTop: 'auto' }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.3rem', background: 'var(--bg-muted)', border: '1px solid var(--border)', borderRadius: '9999px', padding: '0.25rem 0.65rem', fontSize: '0.72rem', color: 'var(--text-muted)', fontWeight: '600' }}>
            <Clock size={11} /> {paper.durationMinutes} min
          </span>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.3rem', background: 'var(--bg-muted)', border: '1px solid var(--border)', borderRadius: '9999px', padding: '0.25rem 0.65rem', fontSize: '0.72rem', color: 'var(--text-muted)', fontWeight: '600' }}>
            <Hash size={11} /> {questionCount} {isKPSEA ? 'Qs' : 'MCQs'}
          </span>
        </div>

        <button
          onClick={(e) => { e.stopPropagation(); onSelect(); }}
          style={{
            width: '100%', padding: '0.8rem',
            background: hov ? gradient : 'transparent',
            border: `1.5px solid ${hov ? 'transparent' : accentColor + '40'}`,
            borderRadius: '0.75rem',
            color: hov ? '#fff' : accentColor,
            fontWeight: '700', fontSize: '0.9rem', cursor: 'pointer',
            display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem',
            boxShadow: hov ? `0 6px 20px ${accentColor}35` : 'none',
          }}
        >
          <Play size={15} fill={hov ? '#fff' : 'none'} /> Start Exam
        </button>
      </div>
    </div>
  );
};

