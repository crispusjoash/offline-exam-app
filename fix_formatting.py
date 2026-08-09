import json
import re

files = ['src/data/kpsea-science-2025.js', 'src/data/kpsea-math-2025.js']

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(export const \w+ = )(\{.*\});?\s*$', content, re.DOTALL)
    if not match:
        print(f"Could not parse file {file_path}")
        continue
    
    prefix = match.group(1)
    data = json.loads(match.group(2))

    # Fix spacing
    section_key = "sectionA" if "sectionA" in data else "questions"
    for q in data.get(section_key, []):
        if "questionText" in q:
            # Fix \n\n(i) to \n(i)
            q["questionText"] = re.sub(r'\n\n(\([ivxIVX]+\))', r'\n\1', q["questionText"])
            q["questionText"] = re.sub(r'\n\n(\([a-d]\))', r'\n\1', q["questionText"])
        
        if "options" in q:
            for opt in q["options"]:
                if opt["text"].startswith('\n'):
                    opt["text"] = opt["text"].lstrip('\n')
                opt["text"] = re.sub(r'\n\n(\([ivxIVX]+\))', r'\n\1', opt["text"])

    # Fix shared contexts in Science 2025
    if "kpsea-science-2025" in file_path:
        # Q32
        q32_text = "The following picture shows a farmer carrying out a caring practice on an innovative garden. Use it to answer questions 32 to 34.\n\nIdentify the innovative garden."
        q32_inst = "The following picture shows a farmer carrying out a caring practice on an innovative garden. Use it to answer questions 32 to 34."
        q32_actual = "Identify the innovative garden."
        
        # Q37
        q37_text = "Grade 5 learners used the garden tool shown in the picture on a tree nursery. Use the picture to answer questions 37 and 38.\n\nWhat was the appropriate use of the tool on the tree nursery?"
        q37_inst = "Grade 5 learners used the garden tool shown in the picture on a tree nursery. Use the picture to answer questions 37 and 38."
        q37_actual = "What was the appropriate use of the tool on the tree nursery?"
        
        # Q42
        q42_text = "Use the following statement to answer questions 42 and 43.\nKevin wants to shallow fry an egg for breakfast using the following steps:\n\n(i) pour the beaten egg into the pan\n(ii) heat a little oil in a frying pan\n(iii) beat the egg in a bowl using a fork\n(iv) fry the egg and turn using a flat spoon and fry the other side.\n\nWhich is the correct order of steps Kevin should follow?"
        q42_inst = "Use the following statement to answer questions 42 and 43.\nKevin wants to shallow fry an egg for breakfast using the following steps:\n\n(i) pour the beaten egg into the pan\n(ii) heat a little oil in a frying pan\n(iii) beat the egg in a bowl using a fork\n(iv) fry the egg and turn using a flat spoon and fry the other side."
        q42_actual = "Which is the correct order of steps Kevin should follow?"
        
        for q in data["sectionA"]:
            if q["id"] == "q32":
                q["questionText"] = q32_actual
                if "ctx-science-2025-q32" in data.get("sharedContexts", {}):
                    data["sharedContexts"]["ctx-science-2025-q32"]["text"] = q32_inst
            elif q["id"] == "q37":
                q["questionText"] = q37_actual
                if "ctx-science-2025-q37" in data.get("sharedContexts", {}):
                    data["sharedContexts"]["ctx-science-2025-q37"]["text"] = q37_inst
            elif q["id"] == "q42":
                q["questionText"] = q42_actual
                q["contextRef"] = "ctx-science-2025-q42-43"
            elif q["id"] == "q43":
                q["contextRef"] = "ctx-science-2025-q42-43"
                
        # Add shared context for 42-43
        if "sharedContexts" not in data:
            data["sharedContexts"] = {}
        data["sharedContexts"]["ctx-science-2025-q42-43"] = {
            "type": "text",
            "title": "Cooking Steps",
            "text": q42_inst
        }

    new_content = prefix + json.dumps(data, indent=2) + ";\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Formatting and shared contexts fixed!")
