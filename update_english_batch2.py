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

batch2_explanations = {
    6: """The correct answer is **To make us happy.**

**Detailed Analysis of the Correct Answer:**
Paragraph 1 of the passage explicitly defines a pet as an animal kept for pleasure and companionship: **"We keep pets because we love their company... They are just like our friends, so we keep them happy and comfortable."** Keeping pets brings joy and happiness to our lives.

**Why Other Options Are Incorrect:**
* **To help us carry heavy things.:** The passage states that work animals like donkeys are kept to carry heavy luggage, not pets.
* **To provide food.:** Paragraph 3 explains that livestock (like cows and chickens) are kept as a source of food (milk and eggs), not pets.
* **To protect the environment.:** Protecting the environment is not mentioned in the passage as a reason for keeping pets.

📌 **Key Learning Note:**
Pets are kept for pleasure, love, and companionship ("to make us happy"), while work animals are kept to assist with heavy labor.""",

    7: """The correct answer is **They can do things that we cannot do.**

**Detailed Analysis of the Correct Answer:**
Paragraph 2 explicitly states: **"This is because they have special abilities which human beings do not have. For example, donkeys have strength to carry heavy luggage."** This confirms that animals can perform tasks and have physical capabilities beyond human abilities.

**Why Other Options Are Incorrect:**
* **They are man's best friend.:** Paragraph 1 specifically states that only the **dog** has been said to be man's best friend, not donkeys.
* **They are better than us.:** The text does not claim that animals are superior to humans overall.
* **They are always comfortable and healthy.:** Paragraph 1 states that *we* must make sure to keep them happy and comfortable, not that they are always comfortable on their own.

📌 **Key Learning Note:**
Animals assist humans because they possess unique physical abilities (such as strength or heightened senses) that humans lack.""",

    8: """The correct answer is **unusual.**

**Detailed Analysis of the Correct Answer:**
In Paragraph 2, the phrase **"special abilities"** refers to extraordinary, uncommon, or exceptional traits that set animals apart from humans. Among the given choices, **unusual** best matches this meaning of being remarkable or out of the ordinary.

**Why Other Options Are Incorrect:**
* **strange.:** This implies odd or weird in a negative way, which does not fit the positive context of helpful animal abilities.
* **new.:** Means recently acquired or created, which does not mean exceptional or unique.
* **unknown.:** Means unfamiliar or obscure, whereas these animal abilities are well known to humans.

📌 **Key Learning Note:**
Contextual vocabulary: In this context, "special" means uncommon, extraordinary, or **unusual** abilities.""",

    9: """The correct answer is **We may not get enough benefits from them.**

**Detailed Analysis of the Correct Answer:**
Paragraph 3 emphasizes that all animals—whether kept as pets, work animals, or food sources—deserve kind treatment. If we mistreat them, pets will not provide joyful companionship, work animals will grow weak or fall ill, and food animals will produce fewer products. Thus, we will lose out on their maximum benefits.

**Why Other Options Are Incorrect:**
* **They will not live with us.:** Domestic animals may remain in captivity even if mistreated, so leaving is not the direct main consequence.
* **They may not give us enough food.:** This only applies to livestock (milk/eggs), whereas the question asks about all domestic animals generally.
* **We may not be happy and comfortable.:** This focuses only on pets, rather than the total practical benefits lost across all types of animals.

📌 **Key Learning Note:**
Treating animals kindly ensures they stay healthy, productive, and able to provide us with maximum benefits.""",

    10: """The correct answer is **He wanted Hassan to get the right balance from the shopkeeper.**

**Detailed Analysis of the Correct Answer:**
In Paragraph 1, the story states that Hassan's father wrote the prices on a list, calculating the total cost (425 shillings) from a 500-shilling note. This enabled Hassan to calculate and expect the exact balance of 75 shillings, ensuring he received the right change from the shopkeeper.

**Why Other Options Are Incorrect:**
* **He did not want Hassan to forget any item.:** The prices were written specifically so Hassan could know the exact total cost and expected balance.
* **He did not want Hassan to delay in the shop.:** Saving time was not stated as the primary reason for writing down the prices.
* **He wanted Hassan to do the totals of the cost of the items.:** Hassan's father had already calculated the total cost (425 shillings) and balance on the list.

📌 **Key Learning Note:**
Writing down item prices helps buyers verify total costs and ensure they receive the exact correct change/balance."""
}

for q in data['sectionA']:
    q_num = q['questionNumber']
    if q_num in batch2_explanations:
        q['explanation'] = batch2_explanations[q_num]

new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_js = f"{prefix}{new_json_str}{suffix}\n"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Batch 2 (Q6 - Q10) updated successfully in kpsea-english-2023.js!")
