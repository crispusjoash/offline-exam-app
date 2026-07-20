const fs = require('fs');

try {
    let content = fs.readFileSync('src/data/pastPapers.js', 'utf8');

    // Find all explanation: "..." spanning multiple lines
    content = content.replace(/explanation:\s*"([^"]*)"/g, (match, p1) => {
        // Replace all actual newlines in the string with the literal string \n
        let cleaned = p1.replace(/\r?\n/g, '\\n');
        return `explanation: "${cleaned}"`;
    });

    fs.writeFileSync('src/data/pastPapers.js', content, 'utf8');
    console.log('Fixed newlines in pastPapers.js');
} catch (e) {
    console.error(e);
}
