import React, { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft, Calendar, ChevronRight } from 'lucide-react';
import { PAST_PAPERS } from '../data/pastPapers';

export const YearSelector = () => {
  const { portal } = useParams();
  const navigate = useNavigate();
  const [hoveredId, setHoveredId] = useState(null);

  const isKPSEA = portal === 'KPSEA';
  const accentColor = isKPSEA ? '#2563eb' : '#7c3aed';
  const gradient = isKPSEA ? 'linear-gradient(135deg, #2563eb, #3b82f6)' : 'linear-gradient(135deg, #7c3aed, #db2777)';

  // Find all unique years available for this portal
  const papers = PAST_PAPERS[portal] || [];
  const availableYears = [...new Set(papers.map(p => p.year))].sort((a, b) => b - a);

  return (
    <div style={{ minHeight: '100vh', background: 'var(--bg)', color: 'var(--text)' }}>
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
          onClick={() => navigate('/')}
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
            <Calendar size={15} color="#fff" strokeWidth={2.5} />
          </div>
          <div>
            <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', fontSize: '1rem', color: 'var(--text)', lineHeight: 1 }}>{portal}</div>
            <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', lineHeight: 1, marginTop: '0.15rem' }}>Select Year</div>
          </div>
        </div>

        <div style={{ width: '80px' }} /> {/* spacer */}
      </header>

      {/* ── Hero banner ── */}
      <div style={{
        background: gradient,
        padding: '3rem 1.5rem',
        textAlign: 'center',
        position: 'relative',
        overflow: 'hidden',
      }}>
        {/* decorative blobs */}
        <div style={{ position: 'absolute', top: '-40px', right: '-40px', width: '200px', height: '200px', borderRadius: '50%', background: 'rgba(255,255,255,0.08)' }} />
        <div style={{ position: 'absolute', bottom: '-60px', left: '-30px', width: '160px', height: '160px', borderRadius: '50%', background: 'rgba(255,255,255,0.06)' }} />

        <p style={{ fontSize: '0.72rem', fontWeight: '700', color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase', letterSpacing: '0.15em', marginBottom: '0.5rem' }}>
          {isKPSEA ? 'Grade 6' : 'Grade 9'} · CBC Assessment
        </p>
        <h1 style={{ fontFamily: 'Outfit, sans-serif', fontSize: 'clamp(1.8rem, 5vw, 2.6rem)', fontWeight: '900', color: '#ffffff', marginBottom: '0.5rem', letterSpacing: '-0.02em' }}>
          {portal} Past Papers
        </h1>
        <p style={{ color: 'rgba(255,255,255,0.8)', fontSize: '0.9rem', fontWeight: '500' }}>
          Select an academic year to continue
        </p>
      </div>

      {/* ── Cards ── */}
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '3rem 1.25rem' }}>
        {availableYears.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '5rem 0', color: 'var(--text-muted)' }}>
            <Calendar size={48} style={{ opacity: 0.3, marginBottom: '1rem' }} />
            <p>No papers available yet for {portal}.</p>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))', gap: '1.25rem' }}>
            {availableYears.map((year, idx) => {
              const paperCount = papers.filter(p => p.year === year).length;
              const hov = hoveredId === year;
              return (
                <div
                  key={year}
                  onMouseEnter={() => setHoveredId(year)}
                  onMouseLeave={() => setHoveredId(null)}
                  onClick={() => navigate(`/papers/${portal}/${year}`)}
                  style={{
                    background: '#ffffff',
                    border: '1px solid var(--border)',
                    borderRadius: '1.25rem',
                    padding: '1.5rem',
                    cursor: 'pointer',
                    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
                    transition: 'all 0.3s cubic-bezier(0.16, 1, 0.3, 1)',
                    transform: hov ? 'translateY(-4px)' : 'none',
                    boxShadow: hov ? '0 12px 24px rgba(0,0,0,0.06)' : 'var(--shadow-sm)',
                    position: 'relative',
                    overflow: 'hidden'
                  }}
                >
                  <div style={{
                    position: 'absolute', top: 0, left: 0, right: 0, height: '4px',
                    background: gradient, opacity: hov ? 1 : 0, transition: 'opacity 0.3s'
                  }} />

                  <div style={{ 
                    width: '60px', height: '60px', borderRadius: '1rem',
                    background: hov ? gradient : 'var(--bg-muted)',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    marginBottom: '1rem', transition: 'all 0.3s'
                  }}>
                    <Calendar size={28} color={hov ? '#fff' : accentColor} />
                  </div>
                  
                  <h3 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.8rem', fontWeight: '800', color: 'var(--text)', margin: '0 0 0.2rem 0' }}>
                    {year}
                  </h3>
                  
                  <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: '600', marginBottom: '1.25rem' }}>
                    {paperCount} {paperCount === 1 ? 'Paper' : 'Papers'}
                  </div>

                  <div style={{
                    display: 'flex', alignItems: 'center', gap: '0.3rem',
                    color: hov ? accentColor : 'var(--text-muted)',
                    fontSize: '0.85rem', fontWeight: '700',
                    transition: 'color 0.3s'
                  }}>
                    View Papers <ChevronRight size={16} />
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
