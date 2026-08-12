with open("update_kisw_explanations_all.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "for q in data[\"sectionA\"]:" in line:
        break
    new_lines.append(line)

with open("update_kisw_explanations_all.py", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
