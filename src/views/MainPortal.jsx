import React from 'react';
import { useNavigate } from 'react-router-dom';
import { BookOpen, GraduationCap, ArrowRight, Sparkles, Trophy, Clock, CheckCircle } from 'lucide-react';

export const MainPortal = () => {
  const navigate = useNavigate();

  return (
    <div style={{
      minHeight: '100vh',
      background: 'var(--bg)',
      backgroundImage: `
        radial-gradient(ellipse 80% 60% at 10% 0%, rgba(37, 99, 235, 0.08) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 90% 100%, rgba(124, 58, 237, 0.08) 0%, transparent 60%)
      `,
      display: 'flex',
      flexDirection: 'column',
    }}>

      {/* ── Top Nav Bar ── */}
      <header style={{
        padding: '1.25rem 2rem',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        borderBottom: '1px solid rgba(255,255,255,0.6)',
        background: 'rgba(255,255,255,0.6)',
        backdropFilter: 'blur(12px)',
        WebkitBackdropFilter: 'blur(12px)',
        position: 'sticky',
        top: 0,
        zIndex: 10,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
          <div style={{
            width: '34px', height: '34px', borderRadius: '0.6rem',
            background: 'var(--grad-blue)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            boxShadow: '0 4px 12px rgba(37,99,235,0.35)',
          }}>
            <BookOpen size={17} color="#fff" strokeWidth={2} />
          </div>
          <span style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', fontSize: '1.05rem', color: 'var(--text)' }}>CBC Portal</span>
        </div>
        <div style={{
          display: 'inline-flex', alignItems: 'center', gap: '0.4rem',
          background: 'linear-gradient(135deg, rgba(37,99,235,0.08), rgba(124,58,237,0.08))',
          border: '1px solid rgba(124,58,237,0.2)',
          borderRadius: '9999px', padding: '0.3rem 0.9rem',
          fontSize: '0.72rem', color: '#7c3aed', fontWeight: '700', letterSpacing: '0.08em', textTransform: 'uppercase',
        }}>
          <Sparkles size={11} /> Kenya · 2024
        </div>
      </header>

      {/* ── Hero ── */}
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '3rem 1.5rem 4rem' }}>
        <div style={{ maxWidth: '62rem', width: '100%' }}>

          {/* Hero text */}
          <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
            <div style={{
              display: 'inline-flex', alignItems: 'center', gap: '0.5rem',
              background: '#ffffff',
              border: '1px solid var(--border)',
              borderRadius: '9999px', padding: '0.4rem 1.1rem',
              fontSize: '0.78rem', color: 'var(--text-muted)', fontWeight: '600',
              marginBottom: '1.75rem',
              boxShadow: 'var(--shadow-sm)',
            }}>
              <Trophy size={13} color="#d97706" /> CBC Assessment · Offline Practice
            </div>

            <h1 style={{
              fontFamily: 'Outfit, sans-serif',
              fontSize: 'clamp(2.6rem, 6vw, 4.5rem)',
              fontWeight: '900',
              lineHeight: 1.04,
              letterSpacing: '-0.03em',
              marginBottom: '1.25rem',
              background: 'var(--grad-hero)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
            }}>
              Master Your<br />Exams Offline
            </h1>

            <p style={{
              fontSize: '1.1rem', color: 'var(--text-muted)',
              maxWidth: '480px', margin: '0 auto', lineHeight: 1.7, fontWeight: '500',
            }}>
              Practice real past papers with instant auto-grading and detailed step-by-step explanations.
            </p>
          </div>

          {/* Portal cards */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))', gap: '1.5rem' }}>
            <PortalCard
              label="Grade 6"
              title="KPSEA"
              subtitle="Kenya Primary School Education Assessment"
              desc="Auto-marked MCQ papers with detailed explanations for every question."
              icon={<BookOpen size={28} strokeWidth={2} color="#2563eb" />}
              iconBg="linear-gradient(135deg, #dbeafe, #ede9fe)"
              accentColor="#2563eb"
              accentGlow="rgba(37, 99, 235, 0.2)"
              stats={[{ label: '40 MCQs', icon: <CheckCircle size={12} /> }, { label: '60 min', icon: <Clock size={12} /> }]}
              gradient="linear-gradient(135deg, #2563eb, #7c3aed)"
              onClick={() => navigate('/papers/KPSEA')}
            />
            <PortalCard
              label="Grade 9"
              title="KJSEA"
              subtitle="Kenya Junior Secondary Education Assessment"
              desc="MCQ Section A auto-graded. Section B structured questions with self-marking rubrics."
              icon={<GraduationCap size={28} strokeWidth={2} color="#7c3aed" />}
              iconBg="linear-gradient(135deg, #ede9fe, #fce7f3)"
              accentColor="#7c3aed"
              accentGlow="rgba(124, 58, 237, 0.2)"
              stats={[{ label: '40 MCQs + Sec B', icon: <CheckCircle size={12} /> }, { label: '120 min', icon: <Clock size={12} /> }]}
              gradient="linear-gradient(135deg, #7c3aed, #db2777)"
              onClick={() => navigate('/papers/KJSEA')}
            />
          </div>

          {/* Bottom trust bar */}
          <div style={{
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            gap: '2rem', flexWrap: 'wrap',
            marginTop: '3.5rem',
          }}>
            {[
              { val: 'Auto-graded', sub: 'Instant results' },
              { val: 'Step-by-step', sub: 'Full explanations' },
              { val: 'Works offline', sub: 'No internet needed' },
            ].map(s => (
              <div key={s.val} style={{ textAlign: 'center' }}>
                <div style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '800', fontSize: '0.95rem', color: 'var(--text)' }}>{s.val}</div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.15rem' }}>{s.sub}</div>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
};

const PortalCard = ({ label, title, subtitle, desc, icon, iconBg, accentColor, accentGlow, stats, gradient, onClick }) => {
  const [hov, setHov] = React.useState(false);

  return (
    <div
      onClick={onClick}
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{
        background: '#ffffff',
        borderRadius: '1.5rem',
        overflow: 'hidden',
        cursor: 'pointer',
        transform: hov ? 'translateY(-6px) scale(1.01)' : 'translateY(0) scale(1)',
        boxShadow: hov ? `0 24px 56px -8px ${accentGlow}, var(--shadow-md)` : 'var(--shadow-sm)',
        border: `1px solid ${hov ? accentColor + '40' : 'var(--border)'}`,
        position: 'relative',
        transition: 'all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)',
      }}
    >
      {/* Color band at top */}
      <div style={{ height: '5px', background: gradient }} />

      <div style={{ padding: '2rem' }}>
        {/* Icon + label */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
          <div style={{
            width: '56px', height: '56px', borderRadius: '1rem',
            background: iconBg,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            transform: hov ? 'rotate(-8deg) scale(1.1)' : 'rotate(0deg) scale(1)',
            transition: 'transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)',
          }}>
            {icon}
          </div>
          <div>
            <div style={{ fontSize: '0.7rem', fontWeight: '800', color: accentColor, textTransform: 'uppercase', letterSpacing: '0.12em', marginBottom: '0.2rem' }}>{label}</div>
            <h2 style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '900', fontSize: '1.75rem', lineHeight: 1, color: 'var(--text)', letterSpacing: '-0.02em' }}>{title}</h2>
          </div>
        </div>

        <p style={{ fontSize: '0.78rem', fontWeight: '700', color: accentColor, marginBottom: '0.4rem', letterSpacing: '0.01em' }}>{subtitle}</p>
        <p style={{ fontSize: '0.9rem', color: 'var(--text-muted)', lineHeight: 1.65, marginBottom: '1.5rem' }}>{desc}</p>

        {/* Stats row */}
        <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1.75rem', flexWrap: 'wrap' }}>
          {stats.map(s => (
            <span key={s.label} style={{
              display: 'inline-flex', alignItems: 'center', gap: '0.3rem',
              background: `${accentColor}0d`,
              border: `1px solid ${accentColor}25`,
              borderRadius: '9999px', padding: '0.3rem 0.75rem',
              fontSize: '0.75rem', color: accentColor, fontWeight: '600',
            }}>
              {s.icon} {s.label}
            </span>
          ))}
        </div>

        {/* CTA */}
        <div style={{
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          padding: '0.9rem 1.25rem',
          background: hov ? gradient : 'transparent',
          border: `1.5px solid ${hov ? 'transparent' : accentColor + '30'}`,
          borderRadius: '0.85rem',
          color: hov ? '#fff' : accentColor,
          fontWeight: '700', fontSize: '0.9rem',
          boxShadow: hov ? `0 8px 24px ${accentGlow}` : 'none',
        }}>
          Enter Portal
          <ArrowRight size={18} style={{ transform: hov ? 'translateX(5px)' : 'translateX(0)', transition: 'transform 0.25s' }} />
        </div>
      </div>
    </div>
  );
};
