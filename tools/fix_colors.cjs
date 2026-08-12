const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/JOASH/Desktop/CBC/offline-exam-app/src/views';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.jsx'));

files.forEach(f => {
  const filePath = path.join(dir, f);
  let content = fs.readFileSync(filePath, 'utf8');
  
  // Fix invisible text
  content = content.replace(/color: '#f8fafc'/g, "color: '#0f172a'");
  content = content.replace(/color: '#ffffff'/g, "color: '#0f172a'");
  
  // Restore button text color on gradients
  content = content.replace(/color: '#0f172a', fontWeight: '700'/g, "color: '#ffffff', fontWeight: '700'");
  content = content.replace(/color: '#0f172a', fontSize: '1rem', fontWeight: '700'/g, "color: '#ffffff', fontSize: '1rem', fontWeight: '700'");
  
  // Fix borders
  content = content.replace(/border: '1px solid #334155'/g, "border: '1px solid #e2e8f0'");
  content = content.replace(/border: '1px solid #475569'/g, "border: '1px solid #e2e8f0'");
  content = content.replace(/borderBottom: '1px solid #334155'/g, "borderBottom: '1px solid #e2e8f0'");
  content = content.replace(/borderTop: '1px solid #334155'/g, "borderTop: '1px solid #e2e8f0'");
  
  // Fix backgrounds that are too dark
  content = content.replace(/background: '#0f172a'/g, "background: '#f8fafc'");
  content = content.replace(/background: '#1e293b'/g, "background: '#f1f5f9'");
  
  // Fix text colors
  content = content.replace(/color: '#334155'/g, "color: '#1e293b'");
  
  // PaperCard fix
  content = content.replace(/color: hov \? '#0f172a' : accentColor/g, "color: hov ? '#ffffff' : accentColor");
  
  // ExamSession nav buttons fix (was color: '#0f172a', but we want white on the Next button)
  content = content.replace(/color: '#0f172a', fontWeight: '700', cursor: 'pointer'/g, "color: '#ffffff', fontWeight: '700', cursor: 'pointer'");

  fs.writeFileSync(filePath, content);
});
console.log('Fixed colors globally.');
