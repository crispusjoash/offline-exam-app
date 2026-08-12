const fs = require('fs');

const logs = fs.readFileSync('C:/Users/JOASH/.gemini/antigravity/brain/8ad7f170-147c-4fcb-8ed4-53a319ca7f66/.system_generated/logs/transcript.jsonl', 'utf8');
const lines = logs.split('\n');

let content = '';

for (let line of lines) {
    if (!line) continue;
    try {
        const entry = JSON.parse(line);
        if (entry.type === 'PLANNER_RESPONSE' && entry.tool_calls) {
            for (let tc of entry.tool_calls) {
                if (!tc.args) continue;
                
                const target = tc.args.TargetFile;
                if (target && target.includes('pastPapers.js')) {
                    if (tc.name === 'write_to_file') {
                        content = tc.args.CodeContent;
                    } else if (tc.name === 'replace_file_content') {
                        content = content.replace(tc.args.TargetContent, tc.args.ReplacementContent);
                    } else if (tc.name === 'multi_replace_file_content') {
                        for (let chunk of tc.args.ReplacementChunks) {
                            content = content.replace(chunk.TargetContent, chunk.ReplacementContent);
                        }
                    }
                }
            }
        }
    } catch (e) { }
}

fs.writeFileSync('src/data/pastPapers.js', content);
console.log('Successfully recovered pastPapers.js to last known state from logs!');
