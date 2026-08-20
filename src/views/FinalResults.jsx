import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Home, RotateCcw, Trophy, Star, ArrowRight } from 'lucide-react';

export const FinalResults = () => {
  const { portal, paperId } = useParams();
  const navigate = useNavigate();
  const isKPSEA = portal === 'KPSEA';
  const gradient = isKPSEA
    ? 'linear-gradient(135deg, #2563eb, #7c3aed)'
    : 'linear-gradient(135deg, #7c3aed, #db2777)';
  const accentColor = isKPSEA ? '#2563eb' : '#7c3aed';

  return (
    <div style={{
      minHeight: '100vh',
      background: 'var(--bg)',
      backgroundImage: `radial-gradient(ellipse 80% 60% at 50% 0%, ${isKPSEA ? 'rgba(37,99,235,0.08)' : 'rgba(124,58,237,0.08)'} 0%, transparent 60%)`,
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      padding: '2rem 1.25rem',
    }}>
      <div style={{ maxWidth: '480px', width: '100%' }}>

        {/* Trophy card */}
        <div style={{
          background: 'var(--bg-card)',
          borderRadius: '2rem',
          overflow: 'hidden',
          boxShadow: 'var(--shadow-xl)',
          border: '1px solid var(--border)',
        }}>
          {/* Gradient banner */}
          <div style={{
            background: gradient,
            padding: '2.5rem 2rem',
            textAlign: 'center',
            position: 'relative',
            overflow: 'hidden',
          }}>
            <div style={{ position: 'absolute', top: '-40px', left: '-40px', width: '180px', height: '180px', borderRadius: '50%', background: 'rgba(255,255,255,0.07)' }} />
            <div style={{ position: 'absolute', bottom: '-50px', right: '-30px', width: '160px', height: '160px', borderRadius: '50%', background: 'rgba(255,255,255,0.05)' }} />

            <div style={{ position: 'relative', zIndex: 1 }}>
              <div style={{
                width: '80px', height: '80px', borderRadius: '50%',
                background: 'rgba(255,255,255,0.2)',
                border: '2px solid rgba(255,255,255,0.4)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                margin: '0 auto 1rem',
                backdropFilter: 'blur(4px)',
              }}>
                <Trophy size={36} color="#fff" strokeWidth={1.5} />
              </div>

              <h1 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '2rem', fontWeight: '900', color: 'var(--bg-card)', marginBottom: '0.4rem', letterSpacing: '-0.02em' }}>
                Exam Complete!
              </h1>
              <p style={{ color: 'rgba(255,255,255,0.8)', fontSize: '0.9rem', fontWeight: '500' }}>
                Great work finishing this paper!
              </p>

              {/* Stars */}
              <div style={{ display: 'flex', justifyContent: 'center', gap: '0.3rem', marginTop: '1rem' }}>
                {[1,2,3,4,5].map(i => (
                  <Star key={i} size={18} color="rgba(255,255,255,0.8)" fill="rgba(255,255,255,0.6)" />
                ))}
              </div>
            </div>
          </div>

          {/* Body */}
          <div style={{ padding: '1.75rem 2rem' }}>
            {/* Study tip box */}
            <div style={{ background: 'var(--bg-muted)', border: '1.5px solid var(--border)', borderRadius: '1rem', padding: '1.25rem', marginBottom: '1.75rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
                <div style={{ width: '22px', height: '22px', borderRadius: '50%', background: gradient, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  <Star size={11} color="#fff" fill="#fff" />
                </div>
                <p style={{ fontSize: '0.72rem', fontWeight: '800', color: accentColor, textTransform: 'uppercase', letterSpacing: '0.1em' }}>Study Tip</p>
              </div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem', lineHeight: 1.7 }}>
                Review every wrong answer carefully before attempting the next paper. Understanding your mistakes is the fastest way to improve.
              </p>
            </div>

            {/* Action buttons */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
              <button
                onClick={() => navigate(`/exam/${portal}/${paperId}`)}
                style={{
                  width: '100%', padding: '0.9rem',
                  background: 'var(--bg-muted)', border: '1.5px solid var(--border)',
                  borderRadius: '0.85rem', color: 'var(--text-secondary)',
                  fontWeight: '700', cursor: 'pointer',
                  display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem',
                  fontSize: '0.92rem',
                }}
              >
                <RotateCcw size={16} /> Retake This Paper
              </button>
              <button
                onClick={() => navigate(`/papers/${portal}`)}
                style={{
                  width: '100%', padding: '0.9rem',
                  background: gradient, border: 'none',
                  borderRadius: '0.85rem', color: 'var(--bg-card)',
                  fontWeight: '800', cursor: 'pointer',
                  display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem',
                  fontSize: '0.92rem',
                  boxShadow: `0 8px 24px ${accentColor}35`,
                }}
              >
                <Home size={16} /> Browse More Papers <ArrowRight size={15} />
              </button>
            </div>
          </div>
        </div>

        {/* Tagline */}
        <p style={{ textAlign: 'center', color: 'var(--text-faint)', fontSize: '0.75rem', marginTop: '1.25rem', fontWeight: '500' }}>
          CBC Assessment System · Kenya · Practice Makes Perfect
        </p>
      </div>
    </div>
  );
};
