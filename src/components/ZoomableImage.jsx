import React, { useState } from 'react';
import { ZoomIn, ZoomOut } from 'lucide-react';

export const ZoomableImage = ({ src, alt, baseMaxHeight = '28vh', scanEffect = true, customFilter }) => {
  const [scale, setScale] = useState(1);

  const zoomIn = () => setScale(s => Math.min(s + 0.5, 3));
  const zoomOut = () => setScale(s => Math.max(s - 0.5, 1));

  return (
    <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: '0.4rem' }}>
      {/* Controls */}
      <div style={{ 
        alignSelf: 'flex-end',
        display: 'flex', gap: '0.2rem',
        background: 'rgba(255,255,255,0.9)',
        padding: '0.2rem', borderRadius: '0.5rem',
        border: '1px solid var(--border-bright)',
        boxShadow: 'var(--shadow-sm)'
      }}>
        <button onClick={zoomOut} disabled={scale === 1} style={{ border: 'none', background: 'none', cursor: scale === 1 ? 'default' : 'pointer', padding: '0.3rem', color: scale === 1 ? 'var(--text-faint)' : 'var(--text-secondary)', display: 'flex' }}>
          <ZoomOut size={16} />
        </button>
        <div style={{ width: '1px', background: 'var(--border-bright)', margin: '0.2rem 0' }} />
        <button onClick={zoomIn} disabled={scale >= 3} style={{ border: 'none', background: 'none', cursor: scale >= 3 ? 'default' : 'pointer', padding: '0.3rem', color: scale >= 3 ? 'var(--text-faint)' : 'var(--text-secondary)', display: 'flex' }}>
          <ZoomIn size={16} />
        </button>
      </div>

      {/* Image container */}
      <div style={{ 
        width: '100%', 
        maxHeight: scale === 1 ? baseMaxHeight : '65vh', 
        overflow: scale > 1 ? 'auto' : 'hidden',
        display: scale === 1 ? 'flex' : 'block',
        justifyContent: scale === 1 ? 'center' : 'initial',
        alignItems: scale === 1 ? 'center' : 'initial',
        textAlign: 'center',
        borderRadius: '0.5rem',
        transition: 'max-height 0.3s ease',
      }}>
        <img 
          src={src} 
          alt={alt} 
          style={{ 
            height: scale === 1 ? 'auto' : `calc(${baseMaxHeight} * ${scale})`,
            maxHeight: scale === 1 ? baseMaxHeight : 'none',
            width: 'auto',
            maxWidth: scale === 1 ? '100%' : 'none',
            objectFit: 'contain',
            transition: 'height 0.2s ease, max-height 0.2s ease',
            borderRadius: '0.5rem',
            filter: customFilter ? customFilter : (scanEffect ? 'grayscale(100%) contrast(160%) brightness(115%)' : 'none'),
            mixBlendMode: scanEffect ? 'multiply' : 'normal',
            verticalAlign: 'middle',
          }} 
        />
      </div>
    </div>
  );
};
