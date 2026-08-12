import React from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const katexCache = new Map();

const SafeMath = React.memo(({ math }) => {
  if (katexCache.has(math)) {
    return <span dangerouslySetInnerHTML={{ __html: katexCache.get(math) }} />;
  }

  let html = '';
  try {
    html = katex.renderToString(math, {
      throwOnError: false,
      strict: false,
      output: 'html',
    });
    katexCache.set(math, html);
  } catch {
    return <span style={{ color: '#f87171', fontSize: '0.85em' }}>[{math}]</span>;
  }
  return <span dangerouslySetInnerHTML={{ __html: html }} />;
});

// Render a plain text segment, processing **bold**, *italic*, and <u>underline</u> within it
const renderTextWithFormatting = (text, keyPrefix) => {
  if (!text.includes('**') && !text.includes('*') && !text.includes('<u>')) return <span key={keyPrefix}>{text}</span>;
  
  const boldParts = text.split('**');
  return (
    <span key={keyPrefix}>
      {boldParts.map((part, i) => {
        if (!part) return null;
        const isBold = i % 2 !== 0;
        
        const italicParts = part.split('*');
        const renderedItalic = italicParts.map((iPart, j) => {
          if (!iPart) return null;
          const isItalic = j % 2 !== 0;

          if (!iPart.includes('<u>')) {
            return isItalic ? (
              <em key={`it-${j}`} style={{ fontStyle: 'italic' }}>{iPart}</em>
            ) : (
              <React.Fragment key={`t-${j}`}>{iPart}</React.Fragment>
            );
          }

          const uParts = iPart.split('<u>');
          const renderedU = uParts.map((uPart, k) => {
            if (k === 0) return uPart ? <React.Fragment key={`ut-${k}`}>{uPart}</React.Fragment> : null;
            const closeSplit = uPart.split('</u>');
            const underlined = closeSplit[0];
            const rest = closeSplit[1] || '';
            return (
              <React.Fragment key={`u-${k}`}>
                <u>{underlined}</u>
                {rest ? <React.Fragment key={`r-${k}`}>{rest}</React.Fragment> : null}
              </React.Fragment>
            );
          });

          return isItalic ? (
            <em key={`it-${j}`} style={{ fontStyle: 'italic' }}>{renderedU}</em>
          ) : (
            <React.Fragment key={`t-${j}`}>{renderedU}</React.Fragment>
          );
        });

        return isBold ? <strong key={i} style={{ fontWeight: '700' }}>{renderedItalic}</strong> : <React.Fragment key={i}>{renderedItalic}</React.Fragment>;
      })}
    </span>
  );
};

export const MathRenderer = React.memo(({ text }) => {
  if (!text) return null;

  if (!text.includes('$') && !text.includes('**') && !text.includes('*') && !text.includes('<u>')) return <span style={{ whiteSpace: 'pre-wrap' }}>{text}</span>;

  const parts = text.split('$');
  return (
    <span style={{ whiteSpace: 'pre-wrap' }}>
      {parts.map((part, index) =>
        index % 2 === 0
          ? (part ? renderTextWithFormatting(part, index) : null)
          : (part ? <SafeMath key={index} math={part} /> : null)
      )}
    </span>
  );
});
