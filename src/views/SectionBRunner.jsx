import React, { useState, useRef, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { loadPaper } from '../data/pastPapers';
import { saveSession, loadSession } from '../services/db';
import { KeepAwake } from '@capacitor-community/keep-awake';
import { Haptics, ImpactStyle } from '@capacitor/haptics';
import { MathRenderer } from '../components/MathRenderer';
import { ZoomableImage } from '../components/ZoomableImage';
import { Pencil, Eraser, Trash2, CheckCircle2, AlertTriangle, XCircle, ChevronRight, Eye, ArrowLeft, BookOpen, Loader2 } from 'lucide-react';

export const SectionBRunner = () => {
  const { portal, paperId } = useParams();
  const navigate = useNavigate();

  const [paper, setPaper] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [grades, setGrades] = useState({});
  const [revealed, setRevealed] = useState(false);
  const [activeDrawingId, setActiveDrawingId] = useState(null);
  const [tool, setTool] = useState('pencil');
  const [isDrawing, setIsDrawing] = useState(false);
  const canvasRef = useRef(null);

  const [showResumePrompt, setShowResumePrompt] = useState(false);
  const [pendingSession, setPendingSession] = useState(null);

  useEffect(() => {
    loadPaper(paperId)
      .then(async p => {
        setPaper(p);
        const savedSession = await loadSession('sectionb_sessions', paperId);
        if (savedSession && (Object.keys(savedSession.savedAnswers || {}).length > 0 || savedSession.savedIndex > 0 || Object.keys(savedSession.savedGrades || {}).length > 0)) {
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
      saveSession('sectionb_sessions', paperId, {
        savedAnswers: answers,
        savedIndex: currentIndex,
        savedGrades: grades,
        savedRevealed: revealed
      });
    }
  }, [answers, currentIndex, grades, revealed, paperId, loading, paper]);

  const sectionB = paper?.sectionB || [];

  useEffect(() => {
    if (paper && sectionB.length === 0) {
      navigate(`/exam/${portal}/${paperId}/results`, { replace: true });
    }
  }, [paper, sectionB.length, portal, paperId, navigate]);

  if (loading) return <div style={{ display: 'flex', height: '100vh', justifyContent: 'center', alignItems: 'center' }}><Loader2 size={32} style={{ animation: 'spin 1s linear infinite', color: '#db2777' }} /></div>;
  if (error || !paper) return <div style={{ color: 'red', padding: '2rem' }}>{error || 'Paper not found.'}</div>;
  if (sectionB.length === 0) return null;


  const q = sectionB[currentIndex];
  const context = q.contextRef ? paper.sharedContexts[q.contextRef] : null;
  const progress = ((currentIndex + 1) / sectionB.length) * 100;
  const gradient = 'linear-gradient(135deg, #7c3aed, #db2777)';
  const accentColor = '#7c3aed';

  const items = q.subQuestions && q.subQuestions.length > 0 ? q.subQuestions : [q];
  const allGraded = items.every(item => grades[item.id] !== undefined);

  const handleNext = () => {
    setRevealed(false);
    if (currentIndex < sectionB.length - 1) setCurrentIndex(i => i + 1);
    else navigate(`/exam/${portal}/${paperId}/results`);
  };

  // Canvas helpers
  const getPos = (e, canvas) => {
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;
    return { x: (clientX - rect.left) * scaleX, y: (clientY - rect.top) * scaleY };
  };
  const startDraw = (e) => {
    e.preventDefault();
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const { x, y } = getPos(e, canvas);
    ctx.beginPath(); ctx.moveTo(x, y);
    setIsDrawing(true);
  };
  const doDraw = (e) => {
    e.preventDefault();
    if (!isDrawing) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const { x, y } = getPos(e, canvas);
    if (tool === 'eraser') { ctx.globalCompositeOperation = 'destination-out'; ctx.lineWidth = 24; }
    else { ctx.globalCompositeOperation = 'source-over'; ctx.strokeStyle = '#0f172a'; ctx.lineWidth = 3; ctx.lineCap = 'round'; }
    ctx.lineTo(x, y); ctx.stroke();
  };
  const stopDraw = (e) => { e?.preventDefault(); setIsDrawing(false); };
  const clearCanvas = () => {
    const canvas = canvasRef.current;
    if (canvas) canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
  };
  const saveDrawing = () => {
    const canvas = canvasRef.current;
    if (canvas && activeDrawingId) {
      setAnswers(prev => ({ ...prev, [activeDrawingId]: canvas.toDataURL() }));
    }
    setActiveDrawingId(null);
  };

  const getGradeConfig = (score, maxScore) => {
    const s = Number(score);
    const ms = Number(maxScore);
    const label = s === 1 ? '1 mark' : `${s} marks`;
    
    if (s === 0) return { bg: '#fef2f2', border: '#fecaca', text: '#dc2626', icon: <XCircle size={15} />, label };
    if (s === ms) return { bg: '#f0fdf4', border: '#bbf7d0', text: '#059669', icon: <CheckCircle2 size={15} />, label };
    return { bg: '#fffbeb', border: '#fde68a', text: '#d97706', icon: <AlertTriangle size={15} />, label };
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
            width: '64px', height: '64px', borderRadius: '50%', background: 'linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)',
            display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', margin: '0 auto 1.5rem'
          }}>
            <BookOpen size={32} />
          </div>
          <h2 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.5rem', fontWeight: '800', color: 'var(--text)', marginBottom: '0.75rem', lineHeight: 1.2 }}>
            Resume Section B?
          </h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', lineHeight: 1.5, marginBottom: '2rem' }}>
            We found an unfinished attempt for <strong>{paper?.subject}</strong>. Would you like to pick up where you left off, or start completely fresh?
          </p>
          <div style={{ display: 'flex', gap: '1rem', flexDirection: 'column' }}>
            <button
              onClick={() => {
                if (pendingSession) {
                  if (pendingSession.savedAnswers) setAnswers(pendingSession.savedAnswers);
                  if (pendingSession.savedIndex !== undefined) setCurrentIndex(pendingSession.savedIndex);
                  if (pendingSession.savedGrades) setGrades(pendingSession.savedGrades);
                  if (pendingSession.savedRevealed !== undefined) setRevealed(pendingSession.savedRevealed);
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
                setGrades({});
                setRevealed(false);
                saveSession('sectionb_sessions', paperId, { savedAnswers: {}, savedIndex: 0, savedGrades: {}, savedRevealed: false });
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
        padding: '0 1.5rem',
        height: '60px',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      }}>
        <button
          onClick={() => navigate(`/papers/${portal}`)}
          style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.4rem', fontSize: '0.82rem', fontWeight: '600' }}
        >
          <ArrowLeft size={14} /> Back
        </button>

        <div style={{ textAlign: 'center' }}>
          <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', color: 'var(--text)', fontSize: '0.88rem', lineHeight: 1 }}>{paper.subject}</div>
          <div style={{ fontSize: '0.62rem', color: accentColor, fontWeight: '700', letterSpacing: '0.08em', textTransform: 'uppercase', marginTop: '0.15rem' }}>Section B</div>
        </div>

        <div style={{
          fontFamily: 'Outfit, sans-serif', fontWeight: '800',
          background: gradient,
          padding: '0.3rem 0.85rem', borderRadius: '9999px',
          color: '#fff', fontSize: '0.82rem',
          boxShadow: `0 4px 12px ${accentColor}35`,
        }}>
          {currentIndex + 1} / {sectionB.length}
        </div>
      </header>

      {/* ── Progress bar ── */}
      <div style={{ height: '4px', background: 'var(--border)', flexShrink: 0 }}>
        <div style={{ height: '100%', width: `${progress}%`, background: gradient, transition: 'width 0.4s ease' }} />
      </div>

      <main style={{ flex: 1, overflowY: 'auto', paddingBottom: revealed ? '120px' : '4rem' }}>
        {/* Scrollable context image - not sticky */}
        {context && (
          <div style={{ background: 'rgba(255,255,255,0.95)', borderBottom: '1px solid var(--border)', padding: '0.75rem 1.25rem', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <span style={{ fontSize: '0.62rem', fontWeight: '800', color: accentColor, letterSpacing: '0.12em', textTransform: 'uppercase', marginBottom: '0.4rem' }}>Reference</span>
            {context.type === 'image' && <ZoomableImage src={context.imagePath} alt={context.title} baseMaxHeight="22vh" />}
          </div>
        )}

        <div className="exam-fluid-container">

          {/* Parent Question Context (if exists) */}
          {q.parentQuestionText && (
             <div style={{ background: '#ffffff', border: '1px solid var(--border)', borderRadius: '1.25rem', padding: '1.5rem', marginBottom: '1.5rem', boxShadow: 'var(--shadow-sm)' }}>
               <p style={{ fontSize: '0.68rem', fontWeight: '800', color: accentColor, marginBottom: '0.6rem', textTransform: 'uppercase', letterSpacing: '0.1em' }}>Question {q.questionNumber}</p>
               <p style={{ fontSize: '1.05rem', fontWeight: '600', lineHeight: 1.8, color: 'var(--text)' }}>
                 <MathRenderer text={q.parentQuestionText} />
               </p>
             </div>
          )}

          {/* Items (Sub-questions or the main question itself) */}
          {items.map((item, idx) => {
            const isSub = !!item.subNumber;
            const qType = item.questionType || 'structured'; // default to structured if missing
            const maxScore = item.maxScore || 2;
            const gradesArray = Array.from({ length: maxScore + 1 }, (_, i) => i);

            return (
              <div key={item.id} style={{ marginBottom: '2.5rem' }}>
                
                {/* Question Text */}
                {(!q.parentQuestionText || isSub) && (
                  <div style={{ background: '#ffffff', border: '1px solid var(--border)', borderRadius: '1.25rem', padding: '1.5rem', marginBottom: '1rem', boxShadow: 'var(--shadow-sm)' }}>
                    {!q.parentQuestionText && <p style={{ fontSize: '0.68rem', fontWeight: '800', color: accentColor, marginBottom: '0.6rem', textTransform: 'uppercase', letterSpacing: '0.1em' }}>Question {q.questionNumber}</p>}
                    <p style={{ fontSize: '1.05rem', fontWeight: '600', lineHeight: 1.8, color: 'var(--text)' }}>
                      {isSub && <span style={{fontWeight: '800', marginRight: '0.5rem', color: accentColor}}>{item.subNumber}</span>}
                      <MathRenderer text={item.questionText} />
                    </p>
                  </div>
                )}

                {/* Answer Area */}
                <div style={{ background: '#ffffff', border: '1.5px solid var(--border)', borderRadius: '1rem', padding: '1.25rem', marginBottom: '1rem', boxShadow: 'var(--shadow-sm)' }}>
                  <p style={{ fontSize: '0.7rem', fontWeight: '700', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: '0.75rem' }}>Your Answer</p>
                  {qType === 'structured' && (
                    <textarea
                      style={{
                        width: '100%', minHeight: '120px',
                        background: 'var(--bg-muted)', border: '1.5px solid var(--border)',
                        borderRadius: '0.65rem', padding: '0.8rem',
                        color: 'var(--text)', fontSize: '0.97rem', resize: 'vertical',
                        fontFamily: 'Inter, sans-serif', lineHeight: 1.7,
                        outline: 'none',
                      }}
                      placeholder="Type your answer here..."
                      value={answers[item.id] || ''}
                      onChange={e => setAnswers(prev => ({ ...prev, [item.id]: e.target.value }))}
                      disabled={revealed}
                    />
                  )}
                  {qType === 'drawing' && (
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem', padding: '1.25rem', border: '2px dashed var(--border-bright)', borderRadius: '0.75rem', background: 'var(--bg-muted)' }}>
                      {answers[item.id] ? (
                        <div style={{ background: '#f8fafc', borderRadius: '0.5rem', padding: '0.5rem', border: '1px solid var(--border)', width: '100%' }}>
                          <ZoomableImage src={answers[item.id]} alt="Your drawing" baseMaxHeight="200px" />
                        </div>
                      ) : (
                        <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem', textAlign: 'center' }}>No drawing yet — tap the button below to sketch your answer</p>
                      )}
                      {!revealed && (
                        <button onClick={() => setActiveDrawingId(item.id)} style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.6rem 1.25rem', background: `${accentColor}10`, border: `1.5px solid ${accentColor}30`, borderRadius: '0.6rem', color: accentColor, cursor: 'pointer', fontWeight: '700', fontSize: '0.85rem' }}>
                          <Pencil size={15} /> Open Sketchpad
                        </button>
                      )}
                    </div>
                  )}
                </div>

                {/* Reveal / Answer sections */}
                {revealed && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
                    {/* Model Answer */}
                    <div style={{ background: '#ffffff', border: '1.5px solid #bbf7d0', borderRadius: '1rem', padding: '1.25rem', boxShadow: 'var(--shadow-sm)' }}>
                      <p style={{ color: '#059669', fontWeight: '800', marginBottom: '0.75rem', display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                        <CheckCircle2 size={16} /> Model Answer
                      </p>
                      {qType === 'drawing' ? (
                        <div style={{ background: '#f8fafc', borderRadius: '0.5rem', padding: '0.5rem', border: '1px solid var(--border)', width: '100%' }}>
                          <ZoomableImage src={item.modelAnswer || ''} alt="Model diagram" baseMaxHeight="200px" />
                        </div>
                      ) : (
                        <div style={{ color: 'var(--text)', lineHeight: 1.75, fontSize: '0.97rem', display: 'flex', flexDirection: 'column', gap: '0.6rem' }}>
                          {(item.modelAnswer || 'Answer guide will be provided.').split('\n').map((line, lIdx) => {
                            const trimmed = line.trim();
                            if (!trimmed) return null;
                            return (
                              <div key={lIdx} style={{ marginTop: trimmed.match(/^(\d+\.|-|\*)/) ? '0.35rem' : '0' }}>
                                <MathRenderer text={trimmed} />
                              </div>
                            );
                          })}
                        </div>
                      )}
                    </div>

                    {/* Rubric */}
                    <div style={{ background: '#ffffff', border: `1.5px solid ${accentColor}25`, borderRadius: '1rem', padding: '1.25rem', boxShadow: 'var(--shadow-sm)' }}>
                      <p style={{ color: accentColor, fontWeight: '800', marginBottom: '0.5rem', fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                        <BookOpen size={14} style={{ display: 'inline', marginRight: '0.3rem', verticalAlign: 'middle' }} />
                        Marking Rubric
                      </p>
                      <div style={{ color: 'var(--text-secondary)', lineHeight: 1.75, fontSize: '0.93rem', marginBottom: '1.25rem', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                        {(item.rubric || `Award up to ${maxScore} marks based on accuracy.`).split('\n').map((line, lIdx) => {
                          const trimmed = line.trim();
                          if (!trimmed) return null;
                          return (
                            <div key={lIdx}>
                              <MathRenderer text={trimmed} />
                            </div>
                          );
                        })}
                      </div>
                      
                      {/* Grading Selector for this Item */}
                      <p style={{ fontSize: '0.7rem', fontWeight: '800', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: '0.5rem' }}>Self-Grade ({maxScore} marks max)</p>
                      <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                        {gradesArray.map(score => {
                          const c = getGradeConfig(score, maxScore);
                          const selected = grades[item.id] === score;
                          return (
                            <button
                              key={score}
                              onClick={() => {
                                try { Haptics.impact({ style: ImpactStyle.Light }); } catch(e) {}
                                setGrades(prev => ({ ...prev, [item.id]: score }));
                              }}
                              style={{
                                flex: '1 1 auto', minWidth: '80px', padding: '0.6rem 0.5rem',
                                background: selected ? c.bg : 'var(--bg-muted)',
                                border: `1.5px solid ${selected ? c.border : 'var(--border)'}`,
                                borderRadius: '0.6rem',
                                color: selected ? c.text : 'var(--text-muted)',
                                fontWeight: '700', cursor: 'pointer', fontSize: '0.82rem',
                                display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.35rem',
                                boxShadow: selected ? `0 4px 12px ${c.border}` : 'none',
                              }}
                            >
                              {c.icon} {score}
                            </button>
                          );
                        })}
                      </div>
                    </div>
                  </div>
                )}

              </div>
            );
          })}

          {!revealed && (
            <button
              onClick={() => setRevealed(true)}
              style={{ width: '100%', padding: '1rem', background: gradient, border: 'none', borderRadius: '0.85rem', color: '#fff', fontSize: '0.97rem', fontWeight: '700', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem', boxShadow: `0 8px 24px ${accentColor}35` }}
            >
              <Eye size={18} /> Reveal Model Answer
            </button>
          )}

        </div>
      </main>

      {/* ── Grade bar (floating) ── */}
      {revealed && (
        <div style={{
          position: 'fixed', bottom: 0, left: 0, right: 0,
          background: 'rgba(255,255,255,0.95)',
          backdropFilter: 'blur(12px)',
          WebkitBackdropFilter: 'blur(12px)',
          borderTop: '1px solid var(--border)',
          padding: '0.85rem 1.5rem',
          zIndex: 20,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          boxShadow: '0 -4px 24px rgba(0,0,0,0.06)',
        }}>
          <span style={{ color: allGraded ? '#059669' : 'var(--text-secondary)', fontSize: '0.88rem', fontWeight: '700', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
            {allGraded ? <><CheckCircle2 size={16} /> All parts graded</> : 'Please grade all parts above'}
          </span>
          
          <button
            onClick={handleNext}
            disabled={!allGraded}
            style={{
              padding: '0.6rem 1.5rem',
              background: allGraded ? gradient : 'var(--border)',
              border: 'none', borderRadius: '0.6rem',
              color: allGraded ? '#fff' : 'var(--text-muted)',
              fontWeight: '800', cursor: allGraded ? 'pointer' : 'not-allowed',
              display: 'flex', alignItems: 'center', gap: '0.35rem',
              fontSize: '0.85rem', whiteSpace: 'nowrap',
              boxShadow: allGraded ? `0 6px 18px ${accentColor}35` : 'none',
              flexShrink: 0,
            }}
          >
            {currentIndex === sectionB.length - 1 ? 'Finish' : 'Next'} <ChevronRight size={15} />
          </button>
        </div>
      )}

      {/* ── Drawing modal ── */}
      {activeDrawingId && (
        <div style={{ position: 'fixed', inset: 0, zIndex: 50, background: '#ffffff', display: 'flex', flexDirection: 'column' }}>
          <div style={{ height: '56px', background: 'var(--bg-muted)', borderBottom: '1px solid var(--border)', display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '0 1rem', flexShrink: 0 }}>
            <div style={{ display: 'flex', gap: '0.4rem' }}>
              {[['pencil', <Pencil size={17} key="p" />, 'Draw'], ['eraser', <Eraser size={17} key="e" />, 'Erase']].map(([t, icon, label]) => (
                <button key={t} onClick={() => setTool(t)} style={{ padding: '0.35rem 0.75rem', background: tool === t ? accentColor : 'var(--bg-card)', border: `1.5px solid ${tool === t ? accentColor : 'var(--border)'}`, borderRadius: '0.45rem', color: tool === t ? '#fff' : 'var(--text-muted)', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.78rem', fontWeight: '700' }}>{icon} {label}</button>
              ))}
              <button onClick={clearCanvas} style={{ padding: '0.35rem 0.7rem', background: '#fef2f2', border: '1.5px solid #fecaca', borderRadius: '0.45rem', color: '#dc2626', cursor: 'pointer', display: 'flex', alignItems: 'center' }}><Trash2 size={15} /></button>
            </div>
            <span style={{ color: 'var(--text-muted)', fontSize: '0.82rem', fontWeight: '600' }}>Draw your answer</span>
            <div style={{display:'flex', gap:'0.5rem'}}>
               <button onClick={() => setActiveDrawingId(null)} style={{ padding: '0.4rem 1rem', background: 'var(--border)', border: 'none', borderRadius: '0.45rem', color: 'var(--text)', fontWeight: '700', cursor: 'pointer', fontSize: '0.82rem' }}>Cancel</button>
               <button onClick={saveDrawing} style={{ padding: '0.4rem 1rem', background: gradient, border: 'none', borderRadius: '0.45rem', color: '#fff', fontWeight: '700', cursor: 'pointer', fontSize: '0.82rem' }}>Save</button>
            </div>
          </div>
          <div style={{ flex: 1, position: 'relative', touchAction: 'none' }}>
            <canvas
              ref={canvasRef}
              width={window.innerWidth}
              height={window.innerHeight - 56}
              style={{ position: 'absolute', inset: 0, cursor: 'crosshair', background: '#ffffff', width: '100%', height: '100%' }}
              onMouseDown={startDraw} onMouseMove={doDraw} onMouseUp={stopDraw} onMouseLeave={stopDraw}
              onTouchStart={startDraw} onTouchMove={doDraw} onTouchEnd={stopDraw}
            />
          </div>
        </div>
      )}
    </div>
  );
};
