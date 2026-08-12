import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { loadPaper } from '../data/pastPapers';
import { saveSession, loadSession } from '../services/db';
import { KeepAwake } from '@capacitor-community/keep-awake';
import { Haptics, ImpactStyle } from '@capacitor/haptics';
import { MathRenderer } from '../components/MathRenderer';
import { ZoomableImage } from '../components/ZoomableImage';
import { ArrowLeft, ArrowRight, CheckCircle, Circle, Loader2, BookOpen } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

export const ExamSession = () => {
  const { portal, paperId } = useParams();
  const navigate = useNavigate();
  
  const [paper, setPaper] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [showResumePrompt, setShowResumePrompt] = useState(false);
  const [pendingSession, setPendingSession] = useState(null);

  useEffect(() => {
    loadPaper(paperId)
      .then(async p => {
        setPaper(p);
        const savedSession = await loadSession('exam_sessions', paperId);
        if (savedSession && (Object.keys(savedSession.savedAnswers || {}).length > 0 || savedSession.savedIndex > 0)) {
          setPendingSession(savedSession);
          setShowResumePrompt(true);
        }
        setLoading(false);
      })
      .catch(e => {
        console.error(e);
        setError("Failed to load paper data.");
        setLoading(false);
      });
      
    const keepAwake = async () => {
      try {
        await KeepAwake.keepAwake();
      } catch (e) {}
    };
    keepAwake();
    return () => {
      KeepAwake.allowSleep().catch(() => {});
    };
  }, [paperId]);

  useEffect(() => {
    if (!loading && paper) {
      saveSession('exam_sessions', paperId, { savedAnswers: answers, savedIndex: currentIndex });
    }
  }, [answers, currentIndex, paperId, loading, paper]);

  const sectionA = paper?.sectionA || [];

  useEffect(() => {
    if (paper && sectionA.length === 0) {
      navigate(`/exam/${portal}/${paperId}/sectionB`, { replace: true });
    }
  }, [paper, sectionA.length, portal, paperId, navigate]);

  if (loading) return <div style={{ display: 'flex', height: '100vh', justifyContent: 'center', alignItems: 'center' }}><Loader2 size={32} style={{ animation: 'spin 1s linear infinite', color: '#2563eb' }} /></div>;
  if (error || !paper) return <div style={{ color: 'red', padding: '2rem' }}>{error || 'Paper not found.'}</div>;
  if (sectionA.length === 0) return null;


  const q = sectionA[currentIndex];
  const context = q.contextRef ? paper.sharedContexts[q.contextRef] : null;
  const progress = ((currentIndex + 1) / sectionA.length) * 100;
  const isKPSEA = portal === 'KPSEA';
  const optionLabels = ['A', 'B', 'C', 'D'];
  const accentColor = isKPSEA ? '#2563eb' : '#7c3aed';
  const gradient = isKPSEA ? 'linear-gradient(135deg, #2563eb, #7c3aed)' : 'linear-gradient(135deg, #7c3aed, #db2777)';
  const answeredCount = Object.keys(answers).length;

  const handleNext = () => {
    if (currentIndex < sectionA.length - 1) {
      setCurrentIndex(i => i + 1);
    } else {
      navigate(`/exam/${portal}/${paperId}/sectionAReview`, { state: { answers } });
    }
  };

  if (showResumePrompt) {
    return (
      <div style={{ height: '100vh', display: 'flex', flexDirection: 'column', background: 'var(--bg)', alignItems: 'center', justifyContent: 'center', padding: '2rem' }}>
        <div style={{
          background: '#fff', padding: '2.5rem', borderRadius: '1.5rem',
          boxShadow: '0 20px 40px rgba(0,0,0,0.08)', border: '1px solid var(--border)',
          maxWidth: '440px', width: '100%', textAlign: 'center'
        }}>
          <div style={{
            width: '64px', height: '64px', borderRadius: '50%', background: 'linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%)',
            display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', margin: '0 auto 1.5rem'
          }}>
            <BookOpen size={32} />
          </div>
          <h2 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.5rem', fontWeight: '800', color: 'var(--text)', marginBottom: '0.75rem', lineHeight: 1.2 }}>
            Resume Exam?
          </h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', lineHeight: 1.5, marginBottom: '2rem' }}>
            We found an unfinished attempt for <strong>{paper.subject}</strong>. Would you like to pick up where you left off, or start completely fresh?
          </p>
          <div style={{ display: 'flex', gap: '1rem', flexDirection: 'column' }}>
            <button
              onClick={() => {
                if (pendingSession) {
                  if (pendingSession.savedAnswers) setAnswers(pendingSession.savedAnswers);
                  if (pendingSession.savedIndex !== undefined) setCurrentIndex(pendingSession.savedIndex);
                }
                setShowResumePrompt(false);
              }}
              style={{
                width: '100%', padding: '0.9rem', borderRadius: '0.75rem',
                background: 'linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%)',
                color: '#fff', border: 'none', fontWeight: '700', fontSize: '1rem', cursor: 'pointer',
                boxShadow: '0 8px 16px rgba(59, 130, 246, 0.25)', transition: 'transform 0.2s'
              }}
            >
              Resume Attempt
            </button>
            <button
              onClick={() => {
                setAnswers({});
                setCurrentIndex(0);
                saveSession('exam_sessions', paperId, { savedAnswers: {}, savedIndex: 0 });
                setShowResumePrompt(false);
              }}
              style={{
                width: '100%', padding: '0.9rem', borderRadius: '0.75rem',
                background: 'var(--bg)', color: 'var(--text)', border: '2px solid var(--border)',
                fontWeight: '700', fontSize: '1rem', cursor: 'pointer', transition: 'background 0.2s'
              }}
            >
              Start Fresh
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column', background: 'var(--bg)', overflow: 'hidden' }}>

      {/* ── Header ── */}
      <header style={{
        flexShrink: 0,
        background: 'rgba(255,255,255,0.92)',
        backdropFilter: 'blur(12px)',
        WebkitBackdropFilter: 'blur(12px)',
        borderBottom: '1px solid var(--border)',
        height: '60px',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '0 1.25rem',
        gap: '1rem',
      }}>
        <button
          onClick={() => navigate(`/papers/${portal}`)}
          style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.4rem', fontSize: '0.82rem', fontWeight: '600', padding: '0.3rem 0.5rem', borderRadius: '0.4rem', flexShrink: 0 }}
        >
          <ArrowLeft size={14} /> Back
        </button>

        <div style={{ textAlign: 'center', flex: 1 }}>
          <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', color: 'var(--text)', fontSize: '0.9rem', lineHeight: 1 }}>{paper.subject}</div>
          {!isKPSEA && <div style={{ fontSize: '0.65rem', color: 'var(--text-muted)', fontWeight: '600', letterSpacing: '0.06em', textTransform: 'uppercase', marginTop: '0.15rem' }}>Section A — MCQs</div>}
        </div>

        <div style={{
          fontFamily: 'Outfit, sans-serif', fontWeight: '800',
          background: gradient,
          padding: '0.3rem 0.85rem', borderRadius: '9999px',
          color: '#fff', fontSize: '0.82rem',
          flexShrink: 0,
          boxShadow: `0 4px 12px ${accentColor}35`,
        }}>
          {currentIndex + 1} / {sectionA.length}
        </div>
      </header>

      {/* ── Progress bar ── */}
      <div style={{ height: '4px', background: 'var(--border)', flexShrink: 0, position: 'relative' }}>
        <div style={{
          position: 'absolute', top: 0, left: 0, height: '100%',
          width: `${progress}%`,
          background: gradient,
          transition: 'width 0.4s ease',
          borderRadius: '0 2px 2px 0',
        }} />
      </div>

      {/* ── Question + Options ── */}
      <main style={{ flex: 1, overflowY: 'auto', padding: '0' }}>
        <div className="exam-fluid-container">

          {/* ── Split grid: context LEFT, question RIGHT on desktop ── */}
          <div className={context ? 'exam-split-grid' : ''} style={{ marginBottom: '1.5rem' }}>

            {/* ── Left panel: Reference Context (only rendered when context exists) ── */}
            {context && (
              <div className="exam-left-panel">
                <div style={{
                  background: '#ffffff',
                  border: '1px solid var(--border)',
                  borderRadius: '1.25rem',
                  padding: '1.25rem',
                  display: 'flex', flexDirection: 'column', alignItems: 'center',
                  boxShadow: 'var(--shadow-sm)',
                }}>
                  <span style={{ fontSize: '0.62rem', fontWeight: '800', color: accentColor, letterSpacing: '0.12em', textTransform: 'uppercase', marginBottom: '0.6rem' }}>
                    {context.type === 'text' && !context.text ? 'Instructions' : context.type === 'text' ? 'Reference Passage' : 'Reference Diagram'}
                  </span>

                  {context.title && (
                    <div style={{ width: '100%', textAlign: 'left', marginBottom: context.text || context.imagePath ? '0.8rem' : '0' }}>
                      <strong style={{ display: 'block', color: accentColor, fontSize: '0.88rem', whiteSpace: 'pre-wrap', letterSpacing: '0.01em' }}>{context.title}</strong>
                      {(context.text || context.imagePath) && (
                        <div style={{ color: accentColor, opacity: 0.5, fontSize: '0.7rem', letterSpacing: '3px', margin: '0.4rem 0 0.8rem 0', userSelect: 'none' }}>{'- '.repeat(40)}</div>
                      )}
                    </div>
                  )}
                  
                  {context.type === 'image' && (
                    <>
                      {context.text && (
                        <div style={{ width: '100%', textAlign: 'left', marginBottom: '1rem' }}>
                          <ReactMarkdown
                            remarkPlugins={[remarkGfm]}
                            components={{
                              p: ({ children }) => (
                                <p style={{ margin: '0 0 0.8rem 0', lineHeight: '1.8', color: 'var(--text)', fontSize: '0.92rem' }}>{children}</p>
                              ),
                              strong: ({ children }) => (
                                <strong style={{ color: 'var(--text-emphasis)', fontWeight: '700' }}>{children}</strong>
                              )
                            }}
                          >{context.text}</ReactMarkdown>
                        </div>
                      )}
                      <ZoomableImage 
                        src={context.imagePath} 
                        alt={context.title} 
                        baseMaxHeight="35vh" 
                        scanEffect={context.scanEffect !== false}
                        customFilter={context.cssFilter}
                      />
                      {context.caption && <p style={{ fontSize: '0.72rem', color: 'var(--text-muted)', marginTop: '0.5rem', textAlign: 'center' }}>{context.caption}</p>}
                    </>
                  )}

                  {context.type === 'text' && context.text && (
                    <div style={{ width: '100%', textAlign: 'left', background: 'var(--bg-muted)', padding: '1.25rem', borderRadius: '0.75rem', borderLeft: `4px solid ${accentColor}` }}>
                      <div style={{ fontSize: '0.95rem', lineHeight: '1.8', color: 'var(--text)' }}>
                        <ReactMarkdown
                          remarkPlugins={[remarkGfm]}
                          components={{
                            p: ({ children }) => (
                              <p style={{ margin: '0 0 0.75rem 0', lineHeight: '1.8', color: 'var(--text)', fontSize: '0.95rem' }}>{children}</p>
                            ),
                            strong: ({ children }) => (
                              <strong style={{ fontWeight: '700', color: 'var(--text)' }}>{children}</strong>
                            ),
                            table: ({ children }) => (
                              <div style={{ overflowX: 'auto', margin: '1rem 0' }}>
                                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.9rem' }}>
                                  {children}
                                </table>
                              </div>
                            ),
                            th: ({ children }) => (
                              <th style={{ padding: '0.75rem 1rem', borderBottom: '2px solid var(--border)', backgroundColor: 'var(--bg-muted)', color: 'var(--text-muted)', fontWeight: '600' }}>
                                {children}
                              </th>
                            ),
                            td: ({ children }) => (
                              <td style={{ padding: '0.75rem 1rem', borderBottom: '1px solid var(--border-light)' }}>
                                {children}
                              </td>
                            ),
                            img: ({ src, alt }) => (
                              <div style={{ marginTop: '1rem', marginBottom: '1rem' }}>
                                <ZoomableImage src={src} alt={alt} baseMaxHeight="30vh" />
                              </div>
                            ),
                          }}
                        >
                          {context.text}
                        </ReactMarkdown>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* ── Right panel (or full-width if no context): Question + Options ── */}
            <div className={context ? 'exam-right-panel' : ''}>

              {/* Question number badge + text */}
              <div style={{ background: '#ffffff', borderRadius: '1.25rem', padding: '1.5rem', marginBottom: '1rem', border: '1px solid var(--border)', boxShadow: 'var(--shadow-sm)' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem', marginBottom: '0.9rem' }}>
                  <span style={{
                    width: '30px', height: '30px', borderRadius: '50%',
                    background: gradient,
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontSize: '0.78rem', fontWeight: '800', color: '#fff', flexShrink: 0,
                    boxShadow: `0 3px 10px ${accentColor}35`,
                  }}>{q.questionNumber}</span>
                  <span style={{ fontSize: '0.68rem', fontWeight: '800', color: accentColor, textTransform: 'uppercase', letterSpacing: '0.1em' }}>Question {q.questionNumber}</span>
                </div>
                <div style={{ fontSize: '1.05rem', fontWeight: '600', lineHeight: 1.8, color: 'var(--text)' }}>
                  <MathRenderer text={q.questionText} />
                  {q.questionList && (
                    <ul style={{ margin: '0.6rem 0 0.6rem 1.2rem', padding: 0, listStyleType: 'disc' }}>
                      {q.questionList.map((item, i) => (
                        <li key={i} style={{ marginBottom: '0.2rem' }}>
                          <MathRenderer text={item} />
                        </li>
                      ))}
                    </ul>
                  )}
                  {q.questionSuffix && (
                    <span><MathRenderer text={q.questionSuffix} /></span>
                  )}
                </div>
              </div>

              {/* Options */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.55rem' }}>
                {q.options.map((opt, idx) => {
                  const selected = answers[q.id] === idx;
                  return (
                    <button
                      key={idx}
                      onClick={() => {
                        try { Haptics.impact({ style: ImpactStyle.Light }); } catch(e) {}
                        setAnswers(prev => ({ ...prev, [q.id]: idx }));
                      }}
                      style={{
                        display: 'flex', alignItems: 'center', gap: '0.85rem',
                        width: '100%', textAlign: 'left', padding: '0.9rem 1.1rem',
                        borderRadius: '0.85rem', cursor: 'pointer',
                        background: selected ? `${accentColor}09` : '#ffffff',
                        border: `2px solid ${selected ? accentColor : 'var(--border)'}`,
                        color: 'var(--text)',
                        boxShadow: selected ? `0 4px 14px ${accentColor}20` : 'var(--shadow-sm)',
                        transform: selected ? 'scale(1.005)' : 'scale(1)',
                        transition: 'all 0.18s ease',
                      }}
                    >
                      <span style={{
                        width: '32px', height: '32px', borderRadius: '50%', flexShrink: 0,
                        display: 'flex', alignItems: 'center', justifyContent: 'center',
                        background: selected ? gradient : 'transparent',
                        border: `2px solid ${selected ? 'transparent' : 'var(--border-bright)'}`,
                        fontWeight: '800', fontSize: '0.78rem',
                        color: selected ? '#fff' : 'var(--text-muted)',
                        boxShadow: selected ? `0 3px 10px ${accentColor}35` : 'none',
                      }}>
                        {optionLabels[idx]}
                      </span>
                      <span style={{ fontSize: '0.97rem', lineHeight: 1.65, flex: 1, color: selected ? 'var(--text)' : 'var(--text-secondary)', fontWeight: selected ? '600' : '400' }}>
                        <MathRenderer text={opt.text} />
                      </span>
                      {selected && <CheckCircle size={17} color={accentColor} style={{ flexShrink: 0 }} />}
                    </button>
                  );
                })}
              </div>

            </div>
          </div>

          {/* Navigation row — always full-width, outside the split grid */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '1rem', borderTop: '1px solid var(--border)' }}>
            <button
              onClick={() => setCurrentIndex(i => i - 1)}
              disabled={currentIndex === 0}
              style={{
                display: 'flex', alignItems: 'center', gap: '0.4rem',
                padding: '0.6rem 1.1rem',
                background: '#ffffff', border: '1.5px solid var(--border)',
                borderRadius: '0.6rem', color: 'var(--text-muted)',
                cursor: currentIndex === 0 ? 'not-allowed' : 'pointer',
                opacity: currentIndex === 0 ? 0.4 : 1,
                fontWeight: '600', fontSize: '0.85rem',
                boxShadow: 'var(--shadow-sm)',
              }}
            >
              <ArrowLeft size={14} /> Prev
            </button>

            <div style={{ textAlign: 'center' }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: '600' }}>
                {answers[q.id] !== undefined
                  ? <span style={{ color: '#059669', fontWeight: '700' }}>✓ Answered</span>
                  : <span style={{ color: 'var(--text-faint)' }}>Not answered</span>
                }
              </span>
              <div style={{ fontSize: '0.65rem', color: 'var(--text-faint)', marginTop: '0.1rem' }}>{answeredCount} of {sectionA.length} done</div>
            </div>

            <button
              onClick={handleNext}
              style={{
                display: 'flex', alignItems: 'center', gap: '0.4rem',
                padding: '0.6rem 1.25rem',
                background: gradient,
                border: 'none', borderRadius: '0.6rem', color: '#fff',
                fontWeight: '700', cursor: 'pointer', fontSize: '0.85rem',
                boxShadow: `0 4px 14px ${accentColor}35`,
              }}
            >
              {currentIndex === sectionA.length - 1 ? 'Submit' : 'Next'} <ArrowRight size={14} />
            </button>
          </div>

        </div>
      </main>
    </div>
  );
};
export default ExamSession;
