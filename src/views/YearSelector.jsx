import React, { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Calendar, ChevronRight, BookOpen, Layers, CheckCircle2 } from 'lucide-react';
import { PAST_PAPERS } from '../data/pastPapers';

export const YearSelector = () => {
  const { portal } = useParams();
  const navigate = useNavigate();
  const [hoveredId, setHoveredId] = useState(null);

  const isKPSEA = portal === 'KPSEA';
  const accentColor = isKPSEA ? '#2563eb' : '#7c3aed';
  const badgeBg = isKPSEA ? '#eff6ff' : '#f5f3ff';
  const gradient = isKPSEA 
    ? 'linear-gradient(135deg, #2563eb, #3b82f6)' 
    : 'linear-gradient(135deg, #7c3aed, #db2777)';

  // Find all unique years available for this portal
  const papers = PAST_PAPERS[portal] || [];
  const availableYears = [...new Set(papers.map(p => p.year))].sort((a, b) => b - a);

  return (
    <div style={{ width: '100%', boxSizing: 'border-box' }}>
      <div className="portal-container">

        {/* ── Compact Portal Banner ── */}
        <div style={{
          background: isKPSEA 
            ? 'linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%)' 
            : 'linear-gradient(135deg, #4c1d95 0%, #7c3aed 100%)',
          borderRadius: '1.25rem',
          padding: '1.75rem 2rem',
          color: 'var(--bg-card)',
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
              {isKPSEA ? 'Grade 6 Primary' : 'Grade 9 Junior Secondary'}
            </span>

            <h1 style={{ fontFamily: 'Outfit, sans-serif', fontSize: 'clamp(1.75rem, 3.5vw, 2.3rem)', fontWeight: '900', color: 'var(--bg-card)', marginBottom: '0.35rem' }}>
              {portal} Examination Years
            </h1>

            <p style={{ color: 'rgba(255,255,255,0.85)', fontSize: '0.9rem', maxWidth: '500px' }}>
              Select an academic year below to access the past question papers and complete answer keys.
            </p>
          </div>
        </div>

        {/* ── Available Years Grid ── */}
        {availableYears.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '4rem 1rem', background: 'var(--bg-card)', borderRadius: '1.25rem', border: '1px dashed var(--border-bright)' }}>
            <Calendar size={44} style={{ color: 'var(--text-faint)', marginBottom: '0.75rem' }} />
            <h3 style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '700', fontSize: '1.1rem', color: 'var(--text)' }}>No papers available yet</h3>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginTop: '0.25rem' }}>Check back soon for updated {portal} exam papers.</p>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: '1.25rem' }}>
            {availableYears.map((year) => {
              const paperCount = papers.filter(p => p.year === year && !p.isSubPaper).length;
              const isHov = hoveredId === year;

              return (
                <div
                  key={year}
                  onMouseEnter={() => setHoveredId(year)}
                  onMouseLeave={() => setHoveredId(null)}
                  onClick={() => navigate(`/papers/${portal}/${year}`)}
                  style={{
                    background: 'var(--bg-card)',
                    borderRadius: '1.15rem',
                    padding: '1.5rem',
                    border: isHov ? `1.5px solid ${accentColor}` : '1.5px solid var(--border)',
                    boxShadow: isHov ? `0 12px 28px -5px ${accentColor}25` : '0 4px 16px -2px rgba(15, 23, 42, 0.05)',
                    transform: isHov ? 'translateY(-3px)' : 'translateY(0)',
                    cursor: 'pointer',
                    transition: 'all 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
                    display: 'flex',
                    flexDirection: 'column',
                    justify: 'space-between',
                  }}
                >
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
                      <div style={{
                        width: '42px',
                        height: '42px',
                        borderRadius: '0.75rem',
                        background: badgeBg,
                        color: accentColor,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                      }}>
                        <Calendar size={20} strokeWidth={2.2} />
                      </div>
                      <span style={{
                        fontSize: '0.72rem',
                        fontWeight: '700',
                        color: '#059669',
                        background: '#ecfdf5',
                        border: '1px solid #a7f3d0',
                        padding: '0.25rem 0.65rem',
                        borderRadius: '9999px',
                        display: 'inline-flex',
                        alignItems: 'center',
                        gap: '0.3rem',
                      }}>
                        <CheckCircle2 size={11} /> Verified Paper
                      </span>
                    </div>

                    <h3 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.75rem', fontWeight: '900', color: 'var(--text)', marginBottom: '0.25rem' }}>
                      {year}
                    </h3>
                    <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '1.25rem' }}>
                      Official {portal} Assessment
                    </p>
                  </div>

                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justify: 'space-between',
                    paddingTop: '0.85rem',
                    borderTop: '1px solid #f1f5f9',
                    fontSize: '0.85rem',
                    fontWeight: '700',
                    color: accentColor,
                  }}>
                    <span>{paperCount} Exam Papers</span>
                    <ChevronRight size={18} />
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
};
