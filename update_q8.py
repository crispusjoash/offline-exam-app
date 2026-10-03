import json
import shutil
import os

source_img = r"C:\Users\JOASH\.gemini\antigravity-ide\brain\9d39c76d-2c71-4969-8f52-1885f6f7bfde\.user_uploaded\media_1787435125744.png"

dest1 = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\public\assets\kjsea_cas_2025_q8.png"
dest2 = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\electron\app\assets\kjsea_cas_2025_q8.png"

shutil.copy(source_img, dest1)
shutil.copy(source_img, dest2)

file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\public\data\kjsea-creative-arts-sports-sectiona-2025.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data.get("sectionA", []):
    if q.get("id") == "q8":
        q["imagePath"] = "/assets/kjsea_cas_2025_q8.png"
        break

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open(r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\electron\app\data\kjsea-creative-arts-sports-sectiona-2025.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Q8 image mapped and JSON updated successfully.")
