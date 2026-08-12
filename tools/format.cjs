const fs = require('fs');

let content = fs.readFileSync('src/data/pastPapers.js', 'utf8');

// Regex to find all explanations
content = content.replace(/explanation:\s*"([^"]*)"/g, (match, p1) => {
    // Skip explanations that already have markdown newlines or bolding
    if (p1.includes('\\n') || p1.includes('**')) {
        return match;
    }
    
    let text = p1;
    // Match sentences (anything ending in . ? or ! followed by space or end)
    let sentences = text.match(/[^.?!]+[.?!]+(?:\s|$)/g);
    
    // If we couldn't parse it well or it's a single short sentence, skip
    if (!sentences || sentences.length < 2) return match;
    
    sentences = sentences.map(s => s.trim());
    
    // Format sentences
    sentences = sentences.map((s, idx) => {
        let formatted = s;
        
        // Highlight single quoted words which are often options/quotes
        formatted = formatted.replace(/'([^']+)'/g, "**'$1'**");
        
        // Highlight correct/incorrect keywords in English
        formatted = formatted.replace(/\b(is correct|is incorrect|incorrect because|correct answer|correct because)\b/gi, "**$1**");
        
        // Highlight Swahili keywords
        formatted = formatted.replace(/\b(Chaguo sahihi|Chaguo hili si sahihi|si sahihi|kwa sababu)\b/gi, "**$1**");
        
        return formatted;
    });

    // Join with double line breaks for beautiful spacing
    let newExp = sentences.join('\\n\\n');
    
    return `explanation: "${newExp}"`;
});

fs.writeFileSync('src/data/pastPapers.js', content);
console.log("Successfully formatted explanations!");
