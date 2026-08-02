import json
import re

file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\src\data\kpsea-english-2023.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(r"Why it\'s wrong", "Why it's wrong")
content = content.replace(r"caller\'s", "caller's")
content = content.replace(r"teacher\'s", "teacher's")
content = content.replace(r"donkey\'s", "donkey's")
content = content.replace(r"father\'s", "father's")
content = content.replace(r"character\'s", "character's")
content = content.replace(r"farmer\'s", "farmer's")
content = content.replace(r"Hare\'s", "Hare's")
content = content.replace(r"Hyena\'s", "Hyena's")

# General cleanup of any lingering \'
content = content.replace(r"\'", "'")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully cleaned up all escaped single quotes.")
