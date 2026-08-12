import json
import re
import os

filepath = 'src/data/kpsea-kiswahili-2022.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract json
data = content.replace('export const kpseaKiswahili2022 = ', '').strip(';\n')
js = json.loads(data)

# Process q1-5
q1_5 = js['sharedContexts']['ctx-kisw-2022-q1-5']
if q1_5['type'] == 'dialogue':
    lines_md = []
    for line in q1_5['lines']:
        if line['type'] == 'stage':
            lines_md.append(f"*({line['text']})*")
        elif line['type'] == 'speech':
            stage = f" *({line['stage']})*" if line['stage'] else ""
            lines_md.append(f"**{line['speaker']}**:{stage} {line['text']}")
    
    js['sharedContexts']['ctx-kisw-2022-q1-5'] = {
        "title": q1_5["title"],
        "type": "text",
        "text": "\n\n".join(lines_md)
    }

# Process q10-12
q10_12 = js['sharedContexts']['ctx-kisw-2022-q10-12']
if q10_12['type'] == 'table':
    preamble = q10_12['preamble']
    headers = q10_12['headers']
    rows = q10_12['rows']
    
    md_table = []
    md_table.append("| " + " | ".join(headers) + " |")
    md_table.append("|" + "|".join(["---"] * len(headers)) + "|")
    
    for row in rows:
        md_table.append("| " + " | ".join(row) + " |")
    
    text = preamble + "\n\n" + "\n".join(md_table)
    
    js['sharedContexts']['ctx-kisw-2022-q10-12'] = {
        "title": q10_12["title"],
        "type": "text",
        "text": text
    }

new_content = "export const kpseaKiswahili2022 = " + json.dumps(js, indent=2) + ";\n"
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated kpsea-kiswahili-2022.js successfully!")
