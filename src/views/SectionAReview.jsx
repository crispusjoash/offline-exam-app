import React from 'react';
import { useParams, useNavigate, useLocation } from 'react-router-dom';
import { PAST_PAPERS } from '../data/pastPapers';
import { MathRenderer } from '../components/MathRenderer';
import { ZoomableImage } from '../components/ZoomableImage';
import { CheckCircle, XCircle, ArrowRight, AlertCircle, Home, RotateCcw, Trophy, TrendingUp } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const ExplanationRenderer = ({ text }) => {
  if (!text) return null;
  // Handle newlines (support both literal newlines and escaped \\n)
  const lines = text.split('\n');
  const elements = [];
  let currentList = [];

  const flushList = (key) => {
    if (currentList.length > 0) {
      elements.push(
        <ul key={`list-${key}`} style={{ margin: '0 0 0.75rem 0', paddingLeft: '1.25rem', listStyleType: 'disc' }}>
          {currentList}
        </ul>
      );
      currentList = [];
    }
  };

  lines.forEach((line, idx) => {
    const trimmed = line.trim();
    if (trimmed.startsWith('* ')) {
      const content = trimmed.substring(2);
      currentList.push(
        <li key={idx} style={{ marginBottom: '0.45rem', lineHeight: 1.6 }}>
          <MathRenderer text={content} />
        </li>
      );
    } else {
      flushList(idx);
      if (trimmed) {
        elements.push(
          <p key={idx} style={{ margin: '0 0 0.75rem 0', lineHeight: 1.6 }}>
            <MathRenderer text={trimmed} />
          </p>
        );
      }
    }
  });
  flushList(lines.length);

  return <div style={{ color: 'var(--text-secondary)' }}>{elements}</div>;
};

