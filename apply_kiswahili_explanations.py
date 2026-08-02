import json
from update_kisw_explanations_all import detailed_explanations, detailed_explanations_26_50

with open("src/data/kjsea-kiswahili-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaKiswahili2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

for q in data["sectionA"]:
    if q["id"] in detailed_explanations:
        q["explanation"] = detailed_explanations[q["id"]]
    elif q["id"] in detailed_explanations_26_50:
        q["explanation"] = detailed_explanations_26_50[q["id"]]

with open("src/data/kjsea-kiswahili-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaKiswahili2025 = {json.dumps(data, indent=2)};\n")
