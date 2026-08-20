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
  data.sharedContexts['kjsea_agric_2025_q29_30'] = {
    type: 'image',
    imagePath: '/assets/kjsea_agric_2025_q29_30.png',
    noFilter: true
  };

  // Update questions 29 and 30
  data.sectionA.forEach(q => {
    if (q.id === 'q29' || q.id === 'q30') {
      q.contextRef = 'kjsea_agric_2025_q29_30';
    }
  });

  fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
  console.log(`Updated ${filePath}`);
}

updateFile(path1);
updateFile(path2);
