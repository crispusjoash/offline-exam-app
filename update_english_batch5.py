import json

filepath = 'src/data/kpsea-english-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const kpseaEnglish2023 = '
suffix = ';' if text.strip().endswith(';') else ''

clean_text = text.replace(prefix, '').strip()
if clean_text.endswith(';'):
    clean_text = clean_text[:-1]

data = json.loads(clean_text)

batch5_explanations = {
    21: """The correct answer is **in**.

**Detailed Analysis of the Correct Answer:**
Prepositions of place indicate location. When someone or something is located inside an enclosed 3D space, room, or building, we use the preposition **in** (**in the classroom**).

**Why Other Options Are Incorrect:**
* **to:** Indicates movement or direction towards a destination (e.g. *walking to the classroom**).
* **on:** Indicates position resting on a flat surface (e.g. *on the roof**).
* **over:** Indicates a position directly above something without touching it (e.g. *flew over the classroom**).

📌 **Key Learning Note:**
Use **in** for enclosed locations like rooms, classrooms, houses, and buildings.""",

    22: """The correct answer is **on**.

**Detailed Analysis of the Correct Answer:**
Prepositions of surface location describe where an object rests. When an item rests upon the top flat surface of a piece of furniture, we use **on** (**on the table**).

**Why Other Options Are Incorrect:**
* **with:** Indicates companionship or tool used (e.g. *with a pen**).
* **in:** Means inside an enclosed space (e.g. *in the drawer**).
* **from:** Indicates origin or starting point (e.g. *from the library**).

📌 **Key Learning Note:**
Use **on** when an object is resting on top of a flat surface like a table, desk, or floor.""",

    23: """The correct answer is **aren't they?**

**Detailed Analysis of the Correct Answer:**
Question tags follow three main grammar rules:
1. **Positive statement ➔ Negative tag.** The sentence "The children are planting trees" is positive.
2. **Match the auxiliary verb.** The auxiliary verb is **are**, so the negative form is **aren't**.
3. **Match the pronoun.** The subject "The children" is third-person plural, replaced by **they**.
Putting it together gives the tag **aren't they?**.

**Why Other Options Are Incorrect:**
* **aren't we?:** Changes the pronoun from third-person plural (**they**) to first-person plural (**we**).
* **are they?:** Uses a positive tag, which is incorrect for a positive statement.
* **are we?:** Uses a positive tag and an incorrect pronoun.

📌 **Key Learning Note:**
Question Tag Rule: Positive statement + Positive verb ("are") ➔ Negative tag ("aren't they?").""",

    24: """The correct answer is **somebody**.

**Detailed Analysis of the Correct Answer:**
Indefinite pronouns refer to unspecified people:
- **Somebody / Someone**: Used in affirmative (positive) clauses when referring to an unknown person who took an action.
Because the clause "...because somebody had taken it" is a positive statement explaining why the book was missing, **somebody** is the correct pronoun.

**Why Other Options Are Incorrect:**
* **anybody:** Used in negative statements (**did not see anybody**) or questions (**did anybody take it?**).
* **everybody:** Means all people, which makes no sense because multiple people wouldn't take a single book.
* **nobody:** Means no person; saying "nobody had taken it" would contradict why the book was missing from the bag.

📌 **Key Learning Note:**
Use **somebody** in positive statement clauses when referring to an unknown person.""",

    25: """The correct answer is **ourselves**.

**Detailed Analysis of the Correct Answer:**
Reflexive pronouns refer back to the subject or object of the clause:
- Subject/Object **we / us** (1st person plural) ➔ Reflexive pronoun **ourselves**.
Since the teacher told **us** (first-person plural) to take care of a group including ourselves, the correct reflexive pronoun is **ourselves**.

**Why Other Options Are Incorrect:**
* **themselves:** Reflexive pronoun for *they/them* (3rd person plural).
* **yourself:** Singular reflexive pronoun for *you* (2nd person singular).
* **yourselves:** Plural reflexive pronoun for *you all* (2nd person plural).

📌 **Key Learning Note:**
Reflexive pronoun pairing: **we / us ➔ ourselves**."""
}

for q in data['sectionA']:
    q_num = q['questionNumber']
    if q_num in batch5_explanations:
        q['explanation'] = batch5_explanations[q_num]

new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_js = f"{prefix}{new_json_str}{suffix}\n"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Batch 5 (Q21 - Q25) updated successfully in kpsea-english-2023.js!")
