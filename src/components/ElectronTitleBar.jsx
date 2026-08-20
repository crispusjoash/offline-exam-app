import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { BookOpen, Minus, Square, X, Maximize2, ArrowLeft } from 'lucide-react';

const api = () => window.electronAPI;

export const ElectronTitleBar = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [isMaximized, setIsMaximized] = useState(false);
  const [isHoveringClose, setIsHoveringClose] = useState(false);
  const [isHoveringMax, setIsHoveringMax] = useState(false);
  const [isHoveringMin, setIsHoveringMin] = useState(false);

  useEffect(() => {
    // Sync initial state
    api()?.isMaximized().then(setIsMaximized);
    // Listen for maximize/restore events from main
    api()?.onMaximizeChange?.(setIsMaximized);
  }, []);

  const handleMinimize = () => api()?.minimize();
  const handleMaximize = async () => {
    const nowMaximized = await api()?.maximize();
    setIsMaximized(nowMaximized);
  };
  const handleClose = () => api()?.close();

  const isNotHome = location.pathname !== '/';

  return (
    <div
      id="electron-title-bar"
      style={{
        height: '40px',
        width: '100%',
        background: 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        WebkitAppRegion: 'drag',
        userSelect: 'none',
        flexShrink: 0,
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        zIndex: 9999,
        borderBottom: '1px solid rgba(255,255,255,0.06)',
      }}
    >
      {/* Left: Sticky Windows Back Button + App branding */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: '0.65rem',
        padding: '0 0.75rem',
      }}>
        {/* Sticky Back Button for Windows App — visible on all pages except root Home */}
        {isNotHome && (
          <button
            onClick={() => navigate(-1)}
            id="electron-sticky-back-btn"
            title="Go Back"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.35rem',
              background: 'rgba(255, 255, 255, 0.12)',
              border: '1px solid rgba(255, 255, 255, 0.25)',
              borderRadius: '6px',
              padding: '0.22rem 0.65rem',
              color: '#ffffff',
              fontSize: '0.74rem',
              fontWeight: '700',
              cursor: 'pointer',
              WebkitAppRegion: 'no-drag',
              transition: 'all 0.15s ease',
              boxShadow: '0 1px 4px rgba(0,0,0,0.2)',
            }}
            onMouseEnter={e => {
              e.currentTarget.style.background = 'rgba(255, 255, 255, 0.24)';
              e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.4)';
              e.currentTarget.style.transform = 'translateX(-1px)';
            }}
            onMouseLeave={e => {
              e.currentTarget.style.background = 'rgba(255, 255, 255, 0.12)';
              e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.25)';
              e.currentTarget.style.transform = 'none';
            }}
          >
            <ArrowLeft size={13} strokeWidth={2.5} />
            <span>Back</span>
          </button>
        )}

        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '0.55rem',
        }}>
          <div style={{
            width: '22px',
            height: '22px',
            borderRadius: '6px',
            background: 'linear-gradient(135deg, #3b82f6, #8b5cf6)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 2px 8px rgba(59,130,246,0.4)',
            flexShrink: 0,
          }}>
            <BookOpen size={11} color="#fff" strokeWidth={2.5} />
          </div>
          <span style={{
            fontFamily: 'Outfit, sans-serif',
            fontWeight: '700',
            fontSize: '0.78rem',
            color: 'rgba(255,255,255,0.9)',
            letterSpacing: '0.01em',
          }}>
            CBC Portal
          </span>
          <span style={{
            fontSize: '0.62rem',
            color: 'rgba(255,255,255,0.3)',
            fontWeight: '400',
          }}>
            Offline Assessment Suite
          </span>
        </div>
      </div>

      {/* Center: Drag area hint (decorative dots) */}
      <div style={{
        position: 'absolute',
        left: '50%',
        transform: 'translateX(-50%)',
        display: 'flex',
        gap: '3px',
        opacity: 0.2,
      }}>
        {[...Array(5)].map((_, i) => (
          <div key={i} style={{ width: '3px', height: '3px', borderRadius: '50%', background: '#fff' }} />
        ))}
      </div>

      {/* Right: Window controls */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        WebkitAppRegion: 'no-drag',
        height: '100%',
      }}>
        {/* Minimize */}
        <button
          onClick={handleMinimize}
          onMouseEnter={() => setIsHoveringMin(true)}
          onMouseLeave={() => setIsHoveringMin(false)}
          title="Minimize"
          style={{
            width: '46px',
            height: '100%',
            border: 'none',
            background: isHoveringMin ? 'rgba(255,255,255,0.08)' : 'transparent',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            transition: 'background 0.15s',
            color: 'rgba(255,255,255,0.7)',
          }}
        >
          <Minus size={14} />
        </button>

        {/* Maximize / Restore */}
        <button
          onClick={handleMaximize}
          onMouseEnter={() => setIsHoveringMax(true)}
          onMouseLeave={() => setIsHoveringMax(false)}
          title={isMaximized ? 'Restore' : 'Maximize'}
          style={{
            width: '46px',
            height: '100%',
            border: 'none',
            background: isHoveringMax ? 'rgba(255,255,255,0.08)' : 'transparent',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            transition: 'background 0.15s',
            color: 'rgba(255,255,255,0.7)',
          }}
        >
          {isMaximized ? <Square size={12} /> : <Maximize2 size={12} />}
        </button>

        {/* Close */}
        <button
          onClick={handleClose}
          onMouseEnter={() => setIsHoveringClose(true)}
          onMouseLeave={() => setIsHoveringClose(false)}
          title="Close"
          style={{
            width: '46px',
            height: '100%',
            border: 'none',
            background: isHoveringClose ? '#ef4444' : 'transparent',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            transition: 'background 0.15s',
            color: isHoveringClose ? '#fff' : 'rgba(255,255,255,0.7)',
            borderRadius: '0 0 0 0',
          }}
        >
          <X size={14} />
        </button>
      </div>
    </div>
  );
};
