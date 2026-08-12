import json

with open("src/data/kjsea-kiswahili-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaKiswahili2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

# 1. Fix dialogue formatting
dialogue_text = """(Ni uwanjani. Wanafunzi wanafanya mazoezi ya mwili. Tezi na Nira wanakimbia polepole huku wakizungumza.)

**Tezi:** (Akimsogelea.) Hali vipi Nira?

**Nira:** Nzuri sana dada. Nawe waendelea vipi?

**Tezi:** (Kwa furaha.) ----21----. Ninaendelea kufanya mazoezi. Si unajua ni wakati wa matayarisho ya michuano ya futiboli? Timu yetu inajikaza kisabuni. Unajua, ajizi ni ...

**Nira:** (Akidakia.) Nyumba ya njaa, eti. Hata sisi tunajikakamua.

**Tezi:** (Akihema.) Hapo sawa mwenzangu! Mwaka jana tulinyakua kombe. Tunatumai mwaka huu pia tutalileta kwetu. Wavulana wote wameamua liwe liwalo, ushindi utabaki kwetu.

**Nira:** Hali kadhalika, kwa upande wa timu yetu, mabanati hawalali. Tumeamua kuwa sharti tulinyakue kombe mwaka huu. Mwaka jana lilitupita.

**Tezi:** (Akipunguza mwendo.) Wacha nipumue kidogo. Nimekimbia kwa muda mrefu; moyo wangu unadunda. Nikiendelea hivi nitaanguka.

**Nira:** (Akisimama.) ----24----. Hakika hata mimi ninahitaji kupumzika sasa. Kwaheri. Tutaonana kesho tena.

**Tezi:** (Akimtazama.) Nami nitakufuata punde.
(Wanaagana.)"""

data["sharedContexts"]["ctx-kisw-2025-q21-25"]["text"] = dialogue_text

# 2. Fix question text for Q26-35
q_texts = {
    "q26": '"Daktari ----26---- tembe za kumezea hapa na ----27---- za kubeba."',
    "q27": '"Daktari ----26---- tembe za kumezea hapa na ----27---- za kubeba."',
    "q28": '"Hakikisha kuwa ----28---- mara tatu kwa siku,"',
    "q29": '"----29---- Ninafahamu kuwa ----30---- maradhi ni ghali kuliko kuyazuia."',
    "q30": '"----29---- Ninafahamu kuwa ----30---- maradhi ni ghali kuliko kuyazuia."',
    "q31": 'Topasa ----31---- unyounyo huku amebeba bahasha ya dawa na kuelekea nyumbani.',
    "q32": 'Kwa siku tano ----32----, Topasa ----33---- maagizo ya daktari.',
    "q33": 'Kwa siku tano ----32----, Topasa ----33---- maagizo ya daktari.',
    "q34": 'Alikula chakula chenye virutubishi ----34---- kumeza dawa.',
    "q35": '----35---- kazi ngumu, alipumzika nyumbani.'
}

for q in data["sectionA"]:
    if q["id"] in q_texts:
        q["questionText"] = q_texts[q["id"]]

with open("src/data/kjsea-kiswahili-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaKiswahili2025 = {json.dumps(data, indent=2)};\n")
