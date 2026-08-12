import json
import re

file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\src\data\kpsea-english-2023.js"

explanations = {
    "eq1": """📌 **Concept Overview: Telephone Etiquette & Grammatical Case (Who vs. Whom)**

When speaking on the telephone in a formal or respectful context (such as a student calling a teacher), it is essential to use polite expressions. Grammatically, we also need to pay attention to the difference between **who** (subject pronoun) and **whom** (object pronoun).

• **Subject pronoun (Who):** Refers to the person performing the action (e.g., *Who answered the phone?*).
• **Object pronoun (Whom):** Refers to the person receiving the action or standing as the object of a preposition like 'to', 'with', or 'for' (e.g., *To whom am I speaking?* or *Whom am I speaking to?*).

In this question, Barasa calls his class teacher. After saying hello, he wants to confirm the identity of the person on the line before proceeding.

---

✅ **Why Option C ("Whom am I speaking to?") is Correct:**
Option C is the most grammatically correct and polite phrasing. Here, the pronoun is the object of the preposition **to** (*I am speaking to [person]*), making **whom** the correct grammatical choice. Furthermore, it is respectful and appropriate for a pupil speaking to a teacher.

---

❌ **Detailed Analysis of Incorrect Options:**

* **Option A: "Who are you?"**
  * *Why it's wrong:* This phrase is very blunt, rude, and aggressive. In formal telephone communication—especially with authority figures like teachers—asking "Who are you?" comes across as disrespectful.
* **Option B: "Who is this?"**
  * *Why it's wrong:* While common in very informal or casual chats with friends, it lacks formal courtesy. Additionally, grammatically, when asking for the object of your call, "whom" is preferred in formal dialogue.
* **Option D: "Whom do you want to speak to?"**
  * *Why it's wrong:* This option reverses the caller's role. Barasa is the one who initiated the call to get help; he is not an operator asking the teacher who *she* wants to speak to!

---

💡 **Key Takeaway for Your Revision Notes:**
1. Use **Whom** after or before prepositions like *to*, *with*, or *for* (e.g., *To whom it may concern*, *Whom am I speaking to?*).
2. Always use polite, formal phrasing when speaking to teachers or elders on the telephone.""",

    "eq2": """📌 **Concept Overview: Modal Auxiliary Verbs for Seeking Permission**

Modal auxiliary verbs (such as **may**, **can**, **must**, **will**, **should**) express mood, permission, ability, obligation, or certainty. When interacting with teachers, parents, or authority figures, choosing the right modal verb determines whether your request sounds polite, demanding, or confusing.

In this context, Barasa needs to explain why he might be late and ask his teacher for approval/permission to arrive late while helping his younger sister on her first day of Grade 1.

---

✅ **Why Option A ("May I be late for school today?") is Correct:**
**May** is the standard modal verb used in formal English to politely request permission from a person in authority.
• Example: *May I come in?*, *May I leave early?*, *May I be late today?*
Barasa is politely asking his teacher to allow him to arrive late, which fits the dialogue perfectly.

---

❌ **Detailed Analysis of Incorrect Options:**

* **Option B: "I want to be late for school today."**
  * *Why it's wrong:* Expressing what you *want* sounds self-centered and childish. Arriving late is a necessity due to a family situation, not a fun activity Barasa "wants" to do.
* **Option C: "I will be late for school today."**
  * *Why it's wrong:* Using **will** creates a direct, demand-like statement of fact without asking for permission or showing respect for school rules.
* **Option D: "Must I be late for school today?"**
  * *Why it's wrong:* **Must** expresses compulsion or strong obligation (e.g., *Must I do my homework now?*). Asking "Must I be late?" implies someone is forcing him to be late against his will, which makes no sense here.

---

💡 **Key Takeaway for Your Revision Notes:**
When requesting permission from teachers or elders, always start with **"May I..."** rather than stating desires (**"I want to..."**) or commands (**"I will..."**).""",

    "eq3": """📌 **Concept Overview: Social Etiquette & Dialogue Responses**

In English dialogue comprehension, choosing the right response depends on the context of the conversation. When an authority figure (like a class teacher) listens to your request and grants you permission or assistance, standard politeness requires expressing gratitude.

In the passage, the teacher says: *"Okay, Barasa. You can come along with her. Make sure you come to see me after she settles down in her classroom."*

---

✅ **Why Option D ("Thank you, Teacher.") is Correct:**
Since the teacher has kindly granted Barasa permission to come to school late with his younger sister, the only appropriate, polite response is to thank her. **"Thank you, Teacher."** acknowledges the favor and closes the dialogue respectfully.

---

❌ **Detailed Analysis of Incorrect Options:**

* **Option A: "That's good, Teacher."**
  * *Why it's wrong:* This sounds evaluative—as if the student is rating or approving the teacher's decision, which is improper etiquette for a student.
* **Option B: "It's okay, Teacher."**
  * *Why it's wrong:* "It's okay" is typically used to reassure someone or forgive a minor mistake (e.g., *"Sorry I bumped into you." — "It's okay."*). It does not convey appreciation.
* **Option C: "It's alright, Teacher."**
  * *Why it's wrong:* Similar to "It's okay", this phrase is an informal response to an apology or comfort, not a respectful reply when granted a permission.

---

💡 **Key Takeaway for Your Revision Notes:**
Whenever someone in authority grants your request, grants permission, or helps you out, the correct formal response is **"Thank you"**.""",

    "eq4": """📌 **Concept Overview: Second Conditional Sentences (Hypothetical Situations)**

Conditional sentences in English consist of two parts: an **If-clause** (the condition) and a **Main clause** (the result).

There are three main types of conditionals:
1. **First Conditional (Real Future Possibility):**
   * Formula: *If + Present Simple, WILL + Base Verb*
   * Example: *If I have money, I will travel.* (Real possibility)
2. **Second Conditional (Unreal / Imaginary Present or Future Situation):**
   * Formula: *If + Past Simple, WOULD + Base Verb*
   * Example: *If I had money, I would travel.* (Imaginary situation right now)
3. **Third Conditional (Past Impossible Condition):**
   * Formula: *If + Past Perfect (had had), WOULD HAVE + Past Participle*

In this sentence: *"If I had a lot of money, I ------- travel all over the world."*
The verb in the If-clause is **had** (past simple), showing that this is a hypothetical or imaginary situation (Second Conditional).

---

✅ **Why Option B ("would") is Correct:**
Following the Second Conditional rule (*If + past simple -> WOULD + base verb*), the modal verb **would** pairs correctly with **had** to express what the speaker *would do* in this hypothetical situation.

---

❌ **Detailed Analysis of Incorrect Options:**

* **Option A: "should"**
  * *Why it's wrong:* **Should** is used to give advice or express duty (e.g., *You should study hard*), not to complete a second conditional hypothetical statement.
* **Option C: "can"**
  * *Why it's wrong:* **Can** is present tense and cannot pair with the past simple verb *had* in a conditional clause.
* **Option D: "will"**
  * *Why it's wrong:* **Will** is used in the First Conditional with a present simple verb (*If I HAVE money, I WILL travel*). Since the sentence uses past simple *had*, *will* is grammatically incorrect.

---

💡 **Key Takeaway for Your Revision Notes:**
* **If + HAD (Past Simple) ➔ WOULD + Verb** (Second Conditional for imaginary events).
* **If + HAVE (Present Simple) ➔ WILL + Verb** (First Conditional for real possibilities).""",

    "eq5": """📌 **Concept Overview: Prepositions of Transport and Movement**

In English grammar, prepositions used with modes of transport follow specific rules:

1. **Using 'BY' + Vehicle:**
   * Used for general modes of transport without an article (*a/an/the*).
   * Examples: *by car*, *by bus*, *by train*, *by plane*, *by boat*.
2. **Using 'IN' / 'ON' + Specific Vehicle:**
   * *in a car*, *in a taxi* (small enclosed transport where you sit).
   * *on a bus*, *on a train*, *on a plane* (large public transport where you can walk).
3. **Walking (The Exception):**
   * When you travel by walking, the fixed idiomatic expression is strictly **ON FOOT**.

In the question: *"Odoko goes to school ------- foot every morning."*

---

✅ **Why Option C ("on") is Correct:**
**On foot** is an established, unbreakable English idiom meaning to walk. We say *"on foot"*, never *"by foot"*.

---

❌ **Detailed Analysis of Incorrect Options:**

* **Option A: "by"**
  * *Why it's wrong:* Although we say *by car* or *by bus*, saying *by foot* is a common error made by English learners. Standard English requires **on foot**.
* **Option B: "with"**
  * *Why it's wrong:* **With** indicates using an instrument or tool (e.g., *write with a pen*, *cut with a knife*) or being accompanied by someone, not a mode of transport.
* **Option D: "in"**
  * *Why it's wrong:* **In** is used for being inside certain vehicles (*in a taxi*), not for walking.

---

💡 **Key Takeaway for Your Revision Notes:**
* **Walking ➔ ON foot** (Always! Never say "by foot").
* **Vehicles ➔ BY car, BY bus, BY bicycle, BY train**."""
}

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract json part after export const kpseaEnglish2023 = 
match = re.search(r'export const kpseaEnglish2023 = (\{.*\});?', content, re.DOTALL)
if match:
    json_str = match.group(1)
    data = json.loads(json_str)
    
    for q in data["sectionA"]:
        if q["id"] in explanations:
            q["explanation"] = explanations[q["id"]]
            
    new_content = "export const kpseaEnglish2023 = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated questions 1 to 5 in kpsea-english-2023.js")
else:
    print("Could not match JS object")
