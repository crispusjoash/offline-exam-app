import json

with open("src/data/kjsea-kiswahili-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaKiswahili2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

# Fix titles
data["sharedContexts"]["ctx-kisw-2025-q1-6"]["title"] = "Swali la 1 hadi la 6\nSoma kifungu kifuatacho kisha ujibu maswali."
data["sharedContexts"]["ctx-kisw-2025-q7-12"]["title"] = "Swali la 7 hadi la 12\nSoma kifungu kifuatacho kisha ujibu maswali."
data["sharedContexts"]["ctx-kisw-2025-q13-17"]["title"] = "Swali la 13 hadi la 17\nSoma kifungu kifuatacho kisha ujibu maswali."
data["sharedContexts"]["ctx-kisw-2025-q18-20"]["title"] = "Swali la 18 hadi la 20\nSoma kifungu kifuatacho kisha ujibu maswali."
data["sharedContexts"]["ctx-kisw-2025-q21-25"]["title"] = "Swali la 21 hadi la 25\nSoma kifungu kifuatacho kisha ujibu maswali."
data["sharedContexts"]["ctx-kisw-2025-q26-35"]["title"] = "Swali la 26 hadi la 35\nKifungu kifuatacho kina nafasi 26 hadi 35. Chagua jibu lifaalo zaidi kujaza nafasi kati ya majibu manne uliyopewa baada ya kifungu."

# Fix the broken passage (convert __ to ----)
text_26_35 = data["sharedContexts"]["ctx-kisw-2025-q26-35"]["text"]
for i in range(26, 36):
    text_26_35 = text_26_35.replace(f"__{i}__", f"----{i}----")
data["sharedContexts"]["ctx-kisw-2025-q26-35"]["text"] = text_26_35

# Add context for Q36-50
data["sharedContexts"]["ctx-kisw-2025-q36-50"] = {
    "title": "Swali la 36 hadi la 50\nKutoka swali la 36 hadi la 50, chagua jibu sahihi.",
    "type": "text",
    "text": ""
}

for q in data["sectionA"]:
    if 36 <= q["questionNumber"] <= 50:
        q["contextRef"] = "ctx-kisw-2025-q36-50"
    
    # Let's ensure quotes in the question are bolded in the passage just in case.
    # Q2: Mtoto anafanya nini peke yake kando ya barabara? -> already bolded
    # Q5: lilikuwa limetulia kama maji mtungini -> already bolded
    # Q9: kuwataarifu -> already bolded
    # Q17: dhuluma -> already bolded

with open("src/data/kjsea-kiswahili-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaKiswahili2025 = {json.dumps(data, indent=2)};\n")
