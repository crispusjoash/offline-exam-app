import React from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const SafeMath = ({ math }) => {
  let html = '';
  try {
    html = katex.renderToString(math, {
      throwOnError: false,
      strict: false,
      output: 'html',
    });
  } catch {
    return <span style={{ color: '#f87171', fontSize: '0.85em' }}>[{math}]</span>;
  }
  return <span dangerouslySetInnerHTML={{ __html: html }} />;
};

// Render a plain text segment, processing **bold** markdown within it
const renderTextWithBold = (text, keyPrefix) => {
  if (!text.includes('**')) return <span key={keyPrefix}>{text}</span>;
  const boldParts = text.split('**');
  return (
    <span key={keyPrefix}>
      {boldParts.map((part, i) =>
        i % 2 === 0
          ? (part ? <span key={i}>{part}</span> : null)
          : (part ? <strong key={i} style={{ fontWeight: '700' }}>{part}</strong> : null)
      )}
    </span>
  );
};

export const MathRenderer = ({ text }) => {
  if (!text) return null;

  // If no math and no bold, just render as plain text
  if (!text.includes('$') && !text.includes('**')) return <span>{text}</span>;

  // Split by $...$ math segments first
  const parts = text.split('$');
  return (
    <span>
      {parts.map((part, index) =>
        index % 2 === 0
          ? (part ? renderTextWithBold(part, index) : null)
          : (part ? <SafeMath key={index} math={part} /> : null)
      )}
    </span>
  );
};
