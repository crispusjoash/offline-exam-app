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

batch4_explanations = {
    16: """The correct answer is **her**.

**Detailed Analysis of the Correct Answer:**
Possessive adjectives show ownership before a noun. Since Asha is a female person (singular female subject pronoun *she**), the corresponding possessive adjective for her grandfather is **her** (**her grandfather**).

**Why Other Options Are Incorrect:**
* **his:** Possessive adjective used for a male person (e.g. *his grandfather**).
* **hers:** Possessive pronoun used without a noun following it (e.g. *the garden is hers**), whereas here it precedes the noun *grandfather*.
* **him:** Object pronoun (e.g. *I called him**), not a possessive adjective.

📌 **Key Learning Note:**
Use **her** as a possessive adjective before a noun when referring to a female person (e.g. *her book*, *her garden*, *her grandfather**).""",

    17: """The correct answer is **different**.

**Detailed Analysis of the Correct Answer:**
In the context of growing crops in a garden, the adjective **different** is used to describe growing various types or kinds of healthy vegetables (such as spinach, kales, carrots, and onions).

**Why Other Options Are Incorrect:**
* **dry:** Living, growing vegetables in a garden are fresh and watered, not dry.
* **cooked:** Vegetables grow raw in the soil; they are only cooked after harvesting.
* **plenty:** Requires the preposition "of" to function correctly as a determiner (**plenty of vegetables**), so it cannot directly modify "vegetables" here.

📌 **Key Learning Note:**
"Different vegetables" means various types of healthy crops growing together in a garden.""",

    18: """The correct answer is **enjoys**.

**Detailed Analysis of the Correct Answer:**
Contextual verbs express feelings towards an activity. The passage states Asha likes her garden and prefers working in it over sitting inside playing phone games. Therefore, she **enjoys** taking care of her vegetables.

**Why Other Options Are Incorrect:**
* **begins:** Refers only to starting an action, which does not convey her affection or passion for gardening.
* **accepts:** Means agreeing to receive something, which does not make sense with taking care of vegetables.
* **admires:** Means looking at something with appreciation, whereas taking care of a garden is active labor (**enjoys taking care**).

📌 **Key Learning Note:**
Phrasing like "enjoys taking care of" shows active pleasure and dedication in looking after something.""",

    19: """The correct answer is **and**.

**Detailed Analysis of the Correct Answer:**
The coordinating conjunction **and** is used to connect two related indoor activities that Asha dislikes doing: *sitting in the house* AND *playing games on the phone*. 

**Why Other Options Are Incorrect:**
* **also:** An adverb used for adding information, requiring a different sentence structure.
* **yet:** A contrasting conjunction meaning "but", which is incorrect because both activities are complementary indoor actions.
* **because:** A causal conjunction used to introduce a reason, not to link two parallel actions.

📌 **Key Learning Note:**
Use **and** to join two related or parallel activities in a single clause.""",

    20: """The correct answer is **next**.

**Detailed Analysis of the Correct Answer:**
When expressing expectations about an upcoming time period in English, we use the adjective **next**. Therefore, "sell her harvest **next month**" correctly refers to the month immediately following the present one.

**Why Other Options Are Incorrect:**
* **future:** Needs a prepositional phrase like *in the future* or an adjective like *future plans*, not *future month*.
* **new:** Refers to something recently created or acquired, not a coming calendar month.
* **later:** An adverb requiring a phrase like *later this month*, not *later month*.

📌 **Key Learning Note:**
Use **next month**, **next week**, or **next year** to refer to upcoming calendar time periods."""
}

for q in data['sectionA']:
    q_num = q['questionNumber']
    if q_num in batch4_explanations:
        q['explanation'] = batch4_explanations[q_num]

new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_js = f"{prefix}{new_json_str}{suffix}\n"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Batch 4 (Q16 - Q20) updated successfully in kpsea-english-2023.js!")
