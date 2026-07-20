
const fs = require("fs");

let content = fs.readFileSync("src/data/pastPapers.js", "utf8");
const exportIndex = content.indexOf("export const PAST_PAPERS");

// The original file without the corrupted top part:
let originalContent = content.substring(exportIndex);

// We need to extract the CASS paper object string from the top part.
// The top part looks like:
// ,
//     {
//         "id": "kpsea-cass-2023",
// ...
//         "explanation": "Pending."
//       }
//     ]
//   }

// So it starts with "{" and ends with "}".
const topPart = content.substring(0, exportIndex);
const firstBrace = topPart.indexOf("{");
const lastBrace = topPart.lastIndexOf("}");
const cassString = topPart.substring(firstBrace, lastBrace + 1);

// Now we need to insert it into originalContent
// We find where the KPSEA array ends.
// In the original file, it ended with:
//         "explanation": "..."
//       }
//     ]
//   },
//   KJSEA: [

// Wait, the structure of PAST_PAPERS is:
// export const PAST_PAPERS = {
//   KPSEA: [
//     { ... }
//   ],
//   KJSEA: []
// };
const kjseaIndex = originalContent.indexOf("KJSEA: [");
const arrayEndBracket = originalContent.lastIndexOf("]", kjseaIndex - 1);

// arrayEndBracket points to the ] that closes the KPSEA array.
// Let us insert a comma and cassString before that bracket.
// But wait, the previous paper might not have a comma.
// The previous paper ends with `}`. So it would be `}, cassString ]`.
// Let us find the last `}` before `arrayEndBracket`.
const lastPaperBrace = originalContent.lastIndexOf("}", arrayEndBracket);

const newFileContent = originalContent.substring(0, lastPaperBrace + 1) + 
                       ",\n    " + cassString + "\n  " + 
                       originalContent.substring(arrayEndBracket);

fs.writeFileSync("src/data/pastPapers.js", newFileContent);
console.log("Fixed the file entirely!");

