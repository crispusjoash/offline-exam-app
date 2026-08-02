import json
import re

filepath = 'src/data/kpsea-kiswahili-2022.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

data = content.replace('export const kpseaKiswahili2022 = ', '').strip(';\n')
js = json.loads(data)

# Process q10-12
q10_12 = js['sharedContexts']['ctx-kisw-2022-q10-12']
text = q10_12['text']

# The preamble is everything before the table. The table starts with | VIKUNDI |
preamble = text.split('| VIKUNDI |')[0].strip()

# Replace with preamble + image markdown
new_text = preamble + "\n\n![Jedwali](/assets/kiswahili_2022_table_10_12.svg)"

js['sharedContexts']['ctx-kisw-2022-q10-12']['text'] = new_text

new_content = "export const kpseaKiswahili2022 = " + json.dumps(js, indent=2) + ";\n"
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated kpsea-kiswahili-2022.js successfully!")
