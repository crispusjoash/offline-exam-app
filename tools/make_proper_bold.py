import json
import re

file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\src\data\kpsea-english-2023.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'export const kpseaEnglish2023 = (\{.*\});?', content, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    
    for q in data["sectionA"]:
        if "explanation" in q:
            exp = q["explanation"]
            
            # Make sure we clean out any legacy messy asterisks first
            exp = exp.replace('*', '')
            
            lines = exp.split('\n')
            new_lines = []
            for line in lines:
                # 1. Concept Overview header
                if line.startswith('📌 Concept Overview:'):
                    line = re.sub(r'^📌 Concept Overview:\s*(.*)', r'📌 **Concept Overview: \1**', line)
                
                # 2. Why Option X is Correct header
                elif line.startswith('✅ Why Option'):
                    line = re.sub(r'^✅ Why Option ([A-D]) (.*?)( is Correct:)', r'✅ **Why Option \1 \2\3**', line)
                    # fallback if regex didn't hit perfectly
                    if not line.startswith('✅ **'):
                        line = re.sub(r'^✅ (.*)', r'✅ **\1**', line)
                
                # 3. Detailed Analysis header
                elif line.startswith('❌ Detailed Analysis of Incorrect Options:'):
                    line = '❌ **Detailed Analysis of Incorrect Options:**'
                
                # 4. Key Takeaway header
                elif line.startswith('💡 Key Takeaway'):
                    line = re.sub(r'^💡 (.*)', r'💡 **\1**', line)
                
                # 5. Bullet Option headers (e.g. • Option A ("..."):)
                elif line.startswith('• Option '):
                    line = re.sub(r'^• Option ([A-D])', r'• **Option \1**', line)
                
                # 6. Why it's wrong line
                elif 'Why it\'s wrong:' in line:
                    line = re.sub(r'(\s*-\s*)Why it\'s wrong:', r'\1**Why it\'s wrong:**', line)
                elif 'Why it is wrong:' in line:
                    line = re.sub(r'(\s*-\s*)Why it is wrong:', r'\1**Why it is wrong:**', line)
                
                # 7. Revision notes key items with arrows (e.g., - Term ➔ Explanation)
                elif line.strip().startswith('- ') and '➔' in line:
                    line = re.sub(r'^(\s*-\s*)(.*?)(\s*➔)', r'\1**\2**\3', line)
                
                new_lines.append(line)
            
            q["explanation"] = '\n'.join(new_lines)
            
    new_content = "export const kpseaEnglish2023 = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully converted all section & list headers to bold Markdown (**).")
else:
    print("Could not match JS object")
