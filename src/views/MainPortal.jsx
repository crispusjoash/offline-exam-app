import React from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  BookOpen, 
  GraduationCap, 
  ArrowRight, 
  Trophy, 
  Clock, 
  CheckCircle2, 
  Zap, 
  ShieldCheck, 
  Sparkles,
  Layers
} from 'lucide-react';

export const MainPortal = () => {
  const navigate = useNavigate();

  return (
    <div className="portal-container">

      {/* ── Hero Banner ── */}
      <section className="portal-hero">
        {/* Decorative blobs */}
        <div style={{ position: 'absolute', top: '-40px', right: '-40px', width: '200px', height: '200px', borderRadius: '50%', background: 'radial-gradient(circle, rgba(59,130,246,0.3) 0%, transparent 70%)', pointerEvents: 'none' }} />
        <div style={{ position: 'absolute', bottom: '-60px', left: '30%', width: '220px', height: '220px', borderRadius: '50%', background: 'radial-gradient(circle, rgba(147,51,234,0.25) 0%, transparent 70%)', pointerEvents: 'none' }} />

        <div style={{ position: 'relative', zIndex: 2 }}>
          <div style={{
            display: 'inline-flex', alignItems: 'center', gap: '0.4rem',
            background: 'rgba(255, 255, 255, 0.1)',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            borderRadius: '9999px', padding: '0.25rem 0.75rem',
            fontSize: '0.72rem', color: '#f1f5f9', fontWeight: '600',
            marginBottom: '0.85rem',
          }}>
            <Trophy size={12} color="#f59e0b" /> KNEC Assessment Standards
          </div>

          <h1 style={{
            fontFamily: 'Outfit, sans-serif',
            fontSize: 'clamp(1.6rem, 4vw, 2.5rem)',
            fontWeight: '900',
            lineHeight: 1.1,
            letterSpacing: '-0.02em',
            marginBottom: '0.6rem',
            color: '#ffffff',
          }}>
            Master Your Exams{' '}
            <span style={{ background: 'linear-gradient(135deg, #60a5fa, #c084fc)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
              Offline
            </span>
          </h1>

          <p style={{ fontSize: '0.9rem', color: 'var(--text-faint)', lineHeight: 1.55, marginBottom: '1.1rem', maxWidth: '520px' }}>
            Practice official past papers with instant auto-grading and step-by-step teacher explanations.
          </p>

          {/* Subject pills */}
          <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
            {['Mathematics', 'English', 'Kiswahili', 'Science & Tech', 'Social Studies'].map(subject => (
              <span key={subject} style={{
                fontSize: '0.68rem', fontWeight: '600',
                background: 'rgba(255, 255, 255, 0.08)',
                border: '1px solid rgba(255, 255, 255, 0.12)',
                color: '#cbd5e1', padding: '0.2rem 0.6rem',
                borderRadius: '0.4rem', whiteSpace: 'nowrap',
              }}>
                {subject}
              </span>
            ))}
          </div>
        </div>
      </section>

      <div className="portal-content-grid">
        {/* ── Section Label ── */}
      <div style={{ marginBottom: '1rem' }}>
        <h2 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.2rem', fontWeight: '800', color: 'var(--text)' }}>
          Select Assessment Level
        </h2>
        <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: '0.15rem' }}>
          Choose your grade level to access past examination papers
        </p>
      </div>

      {/* ── Portal Cards ── */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
        gap: '1.1rem',
        marginBottom: '1.75rem',
        width: '100%',
      }}>
        <PortalCard
          onClick={() => navigate('/papers/KPSEA')}
          accentColor="#2563eb"
          gradient="linear-gradient(90deg, #2563eb, #3b82f6)"
          shadowColor="rgba(37, 99, 235, 0.15)"
          hoverBorder="#3b82f6"
          iconBg="linear-gradient(135deg, #dbeafe, #eff6ff)"
          icon={<BookOpen size={22} strokeWidth={2.2} color="#2563eb" />}
          grade="Grade 6"
          gradeBg="#eff6ff"
          gradeColor="#2563eb"
          gradeBorder="#bfdbfe"
          title="KPSEA"
          subtitle="Kenya Primary School Education Assessment"
          subtitleColor="#2563eb"
          desc="Complete auto-graded multiple choice questions with detailed explanations for every subject."
          stats={[
            { icon: <CheckCircle2 size={12} color="#2563eb" />, label: '40 MCQs per Paper' },
            { icon: <Clock size={12} color="#2563eb" />, label: '60 Min Timer' },
          ]}
          actionColor="#2563eb"
          actionLabel="Explore KPSEA Papers"
        />

        <PortalCard
          onClick={() => navigate('/papers/KJSEA')}
          accentColor="#7c3aed"
          gradient="linear-gradient(90deg, #7c3aed, #db2777)"
          shadowColor="rgba(124, 58, 237, 0.15)"
          hoverBorder="#9333ea"
          iconBg="linear-gradient(135deg, #f3e8ff, #f5f3ff)"
          icon={<GraduationCap size={22} strokeWidth={2.2} color="#7c3aed" />}
          grade="Grade 9"
          gradeBg="#f5f3ff"
          gradeColor="#7c3aed"
          gradeBorder="#ddd6fe"
          title="KJSEA"
          subtitle="Kenya Junior Secondary Education Assessment"
          subtitleColor="#7c3aed"
          desc="MCQ Section A auto-graded + Section B structured practice questions with marking rubrics."
          stats={[
            { icon: <Layers size={12} color="#7c3aed" />, label: 'Sec A & B Papers' },
            { icon: <Clock size={12} color="#7c3aed" />, label: '120 Min Timer' },
          ]}
          actionColor="#7c3aed"
          actionLabel="Explore KJSEA Papers"
        />
      </div>

      {/* ── Feature Highlights ── */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))',
        gap: '0.85rem',
        width: '100%',
      }}>
        {[
          { icon: <Zap size={17} color="#2563eb" />, bg: '#eff6ff', title: 'Instant Auto-Grading', desc: 'Get your full score breakdown immediately on submission.' },
          { icon: <Sparkles size={17} color="#7c3aed" />, bg: '#f5f3ff', title: 'Step-by-step Explanations', desc: 'Detailed teacher rationale for every question.' },
          { icon: <ShieldCheck size={17} color="#059669" />, bg: '#ecfdf5', title: '100% Offline Practice', desc: 'No internet needed to write or review exams.' },
        ].map((feat, idx) => (
          <div key={idx} style={{
            background: 'var(--bg-card)',
            border: '1px solid #e2e8f0',
            borderRadius: '0.9rem',
            padding: '1rem',
            display: 'flex',
            alignItems: 'flex-start',
            gap: '0.75rem',
            boxSizing: 'border-box',
          }}>
            <div style={{
              width: '34px', height: '34px', borderRadius: '0.6rem',
              background: feat.bg, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0,
            }}>
              {feat.icon}
            </div>
            <div style={{ minWidth: 0 }}>
              <h4 style={{ fontFamily: 'Outfit, sans-serif', fontWeight: '700', fontSize: '0.88rem', color: 'var(--text)', marginBottom: '0.15rem' }}>
                {feat.title}
              </h4>
              <p style={{ fontSize: '0.76rem', color: 'var(--text-muted)', lineHeight: 1.45 }}>
                {feat.desc}
              </p>
            </div>
          </div>
        ))}
      </div>
      </div>
    </div>
  );
};

