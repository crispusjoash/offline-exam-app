import re
import json

file_path = 'src/data/kpsea-sst-parta-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Q1
q1_old = r'"questionText": "A Grade 6 learner mounted and framed the following picture in readiness for an exhibition.\\n\\n\[Image: A framed picture of a lion\'s head\]\\n\\nWhy was the picture mounted and framed?",'
q1_new = '"questionText": "A Grade 6 learner mounted and framed the following picture in readiness for an exhibition.",\n      "questionSuffix": "Why was the picture mounted and framed?",\n      "imageUrl": "/assets/images/sst-2024-q1.png",'
content = content.replace(q1_old, q1_new)

# Fix Q3
q3_old = r'"questionText": "The following image shows a passing skill in netball.\\n\\n\[Image: Two people passing a ball. One player is throwing the ball from the shoulder height.\]\\n\\nWhat type of pass does the image represent?",'
q3_new = '"questionText": "The following image shows a passing skill in netball.",\n      "questionSuffix": "What type of pass does the image represent?",\n      "imageUrl": "/assets/images/sst-2024-q3.png",'
content = content.replace(q3_old, q3_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images added for Q1 and Q3 successfully.")
