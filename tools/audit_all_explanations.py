import json
import re

with open('all_non_math_questions.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)

for paper_id, paper in papers.items():
    questions = paper.get('sectionA', [])
    print(f"\n==================== AUDITING {paper_id} ({len(questions)} questions) ====================")
    hallucinations_found = 0
    for q in questions:
        q_num = q['questionNumber']
        opts = [o['text'].strip() for o in q['options']]
        exp = q.get('explanation', '')
        
        # Check if "Why other options are incorrect" section exists
        exp_lower = exp.lower()
        if "why other options are incorrect" not in exp_lower and "kwa nini chaguzi zingine si sahihi" not in exp_lower and "kwa nini" not in exp_lower:
            print(f"  [Q{q_num}] Missing 'Why other options are incorrect' section!")
            hallucinations_found += 1
            continue
        
        # Check if the explanation mentions option texts or key words from options
        # Extract the incorrect options
        incorrect_opts = [o['text'].strip() for o in q['options'] if not o.get('isCorrect', False)]
        
        # Check if any incorrect option is completely missing from the explanation
        missing_opts = []
        for opt in incorrect_opts:
            # Clean option text for searching (remove trailing period, etc.)
            clean_opt = re.sub(r'[\.\;\:\s]+$', '', opt).strip()
            # If clean_opt is not in explanation (case insensitive)
            if clean_opt.lower() not in exp.lower():
                missing_opts.append(clean_opt)
        
        if missing_opts:
            print(f"  [Q{q_num}] Options missing from explanation: {missing_opts}")
            hallucinations_found += 1

    if hallucinations_found == 0:
        print(f"  --> ALL {len(questions)} questions passed audit cleanly!")
    else:
        print(f"  --> TOTAL ISSUES FOUND in {paper_id}: {hallucinations_found}")