const PortalCard = ({ onClick, accentColor, gradient, shadowColor, hoverBorder, iconBg, icon, grade, gradeBg, gradeColor, gradeBorder, title, subtitle, subtitleColor, desc, stats, actionColor, actionLabel }) => {
  const [hov, setHov] = React.useState(false);

  return (
    <div
      onClick={onClick}
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      onTouchStart={() => setHov(true)}
      onTouchEnd={() => setHov(false)}
      style={{
        background: 'var(--bg-card)',
        borderRadius: '1.15rem',
        padding: '1.35rem',
        border: `1.5px solid ${hov ? hoverBorder : '#e2e8f0'}`,
        boxShadow: hov ? `0 12px 28px -4px ${shadowColor}` : '0 2px 8px rgba(15,23,42,0.05)',
        cursor: 'pointer',
        position: 'relative',
        overflow: 'hidden',
        display: 'flex',
        flexDirection: 'column',
        transition: 'all 0.22s ease',
        transform: hov ? 'translateY(-2px)' : 'translateY(0)',
        width: '100%',
        boxSizing: 'border-box',
      }}
    >
      {/* Top accent bar */}
      <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: '4px', background: gradient }} />

      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.85rem' }}>
        <div style={{
          width: '42px', height: '42px', borderRadius: '0.8rem',
          background: iconBg, display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}>
          {icon}
        </div>
        <span style={{
          fontSize: '0.68rem', fontWeight: '800', letterSpacing: '0.06em', textTransform: 'uppercase',
          background: gradeBg, color: gradeColor, padding: '0.28rem 0.65rem',
          borderRadius: '9999px', border: `1px solid ${gradeBorder}`,
          whiteSpace: 'nowrap',
        }}>
          {grade}
        </span>
      </div>

      <h3 style={{ fontFamily: 'Outfit, sans-serif', fontSize: '1.45rem', fontWeight: '800', color: 'var(--text)', marginBottom: '0.2rem' }}>
        {title}
      </h3>
      <p style={{ fontSize: '0.78rem', fontWeight: '600', color: subtitleColor, marginBottom: '0.6rem' }}>
        {subtitle}
      </p>
      <p style={{ fontSize: '0.83rem', color: 'var(--text-muted)', lineHeight: 1.5, marginBottom: '1rem', flex: 1 }}>
        {desc}
      </p>

      <div style={{ display: 'flex', gap: '0.6rem', flexWrap: 'wrap', marginBottom: '1rem' }}>
        {stats.map((s, i) => (
          <div key={i} style={{ display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.74rem', color: 'var(--text-secondary)', background: 'var(--bg-muted)', padding: '0.22rem 0.55rem', borderRadius: '0.45rem', border: '1px solid #e2e8f0' }}>
            {s.icon} {s.label}
          </div>
        ))}
      </div>

      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        paddingTop: '0.85rem', borderTop: '1px solid #f1f5f9',
        fontWeight: '700', fontSize: '0.85rem', color: actionColor,
      }}>
        <span>{actionLabel}</span>
        <div style={{
          width: '28px', height: '28px', borderRadius: '50%',
          background: actionColor, display: 'flex', alignItems: 'center', justifyContent: 'center',
          color: 'var(--bg-card)', flexShrink: 0,
        }}>
          <ArrowRight size={14} />
        </div>
      </div>
    </div>
  );
};
