import json
import re

file_path = 'src/data/kpsea-science-2022.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON array from the file
match = re.search(r'"sectionA":\s*(\[.*\])\s*\}', content, re.DOTALL)
if not match:
    print("Could not find sectionA array!")
    exit(1)
    
section_a_json = match.group(1)
# Parse the JSON
try:
    # There might be a trailing comma or something, but python json usually handles strict JSON.
    # The file is a JS file so the keys are string quoted. It should be valid JSON.
    questions = json.loads(section_a_json)
except Exception as e:
    print("Error parsing JSON:", e)
    exit(1)

for q in questions:
    if q.get("questionNumber") == 1:
        q["questionText"] = "Learners went for a nature walk to study the importance of plants. They listed the following as the importance of plants.\nThey"
        q["questionList"] = [
            "(i) produce fruits",
            "(ii) attract rain",
            "(iii) beautify environment",
            "(iv) protect soil",
            "(v) produce nectar"
        ]
        q["questionSuffix"] = "Which **two** are true for flowering plants?"
        
    elif q.get("questionNumber") == 11:
        q["questionText"] = "During a class discussion, learners listed the following as some effects of gravity."
        q["questionList"] = [
            "(i) Flowing of water in rivers.",
            "(ii) Writing on chalkboard.",
            "(iii) Fruits falling from a tree.",
            "(iv) Swimming in a pool."
        ]
        q["questionSuffix"] = "Which **two** are correct effects of gravity?"
        
    elif q.get("questionNumber") == 29:
        q["questionText"] = "Grade 4 learners were asked by their Home Science teacher to make posters on the foods that make us healthy. Read what they wrote on the posters."
        q["questionList"] = [
            "**Poster 1:** Beans, Meat, Eggs, Fish",
            "**Poster 2:** Cassava, Rice, Bread, Ugali",
            "**Poster 3:** Oranges, Spinach, Pineapples, Cabbages"
        ]
        q["questionSuffix"] = "Which of the posters contain foods that provide our body with energy?"
        
    elif q.get("questionNumber") == 31:
        q["questionText"] = "Grade 6 learners used their digital devices to get information on cleaning a charcoal *jiko* that was used for cooking. The following is the information:"
        q["questionList"] = [
            "(i) Empty the *jiko*.",
            "(ii) Let the *jiko* cool.",
            "(iii) Leave it in an airy place to dry.",
            "(iv) Wipe the metal parts with a cloth wrung out of warm soapy water."
        ]
        q["questionSuffix"] = "Which of the following shows the correct order the learners can follow when cleaning the *jiko*?"

new_section_a_json = json.dumps(questions, indent=6)

# We need to replace the original array string with the new one
# Wait, replacing directly might be tricky because of indentations. Let's just reconstruct the whole file.
new_file_content = """export const kpseaScience2022 = {
  "id": "kpsea-science-2022",
  "title": "KPSEA 2022 Integrated Science",
  "subject": "Integrated Science",
  "year": "2022",
  "durationMinutes": 100,
  "sharedContexts": {},
  "sectionA": """ + new_section_a_json + """
};
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_file_content)

print("Questions list structures fixed successfully.")