export const SectionAReview = () => {
  const { portal, paperId } = useParams();
  const navigate = useNavigate();
  const location = useLocation();
  const answers = location.state?.answers || {};

  const paper = PAST_PAPERS[portal]?.find(p => p.id === paperId);
  if (!paper) return null;

  const isKPSEA = portal === 'KPSEA';
  const sectionA = paper.sectionA || [];
  const hasSectionB = paper.sectionB?.length > 0;
  const accentColor = isKPSEA ? '#2563eb' : '#7c3aed';
  const gradient = isKPSEA ? 'linear-gradient(135deg, #2563eb, #7c3aed)' : 'linear-gradient(135deg, #7c3aed, #db2777)';

  let correct = 0;
  sectionA.forEach(q => {
    if (answers[q.id] !== undefined && q.options[answers[q.id]]?.isCorrect) correct++;
  });
  const incorrect = sectionA.length - correct;
  const unansweredCount = sectionA.filter(q => answers[q.id] === undefined).length;
  const percent = sectionA.length ? Math.round((correct / sectionA.length) * 100) : 0;

  const scoreGrad = percent >= 80
    ? 'linear-gradient(135deg, #059669, #0891b2)'
    : percent >= 50
    ? 'linear-gradient(135deg, #d97706, #f59e0b)'
    : 'linear-gradient(135deg, #dc2626, #f97316)';

  const scoreLabel = percent >= 80 ? 'Excellent!' : percent >= 60 ? 'Good Work!' : percent >= 40 ? 'Keep Practising' : 'Needs Improvement';

  return (
    <div style={{ minHeight: '100vh', background: 'var(--bg)', color: 'var(--text)' }}>

      {/* ── Score Hero ── */}
      <div style={{
        background: gradient,
        padding: '2.5rem 1.5rem 3rem',
        textAlign: 'center',
        position: 'relative',
        overflow: 'hidden',
      }}>
        {/* decorative circles */}
        <div style={{ position: 'absolute', top: '-50px', right: '-50px', width: '220px', height: '220px', borderRadius: '50%', background: 'rgba(255,255,255,0.07)' }} />
        <div style={{ position: 'absolute', bottom: '-60px', left: '-40px', width: '180px', height: '180px', borderRadius: '50%', background: 'rgba(255,255,255,0.05)' }} />

        <div style={{ position: 'relative', zIndex: 1 }}>
          <div style={{ fontSize: '0.7rem', fontWeight: '800', color: 'rgba(255,255,255,0.75)', textTransform: 'uppercase', letterSpacing: '0.15em', marginBottom: '0.75rem' }}>
            <Trophy size={12} style={{ display: 'inline', marginRight: '0.35rem', verticalAlign: 'middle' }} />
            {isKPSEA ? 'Exam Results' : 'Section A Results'}
          </div>

          {/* Score circle */}
          <div style={{
            display: 'inline-flex', alignItems: 'center', justifyContent: 'center',
            width: '130px', height: '130px', borderRadius: '50%',
            background: 'rgba(255,255,255,0.15)',
            border: '3px solid rgba(255,255,255,0.3)',
            marginBottom: '1rem',
            backdropFilter: 'blur(4px)',
          }}>
            <div>
              <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '900', fontSize: '2.5rem', color: '#ffffff', lineHeight: 1 }}>{percent}<span style={{ fontSize: '1.2rem' }}>%</span></div>
            </div>
          </div>

          <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', fontSize: '1.4rem', color: '#ffffff', marginBottom: '0.5rem' }}>{scoreLabel}</div>

          {/* Stats row */}
          <div style={{ display: 'flex', justifyContent: 'center', gap: '1.5rem', flexWrap: 'wrap', marginBottom: '1.75rem' }}>
            {[
              { val: correct, label: 'Correct', color: 'rgba(255,255,255,0.9)' },
              { val: incorrect - unansweredCount, label: 'Wrong', color: 'rgba(255,255,255,0.7)' },
              { val: unansweredCount, label: 'Skipped', color: 'rgba(255,255,255,0.6)' },
              { val: sectionA.length, label: 'Total', color: 'rgba(255,255,255,0.5)' },
            ].map(s => (
              <div key={s.label} style={{ textAlign: 'center' }}>
                <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', fontSize: '1.3rem', color: s.color }}>{s.val}</div>
                <div style={{ fontSize: '0.7rem', color: 'rgba(255,255,255,0.6)', textTransform: 'uppercase', letterSpacing: '0.08em', fontWeight: '600' }}>{s.label}</div>
              </div>
            ))}
          </div>

          {/* CTA buttons */}
          <div style={{ display: 'flex', gap: '0.75rem', justifyContent: 'center', flexWrap: 'wrap' }}>
            {hasSectionB && !isKPSEA ? (
              <button
                onClick={() => navigate(`/exam/${portal}/${paperId}/sectionB`)}
                style={{
                  padding: '0.8rem 2rem',
                  background: '#ffffff', border: 'none',
                  borderRadius: '0.75rem', color: accentColor,
                  fontWeight: '800', fontSize: '0.95rem', cursor: 'pointer',
                  display: 'inline-flex', alignItems: 'center', gap: '0.5rem',
                  boxShadow: '0 8px 24px rgba(0,0,0,0.2)',
                }}
              >
                Proceed to Section B <ArrowRight size={17} />
              </button>
            ) : (
              <>
                <button
                  onClick={() => navigate(`/exam/${portal}/${paperId}`)}
                  style={{ padding: '0.8rem 1.5rem', background: 'rgba(255,255,255,0.15)', border: '1px solid rgba(255,255,255,0.3)', borderRadius: '0.75rem', color: '#fff', fontWeight: '700', cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.9rem', backdropFilter: 'blur(4px)' }}
                >
                  <RotateCcw size={15} /> Retake
                </button>
                <button
                  onClick={() => navigate(`/papers/${portal}`)}
                  style={{ padding: '0.8rem 1.5rem', background: '#ffffff', border: 'none', borderRadius: '0.75rem', color: accentColor, fontWeight: '700', cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.9rem', boxShadow: '0 6px 20px rgba(0,0,0,0.15)' }}
                >
                  <Home size={15} /> All Papers
                </button>
              </>
            )}
          </div>
        </div>
      </div>

      {/* ── Review Section ── */}
      <div style={{ maxWidth: '780px', margin: '0 auto', padding: '1.5rem 1rem 3rem', width: '100%', boxSizing: 'border-box' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.5rem' }}>
          <TrendingUp size={18} color={accentColor} />
          <h2 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.25rem', fontWeight: '800', color: 'var(--text)' }}>Answer Review</h2>
          <span style={{ marginLeft: 'auto', fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: '600' }}>{sectionA.length} questions</span>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {sectionA.map(q => {
            const chosen = answers[q.id];
            const isCorrect = chosen !== undefined && q.options[chosen]?.isCorrect;
            const correctIdx = q.options.findIndex(o => o.isCorrect);
            const unanswered = chosen === undefined;

            const statusColor = isCorrect ? '#059669' : unanswered ? '#d97706' : '#dc2626';
            const statusBg = isCorrect ? '#f0fdf4' : unanswered ? '#fffbeb' : '#fef2f2';
            const statusBorder = isCorrect ? '#bbf7d0' : unanswered ? '#fde68a' : '#fecaca';

            return (
              <div key={q.id} style={{
                background: '#ffffff',
                border: `1.5px solid ${statusBorder}`,
                borderRadius: '1.1rem',
                overflow: 'hidden',
                boxShadow: 'var(--shadow-sm)',
              }}>
                {/* Status stripe */}
                <div style={{ height: '3px', background: statusColor, opacity: 0.7 }} />

                <div style={{ padding: '1.25rem 1.4rem' }}>
                  {/* Reference Context */}
                  {q.contextRef && paper.sharedContexts[q.contextRef] && (
                    <div style={{ marginBottom: '1rem', background: 'var(--bg-muted)', border: '1px solid var(--border)', borderRadius: '0.65rem', padding: '0.75rem', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                      <span style={{ fontSize: '0.6rem', fontWeight: '800', color: accentColor, letterSpacing: '0.12em', textTransform: 'uppercase', marginBottom: '0.4rem' }}>
                        {paper.sharedContexts[q.contextRef].type === 'text' && !paper.sharedContexts[q.contextRef].text ? 'Instructions' : paper.sharedContexts[q.contextRef].type === 'text' ? 'Reference Passage' : 'Reference Diagram'}
                      </span>
                      
                      {paper.sharedContexts[q.contextRef].title && (
                        <div style={{ width: '100%', textAlign: 'left', marginBottom: paper.sharedContexts[q.contextRef].text || paper.sharedContexts[q.contextRef].imagePath ? '0.5rem' : '0' }}>
                          <strong style={{ display: 'block', color: accentColor, fontSize: '0.8rem', whiteSpace: 'pre-wrap' }}>{paper.sharedContexts[q.contextRef].title}</strong>
                          {(paper.sharedContexts[q.contextRef].text || paper.sharedContexts[q.contextRef].imagePath) && (
                            <div style={{ color: accentColor, opacity: 0.4, fontSize: '0.7rem', letterSpacing: '2px', margin: '0.3rem 0 0.6rem 0', userSelect: 'none', overflow: 'hidden', whiteSpace: 'nowrap' }}>{'- '.repeat(20)}</div>
                          )}
                        </div>
                      )}

                      {paper.sharedContexts[q.contextRef].type === 'image' && (
                        <>
                          {paper.sharedContexts[q.contextRef].text && (
                            <div style={{ width: '100%', textAlign: 'left', marginBottom: '0.5rem' }}>
                              <ReactMarkdown
                                remarkPlugins={[remarkGfm]}
                                components={{
                                  p: ({ children }) => (
                                    <p style={{ margin: '0 0 0.6rem 0', lineHeight: '1.8', color: 'var(--text)', fontSize: '0.85rem' }}>{children}</p>
                                  ),
                                  strong: ({ children }) => (
                                    <strong style={{ color: 'var(--text-emphasis)', fontWeight: '700' }}>{children}</strong>
                                  )
                                }}
                              >{paper.sharedContexts[q.contextRef].text}</ReactMarkdown>
                            </div>
                          )}
                          <ZoomableImage src={paper.sharedContexts[q.contextRef].imagePath} alt={paper.sharedContexts[q.contextRef].title} baseMaxHeight="18vh" customFilter={paper.sharedContexts[q.contextRef].cssFilter} />
                          {paper.sharedContexts[q.contextRef].caption && <p style={{ fontSize: '0.7rem', color: 'var(--text-muted)', marginTop: '0.3rem', textAlign: 'center' }}>{paper.sharedContexts[q.contextRef].caption}</p>}
                        </>
                      )}

                      {paper.sharedContexts[q.contextRef].type === 'text' && paper.sharedContexts[q.contextRef].text && (
                        <div style={{ width: '100%', textAlign: 'left', padding: '0.5rem', borderLeft: `3px solid ${accentColor}` }}>
                          <div style={{ fontSize: '0.85rem', lineHeight: '1.8', color: 'var(--text)' }}>
                            <ReactMarkdown
                              remarkPlugins={[remarkGfm]}
                              components={{
                                p: ({ children }) => (
                                  <p style={{ margin: '0 0 0.6rem 0', lineHeight: '1.8', color: 'var(--text)', fontSize: '0.85rem' }}>{children}</p>
                                ),
                                strong: ({ children }) => (
                                  <strong style={{ fontWeight: '700', color: 'var(--text)' }}>{children}</strong>
                                ),
                                table: ({ children }) => (
                                  <div style={{ overflowX: 'auto', margin: '1rem 0' }}>
                                    <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.8rem' }}>
                                      {children}
                                    </table>
                                  </div>
                                ),
                                th: ({ children }) => (
                                  <th style={{ padding: '0.5rem', borderBottom: '2px solid var(--border)', backgroundColor: 'var(--bg-muted)', color: 'var(--text-muted)', fontWeight: '600' }}>
                                    {children}
                                  </th>
                                ),
                                td: ({ children }) => (
                                  <td style={{ padding: '0.5rem', borderBottom: '1px solid var(--border-light)' }}>
                                    {children}
                                  </td>
                                ),
                                img: ({ src, alt }) => (
                                  <div style={{ marginTop: '1rem', marginBottom: '1rem' }}>
                                    <ZoomableImage src={src} alt={alt} baseMaxHeight="25vh" />
                                  </div>
                                ),
                              }}
                            >
                              {paper.sharedContexts[q.contextRef].text}
                            </ReactMarkdown>
                          </div>
                        </div>
                      )}
                    </div>
                  )}

                  {/* Question */}
                  <div style={{ display: 'flex', gap: '0.75rem', marginBottom: '0.85rem' }}>
                    <div style={{ flexShrink: 0, marginTop: '3px' }}>
                      {isCorrect
                        ? <CheckCircle size={19} color="#059669" />
                        : unanswered
                        ? <AlertCircle size={19} color="#d97706" />
                        : <XCircle size={19} color="#dc2626" />}
                    </div>
                    <div style={{ fontSize: '0.95rem', lineHeight: 1.75, color: 'var(--text)', fontWeight: '500', flexGrow: 1 }}>
                      <span style={{ fontWeight: '700', color: 'var(--text-muted)', marginRight: '0.4rem' }}>{q.questionNumber}.</span>
                      <MathRenderer text={q.questionText} />
                      {q.questionList && (
                        <div style={{ marginLeft: '1.2rem', marginTop: '0.5rem', marginBottom: '0.5rem' }}>
                          {q.questionList.map((item, i) => (
                            <div key={i} style={{ marginBottom: '0.2rem' }}>
                              <MathRenderer text={item} />
                            </div>
                          ))}
                        </div>
                      )}
                      {q.questionSuffix && (
                        <div style={{ marginTop: '0.5rem' }}>
                          <MathRenderer text={q.questionSuffix} />
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Options */}
                  <div style={{ paddingLeft: '0', display: 'flex', flexDirection: 'column', gap: '0.3rem', marginBottom: '0.9rem' }}>
                    {q.options.map((opt, i) => {
                      const isCorrectOpt = i === correctIdx;
                      const isChosen = i === chosen;
                      const isWrong = isChosen && !isCorrect;
                      const letter = String.fromCharCode(65 + i);
                      return (
                        <div key={i} style={{
                          padding: '0.4rem 0.75rem', borderRadius: '0.45rem', fontSize: '0.88rem',
                          background: isCorrectOpt ? '#f0fdf4' : isWrong ? '#fef2f2' : 'transparent',
                          color: isCorrectOpt ? '#059669' : isWrong ? '#dc2626' : 'var(--text-muted)',
                          border: isCorrectOpt ? '1px solid #bbf7d0' : isWrong ? '1px solid #fecaca' : '1px solid transparent',
                          fontWeight: isCorrectOpt || isWrong ? '700' : '500',
                          display: 'flex', alignItems: 'center', gap: '0.5rem',
                        }}>
                          {isCorrectOpt ? '✓' : isWrong ? '✗' : <span style={{ width: '0.65rem' }} />}
                          <span style={{ fontWeight: '800', color: isCorrectOpt ? '#059669' : isWrong ? '#dc2626' : 'var(--text)' }}>
                            {letter}.
                          </span>
                          <MathRenderer text={opt.text} />
                        </div>
                      );
                    })}
                    {unanswered && <p style={{ color: '#d97706', fontSize: '0.78rem', fontStyle: 'italic', paddingLeft: '0.5rem', marginTop: '0.15rem', fontWeight: '600' }}>Not answered</p>}
                  </div>

                  {/* Explanation */}
                  {q.explanation && (
                    <div style={{ paddingLeft: '0', borderTop: '1px solid var(--border)', paddingTop: '0.85rem' }}>
                      <p style={{ fontSize: '0.68rem', fontWeight: '800', color: accentColor, letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: '0.6rem' }}>Teacher's Explanation</p>
                      <div className="explanation-markdown" style={{ 
                        color: 'var(--text-secondary)', 
                        fontSize: '0.94rem', 
                        lineHeight: 1.7,
                        background: 'var(--bg-muted)',
                        padding: '0.75rem 1.25rem',
                        borderRadius: '0.6rem',
                        borderLeft: `3px solid ${accentColor}`
                      }}>
                        <ExplanationRenderer text={q.explanation} />
                      </div>
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>

        {/* ── Close Review Button ── */}
        <div style={{ marginTop: '2.5rem', display: 'flex', justifyContent: 'center' }}>
          <button
            onClick={() => navigate(`/exam/${portal}/${paperId}/results`)}
            style={{
              padding: '1rem 2rem',
              background: '#ffffff',
              border: '2px solid var(--border)',
              borderRadius: '1rem',
              color: 'var(--text)',
              fontWeight: '700',
              fontSize: '1rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '0.6rem',
              boxShadow: 'var(--shadow-sm)',
              transition: 'all 0.2s',
            }}
            onMouseOver={(e) => e.currentTarget.style.transform = 'translateY(-2px)'}
            onMouseOut={(e) => e.currentTarget.style.transform = 'translateY(0)'}
          >
            Close Review
          </button>
        </div>
      </div>
    </div>
  );
};
