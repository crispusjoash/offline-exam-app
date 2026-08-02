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

batch1_explanations = {
    1: """The correct answer is **Whom am I speaking to?**

**Detailed Analysis of the Correct Answer:**
In polite telephone conversations (especially when speaking to an elder, authority figure, or teacher), asking "Whom am I speaking to?" is the most formal and respectful way to inquire about the caller's identity. In grammar, "whom" is used because it acts as the object of the preposition "to" (as in, "I am speaking to whom?").

**Why Other Options Are Incorrect:**
* **Who are you?:** This is too abrupt, rude, and informal for a teacher to say in a polite phone conversation.
* **Who is this?:** This is very casual and informal. It lacks the professional respect required in a school context.
* **Whom do you want to speak to?:** This reverses the roles. Barasa (the pupil) is the one calling the teacher, so the teacher needs to ask who is on the line, not whom the caller wants to talk to.

📌 **Key Learning Note:**
When asking for someone's identity on the phone in formal English, use "Whom am I speaking to?" or "May I know who is calling?".""",

    2: """The correct answer is **May I be late for school today?**

**Detailed Analysis of the Correct Answer:**
The modal verb **"May"** is used to ask for permission politely from a teacher or an authority figure. Barasa needs permission from his class teacher to arrive late so he can accompany his young sister on her first day of Grade 1.

**Why Other Options Are Incorrect:**
* **I want to be late for school today.:** This states a personal desire rather than asking for permission politely.
* **I will be late for school today.:** This is a direct command/statement declaring that he will be late, without asking the teacher's permission first.
* **Must I be late for school today?:** This asks if being late is a compulsory requirement or obligation, which does not make sense here.

📌 **Key Learning Note:**
Always use **"May I..."** when asking for permission from teachers, parents, or elders.""",

    3: """The correct answer is **Thank you, Teacher.**

**Detailed Analysis of the Correct Answer:**
Whenever someone grants your request or offers help, social dialogue etiquette requires you to express gratitude. Since the teacher agreed to let Barasa come late with his sister, the proper response is to thank the teacher.

**Why Other Options Are Incorrect:**
* **That's good, Teacher.:** This sounds like you are evaluating or grading the teacher's response rather than showing gratitude.
* **It's okay, Teacher.:** This is informal and sounds like you are forgiving someone or accepting an apology, not showing appreciation.
* **It's alright, Teacher.:** This is used to reassure someone or accept an apology, which is inappropriate after receiving permission.

📌 **Key Learning Note:**
Always say **"Thank you"** whenever a teacher or elder grants a request or helps you out.""",

    4: """The correct answer is **would**.

**Detailed Analysis of the Correct Answer:**
This question tests the **Second Conditional** in English grammar, which is used for hypothetical or imaginary situations in the present or future. The rule for the Second Conditional is:
`If + Past Simple (had), ... WOULD + base verb (travel)`.
Since the sentence imagines something that is not currently true ("If I had a lot of money..."), we use **would**.

**Why Other Options Are Incorrect:**
* **should:** Used for giving advice or expressing duty/obligation, not for conditional imaginary outcomes.
* **can:** Used for present ability in real situations, whereas past conditional clauses require the past modal "would".
* **will:** Used in the First Conditional for real/likely future possibilities (`If I have money, I will travel...`).

📌 **Key Learning Note:**
Second Conditional Rule: `If + Past Simple (had), ... WOULD + verb (travel)`.""",

    5: """The correct answer is **on**.

**Detailed Analysis of the Correct Answer:**
In English grammar, prepositions of transport have fixed rules. We say **by car**, **by bus**, **by train**, or **by plane** when referring to vehicles. However, when talking about walking, the only correct idiomatic expression is strictly **on foot**.

**Why Other Options Are Incorrect:**
* **by:** Used for vehicles and mechanical modes of transport (e.g. *by bus*, *by bicycle**), but never for walking on your feet.
* **with:** Used to show the instrument used to perform an action (e.g. *cut with a knife**), not for walking.
* **in:** Used for being inside enclosed transport (e.g. *in a car*, *in a taxi**).

📌 **Key Learning Note:**
Always say **"on foot"** when referring to walking to school or any destination."""
}

for q in data['sectionA']:
    q_num = q['questionNumber']
    if q_num in batch1_explanations:
        q['explanation'] = batch1_explanations[q_num]

new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_js = f"{prefix}{new_json_str}{suffix}\n"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Batch 1 (Q1 - Q5) updated successfully in kpsea-english-2023.js!")
