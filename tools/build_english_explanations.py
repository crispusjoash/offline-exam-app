import json

explanations_map = {
    1: """📘 **Study Note & Concept Overview:**
In polite telephone etiquette and formal English grammar, when asking for the identity of the person on the other end of the line, we use the objective pronoun 'whom' because it acts as the object of the preposition 'to' (*To whom am I speaking?* or *Whom am I speaking to?*).

✅ **Correct Answer Breakdown:**
**Whom am I speaking to?** is correct because it uses the polite, objective pronoun 'whom' to ask for the recipient's identity in formal telephone communication.

❌ **Why Other Options Are Incorrect:**
* **Who are you?:** Blunt, demanding, and impolite for formal telephone conversations.
* **Who is this?:** Very informal and lacks the professional respect required when speaking to a teacher on the phone.
* **Whom do you want to speak to?:** Reverses the roles; the caller (pupil) is trying to confirm who answered the phone, not asking the teacher who they want to talk to.

💡 **Key Takeaway for Revision:** Use formal, polite phrasing like "Whom am I speaking to?" when inquiring about someone's identity on the phone.""",

    2: """📘 **Study Note & Concept Overview:**
The modal auxiliary verb **May** is used in formal English to politely request permission from an authority figure (such as a teacher or parent).

✅ **Correct Answer Breakdown:**
**May I be late for school today?** is correct because it uses 'May I...' to politely request the teacher's permission to arrive late due to helping his younger sister.

❌ **Why Other Options Are Incorrect:**
* **I want to be late for school today.:** Expresses a personal desire rather than asking for permission politely.
* **I will be late for school today.:** A blunt, direct statement declaring a future action without seeking approval.
* **Must I be late for school today?:** Asks if being late is a compulsory obligation, which makes no sense in this context.

💡 **Key Takeaway for Revision:** Use "May I..." when politely requesting permission from teachers, elders, or authority figures.""",

    3: """📘 **Study Note & Concept Overview:**
In social dialogue etiquette, when someone in authority grants your request or offers assistance, the appropriate and courteous response is to express gratitude.

✅ **Correct Answer Breakdown:**
**Thank you, Teacher.** is correct because Barasa must show gratitude after his class teacher grants him permission to accompany his sister.

❌ **Why Other Options Are Incorrect:**
* **That's good, Teacher.:** Sounds casual and evaluative rather than showing personal appreciation.
* **It's okay, Teacher.:** Informal and sounds like reassuring the teacher instead of thanking them.
* **It's alright, Teacher.:** Casual expression used to accept an apology, not to thank someone for permission.

💡 **Key Takeaway for Revision:** Always respond with "Thank you" when someone grants a request or helps you.""",

    4: """📘 **Study Note & Concept Overview:**
In English grammar, conditional sentences talk about real or imaginary situations. The Second Conditional is used for hypothetical or imaginary situations in the present/future: **If + past simple, ... would + base verb**.

✅ **Correct Answer Breakdown:**
**would** is correct because "If I had a lot of money..." is an unreal/imaginary condition (Second Conditional), requiring **would travel**.

❌ **Why Other Options Are Incorrect:**
* **should:** Used to give advice or state obligation, not to express hypothetical conditional results.
* **can:** Used for real present ability, whereas a past conditional clause (*had*) requires the past modal form (*would*).
* **will:** Used in First Conditional sentences (*If I have money, I will travel...*) for real future possibilities.

💡 **Key Takeaway for Revision:** Second Conditional structure: *If + past simple (had), ... WOULD + main verb (travel)*.""",

    5: """📘 **Study Note & Concept Overview:**
Prepositions of travel and movement have specific rules in English. We say **by car**, **by bus**, **by train**, **by plane**, but when referring to walking, the set idiomatic phrase is strictly **on foot**.

✅ **Correct Answer Breakdown:**
**on** is correct because the standard English preposition used with "foot" to mean walking is **on foot**.

❌ **Why Other Options Are Incorrect:**
* **by:** Used for vehicles and modes of transport (e.g., *by bus*, *by car*), not for walking on your feet.
* **with:** Means using a tool or accompanying someone (e.g., *with a pen*), not for walking.
* **in:** Indicates being inside a vehicle (e.g., *in a taxi*), not walking on foot.

💡 **Key Takeaway for Revision:** Always use "on foot" when referring to walking to a destination.""",

    6: """📘 **Study Note & Concept Overview:**
Reading comprehension requires extracting direct facts stated in a text. Paragraph 1 of the passage explicitly defines a pet as an animal kept for pleasure and companionship.

✅ **Correct Answer Breakdown:**
**To make us happy.** is correct because the text states that pets are kept for pleasure, companionship, and to bring happiness to our lives.

❌ **Why Other Options Are Incorrect:**
* **To help us carry heavy things.:** The passage states that donkeys are kept to carry heavy luggage (work animals), not pets.
* **To provide food.:** The passage notes that some livestock are kept as a source of food (milk and eggs), not pets.
* **To protect the environment.:** Environmental protection is not mentioned as a reason for keeping pets in the passage.

💡 **Key Takeaway for Revision:** Pets are kept for pleasure and companionship ("to make us happy"), while work animals carry loads.""",

    7: """📘 **Study Note & Concept Overview:**
Comprehension questions ask learners to identify true statements based on the provided passage. Paragraph 2 mentions that animals have special abilities that human beings do not have (e.g., donkeys carrying heavy loads, dogs' acute senses).

✅ **Correct Answer Breakdown:**
**They can do things that we cannot do.** is correct because the passage explicitly states that animals possess special abilities that human beings lack.

❌ **Why Other Options Are Incorrect:**
* **They are man's best friend.:** The passage specifically mentions that the dog is man's best friend, not donkeys.
* **They are better than us.:** The text does not make a moral or general claim that animals are superior to humans.
* **They are always comfortable and healthy.:** The passage emphasizes that humans must care for animals to keep them comfortable, not that they are always healthy on their own.

💡 **Key Takeaway for Revision:** Animals assist humans because they possess unique physical abilities that humans do not have.""",

    8: """📘 **Study Note & Concept Overview:**
Vocabulary in context requires finding a synonym that fits the exact meaning of a word as used in a sentence. In the passage, "special abilities" means abilities that are exceptional, distinct, or out of the ordinary.

✅ **Correct Answer Breakdown:**
**unusual.** is correct because "special" refers to uncommon, extraordinary, or exceptional traits that set them apart.

❌ **Why Other Options Are Incorrect:**
* **strange.:** Means odd or weird in a negative way, which does not match the positive context of special abilities.
* **new.:** Means recently made or acquired, not exceptional.
* **unknown.:** Means unfamiliar or obscure, which does not fit known animal abilities.

💡 **Key Takeaway for Revision:** Contextual vocabulary: "special" in this context means exceptional or unusual abilities.""",

    9: """📘 **Study Note & Concept Overview:**
Making inferences based on text evidence requires looking at cause-and-effect relationships in the passage. The final paragraph emphasizes that treating animals kindly ensures they remain helpful and productive for us.

✅ **Correct Answer Breakdown:**
**We may not get enough benefits from them.** is correct because mistreating work animals, pets, or food source animals reduces their ability to serve, work, or produce for us.

❌ **Why Other Options Are Incorrect:**
* **They will not live with us.:** Animals may remain captive even if mistreated, so this is not the main logical outcome.
* **They may not give us enough food.:** Applies only to food animals, whereas the passage covers pets, work animals, and food animals together.
* **We may not be happy and comfortable.:** Relates mainly to pets, not the broader practical benefits of all domestic animals.

💡 **Key Takeaway for Revision:** Treating animals kindly ensures we receive maximum benefits, help, and companionship from them.""",

    10: """📘 **Study Note & Concept Overview:**
In reading comprehension, identifying character motives requires analyzing the details given in the story. Paragraph 1 explains that Hassan's father wrote the item prices on a list so Hassan could calculate the correct expected balance.

✅ **Correct Answer Breakdown:**
**He wanted Hassan to get the right balance from the shopkeeper.** is correct because the story notes the father wrote down prices so Hassan knew he was expecting exactly 75 shillings balance.

❌ **Why Other Options Are Incorrect:**
* **He did not want Hassan to forget any item.:** The list contained prices specifically to calculate the total cost and balance.
* **He did not want Hassan to delay in the shop.:** Saving time was not stated as the motive for listing prices.
* **He wanted Hassan to do the totals of the cost of the items.:** Hassan's main check at the shop was calculating his expected change/balance.

💡 **Key Takeaway for Revision:** Writing down item prices helps buyers verify the total cost and calculate the exact change expected.""",

    11: """📘 **Study Note & Concept Overview:**
Analyzing story details helps explain character reactions. The story states Hassan counted his money under a tree right outside the shop and immediately walked back when he realized the error.

✅ **Correct Answer Breakdown:**
**Hassan had just left the shop.** is correct because Hassan returned almost immediately after stepping out, catching the shopkeeper by surprise.

❌ **Why Other Options Are Incorrect:**
* **Hassan returned the money.:** Returning money explained why she was grateful, but seeing him back so *soon* (just after leaving) is what surprised her.
* **the shopkeeper was very busy that day.:** Being busy explains why she made a mistake, not why she was surprised by Hassan's quick return.
* **the shopkeeper had given him the balance.:** Giving change was a routine transaction, not the cause of her surprise.

💡 **Key Takeaway for Revision:** The shopkeeper was surprised because Hassan returned almost immediately after leaving.""",

    12: """📘 **Study Note & Concept Overview:**
A fable or narrative lesson summarizes the moral story message. Hassan chose to return the extra 500 shillings because of his father's advice: "Never take what does not belong to you."

✅ **Correct Answer Breakdown:**
**honesty is the best policy.** is correct because Hassan's honest decision earned him praise, self-respect, and a clean conscience.

❌ **Why Other Options Are Incorrect:**
* **hurry hurry has no blessing.:** This proverb warns against rash speed, which is unrelated to returning stolen/extra money.
* **once bitten twice shy.:** Refers to learning from past bad experiences, not returning extra change.
* **a friend in need is a friend indeed.:** Refers to true friendship during difficult times, which does not fit the shopkeeper encounter.

💡 **Key Takeaway for Revision:** Returning money that does not belong to you illustrates the classic moral: "Honesty is the best policy.""",

    13: """📘 **Study Note & Concept Overview:**
Story comprehension requires verifying factual accuracy against events in the narrative. In the story, both Hyena and Hare were eating the farmer's groundnuts without permission.

✅ **Correct Answer Breakdown:**
**Hare stole the groundnuts just like Hyena.** is correct because both animals were illegally eating the farmer's crops in the field.

❌ **Why Other Options Are Incorrect:**
* **Hare was a true friend of the farmer.:** Hare was deceiving both the farmer and Hyena to avoid punishment.
* **Hare was not able to cheat Hyena.:** Hare successfully tricked Hyena into burying his legs in the soil.
* **Hare buried one of his legs in the ground.:** Hare lied that his legs were too short and did not bury any of his legs.

💡 **Key Takeaway for Revision:** Both Hare and Hyena were crop thieves, but Hare tricked Hyena to save himself.""",

    14: """📘 **Study Note & Concept Overview:**
Character traits are identified through a character's actions and dialogue. Hare tricked Hyena into burying his legs so Hare could escape while Hyena took the blame and got beaten.

✅ **Correct Answer Breakdown:**
**tricky** is correct because Hare used clever deceit and trickery to trap Hyena and escape unharmed.

❌ **Why Other Options Are Incorrect:**
* **friendly:** Hare acted deceitfully towards Hyena, showing he was not a true friend.
* **funny:** While the trick was humorous, Hare's defining character trait in animal tales is being sly and tricky.
* **busy:** Hare was spending time stealing crops and plotting tricks, not engaged in productive work.

💡 **Key Takeaway for Revision:** In traditional folktales, Hare is portrayed as a cunning and tricky character.""",

    15: """📘 **Study Note & Concept Overview:**
Moral themes highlight the broader life lessons learned from characters' mistakes. Hyena trusted Hare blindly despite Hare's suspicious actions, leading to Hyena getting caught and beaten.

✅ **Correct Answer Breakdown:**
**We should keep the right friends.** is correct because trusting a dishonest, tricky companion like Hare leads to betrayal and trouble.

❌ **Why Other Options Are Incorrect:**
* **People need to share what they have.:** The story is about stealing and betrayal, not generous sharing.
* **Farmers should beat all Hyenas.:** Physical punishment of animals is not the intended moral lesson of the folktale.
* **We should always do what we are told.:** Blindly obeying bad advice (like Hyena burying his legs) leads to disaster.

💡 **Key Takeaway for Revision:** Be cautious about who you trust; keeping untrustworthy friends leads to trouble.""",

    16: """📘 **Study Note & Concept Overview:**
Possessive adjectives show ownership. Since "Asha" is a female person (she/her), the corresponding possessive adjective for a singular female owner is **her**.

✅ **Correct Answer Breakdown:**
**her** is correct because Asha is female, making "her grandfather" the grammatically correct possessive form.

❌ **Why Other Options Are Incorrect:**
* **his:** Possessive adjective used for a male person (he/his).
* **hers:** Possessive pronoun used without a noun (e.g., *the garden is hers*), whereas here it precedes the noun *grandfather*.
* **him:** Objective pronoun (e.g., *I saw him*), not a possessive modifier.

💡 **Key Takeaway for Revision:** Use "her" as a possessive adjective before a noun for a female person (e.g., *her garden*, *her grandfather*).""",

    17: """📘 **Study Note & Concept Overview:**
Adjectives describe nouns. In the context of a vegetable garden, growing various types of crops is described using the adjective **different**.

✅ **Correct Answer Breakdown:**
**different** is correct because it fits the context of growing various kinds of vegetables (such as spinach, kales, carrots).

❌ **Why Other Options Are Incorrect:**
* **dry:** Vegetables being grown in a garden are living and watered, not dry.
* **cooked:** Vegetables grow raw in a garden, not already cooked.
* **plenty:** "Plenty" is a noun/determiner used with "of" (*plenty of vegetables*), not a direct pre-modifier here.

💡 **Key Takeaway for Revision:** "Different vegetables" means various types of healthy crops growing in a garden.""",

    18: """📘 **Study Note & Concept Overview:**
Verb selection relies on contextual meaning. The passage states Asha likes her garden and prefers working in it over sitting inside playing phone games.

✅ **Correct Answer Breakdown:**
**enjoys** is correct because it expresses her positive feeling and pleasure in taking care of her vegetables.

❌ **Why Other Options Are Incorrect:**
* **begins:** Refers to starting an action, which does not express her love or passion for gardening.
* **accepts:** Means agreeing to something, which does not capture her joyful active participation.
* **admires:** Means looking at something with appreciation, whereas taking care requires active work (*enjoys taking care*).

💡 **Key Takeaway for Revision:** "Enjoys taking care" shows active pleasure and dedication in maintaining a garden.""",

    19: """📘 **Study Note & Concept Overview:**
Conjunctions connect words or clauses. The coordinating conjunction **and** is used to join two parallel negative activities that Asha dislikes doing together (*sit in the house AND play games on the phone*).

✅ **Correct Answer Breakdown:**
**and** is correct because it smoothly joins the two linked indoor activities she avoids.

❌ **Why Other Options Are Incorrect:**
* **also:** An adverb used for adding info, requiring a different sentence structure.
* **yet:** A contrasting conjunction meaning "but", which does not fit two parallel negative choices.
* **because:** A causal conjunction used to give a reason, not to join two parallel actions.

💡 **Key Takeaway for Revision:** Use "and" to join two related actions or items in a sentence.""",

    20: """📘 **Study Note & Concept Overview:**
Time expressions modify future expectations. The phrase "hopes to sell her harvest..." refers to a coming time period, expressed by the adjective **next**.

✅ **Correct Answer Breakdown:**
**next** is correct because "next month" is the standard time expression for the upcoming month.

❌ **Why Other Options Are Incorrect:**
* **future:** Used as a noun (*in the future*) or modifier (*future plans*), not directly as *future month*.
* **new:** Refers to something recently created, not a calendar time expression.
* **later:** An adverb (*sell it later*), requiring "later this month" rather than *later month*.

💡 **Key Takeaway for Revision:** Use "next month" to refer to the month immediately following the present one.""",

    21: """📘 **Study Note & Concept Overview:**
Prepositions of place show location. To indicate being enclosed inside a room or building, we use the preposition **in**.

✅ **Correct Answer Breakdown:**
**in** is correct because a classroom is an enclosed space (*inside the classroom*).

❌ **Why Other Options Are Incorrect:**
* **to:** Indicates direction or movement towards a destination (*walking to the classroom*).
* **on:** Indicates resting on a flat surface (*on the table*).
* **over:** Indicates position above or higher than something (*over the roof*).

💡 **Key Takeaway for Revision:** Use "in" for enclosed locations like classrooms, rooms, and buildings.""",

    22: """📘 **Study Note & Concept Overview:**
Prepositions of surface location describe where an object is resting. When an item rests on the top flat surface of furniture, we use **on**.

✅ **Correct Answer Breakdown:**
**on** is correct because a book rests on top of the flat surface of a table.

❌ **Why Other Options Are Incorrect:**
* **with:** Indicates companionship or instrument used.
* **in:** Means inside an enclosed space (e.g., *in the drawer*).
* **from:** Indicates source or origin (*from the library*).

💡 **Key Takeaway for Revision:** Use "on" when an object rests on a surface like a table, desk, or floor.""",

    23: """📘 **Study Note & Concept Overview:**
Question tags follow specific rules:
1. Positive statement ➔ Negative tag.
2. The statement uses auxiliary verb **are** and subject pronoun **they** (*The children* = *they*).
3. Therefore, the correct tag is **aren't they?**.

✅ **Correct Answer Breakdown:**
**aren't they?** is correct because it matches the positive statement "The children are..." with a negative auxiliary and matching pronoun.

❌ **Why Other Options Are Incorrect:**
* **aren't we?:** Changes the subject pronoun from 3rd person plural (*they*) to 1st person plural (*we*).
* **are they?:** Positive tag; a positive statement requires a negative tag.
* **are we?:** Positive tag with an incorrect subject pronoun.

💡 **Key Takeaway for Revision:** Positive statement ➔ Negative tag matching subject and verb (*The children are... aren't they?*).""",

    24: """📘 **Study Note & Concept Overview:**
Indefinite pronouns refer to unspecified persons:
- **Somebody / Someone**: Used in affirmative statements when a specific unknown person took an action.
- **Anybody**: Used in questions and negative statements.

✅ **Correct Answer Breakdown:**
**somebody** is correct because the clause "...because somebody had taken it" is an affirmative statement explaining an unknown thief/person.

❌ **Why Other Options Are Incorrect:**
* **anybody:** Used in negative statements (*did not see anybody*) or questions (*did anybody take it?*).
* **everybody:** Means all people, which makes no sense as multiple people wouldn't take a single book.
* **nobody:** Means no person; saying "nobody took it" would contradict why the book was missing.

💡 **Key Takeaway for Revision:** Use "somebody" in positive statement clauses to refer to an unknown person.""",

    25: """📘 **Study Note & Concept Overview:**
Reflexive pronouns refer back to the subject of the sentence:
- Subject **us / we** ➔ Reflexive pronoun **ourselves**.

✅ **Correct Answer Breakdown:**
**ourselves** is correct because the teacher told *us* (1st person plural) to take care of *ourselves*.

❌ **Why Other Options Are Incorrect:**
* **themselves:** Reflexive pronoun for *they* (3rd person plural).
* **yourself:** Singular reflexive pronoun for *you* (2nd person singular).
* **yourselves:** Plural reflexive pronoun for *you all* (2nd person plural).

💡 **Key Takeaway for Revision:** Subject pronoun 'we / us' pairs with reflexive pronoun 'ourselves'.""",

    26: """📘 **Study Note & Concept Overview:**
Prepositional phrases indicating manner or method use set expressions. The standard phrase meaning using physical compulsion or violence is **by force**.

✅ **Correct Answer Breakdown:**
**by** is correct because **by force** is the correct idiomatic phrase in English.

❌ **Why Other Options Are Incorrect:**
* **with:** Used for instruments (*with a knife*), not in the phrase *by force*.
* **at:** Used for location or time, not manner of taking.
* **under:** Used in phrases like *under pressure* or *under arrest*, not *by force*.

💡 **Key Takeaway for Revision:** The correct idiomatic prepositional phrase is "by force".""",

    27: """📘 **Study Note & Concept Overview:**
Relative pronouns link clauses:
- **whose**: Shows possession for people, animals, or objects (*the hen whose egg broke*).
- **who / whom**: Used for human subjects/objects.

✅ **Correct Answer Breakdown:**
**whose** is correct because it shows possession (*the egg belonging to the hen*).

❌ **Why Other Options Are Incorrect:**
* **who:** Subject pronoun used for human beings (*the teacher who taught us*).
* **whom:** Object pronoun used for human beings (*the person whom I met*).
* **which:** Used for non-possessive references to animals/things (*the hen which laid an egg*).

💡 **Key Takeaway for Revision:** Use "whose" to show possession for people, animals, or objects.""",

    28: """📘 **Study Note & Concept Overview:**
Modal auxiliary verbs (**will, shall, can, may, must, should, would**) are always followed by the **bare infinitive** (base form of the main verb without 'to').

✅ **Correct Answer Breakdown:**
**give** is correct because the modal verb **will** takes the base verb form **give** (*will give*).

❌ **Why Other Options Are Incorrect:**
* **given:** Past participle form (*has given*), cannot follow modal *will* directly.
* **gives:** Third-person singular present form, cannot follow a modal verb.
* **gave:** Simple past tense form, cannot follow a modal verb.

💡 **Key Takeaway for Revision:** Modal verbs (will, shall, can, may) MUST be followed by the base verb form (give).""",

    29: """📘 **Study Note & Concept Overview:**
Correlative conjunctions **Neither ... nor** mean "not the one and not the other" (negating both items mentioned).

✅ **Correct Answer Breakdown:**
**Both Kalusi and Sofia did not come late to class.** is correct because *neither... nor* means that neither student was late (both arrived on time).

❌ **Why Other Options Are Incorrect:**
* **Only Kalusi came late to class.:** Incorrectly claims one student came late.
* **Only Sofia came late to class.:** Incorrectly claims the other student came late.
* **Both Kalusi and Sofia came late to class.:** Reverses the meaning into a positive statement of lateness for both.

💡 **Key Takeaway for Revision:** "Neither A nor B" means BOTH A and B did NOT perform or experience the action.""",

    30: """📘 **Study Note & Concept Overview:**
Reading logic matrices requires carefully checking every condition in the short passage:
- *Nasir*: plays football AND volleyball.
- *Banda*: plays football ONLY.
- *Lona*: plays football AND netball.

✅ **Correct Answer Breakdown:**
**Banda.** is correct because Banda plays football and has no other additional sport mentioned, making him the only one who plays football ONLY.

❌ **Why Other Options Are Incorrect:**
* **Nasir.:** Plays football AND volleyball.
* **Lona.:** Plays football AND netball.
* **All of them.:** All three play football, but Nasir and Lona play additional sports, so they do not play football *only*.

💡 **Key Takeaway for Revision:** Pay close attention to restrictive words like "only" when reading comprehension puzzles."""
}

file_path = 'src/data/kpsea-english-2023.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for q_num, exp_text in explanations_map.items():
    q_str = f'"questionNumber": {q_num},'
    q_pos = content.find(q_str)
    if q_pos != -1:
        exp_pos = content.find('"explanation":', q_pos)
        if exp_pos != -1:
            quote_start = content.find('"', exp_pos + 14)
            curr = quote_start + 1
            while curr < len(content):
                if content[curr] == '"' and content[curr-1] != '\\':
                    rest = content[curr+1:curr+30].lstrip()
                    if rest.startswith('}') or rest.startswith(','):
                        quote_end = curr
                        break
                curr += 1
            
            new_json_exp = json.dumps(exp_text)
            content = content[:exp_pos] + '"explanation": ' + new_json_exp + content[quote_end+1:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated English explanations successfully!")
