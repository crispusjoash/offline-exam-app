import json

def dump_religious_ed(filename, export_name, output_txt):
    filepath = f'src/data/{filename}'
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    clean_text = text.replace(f'export const {export_name} = ', '').strip().rstrip(';')
    data = json.loads(clean_text)
    
    with open(output_txt, 'w', encoding='utf-8') as out:
        out.write(f"Title: {data.get('title')}\n")
        out.write(f"Total questions: {len(data.get('sectionA', []))}\n\n")
        for q in data.get('sectionA', []):
            out.write(f"=== Q{q['questionNumber']} (id: {q['id']}) ===\n")
            out.write(f"QuestionText: {q.get('questionText')}\n")
            if 'questionList' in q:
                out.write(f"QuestionList: {q.get('questionList')}\n")
            if 'questionSuffix' in q:
                out.write(f"QuestionSuffix: {q.get('questionSuffix')}\n")
            out.write(f"Options: {q.get('options')}\n")
            out.write(f"Current Explanation: {q.get('explanation')}\n\n")

dump_religious_ed('kpsea-sst-cre-2023.js', 'kpseaSstCre2023', 'cre_dump.txt')
dump_religious_ed('kpsea-sst-ire-2023.js', 'kpseaSstIre2023', 'ire_dump.txt')
dump_religious_ed('kpsea-sst-hre-2023.js', 'kpseaSstHre2023', 'hre_dump.txt')

print("Dumped CRE, IRE, and HRE successfully.")
