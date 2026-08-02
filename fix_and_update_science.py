import json
import re

with open('src/data/kpsea-science-2023.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's import explanations_map from update_science_complete
from update_science_complete import explanations_map

# Rebuild sectionA from scratch or replace each question's explanation accurately!
# We can find each question object and replace its "explanation": ...
for q_num, exp_text in explanations_map.items():
    # Find "questionNumber": q_num
    q_str = f'"questionNumber": {q_num},'
    q_pos = content.find(q_str)
    if q_pos != -1:
        # Find next "explanation": 
        exp_pos = content.find('"explanation":', q_pos)
        if exp_pos != -1:
            # Find the end of this explanation property (before \n    } or \n  })
            # It starts after "explanation": "
            quote_start = content.find('"', exp_pos + 14)
            # To find quote_end, search for quote followed by comma or newline brace
            # Since JSON string escapes quotes as \", we find quote not preceded by \
            curr = quote_start + 1
            while curr < len(content):
                if content[curr] == '"' and content[curr-1] != '\\':
                    # Check if next non-whitespace is } or ,
                    rest = content[curr+1:curr+30].lstrip()
                    if rest.startswith('}') or rest.startswith(','):
                        quote_end = curr
                        break
                curr += 1
            
            # Replace between quote_start and quote_end + 1
            new_json_exp = json.dumps(exp_text)
            content = content[:exp_pos] + '"explanation": ' + new_json_exp + content[quote_end+1:]

with open('src/data/kpsea-science-2023.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced all 50 explanations precisely.")
