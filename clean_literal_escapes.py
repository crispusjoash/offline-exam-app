file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\src\data\kpsea-english-2023.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace literal backslash-quote with plain single quote
content = content.replace(r"\'", "'")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully replaced all \\' with ' in JS file!")
