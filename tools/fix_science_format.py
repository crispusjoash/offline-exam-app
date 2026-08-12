import re

filepath = 'src/data/kpsea-science-2024.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Question 3
q3_old = r'"questionText": "Learners listed the following as functions of the human skeleton:\\n(i) protection of organs\\n(ii) maintenance of body posture\\n(iii) manufacture of red blood cells\\n(iv) movement of the body\\n\\nWhich of the listed functions are for limb bones of the human skeleton?"'
q3_new = r'''"questionText": "Learners listed the following as functions of the human skeleton:",
      "questionList": [
        "(i) protection of organs",
        "(ii) maintenance of body posture",
        "(iii) manufacture of red blood cells",
        "(iv) movement of the body"
      ],
      "questionSuffix": "Which of the listed functions are for limb bones of the human skeleton?"'''

# Question 4
q4_old = r'"questionText": "During a class discussion on signs and symptoms of diseases of the human breathing system, learners identified the following:\\n(i) coughing up blood\\n(ii) blocked nostrils\\n(iii) pain in the chest\\n(iv) vomiting\\n(v) difficulties in breathing\\n\\nWhich of the following consists **only** of signs and symptoms of tuberculosis?"'
q4_new = r'''"questionText": "During a class discussion on signs and symptoms of diseases of the human breathing system, learners identified the following:",
      "questionList": [
        "(i) coughing up blood",
        "(ii) blocked nostrils",
        "(iii) pain in the chest",
        "(iv) vomiting",
        "(v) difficulties in breathing"
      ],
      "questionSuffix": "Which of the following consists **only** of signs and symptoms of tuberculosis?"'''

# Question 9
q9_old = r'"questionText": "During a class discussion, learners listed the following as causes of air pollution.\\n(i) Smoke from burning farm waste\\n(ii) Smell from waste in a pit latrine\\n(iii) Waste from a construction site\\n(iv) Smell from kitchen waste\\n\\nWhich one of the following pairs consists only of causes that can be controlled by changing waste into manure?"'
q9_new = r'''"questionText": "During a class discussion, learners listed the following as causes of air pollution:",
      "questionList": [
        "(i) Smoke from burning farm waste",
        "(ii) Smell from waste in a pit latrine",
        "(iii) Waste from a construction site",
        "(iv) Smell from kitchen waste"
      ],
      "questionSuffix": "Which one of the following pairs consists only of causes that can be controlled by changing waste into manure?"'''

# Question 16
q16_old = r'"questionText": "Grade 5 learners used the internet to search for health measures that prevent common communicable diseases. Some of the information they found included:\\n(i) using a handkerchief always.\\n(ii) proper use of latrines.\\n(iii) washing hands after visiting the toilet.\\n(iv) not sharing personal items.\\n(v) observing personal hygiene.\\n\\nWhich one of the following common communicable diseases may **not** be prevented by observing all the above health measures?"'
q16_new = r'''"questionText": "Grade 5 learners used the internet to search for health measures that prevent common communicable diseases. Some of the information they found included:",
      "questionList": [
        "(i) using a handkerchief always.",
        "(ii) proper use of latrines.",
        "(iii) washing hands after visiting the toilet.",
        "(iv) not sharing personal items.",
        "(v) observing personal hygiene."
      ],
      "questionSuffix": "Which one of the following common communicable diseases may **not** be prevented by observing all the above health measures?"'''

# Question 44
q44_old = r'"questionText": "Grade 6 learners normally carry out the following activities when cleaning their classroom.\\n(i) dust windows, chairs, tables and desks\\n(ii) sweep the class, dispose of waste in a dust bin and take it to the rubbish pit\\n(iii) arrange the furniture after cleaning\\n(iv) mop the class and allow to dry\\n(v) clean and store the cleaning materials and tools properly\\n\\nWhich of the following shows the **correct order** of activities?"'
q44_new = r'''"questionText": "Grade 6 learners normally carry out the following activities when cleaning their classroom.",
      "questionList": [
        "(i) dust windows, chairs, tables and desks",
        "(ii) sweep the class, dispose of waste in a dust bin and take it to the rubbish pit",
        "(iii) arrange the furniture after cleaning",
        "(iv) mop the class and allow to dry",
        "(v) clean and store the cleaning materials and tools properly"
      ],
      "questionSuffix": "Which of the following shows the **correct order** of activities?"'''


content = content.replace(q3_old, q3_new)
content = content.replace(q4_old, q4_new)
content = content.replace(q9_old, q9_new)
content = content.replace(q16_old, q16_new)
content = content.replace(q44_old, q44_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done replacing.")
