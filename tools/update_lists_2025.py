import json
import re

# Update IRE 2025 Q46
file_path_ire = 'src/data/kpsea-sst-ire-2025.js'
with open(file_path_ire, 'r', encoding='utf-8') as f:
    content_ire = f.read()

match_ire = re.search(r'export const \w+ = (\{.*\});?\s*$', content_ire, re.DOTALL)
if match_ire:
    data_ire = json.loads(match_ire.group(1))
    for q in data_ire["sectionA"]:
        if q["id"] == "q46":
            q["questionText"] = "Teacher Amina displayed flash cards showing the following acts:\n\ni. talking\nii. intentional vomiting\niii. passing wind\niv. menstruation\n\nWhich two of the acts nullify both Swalah and Saum?"
    new_content_ire = "export const kpseaSstIre2025 = " + json.dumps(data_ire, indent=2) + ";\n"
    with open(file_path_ire, 'w', encoding='utf-8') as f:
        f.write(new_content_ire)

# Update HRE 2025 Q49
file_path_hre = 'src/data/kpsea-sst-hre-2025.js'
with open(file_path_hre, 'r', encoding='utf-8') as f:
    content_hre = f.read()

match_hre = re.search(r'export const \w+ = (\{.*\});?\s*$', content_hre, re.DOTALL)
if match_hre:
    data_hre = json.loads(match_hre.group(1))
    for q in data_hre["sectionA"]:
        if q["id"] == "q49":
            q["questionText"] = "The following statements describe a festival:\n\ni. Prayers are offered to Laxmi Devi.\nii. Homes are lighted with deepaks.\niii. Places of worship are visited.\niv. Donations are given.\nv. New clothes are worn.\nvi. Gifts are exchanged.\nvii. Fun fairs are organized.\n\nThe festival described is"
    new_content_hre = "export const kpseaSstHre2025 = " + json.dumps(data_hre, indent=2) + ";\n"
    with open(file_path_hre, 'w', encoding='utf-8') as f:
        f.write(new_content_hre)

print("Q46 and Q49 updated successfully.")
