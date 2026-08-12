import json
import re

input_file = 'kjsea_sst_2025_dump.txt'
output_file = 'src/data/kjsea-sst-2025.js'

with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Split by SECTION B if present
if 'SECTION B' in text:
    section_a_text = text.split('SECTION B')[0]
else:
    section_a_text = text

questions_data = []

# Find all questions using regex. Match a number followed by a dot at the start of a line.
pattern = r'^(\d+)\.\s+(.*?)(?=\n^\d+\.\s+|\Z)'
matches = re.findall(pattern, section_a_text, re.DOTALL | re.MULTILINE)

answers = {
    1: "law",
    2: "Arts and Sports Science",
    3: "existence of plateaus",
    4: "Topographical map.",
    5: "Traditional mode of dressing.",
    6: "arbitration",
    7: "availability of water",
    8: "Keeping to oneself.",
    9: "understanding the problems facing the community.",
    10: "population growth rate",
    11: "rural to urban migration",
    12: "measure distances",
    13: "rainforest.",
    14: "Deforestation.",
    15: "disciplining",
    16: "Prevention of drought.",
    17: "Invention of fire.",
    18: "school enrolment",
    19: "Nebula Cloud Theory",
    20: "participating in a community project"
}

shared_contexts = {
    "ctx-sst-q13": {
      "type": "image",
      "imagePath": "/assets/kjsea_sst_2025_q13.png",
      "title": "Vegetation zones diagram for Question 13"
    }
}

for match in matches:
    q_num = int(match[0])
    q_body = match[1].strip()
    
    # Extract options
    options_match = re.search(r'\nA\.\s+(.*?)\nB\.\s+(.*?)\nC\.\s+(.*?)\nD\.\s+(.*)', q_body, re.DOTALL)
    if options_match:
        raw_opts = [
            options_match.group(1).strip(),
            options_match.group(2).strip(),
            options_match.group(3).strip(),
            options_match.group(4).strip()
        ]
        q_text = q_body[:options_match.start()].strip()
    else:
        print(f"Failed to parse options for question {q_num}")
        continue
        
    context_ref = None
    if "[IMAGE_PLACEHOLDER" in q_text:
        context_ref = f"ctx-sst-q{q_num}"
        q_text = re.sub(r'\[IMAGE_PLACEHOLDER.*?\]', '', q_text).strip()
        
    correct_val = answers.get(q_num, "")
    
    options_objs = []
    for opt_str in raw_opts:
        is_corr = (opt_str.lower().strip() == correct_val.lower().strip())
        options_objs.append({
            "text": opt_str,
            "isCorrect": is_corr
        })
    
    q_obj = {
        "id": f"kjsea-sst-2025-q{q_num}",
        "questionNumber": q_num,
        "questionText": q_text,
        "options": options_objs,
        "explanation": f"The correct answer is **{correct_val}**."
    }
    
    if context_ref:
        q_obj["contextRef"] = context_ref
        
    questions_data.append(q_obj)

paper_obj = {
  "id": "kjsea-sst-2025",
  "title": "KJSEA 2025 Social Studies",
  "subject": "Social Studies",
  "year": "2025",
  "isSubPaper": False,
  "durationMinutes": 120,
  "sharedContexts": shared_contexts,
  "sectionA": questions_data,
  "sectionB": []
}

js_content = f"export const kjseaSst2025 = {json.dumps(paper_obj, indent=2, ensure_ascii=False)};\n"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully regenerated {output_file} with {len(questions_data)} questions in sectionA matching UI schema.")
