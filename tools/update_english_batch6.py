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

batch6_explanations = {
    26: """The correct answer is **by**.

**Detailed Analysis of the Correct Answer:**
Prepositional phrases indicating manner or method follow fixed idiomatic expressions. The standard English expression meaning using physical compulsion or violence is **by force** (**took away our goats by force**).

**Why Other Options Are Incorrect:**
* **with:** Used for instruments (e.g. *cut with a knife**), not in the phrase *by force*.
* **at:** Used for location or time (e.g. *at noon**), not manner.
* **under:** Used in phrases like *under pressure* or *under arrest*, but not *by force*.

📌 **Key Learning Note:**
The correct fixed idiomatic prepositional phrase is **by force**.""",

    27: """The correct answer is **whose**.

**Detailed Analysis of the Correct Answer:**
Relative pronouns link clauses by indicating identity or possession:
- **whose**: Shows possession for people, animals, or objects (**the hen whose egg broke* = the egg belonging to the hen).

**Why Other Options Are Incorrect:**
* **who:** Subject pronoun used for human beings (e.g. *the teacher who taught us**).
* **whom:** Object pronoun used for human beings (e.g. *the man whom I met**).
* **which:** Used for non-possessive references to animals or things (e.g. *the hen which laid an egg**).

📌 **Key Learning Note:**
Use **whose** to show possession for people, animals, or things.""",

    28: """The correct answer is **give**.

**Detailed Analysis of the Correct Answer:**
Modal auxiliary verbs (**will, shall, can, may, must, should, would**) must ALWAYS be followed by the **bare infinitive** (the base form of the main verb without 'to').
Therefore, after the modal **will**, the base verb **give** is required (**will give**).

**Why Other Options Are Incorrect:**
* **given:** Past participle form (**has given**), which cannot follow a modal verb directly.
* **gives:** Third-person singular present form (**he gives**), which cannot follow a modal verb.
* **gave:** Simple past tense form (**he gave**), which cannot follow a modal verb.

📌 **Key Learning Note:**
Grammar Rule: Modal verbs (will, shall, can, may) + Base Verb (**will give**).""",

    29: """The correct answer is **Both Kalusi and Sofia did not come late to class.**

**Detailed Analysis of the Correct Answer:**
Correlative conjunctions **Neither ... nor** mean "not the one and not the other". They negate both persons or items mentioned in the sentence.
Therefore, "Neither Kalusi nor Sofia came late" means that Kalusi did NOT come late, and Sofia did NOT come late either (both were on time).

**Why Other Options Are Incorrect:**
* **Only Kalusi came late to class.:** Incorrectly claims one student was late.
* **Only Sofia came late to class.:** Incorrectly claims the other student was late.
* **Both Kalusi and Sofia came late to class.:** Reverses the meaning into a positive statement of lateness for both students.

📌 **Key Learning Note:**
"Neither A nor B" means **BOTH A and B did NOT** perform or experience the action.""",

    30: """The correct answer is **Banda.**

**Detailed Analysis of the Correct Answer:**
Reading logic puzzles requires carefully matching every condition in the text:
- *Nasir*: plays football AND volleyball.
- *Banda*: plays football ONLY.
- *Lona*: plays football AND netball.
Since Banda plays football and has no other additional sport listed, **Banda** is the only one who plays football *only*.

**Why Other Options Are Incorrect:**
* **Nasir.:** Plays football AND volleyball.
* **Lona.:** Plays football AND netball.
* **All of them.:** All three play football, but Nasir and Lona play other sports too, so they do not play football *only*.

📌 **Key Learning Note:**
Pay close attention to restrictive words like **"only"** when answering comprehension puzzles."""
}

for q in data['sectionA']:
    q_num = q['questionNumber']
    if q_num in batch6_explanations:
        q['explanation'] = batch6_explanations[q_num]

new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_js = f"{prefix}{new_json_str}{suffix}\n"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Batch 6 (Q26 - Q30) updated successfully in kpsea-english-2023.js!")
