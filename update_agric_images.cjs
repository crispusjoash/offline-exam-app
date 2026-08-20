const fs = require('fs');
const path1 = './public/data/kjsea-agric-nutrition-2025.json';
const path2 = './electron/app/data/kjsea-agric-nutrition-2025.json';

function updateFile(filePath) {
  if (!fs.existsSync(filePath)) return;
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

  if (!data.sharedContexts) {
    data.sharedContexts = {};
  }

  // Add the shared contexts for the images
  data.sharedContexts['kjsea_agric_2025_q1_2'] = {
    type: 'image',
    imagePath: '/assets/kjsea_agric_2025_q1_2.png',
    noFilter: true
  };

  data.sharedContexts['kjsea_agric_2025_q4_5'] = {
    type: 'image',
    imagePath: '/assets/kjsea_agric_2025_q4_5.png',
    noFilter: true
  };

  // Update questions 1, 2, 4, 5
  data.sectionA.forEach(q => {
    if (q.id === 'q1' || q.id === 'q2') {
      q.contextRef = 'kjsea_agric_2025_q1_2';
    }
    if (q.id === 'q4' || q.id === 'q5') {
      q.contextRef = 'kjsea_agric_2025_q4_5';
    }
  });

  fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
  console.log(`Updated ${filePath}`);
}

updateFile(path1);
updateFile(path2);
