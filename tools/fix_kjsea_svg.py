import json

with open("src/data/kjsea-kiswahili-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaKiswahili2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

# Update the context to use the image markdown instead of raw SVG
new_text = "Wanafunzi wa shule ya Junia huwa na ratiba ya Klabu mbalimbali kila siku ya wiki kama ilivyo kwenye jedwali lifuatalo:\n\n![Jedwali la Ratiba](/ratiba-klabu.svg)"
data["sharedContexts"]["ctx-kisw-2025-q18-20"]["text"] = new_text

with open("src/data/kjsea-kiswahili-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaKiswahili2025 = {json.dumps(data, indent=2)};\n")
