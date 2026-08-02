import json
import re

file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\src\data\kpsea-english-2023.js"

explanations = {
    "eq1": """📌 **Concept Overview: Telephone Etiquette & Grammatical Case (Who vs. Whom)**

When speaking on the telephone in a formal or respectful context (such as a student calling a teacher), it is essential to use polite expressions. Grammatically, we also need to pay attention to the difference between **who** (subject pronoun) and **whom** (object pronoun).

• **Subject pronoun (Who):** Refers to the person performing the action (e.g., *Who answered the phone?*).
• **Object pronoun (Whom):** Refers to the person receiving the action or standing as the object of a preposition like *to*, *with*, or *for* (e.g., *To whom am I speaking?* or *Whom am I speaking to?*).

In this question, Barasa calls his class teacher. After saying hello, he wants to confirm the identity of the person on the line before proceeding.

---

✅ **Why Option C (*"Whom am I speaking to?"*) is Correct:**
Option C is the most grammatically correct and polite phrasing. Here, the pronoun is the object of the preposition **to** (*I am speaking to [person]*), making **whom** the correct grammatical choice. Furthermore, it is respectful and appropriate for a pupil speaking to a teacher.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"Who are you?"*):
  * *Why it's wrong:* This phrase is very blunt, rude, and aggressive. In formal telephone communication—especially with authority figures like teachers—asking "Who are you?" comes across as disrespectful.
• **Option B** (*"Who is this?"*):
  * *Why it's wrong:* While common in very informal or casual chats with friends, it lacks formal courtesy. Additionally, grammatically, when asking for the object of your call, "whom" is preferred in formal dialogue.
• **Option D** (*"Whom do you want to speak to?"*):
  * *Why it's wrong:* This option reverses the caller's role. Barasa is the one who initiated the call to get help; he is not an operator asking the teacher who she wants to speak to!

---

💡 **Key Takeaway for Your Revision Notes:**
1. Use **Whom** after or before prepositions like *to*, *with*, or *for* (e.g., *To whom it may concern*, *Whom am I speaking to?*).
2. Always use polite, formal phrasing when speaking to teachers or elders on the telephone.""",

    "eq2": """📌 **Concept Overview: Modal Auxiliary Verbs for Seeking Permission**

Modal auxiliary verbs (such as **may**, **can**, **must**, **will**, **should**) express mood, permission, ability, obligation, or certainty. When interacting with teachers, parents, or authority figures, choosing the right modal verb determines whether your request sounds polite, demanding, or confusing.

In this context, Barasa needs to explain why he might be late and ask his teacher for approval/permission to arrive late while helping his younger sister on her first day of Grade 1.

---

✅ **Why Option A (*"May I be late for school today?"*) is Correct:**
**May** is the standard modal verb used in formal English to politely request permission from a person in authority.
• Example: *May I come in?*, *May I leave early?*, *May I be late today?*
Barasa is politely asking his teacher to allow him to arrive late, which fits the dialogue perfectly.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option B** (*"I want to be late for school today."*):
  * *Why it's wrong:* Expressing what you *want* sounds self-centered and childish. Arriving late is a necessity due to a family situation, not a fun activity Barasa "wants" to do.
• **Option C** (*"I will be late for school today."*):
  * *Why it's wrong:* Using **will** creates a direct, demand-like statement of fact without asking for permission or showing respect for school rules.
• **Option D** (*"Must I be late for school today?"*):
  * *Why it's wrong:* **Must** expresses compulsion or strong obligation (e.g., *Must I do my homework now?*). Asking "Must I be late?" implies someone is forcing him to be late against his will, which makes no sense here.

---

💡 **Key Takeaway for Your Revision Notes:**
When requesting permission from teachers or elders, always start with **"May I..."** rather than stating desires (**"I want to..."**) or commands (**"I will..."**).""",

    "eq3": """📌 **Concept Overview: Social Etiquette & Dialogue Responses**

In English dialogue comprehension, choosing the right response depends on the context of the conversation. When an authority figure (like a class teacher) listens to your request and grants you permission or assistance, standard politeness requires expressing gratitude.

In the passage, the teacher says: *"Okay, Barasa. You can come along with her. Make sure you come to see me after she settles down in her classroom."*

---

✅ **Why Option D (*"Thank you, Teacher."*) is Correct:**
Since the teacher has kindly granted Barasa permission to come to school late with his younger sister, the only appropriate, polite response is to thank her. **"Thank you, Teacher."** acknowledges the favor and closes the dialogue respectfully.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"That's good, Teacher."*):
  * *Why it's wrong:* This sounds evaluative—as if the student is rating or approving the teacher's decision, which is improper etiquette for a student.
• **Option B** (*"It's okay, Teacher."*):
  * *Why it's wrong:* "It's okay" is typically used to reassure someone or forgive a minor mistake (e.g., *"Sorry I bumped into you." — "It's okay."*). It does not convey appreciation.
• **Option C** (*"It's alright, Teacher."*):
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

✅ **Why Option B (*"would"*) is Correct:**
Following the Second Conditional rule (*If + past simple -> WOULD + base verb*), the modal verb **would** pairs correctly with **had** to express what the speaker *would do* in this hypothetical situation.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"should"*):
  * *Why it's wrong:* **Should** is used to give advice or express duty (e.g., *You should study hard*), not to complete a second conditional hypothetical statement.
• **Option C** (*"can"*):
  * *Why it's wrong:* **Can** is present tense and cannot pair with the past simple verb *had* in a conditional clause.
• **Option D** (*"will"*):
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

✅ **Why Option C (*"on"*) is Correct:**
**On foot** is an established, unbreakable English idiom meaning to walk. We say *"on foot"*, never *"by foot"*.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"by"*):
  * *Why it's wrong:* Although we say *by car* or *by bus*, saying *by foot* is a common error made by English learners. Standard English requires **on foot**.
• **Option B** (*"with"*):
  * *Why it's wrong:* **With** indicates using an instrument or tool (e.g., *write with a pen*, *cut with a knife*) or being accompanied by someone, not a mode of transport.
• **Option D** (*"in"*):
  * *Why it's wrong:* **In** is used for being inside certain vehicles (*in a taxi*), not for walking.

---

💡 **Key Takeaway for Your Revision Notes:**
* **Walking ➔ ON foot** (Always! Never say "by foot").
* **Vehicles ➔ BY car, BY bus, BY bicycle, BY train**.""",

    "eq6": """📌 **Concept Overview: Extracting Direct Facts in Reading Comprehension**

When answering reading comprehension questions, always refer directly to the facts stated in the passage rather than relying on general real-world knowledge.

In Paragraph 1, the text defines a pet and explains why humans keep them:
> *"A pet is an animal kept for pleasure. We keep pets because we love their company. We play with them."*

---

✅ **Why Option B (*"To make us happy."*) is Correct:**
The passage explicitly states that pets are kept for **pleasure** and **companionship**. Bringing us pleasure and playing with us is another way of saying they make us happy.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"To help us carry heavy things."*):
  * *Why it's wrong:* The second paragraph states that donkeys are kept to carry heavy luggage (work animals), not pets.
• **Option C** (*"To provide food."*):
  * *Why it's wrong:* Paragraph 3 notes that livestock (like cows and chickens) are kept as a source of food (milk and eggs), not pets.
• **Option D** (*"To protect the environment."*):
  * *Why it's wrong:* Environmental protection is not mentioned anywhere in the passage as a purpose for keeping pets.

---

💡 **Key Takeaway for Your Revision Notes:**
* **Pets** ➔ Kept for pleasure and companionship (to make us happy).
* **Work animals** ➔ Kept for labor (carrying loads).
* **Livestock** ➔ Kept as a source of food (milk, eggs, meat).""",

    "eq7": """📌 **Concept Overview: Identifying True Statements in Comprehension**

To identify which statement is **true**, compare each choice carefully against the exact information provided in the passage.

Paragraph 2 states:
> *"Animals can also be kept to help human beings do certain tasks. This is because they have special abilities which human beings do not have."*

---

✅ **Why Option C (*"They can do things that we cannot do."*) is Correct:**
This option directly matches the text in Paragraph 2, which highlights that animals have **special abilities** (such as immense strength or extraordinary sense of smell) that human beings do not possess.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"They are man's best friend."*):
  * *Why it's wrong:* The text specifically says that *the dog* is man's best friend, not donkeys. We cannot apply a statement about dogs to donkeys as well.
• **Option B** (*"They are better than us."*):
  * *Why it's wrong:* The text never states or implies that animals are superior to humans; it only notes they have specific abilities humans lack.
• **Option D** (*"They are always comfortable and healthy."*):
  * *Why it's wrong:* Paragraph 1 says *we keep them happy and comfortable*, meaning human care makes them comfortable, not that they are automatically healthy on their own.

---

💡 **Key Takeaway for Your Revision Notes:**
When a question asks what is **true** about two subjects (e.g., donkeys AND dogs), ensure the statement applies to **both** according to the passage.""",

    "eq8": """📌 **Concept Overview: Vocabulary in Context (Synonyms)**

In reading comprehension, the meaning of a word depends on how it is used in the passage. Finding a synonym requires choosing the word that preserves the original meaning of the sentence.

In the passage, the word **special** describes abilities that set animals apart from humans (such as a donkey's exceptional pulling power). In this context, *special* means exceptional, extraordinary, or out of the ordinary (**unusual**).

---

✅ **Why Option B (*"unusual."*) is Correct:**
In this sentence, **unusual** means extraordinary or non-ordinary traits that humans do not have. Replacing "special abilities" with "unusual abilities" preserves the true meaning of the text.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"strange."*):
  * *Why it's wrong:* "Strange" means odd, weird, or unnatural. It has a negative tone that does not fit the positive context of useful animal abilities.
• **Option C** (*"new."*):
  * *Why it's wrong:* "New" means recently created or discovered. Animals have possessed these abilities naturally for thousands of years.
• **Option D** (*"unknown."*):
  * *Why it's wrong:* "Unknown" means hidden or undiscovered. Animal abilities like carrying heavy loads are well known.

---

💡 **Key Takeaway for Your Revision Notes:**
* **Special (in context)** = Extraordinary, unique, or unusual.
* Always test candidate synonyms by substituting them into the sentence to check if the meaning remains unchanged.""",

    "eq9": """📌 **Concept Overview: Making Logical Inferences from a Passage**

An **inference** is a logical conclusion reached based on evidence from the text.

The passage explains that animals serve three main purposes:
1. Providing companionship (pets)
2. Assisting with work (labor)
3. Providing food (milk and eggs)

The final sentence states: *"whether we keep animals as pets, to help in work, or for food, they deserve kind treatment."*

---

✅ **Why Option C (*"We may not get enough benefits from them."*) is Correct:**
If animals are mistreated, neglected, or abused, pets won't provide companionship, work animals won't have strength to work, and livestock won't produce food. Therefore, we lose the **overall benefits** they provide to human beings.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"They will not live with us."*):
  * *Why it's wrong:* Domestic animals often cannot leave on their own even if mistreated, so this is factually inaccurate.
• **Option B** (*"They may not give us enough food."*):
  * *Why it's wrong:* This applies only to livestock, but the conclusion must apply to **all** categories of animals mentioned in the text (pets, work animals, and food animals).
• **Option D** (*"We may not be happy and comfortable."*):
  * *Why it's wrong:* This focuses primarily on pets, ignoring the economic and physical work benefits of donkeys and livestock.

---

💡 **Key Takeaway for Your Revision Notes:**
When drawing conclusions about a whole passage, choose the option that covers **all** examples mentioned in the text (pets, work animals, and food animals combined).""",

    "eq10": """📌 **Concept Overview: Understanding Character Motives in Narrative Passages**

Narrative passages often contain details that explain why a character takes a specific action.

Paragraph 1 explains:
> *"His father had written the prices of the items on a list. The total cost was four hundred and twenty five shillings. His father had given him five hundred shillings. Hassan was expecting a balance of seventy five shillings."*

---

✅ **Why Option C (*"He wanted Hassan to get the right balance from the shopkeeper."*) is Correct:**
By writing down the price of each item on the list, Hassan's father enabled Hassan to calculate the exact total cost (425 shillings) and know the exact change/balance he was supposed to receive (75 shillings).

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"He did not want Hassan to forget any item."*):
  * *Why it's wrong:* The story specifically emphasizes that the father wrote down the **prices** of the items so Hassan could track the money and change.
• **Option B** (*"He did not want Hassan to delay in the shop."*):
  * *Why it's wrong:* Speeding up shopping time is not mentioned or implied as the father's motive.
• **Option D** (*"He wanted Hassan to do the totals of the cost of the items."*):
  * *Why it's wrong:* Calculating the total was just a step toward knowing the **expected balance**, which was the primary purpose when giving him a 500 shilling note.

---

💡 **Key Takeaway for Your Revision Notes:**
Listing prices before going shopping ensures you know the total cost beforehand and can verify that you receive the exact change.""",

    "eq11": """📌 **Concept Overview: Cause and Effect in Story Details**

In reading comprehension, it is vital to link a character's reaction (surprise) to its immediate cause in the text.

Paragraph 4 explicitly connects her reaction to time:
> *"The shopkeeper was surprised to see him back **so soon**."*

---

✅ **Why Option C (*"Hassan had just left the shop."*) is Correct:**
The shopkeeper was surprised because Hassan had literally just walked out a moment earlier. Seeing him re-enter the shop almost immediately (**so soon**) caught her off guard.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"Hassan returned the money."*):
  * *Why it's wrong:* Returning the money caused her to feel **grateful** and call him an "angel", but her initial surprise was triggered by how fast he came back.
• **Option B** (*"the shopkeeper was very busy that day."*):
  * *Why it's wrong:* Being busy explains why she made a mistake giving too much change, not why she was surprised to see Hassan return.
• **Option D** (*"the shopkeeper had given him the balance."*):
  * *Why it's wrong:* Giving change was a routine shopkeeper task, not something that would cause her surprise.

---

💡 **Key Takeaway for Your Revision Notes:**
Pay close attention to time clues in stories (such as *"so soon"* or *"immediately"*) when explaining why a character is surprised.""",

    "eq12": """📌 **Concept Overview: Identifying Proverbs and Moral Lessons**

Stories often teach a moral lesson summarized by a classic proverb.

In this story, Hassan realizes he was given 575 shillings instead of 75 shillings balance. Although he initially wanted to spend it, he remembered his father's advice: *"Never take what does not belong to you."* He returned the extra money, demonstrating **honesty**.

---

✅ **Why Option A (*"honesty is the best policy."*) is Correct:**
This proverb means that being truthful and honest is always the right and most rewarding path. Hassan's honest act earned him praise, self-respect, and made his parents proud.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option B** (*"hurry hurry has no blessing."*):
  * *Why it's wrong:* This proverb warns against acting too fast without thinking (*Swahili: Haraka haraka haina baraka*). Hassan did not suffer due to rushing.
• **Option C** (*"once bitten twice shy."*):
  * *Why it's wrong:* This means being cautious after experiencing a past bad event. Hassan was not previously cheated or hurt.
• **Option D** (*"a friend in need is a friend indeed."*):
  * *Why it's wrong:* This proverb relates to true friendship during difficult times, which is unrelated to returning extra money to a shopkeeper.

---

💡 **Key Takeaway for Your Revision Notes:**
* **Honesty is the best policy** ➔ Always do what is right and return what doesn't belong to you.""",

    "eq13": """📌 **Concept Overview: Fact Checking Fables**

When answering questions about a fable, verify each statement against the story events to determine which choice is factually accurate.

The very first sentence of the story states:
> *"Many afternoons, Hyena and Hare spent hours in a field eating the farmer's groundnuts."*

---

✅ **Why Option A (*"Hare stole the groundnuts just like Hyena."*) is Correct:**
Both Hare and Hyena went into the farmer's field to eat groundnuts without permission. Therefore, both of them were stealing the farmer's crops.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option B** (*"Hare was a true friend of the farmer."*):
  * *Why it's wrong:* Hare lied to the farmer that he would catch the thief, while secretly stealing the groundnuts himself. He was deceiving the farmer.
• **Option C** (*"Hare was not able to cheat Hyena."*):
  * *Why it's wrong:* Hare successfully tricked Hyena into burying his four legs in the soil so Hyena couldn't run away.
• **Option D** (*"Hare buried one of his legs in the ground."*):
  * *Why it's wrong:* Hare did not bury any of his legs; he lied to Hyena that his legs were too short to be buried.

---

💡 **Key Takeaway for Your Revision Notes:**
Do not be fooled by Hare's lies to the farmer; both Hare and Hyena were thieves stealing groundnuts.""",

    "eq14": """📌 **Concept Overview: Identifying Character Traits in Folktales**

A **character trait** describes a character's personality based on their actions, words, and decisions throughout a story.

In this story, Hare:
1. Pretended to help the farmer catch the thief.
2. Formulated a lie to trick Hyena into burying his legs in the dirt.
3. Abandoned Hyena to get beaten while he ran away safely.

---

✅ **Why Option D (*"tricky"*) is Correct:**
Hare demonstrated deceit, cunning, and trickery to save himself at the expense of Hyena. In African folktales, Hare is famously portrayed as a **tricky** character.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"friendly"*):
  * *Why it's wrong:* A true friend would not trick you into getting caught and beaten. Hare betrayed Hyena.
• **Option B** (*"funny"*):
  * *Why it's wrong:* While the situation may seem humorous, Hare's core personality trait is cunningness/trickery, not being a comedian.
• **Option C** (*"busy"*):
  * *Why it's wrong:* Being "busy" implies doing productive work. Hare was spending time stealing crops and plotting tricks.

---

💡 **Key Takeaway for Your Revision Notes:**
* **Tricky / Cunning / Sly** ➔ A character who uses clever lies and tricks to outsmart others.""",

    "eq15": """📌 **Concept Overview: Deriving Moral Lessons from Fables**

Fables use animal characters to teach humans valuable life lessons about behavior, friendship, and wisdom.

In the story, Hyena blindly trusted Hare's trick (*"groundnuts are sweeter when you eat them with your legs buried"*), which resulted in Hyena getting caught and severely beaten by the farmer.

---

✅ **Why Option B (*"We should keep the right friends."*) is Correct:**
The story warns us against keeping dishonest, treacherous companions. Hyena's choice to hang around a tricky friend like Hare led directly to his punishment.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"People need to share what they have."*):
  * *Why it's wrong:* The story is about stealing and betrayal, not generous sharing.
• **Option C** (*"Farmers should beat all Hyenas."*):
  * *Why it's wrong:* Animal beating is a plot event in the story, not the moral lesson meant for human readers.
• **Option D** (*"We should always do what we are told."*):
  * *Why it's wrong:* Doing whatever you are told without thinking (like Hyena obeying Hare's bad advice) leads to disaster!

---

💡 **Key Takeaway for Your Revision Notes:**
Choose your friends carefully! Keeping untrustworthy or trickster friends will bring you trouble."""
}

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

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
    print("Successfully updated questions 1 to 15 in kpsea-english-2023.js")
else:
    print("Could not match JS object")
