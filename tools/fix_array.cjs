const fs = require('fs');

let content = fs.readFileSync('src/data/pastPapers.js', 'utf8');

// Find the start of the english paper
const startIdx = content.indexOf('    {\n      id: "kpsea-english-2023",');
if (startIdx === -1) {
    console.error("Could not find start");
    process.exit(1);
}

// The paper block starts with `    {\n      id: "kpsea-english-2023",`
// Let's find the closing of this paper. It's at the very end of the file.
// The end of the file currently looks like:
//         }
//       ]
//     }
//   ]
// };
// We want to slice from `    {\n      id: "kpsea-english-2023",` all the way to `    }` before `  ]\n};`.
const endOfFileIdx = content.lastIndexOf('  ]\n};');
if (endOfFileIdx === -1) {
    console.error("Could not find EOF marker");
    process.exit(1);
}

// Cut out the english paper
// It includes `    {\n ...     }\n`
let englishPaperStr = content.substring(startIdx, endOfFileIdx);
// Make sure it ends with `    }`
englishPaperStr = englishPaperStr.trimEnd();

// Remove it from the KJSEA array and restore the end of KJSEA
content = content.substring(0, startIdx) + '  ]\n};';
// Note: right before `startIdx`, there is a `    },\n`. We might need to trim that trailing comma.
content = content.replace('    },\n  ]\n};', '    }\n  ]\n};');

// Now find the end of KPSEA array.
// It looks like:
//         }
//       ]
//     }
//   ],
//   KJSEA: [
const kjseaStartIdx = content.indexOf('  KJSEA: [');
if (kjseaStartIdx === -1) {
    console.error("Could not find KJSEA array");
    process.exit(1);
}

// We want to insert the english paper right before `  ],\n  KJSEA: [`
// Wait, the KPSEA array ends with:
//     }
//   ],
// We can find `  ],\n  KJSEA: [` and replace it.
// Before `  ],\n  KJSEA: [`, there is a `    }\n`. We should change it to `    },\n` and then insert english paper.
const insertTarget = '    }\n  ],\n  KJSEA: [';
if (!content.includes(insertTarget)) {
    console.error("Could not find insert target exactly");
    process.exit(1);
}

content = content.replace(insertTarget, '    },\n' + englishPaperStr + '\n  ],\n  KJSEA: [');

fs.writeFileSync('src/data/pastPapers.js', content, 'utf8');
console.log("Successfully moved English paper to KPSEA array!");
