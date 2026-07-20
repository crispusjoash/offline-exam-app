
const fs = require("fs");

let content = fs.readFileSync("src/data/pastPapers.js", "utf8");

// 1. Find where the accidental insertion begins
const startIndex = content.indexOf(`"id": "kpsea-cass-2023"`);

if (startIndex !== -1) {
    // The insertion was roughly: ",\n    {\n        \"id\": \"kpsea-cass-2023\""
    const commaIndex = content.lastIndexOf(",", startIndex);
    
    // Now find the end of the injected object.
    const q31Index = content.indexOf(`"cass-q31"`);
    const endBracket = content.indexOf("]", q31Index); // ends sectionA array
    const endBrace = content.indexOf("}", endBracket); // ends the CASS object
    
    // The total string that was injected:
    const injectedStr = content.substring(commaIndex, endBrace + 1);
    
    // Remove it from its current location
    content = content.substring(0, commaIndex) + content.substring(endBrace + 1);
    
    // 2. Now properly find the true end of the KPSEA array.
    const kpseaArrayEnd = content.indexOf("],\n  KJSEA: []");
    
    const newContent = content.substring(0, kpseaArrayEnd) + injectedStr + "\n  " + content.substring(kpseaArrayEnd);
    
    fs.writeFileSync("src/data/pastPapers.js", newContent);
    console.log("Successfully moved CASS paper to the end of the KPSEA array!");
} else {
    console.log("Could not find CASS paper in the file.");
}

