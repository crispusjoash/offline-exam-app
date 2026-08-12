import React, { useState, useRef, useEffect } from 'react';
import { ZoomIn, ZoomOut } from 'lucide-react';

const MAX_ZOOM = 8;

export const ZoomableImage = ({ src, alt, baseMaxHeight = '28vh', scanEffect = true, customFilter }) => {
  const [scale, setScale] = useState(1);
  const containerRef = useRef(null);

  const zoomIn = () => setScale(s => Math.min(parseFloat((s + 0.125).toFixed(3)), MAX_ZOOM));
  const zoomOut = () => setScale(s => Math.max(parseFloat((s - 0.125).toFixed(3)), 1));

  // When scale changes, re-center the scroll position so no side is truncated
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;
    requestAnimationFrame(() => {
      // Center horizontally and start from top
      el.scrollLeft = (el.scrollWidth - el.clientWidth) / 2;
      el.scrollTop = 0;
    });
  }, [scale]);

  // Reset scale when src changes
  useEffect(() => {
    setScale(1);
  }, [src]);

  return (
    <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: '0.4rem' }}>
      {/* Controls */}
      <div style={{
        alignSelf: 'center',
        display: 'flex', gap: '0.2rem',
        background: 'rgba(255,255,255,0.9)',
        padding: '0.2rem', borderRadius: '0.5rem',
        border: '1px solid var(--border-bright)',
        boxShadow: 'var(--shadow-sm)'
      }}>
        <button
          onClick={zoomOut}
          disabled={scale <= 1}
          style={{ border: 'none', background: 'none', cursor: scale <= 1 ? 'default' : 'pointer', padding: '0.3rem 0.5rem', color: scale <= 1 ? 'var(--text-faint)' : 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.72rem', fontWeight: '700' }}
        >
          <ZoomOut size={16} />
        </button>
        <div style={{ width: '1px', background: 'var(--border-bright)', margin: '0.2rem 0' }} />
        <span style={{ display: 'flex', alignItems: 'center', padding: '0 0.4rem', fontSize: '0.72rem', fontWeight: '700', color: 'var(--text-muted)', minWidth: '2.5rem', justifyContent: 'center' }}>
          {Math.round(scale * 100)}%
        </span>
        <div style={{ width: '1px', background: 'var(--border-bright)', margin: '0.2rem 0' }} />
        <button
          onClick={zoomIn}
          disabled={scale >= MAX_ZOOM}
          style={{ border: 'none', background: 'none', cursor: scale >= MAX_ZOOM ? 'default' : 'pointer', padding: '0.3rem 0.5rem', color: scale >= MAX_ZOOM ? 'var(--text-faint)' : 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.72rem', fontWeight: '700' }}
        >
          <ZoomIn size={16} />
        </button>
      </div>

      {/* Scroll container — overflow:auto lets user scroll in ALL directions */}
      <div
        ref={containerRef}
        style={{
          width: '100%',
          maxHeight: scale === 1 ? baseMaxHeight : '65vh',
          overflow: scale > 1 ? 'auto' : 'hidden',
          borderRadius: '0.5rem',
          transition: 'max-height 0.3s ease',
          boxSizing: 'border-box',
          /* CRITICAL: use block layout (not flex) so the inner wrapper
             can expand freely and scrollLeft/scrollTop work correctly
             to reach ALL sides of the image */
        }}
      >
        {/* Inner wrapper — min-width ensures the container is wide enough
            to hold the scaled image, preventing left-side clipping */}
        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'flex-start',
            minWidth: scale > 1 ? 'max-content' : '100%',
            minHeight: scale > 1 ? 'max-content' : undefined,
            padding: scale > 1 ? '0.5rem' : '0',
            boxSizing: 'border-box',
          }}
        >
          <img
            src={src}
            alt={alt}
            loading="lazy"
            style={{
              display: 'block',
              flexShrink: 0,
              height: scale === 1 ? 'auto' : `calc(${baseMaxHeight} * ${scale})`,
              maxHeight: scale === 1 ? baseMaxHeight : 'none',
              width: 'auto',
              maxWidth: scale === 1 ? '100%' : 'none',
              objectFit: 'contain',
              transition: 'height 0.2s ease, max-height 0.2s ease',
              borderRadius: '0.5rem',
              filter: customFilter ? customFilter : (scanEffect ? 'grayscale(100%) contrast(160%) brightness(115%)' : 'none'),
              mixBlendMode: scanEffect ? 'multiply' : 'normal',
            }}
          />
        </div>
      </div>
    </div>
  );
};
