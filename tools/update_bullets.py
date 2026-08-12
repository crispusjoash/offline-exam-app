with open("c:/Users/JOASH/Desktop/CBC/offline-exam-app/src/data/pastPapers.js", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("• ", "- ")

with open("c:/Users/JOASH/Desktop/CBC/offline-exam-app/src/data/pastPapers.js", "w", encoding="utf-8") as f:
    f.write(content)
print("Bullets updated to hyphens.")
