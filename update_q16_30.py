import json
import re

file_path = r"c:\Users\JOASH\Desktop\CBC\offline-exam-app\src\data\kpsea-english-2023.js"

explanations = {
    "eq16": """📌 **Concept Overview: Possessive Adjectives vs. Possessive Pronouns**

In English grammar, showing ownership requires choosing the correct pronoun or adjective based on gender and sentence structure:

1. **Possessive Adjectives (my, your, his, her, its, our, their):**
   * Placed **before a noun** to modify it.
   * Example: *This is her book*, *It is her grandfather*.
2. **Possessive Pronouns (mine, yours, his, hers, ours, theirs):**
   * Used **alone without a noun** following it.
   * Example: *This book is hers*, *The garden is hers*.
3. **Objective Pronouns (me, you, him, her, us, them):**
   * Used as the object of a verb or preposition (e.g., *I saw him*).

In this sentence: Asha is female. The blank comes directly **before the noun** *grandfather*.

---

✅ **Why Option D (*"her"*) is Correct:**
Because Asha is female and the word comes immediately before the noun *grandfather*, we use the possessive adjective **her** (*her grandfather*).

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"his"*):
  * *Why it's wrong:* **His** is used for male owners (he/his). Since Asha is a girl, using *his* would refer to a male owner.
• **Option B** (*"hers"*):
  * *Why it's wrong:* **Hers** is a possessive pronoun used without a noun following it (e.g., *the gift is hers*). It cannot be placed directly before *grandfather*.
• **Option C** (*"him"*):
  * *Why it's wrong:* **Him** is an object pronoun (e.g., *give it to him*), not a possessive word.

---

💡 **Key Takeaway for Your Revision Notes:**
* Use **her** before a noun (*her garden*, *her grandfather*).
* Use **hers** when there is no noun following it (*the garden is hers*).""",

    "eq17": """📌 **Concept Overview: Contextual Adjectives in Sentence Completion**

An **adjective** modifies a noun by describing its quality, quantity, or condition. When completing a cloze test (fill-in-the-blanks passage), the chosen adjective must make logical and grammatical sense in a real-world context.

In a thriving home garden, a gardener plants several distinct varieties of vegetables (e.g., spinach, kale, carrots, tomatoes).

---

✅ **Why Option A (*"different"*) is Correct:**
The adjective **different** describes variety and diversity (*growing different kinds of vegetables*). It fits the passage perfectly as Asha cultivates various vegetable types.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option B** (*"dry"*):
  * *Why it's wrong:* Vegetables growing in a home garden are fresh, green, and watered, not withered or dry.
• **Option C** (*"cooked"*):
  * *Why it's wrong:* Vegetables grow raw in the soil; they are only cooked after harvesting in the kitchen!
• **Option D** (*"plenty"*):
  * *Why it's wrong:* Grammatically, **plenty** requires the preposition *of* when modifying a noun (e.g., *plenty OF vegetables*). You cannot say *"grows plenty vegetables"*.

---

💡 **Key Takeaway for Your Revision Notes:**
* **Different vegetables** = a variety of fresh crops.
* Remember: *plenty* MUST be followed by *of* (*plenty of vegetables*).""",

    "eq18": """📌 **Concept Overview: Verbs Followed by Gerunds (-ing forms)**

Certain verbs in English express personal feelings and preferences when paired with a **gerund** (a verb ending in *-ing* acting as a noun, such as *taking care*, *reading*, *playing*).

The context shows that Asha loves her garden (given by her grandfather) and prefers gardening over sitting indoors playing mobile games.

---

✅ **Why Option C (*"enjoys"*) is Correct:**
The verb **enjoys** means taking pleasure in an activity. Paired with the gerund *taking care*, **"enjoys taking care"** accurately reflects her joy and love for her garden.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"begins"*):
  * *Why it's wrong:* "Begins" only indicates the start of an action, ignoring her emotional fondness and happiness in doing it.
• **Option B** (*"accepts"*):
  * *Why it's wrong:* "Accepts" means agreeing to receive something or taking on a duty reluctantly, which contradicts her cheerful passion.
• **Option D** (*"admires"*):
  * *Why it's wrong:* "Admires" means looking at something with approval from a distance. Gardening involves active physical care, not just passive admiring.

---

💡 **Key Takeaway for Your Revision Notes:**
Verbs of preference (**enjoy, love, like**) are naturally followed by *-ing* gerunds (e.g., *She enjoys gardening*, *He loves reading*).""",

    "eq19": """📌 **Concept Overview: Coordinating Conjunctions in Negative List Sentences**

A **conjunction** connects words, phrases, or clauses. The coordinating conjunction **and** links two similar or parallel activities.

When a sentence begins with a negative verb phrase (*"She does not like to..."*), using **and** connects both disliked activities into a single linked list:
1. *sit in the house*
2. *play games on the phone*

---

✅ **Why Option B (*"and"*) is Correct:**
**And** smoothly joins the two parallel infinitive verbs (*sit in the house AND play games on the phone*) that Asha dislikes doing together indoors.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"also"*):
  * *Why it's wrong:* "Also" is an adverb, not a coordinating conjunction. Using it here produces a grammatically broken sentence (*"sit in the house also play games"*).
• **Option C** (*"yet"*):
  * *Why it's wrong:* "Yet" introduces a surprise or contrast (like *but*). There is no contrast between sitting indoors and playing phone games.
• **Option D** (*"because"*):
  * *Why it's wrong:* "Because" gives a cause or reason. Playing games on the phone is not the *reason why* she sits in the house; it is a second activity she dislikes.

---

💡 **Key Takeaway for Your Revision Notes:**
Use **and** to join two parallel actions or activities in a sentence (e.g., *like to read AND write*, *does not like to sit in the house AND play games*).""",

    "eq20": """📌 **Concept Overview: Adjectives in Time Expressions**

When referring to upcoming calendar periods (days, weeks, months, years), English uses specific time adjectives directly before time nouns.

The standard time phrase used to refer to the month immediately following the present one is **next month**.

---

✅ **Why Option C (*"next"*) is Correct:**
The adjective **next** modifies the noun *month* to create the standard time expression **next month** (meaning the coming month).

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"future"*):
  * *Why it's wrong:* "Future" requires a prepositional phrase like *in the future* or acts as a modifier for nouns like *future plans*, but we do not say *"future month"*.
• **Option B** (*"new"*):
  * *Why it's wrong:* "New month" refers to the start of a calendar cycle, not the time when crops reach harvest maturity.
• **Option D** (*"later"*):
  * *Why it's wrong:* "Later" is an adverb. To use *later*, you would say *later this month* or *later on*, not *"later month"*.

---

💡 **Key Takeaway for Your Revision Notes:**
Standard upcoming time phrases: **next week**, **next month**, **next year** (no prepositions needed before them!).""",

    "eq21": """📌 **Concept Overview: Prepositions of Place (In vs. On vs. At vs. Over)**

Prepositions show the spatial relationship between nouns:

1. **IN:** Used for enclosed spaces, rooms, containers, and buildings (*in the room*, *in the classroom*, *in the box*).
2. **ON:** Used for position resting on a surface (*on the desk*, *on the floor*).
3. **TO:** Indicates movement towards a destination (*walking to school*).
4. **OVER:** Indicates a position directly above without touching (*a plane flew over the school*).

---

✅ **Why Option B (*"in"*) is Correct:**
A classroom is a three-dimensional enclosed building space. Therefore, being inside it requires the preposition **in** (*in the classroom*).

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"to"*):
  * *Why it's wrong:* **To** indicates movement/direction towards a place (e.g., *walked to the classroom*), whereas *found* describes finding someone who is already located inside.
• **Option C** (*"on"*):
  * *Why it's wrong:* **On** implies resting on top of a flat surface (e.g., *sitting on top of the roof*), which makes no sense for a person inside a classroom.
• **Option D** (*"over"*):
  * *Why it's wrong:* **Over** means hanging or flying above the classroom in the air.

---

💡 **Key Takeaway for Your Revision Notes:**
* **IN** ➔ Enclosed spaces (classroom, kitchen, hospital, car).
* **ON** ➔ Surfaces (table, wall, floor).
* **TO** ➔ Direction of movement (go to, walk to).""",

    "eq22": """📌 **Concept Overview: Prepositions for Physical Surfaces**

When an object is placed so that it rests upon a flat, horizontal surface (like a desk, table, shelf, or floor), standard English uses the preposition **on**.

---

✅ **Why Option B (*"on"*) is Correct:**
A book placed on top of a table rests on its surface. Therefore, **on** is the exact preposition required (*on the table*).

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"with"*):
  * *Why it's wrong:* **With** indicates companionship (*Ali left with his friend*) or using a tool (*cut with scissors*), not physical surface placement.
• **Option C** (*"in"*):
  * *Why it's wrong:* **In** means inside a container or enclosed space. You could leave a book *in a drawer*, but a table is a surface, not an enclosure.
• **Option D** (*"from"*):
  * *Why it's wrong:* **From** indicates origin or removal (*took the book from the table*), which contradicts leaving it there.

---

💡 **Key Takeaway for Your Revision Notes:**
Always use **ON** when placing objects on top of surfaces (**on the table**, **on the shelf**, **on the wall**, **on the floor**).""",

    "eq23": """📌 **Concept Overview: Rules of Question Tags**

A **question tag** is a short question added to the end of a statement to confirm information.

To form a correct question tag, follow these three rules:
1. **Rule of Opposites:**
   * Positive Statement ➔ **Negative Tag**
   * Negative Statement ➔ **Positive Tag**
2. **Matching Auxiliary Verb:** Use the same auxiliary/helping verb as the statement (*are* ➔ *aren't*).
3. **Matching Subject Pronoun:** Convert the noun subject into its matching personal pronoun (*The children* = 3rd person plural ➔ **they**).

Sentence: *"The children are planting trees"* (Positive statement with auxiliary **are** and subject **they**).

---

✅ **Why Option A (*"aren't they?"*) is Correct:**
Applying the rules:
• Auxiliary verb: **are** ➔ negative: **aren't**
• Subject: *The children* ➔ pronoun: **they**
Combined tag: **aren't they?**

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option B** (*"aren't we?"*):
  * *Why it's wrong:* Incorrect pronoun. "We" refers to the speakers themselves, but "The children" is third-person plural (*they*).
• **Option C** (*"are they?"*):
  * *Why it's wrong:* Violates the rule of opposites. The statement is positive (*are planting*), so the tag MUST be negative (*aren't*).
• **Option D** (*"are we?"*):
  * *Why it's wrong:* Violates both the rule of opposites (uses positive tag) and subject pronoun agreement (uses *we* instead of *they*).

---

💡 **Key Takeaway for Your Revision Notes:**
* Positive Statement ➔ Negative Tag.
* **The children are... ➔ aren't they?**
* **The boy is... ➔ isn't he?**""",

    "eq24": """📌 **Concept Overview: Differences Between Indefinite Pronouns**

Indefinite pronouns refer to unspecified people or things:

1. **Somebody / Someone:** Used in **affirmative (positive) clauses** when an unknown person did something (*Somebody took my pen*).
2. **Anybody / Anyone:** Used in **negative sentences** (*I didn't see anybody*) or **questions** (*Is anybody there?*).
3. **Everybody / Everyone:** Refers to **all people** in a group (*Everybody enjoyed the trip*).
4. **Nobody / No one:** Refers to **no person** (*Nobody came to the meeting*).

In this sentence: *"...because ------- had taken it."*
The clause after "because" is a positive, affirmative statement explaining why the book is missing.

---

✅ **Why Option B (*"somebody"*) is Correct:**
Since an unknown person stole/took the book in a positive cause-clause, **somebody** is the grammatically correct pronoun.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"anybody"*):
  * *Why it's wrong:* "Anybody" is restricted to negative clauses (*I didn't see anybody*) or questions (*Did anybody take it?*). It cannot be used in a positive statement clause like this.
• **Option C** (*"everybody"*):
  * *Why it's wrong:* "Everybody" means all people. It is illogical to say every person in the class took a single storybook.
• **Option D** (*"nobody"*):
  * *Why it's wrong:* Saying "nobody had taken it" would mean the book was still there, contradicting why Rudisha couldn't find it!

---

💡 **Key Takeaway for Your Revision Notes:**
* Use **somebody** in positive statement clauses (*Somebody took my book*).
* Use **anybody** in negative clauses (*I didn't find anybody*) or questions (*Did anybody see it?*).""",

    "eq25": """📌 **Concept Overview: Agreement of Reflexive Pronouns**

**Reflexive pronouns** (ending in *-self* or *-selves*) are used when the object of a sentence is the same person or group as the subject or object being addressed:

• **I** ➔ *myself*
• **You (singular)** ➔ *yourself*
• **He** ➔ *himself*
• **She** ➔ *herself*
• **It** ➔ *itself*
• **We / Us** ➔ **ourselves**
• **You (plural)** ➔ *yourselves*
• **They / Them** ➔ *themselves*

Sentence context: *"The teacher told **us** to take care of..."*
The pronoun being addressed to take care is **us** (1st person plural).

---

✅ **Why Option C (*"ourselves"*) is Correct:**
The object pronoun **us** directly pairs with the 1st person plural reflexive pronoun **ourselves**.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"themselves"*):
  * *Why it's wrong:* "Themselves" pairs with *they / them* (3rd person plural), not *us*.
• **Option B** (*"yourself"*):
  * *Why it's wrong:* "Yourself" is singular 2nd person (one person being spoken to), whereas *us* refers to a plural group.
• **Option D** (*"yourselves"*):
  * *Why it's wrong:* "Yourselves" pairs with 2nd person plural (*you all*). Since the sentence uses *us*, the perspective is 1st person plural (*ourselves*).

---

💡 **Key Takeaway for Your Revision Notes:**
Subject/Object Pronoun ➔ Matching Reflexive Pronoun:
* **Us / We** ➔ **ourselves**
* **Them / They** ➔ **themselves**
* **You (plural)** ➔ **yourselves**""",

    "eq26": """📌 **Concept Overview: Fixed Prepositional Phrases of Manner**

In English, certain prepositions combine with nouns to form **fixed idiomatic phrases** that describe how or in what manner an action was performed.

When describing an action carried out through physical violence, coercion, or compulsion, the set standard phrase is **by force**.

---

✅ **Why Option B (*"by"*) is Correct:**
**By force** is a fixed English prepositional phrase meaning using physical power, violence, or coercion against someone's will.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"with"*):
  * *Why it's wrong:* Although "with" is used for tools (*with a gun*), saying *"with force"* is non-standard in this context. The set idiomatic phrase is strictly **by force**.
• **Option C** (*"at"*):
  * *Why it's wrong:* **At** is used for target points (*at gunpoint*) or times (*at noon*), not in *"at force"*.
• **Option D** (*"under"*):
  * *Why it's wrong:* **Under** is used in phrases like *under compulsion* or *under pressure*, but not with *force*.

---

💡 **Key Takeaway for Your Revision Notes:**
* **By force** = using physical violence or coercion to take or do something.
* Other set phrases: **by accident**, **by mistake**, **by chance**, **by force**.""",

    "eq27": """📌 **Concept Overview: Relative Pronouns (Who vs. Whom vs. Whose vs. Which)**

**Relative pronouns** introduce relative clauses to describe a noun:

1. **Who (Subject for people):** *The girl who won the prize.*
2. **Whom (Object for people):** *The man whom I greeted.*
3. **Which (Subject/Object for animals and things):** *The hen which laid an egg.*
4. **Whose (Possessive for people, animals, or things):** Shows that something belongs to the subject (*The hen whose egg broke* ➔ *the egg belonging to the hen*).

---

✅ **Why Option C (*"whose"*) is Correct:**
The clause describes the *egg* that belongs to the *hen*. To show possession for an animal, we use **whose** (*the hen whose egg broke*).

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"who"*):
  * *Why it's wrong:* "Who" is a subject pronoun reserved exclusively for human beings, not animals or non-humans.
• **Option B** (*"whom"*):
  * *Why it's wrong:* "Whom" is an object pronoun reserved for human beings.
• **Option D** (*"which"*):
  * *Why it's wrong:* "Which" refers to animals and objects, but it does NOT show possession. Saying *"the hen which egg broke"* is grammatically broken because *which* cannot modify a possessed noun directly like *whose*.

---

💡 **Key Takeaway for Your Revision Notes:**
Use **whose** to show possession for **people**, **animals**, or **objects** (e.g., *the boy whose pen was lost*, *the hen whose egg broke*).""",

    "eq28": """📌 **Concept Overview: The Bare Infinitive Rule after Modal Auxiliary Verbs**

In English grammar, **modal auxiliary verbs** (such as **will, shall, can, could, may, might, must, should, would**) must ALWAYS be followed immediately by a **bare infinitive** (the base form of the verb without *'to'* and without any tense endings like *-s*, *-ed*, or *-ing*).

Formula: **MODAL VERB (will) + BASE VERB (give)**

---

✅ **Why Option D (*"give"*) is Correct:**
**Give** is the plain base verb form (bare infinitive). Following the modal verb **will**, it correctly completes the future tense statement (*will give*).

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"given"*):
  * *Why it's wrong:* "Given" is a past participle used with helper verbs like *has/have/had* (*has given*). It can NEVER follow a modal verb directly.
• **Option B** (*"gives"*):
  * *Why it's wrong:* "Gives" is the third-person singular present form (*he gives*). Adding an *-s* to a verb after a modal verb is a major grammatical error.
• **Option C** (*"gave"*):
  * *Why it's wrong:* "Gave" is the simple past tense form. You cannot place a past tense verb immediately after a modal verb (*will gave* is ungrammatical).

---

💡 **Key Takeaway for Your Revision Notes:**
* **Rule:** Modal Verbs (**will, can, may, must, should**) + **BASE VERB** (*give*, *go*, *see*, *play*).
* Examples: *will give*, *can run*, *must study* (Never add *-ed*, *-s*, or *-ing*!).""",

    "eq29": """📌 **Concept Overview: Meaning of Correlative Conjunctions (Neither... Nor)**

Correlative conjunctions work in pairs to join two negative items or people:

• **Neither A nor B:** Means **NOT A and NOT B** (negating both options completely).
• **Either A or B:** Means **one of the two** options (choice between A or B).
• **Both A and B:** Joins two positive items together.

In the sentence: *"Neither Kalusi nor Sofia came late to class."*
• Kalusi did NOT come late.
• Sofia did NOT come late.
• Therefore, **both of them arrived on time (did not come late)**.

---

✅ **Why Option D (*"Both Kalusi and Sofia did not come late to class."*) is Correct:**
Option D accurately conveys the negative pair meaning: neither of the two students was late.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"Only Kalusi came late to class."*):
  * *Why it's wrong:* Claims one student was late, which violates the complete negation of both students by *neither... nor*.
• **Option B** (*"Only Sofia came late to class."*):
  * *Why it's wrong:* Claims the other student was late, which also contradicts the sentence.
• **Option C** (*"Both Kalusi and Sofia came late to class."*):
  * *Why it's wrong:* Reverses the meaning completely into a positive claim that both were late, which is the exact opposite of *Neither... nor*.

---

💡 **Key Takeaway for Your Revision Notes:**
* **Neither A nor B** = **NOT A and NOT B** (Both were not / Neither one did).""",

    "eq30": """📌 **Concept Overview: Reading Comprehension & Restrictive Logic Words**

When analyzing short information passages, pay close attention to restrictive words like **only**, **all**, **also**, and **both**.

Let's break down the facts for each person in the text:
1. **Nasir:** Plays football + **also plays volleyball** (2 sports).
2. **Lona:** Plays football + **also plays netball** (2 sports).
3. **Banda:** Plays football + **no other sport mentioned** (1 sport ONLY).

---

✅ **Why Option B (*"Banda."*) is Correct:**
While all three friends play football, Banda is the only person who plays **football only**, as he does not play any additional sports like volleyball or netball.

---

❌ **Detailed Analysis of Incorrect Options:**

• **Option A** (*"Nasir."*):
  * *Why it's wrong:* Nasir plays football AND volleyball, so he does not play football *only*.
• **Option C** (*"Lona."*):
  * *Why it's wrong:* Lona plays football AND netball, so she does not play football *only*.
• **Option D** (*"All of them."*):
  * *Why it's wrong:* All of them play football, but Nasir and Lona play additional sports, so "All of them" fails the requirement of playing football *only*.

---

💡 **Key Takeaway for Your Revision Notes:**
* Pay close attention to restrictive words like **ONLY** in comprehension questions.
* Make a simple quick list/table when given multi-character facts in a story puzzle."""
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
    print("Successfully updated remaining questions 16 to 30 in kpsea-english-2023.js")
else:
    print("Could not match JS object")
