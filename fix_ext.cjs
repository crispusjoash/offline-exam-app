const fs = require('fs');

try {
    let content = fs.readFileSync('src/data/pastPapers.js', 'utf8');

    // Replace literal tab + "ext" with "\\text"
    // In JavaScript regex, \t matches a literal tab character.
    content = content.replace(/\text/g, '\\\\text');

    fs.writeFileSync('src/data/pastPapers.js', content, 'utf8');
    console.log('Fixed literal tabs / ext in pastPapers.js');
} catch (e) {
    console.error(e);
}
