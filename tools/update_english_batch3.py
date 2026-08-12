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

batch3_explanations = {
    11: """The correct answer is **Hassan had just left the shop.**

**Detailed Analysis of the Correct Answer:**
In Paragraph 4, the text states that Hassan stepped outside, sat under a tree right by the shop, counted the money, remembered his father's advice, and walked straight back to return the extra 500 shillings. The shopkeeper was surprised because Hassan had literally just walked out seconds before and returned so quickly.

**Why Other Options Are Incorrect:**
* **Hassan returned the money.:** Returning the extra cash explains why she felt grateful ("You are an angel"), but seeing him return *so quickly* (just after leaving) is what surprised her initially.
* **the shopkeeper was very busy that day.:** Being busy explains why she made the mistake in giving change, not why she was surprised by his quick return.
* **the shopkeeper had given him the balance.:** Giving change was part of her normal work, not a cause of surprise.

📌 **Key Learning Note:**
The shopkeeper was surprised by Hassan's immediate return right after stepping out of the shop.""",

    12: """The correct answer is **honesty is the best policy.**

**Detailed Analysis of the Correct Answer:**
The main moral of Hassan's story is honesty. Even though Hassan had the chance to keep 500 extra shillings without anyone knowing, he remembered his father's teaching ("Never take what does not belong to you") and returned the money. His honest decision earned him praise, respect, and a peaceful conscience.

**Why Other Options Are Incorrect:**
* **hurry hurry has no blessing.:** This proverb warns against rushing foolishly, which is unrelated to returning extra change.
* **once bitten twice shy.:** This means being cautious after experiencing a bad situation, which does not apply here.
* **a friend in need is a friend indeed.:** This refers to true friends helping each other in tough times, which does not fit the transaction with the shopkeeper.

📌 **Key Learning Note:**
Returning money or items that do not belong to you illustrates the timeless moral: **Honesty is the best policy**.""",

    13: """The correct answer is **Hare stole the groundnuts just like Hyena.**

**Detailed Analysis of the Correct Answer:**
Paragraph 1 states: **"Many afternoons, Hyena and Hare spent hours in a field eating the farmer's groundnuts."** Both animals were stealing and eating the farmer's crops without permission.

**Why Other Options Are Incorrect:**
* **Hare was a true friend of the farmer.:** Hare went to the farmer pretending to help catch the thief, but he was actually the thief deceiving the farmer.
* **Hare was not able to cheat Hyena.:** Hare successfully tricked Hyena into burying his legs in the soil so Hyena couldn't run away.
* **Hare buried one of his legs in the ground.:** Hare lied that his legs were too short and did not bury any of his legs.

📌 **Key Learning Note:**
Both Hare and Hyena were crop thieves, but Hare used trickery to escape while leaving Hyena to get caught.""",

    14: """The correct answer is **tricky**.

**Detailed Analysis of the Correct Answer:**
Throughout the story, Hare acts with cunning deceit. He tricks Hyena into burying all four legs in the dirt so Hyena becomes trapped, while Hare stays free to run away when the farmer approaches. This defines Hare as **tricky** (cunning/sly).

**Why Other Options Are Incorrect:**
* **friendly:** Hare betrayed his companion Hyena to save himself, showing he was not a genuine friend.
* **funny:** Although the story is humorous, Hare's central character trait is being sly and tricky.
* **busy:** Hare spent his time stealing crops and plotting tricks rather than doing honest work.

📌 **Key Learning Note:**
In traditional African folktales, the Hare is typically portrayed as a cunning and **tricky** character.""",

    15: """The correct answer is **We should keep the right friends.**

**Detailed Analysis of the Correct Answer:**
Hyena trusted Hare as a companion, but Hare tricked him into burying his legs, abandoned him, and left him to take a beating from the farmer. This story teaches us to be careful about who we associate with, as untrustworthy friends will betray us in times of trouble.

**Why Other Options Are Incorrect:**
* **People need to share what they have.:** The story is about theft and trickery, not generous sharing.
* **Farmers should beat all Hyenas.:** The moral lesson of a folktale is about human character and wisdom, not physically beating wild animals.
* **We should always do what we are told.:** Blindly obeying bad advice (like Hyena obeying Hare's instruction to bury his legs) leads to disaster.

📌 **Key Learning Note:**
Be wise when choosing companions: keeping untrustworthy or deceitful friends leads to betrayal and trouble."""
}

for q in data['sectionA']:
    q_num = q['questionNumber']
    if q_num in batch3_explanations:
        q['explanation'] = batch3_explanations[q_num]

new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
final_js = f"{prefix}{new_json_str}{suffix}\n"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Batch 3 (Q11 - Q15) updated successfully in kpsea-english-2023.js!")
