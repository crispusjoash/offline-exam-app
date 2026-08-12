import json
import re

explanations_map = {
    1: """In formal telephone etiquette, when asking for the identity of the person on the other end of the line, the polite and grammatically correct expression is **Whom am I speaking to?** (or "To whom am I speaking?"). 'Whom' is the objective pronoun referring to the receiver of the action.

* **Why other options are incorrect:**
  * **Who are you?:** Unnecessarily blunt and impolite for formal telephone conversations.
  * **Who is this?:** Informal and lacks the professional politeness required when speaking on the phone.
  * **Whom do you want to speak to?:** Inverts the roles; the speaker is making the inquiry about the caller's identity in a polite way.

💡 **Key Takeaway:** Use polite, formal phrasing like "Whom am I speaking to?" or "May I know who is calling?" in telephone etiquette.""",

    2: """The modal auxiliary verb **May** is used to request permission politely. The sentence **May I be late for school today?** is a polite request asking for permission to arrive late.

* **Why other options are incorrect:**
  * **I want to be late for school today.:** A direct statement of personal desire, not a polite request for permission.
  * **I will be late for school today.:** A definitive statement predicting future occurrence, rather than seeking approval.
  * **Must I be late for school today?:** Expresses obligation or compulsion rather than seeking permission.

💡 **Key Takeaway:** Use 'May I...' when seeking permission politely in spoken or written English.""",

    3: """When someone in authority (like a teacher) grants a request or provides assistance, the appropriate polite response is **Thank you, Teacher.** expressing gratitude.

* **Why other options are incorrect:**
  * **That's good, Teacher.:** Used to compliment or evaluate something, not to express gratitude for granted permission.
  * **It's okay, Teacher.:** Used to reassure someone after an apology or minor error, not to thank a teacher.
  * **It's alright, Teacher.:** Similar to 'it's okay', used to forgive or dismiss a concern rather than express thanks.

💡 **Key Takeaway:** Always respond with "Thank you" when permission or help is extended to you.""",

    4: """This sentence is a Second Conditional structure (unreal/hypothetical situation in the present/future: *If + past simple, ... would + infinitive*). Therefore, **would** is the correct modal verb to express the hypothetical action (*would travel*).

* **Why other options are incorrect:**
  * **should:** Used to offer advice or duty, not for hypothetical conditional main clauses.
  * **can:** Present tense modal verb; fails to match the past tense condition 'If I had'.
  * **will:** First conditional modal verb used with present tense 'If I have', not past tense 'If I had'.

💡 **Key Takeaway:** Use 'would' in the main clause of a second conditional sentence (*If I had..., I would...*).""",

    5: """The correct fixed prepositional phrase for traveling on foot is **on foot**. We say "on foot" (not "by foot") when referring to walking.

* **Why other options are incorrect:**
  * **by:** Used for vehicles and modes of transport (e.g., *by bus, by car, by train, by plane*), but never for feet.
  * **with:** Indicates an instrument or accompaniment (e.g., *with a pen*), not the mode of walking.
  * **in:** Indicates enclosed transport or location (e.g., *in a car*), not walking on feet.

💡 **Key Takeaway:** Use 'on foot' for walking, but 'by' for vehicular modes of transport (by bus, by train).""",

    6: """According to the passage on animal companionship, we keep domestic pets primarily **To make us happy** through companionship, play, and emotional bonding.

* **Why other options are incorrect:**
  * **To help us carry heavy things.:** Describes the work of draught animals (like donkeys, oxen, or horses), not household pets.
  * **To provide food.:** Describes livestock (like cows, goats, chickens), not domestic companion pets.
  * **To protect the environment.:** While trees and plants protect ecosystems, keeping household pets is aimed at human companionship and joy.

💡 **Key Takeaway:** Domestic pets provide emotional benefits, companionship, and joy to humans.""",

    7: """The passage highlights that animals possess unique abilities, senses, and physical traits, meaning **They can do things that we cannot do** (such as carrying heavy loads effortlessly or smelling distant scents).

* **Why other options are incorrect:**
  * **They are man's best friend.:** The passage specifies dogs as man's best friend, not donkeys.
  * **They are better than us.:** A subjective exaggeration not stated in the passage; humans and animals have distinct roles.
  * **They are always comfortable and healthy.:** Animals can get sick or suffer if mistreated, so they are not always comfortable.

💡 **Key Takeaway:** Animals have unique physical capabilities and instincts that complement human life.""",

    8: """The word 'special' in this context refers to something distinct, extraordinary, or **unusual** that stands out from the ordinary.

* **Why other options are incorrect:**
  * **strange:** Implies weird, odd, or suspicious rather than remarkable or special.
  * **new:** Means recently created or discovered, which is not synonymous with 'special'.
  * **unknown:** Means unfamiliar or undiscovered, whereas special means distinctive and valued.

💡 **Key Takeaway:** Contextual vocabulary requires identifying synonyms that preserve the exact meaning in the passage.""",

    9: """If we fail to care for and treat animals kindly, **We may not get enough benefits from them** because mistreated animals become weak, unproductive, or hostile.

* **Why other options are incorrect:**
  * **They will not live with us.:** Domesticated animals may remain in human custody even if neglected, though they suffer.
  * **They may not give us enough food.:** While true for livestock, this does not apply to all animals (like dogs or donkeys) mentioned in the context.
  * **We may not be happy and comfortable.:** Human happiness is a secondary effect; the direct consequence is losing the full utility and loyal benefits of healthy animals.

💡 **Key Takeaway:** Treating animals with care and kindness ensures they remain healthy, productive, and beneficial.""",

    10: """Hassan's father wrote a detailed list of items along with their prices so that **He wanted Hassan to get the right balance from the shopkeeper** by knowing the exact total cost in advance.

* **Why other options are incorrect:**
  * **He did not want Hassan to forget any item.:** While a shopping list helps memory, the father specifically wrote down prices and cash calculations to ensure correct change.
  * **He did not want Hassan to delay in the shop.:** Saving time was not the primary motive for calculating item prices on the note.
  * **He wanted Hassan to do the totals of the cost of the items.:** The father had already calculated the total cost himself on the list.

💡 **Key Takeaway:** Keeping accurate records of prices and expected balances prevents financial loss during purchases.""",

    11: """The shopkeeper was surprised when Hassan returned because **Hassan had just left the shop** a few moments earlier, making his immediate return unexpected.

* **Why other options are incorrect:**
  * **Hassan returned the money.:** Hassan returned excess money given to him by mistake, but the surprise was caused by his instant reappearance right after stepping out.
  * **the shopkeeper was very busy that day.:** Customer volume was not the reason for the shopkeeper's surprise upon Hassan's sudden return.
  * **the shopkeeper had given him the balance.:** The shopkeeper assumed the transaction was complete and did not expect the boy back so quickly.

💡 **Key Takeaway:** Read narrative details carefully to pinpoint the exact cause of a character's reaction.""",

    12: """Hassan's decision to return extra money given to him by mistake demonstrates that **honesty is the best policy**, showing integrity and moral character.

* **Why other options are incorrect:**
  * **hurry hurry has no blessing.:** Warns against rushing hastily, which is unrelated to returning excess money.
  * **once bitten twice shy.:** Refers to being cautious after experiencing hurt or betrayal, which does not fit Hassan's act of honesty.
  * **a friend in need is a friend indeed.:** Refers to true friendship during difficult times, not financial honesty with a shopkeeper.

💡 **Key Takeaway:** Moral stories highlight core values; returning extra change reflects the proverb 'Honesty is the best policy'.""",

    13: """According to the story, **Hare stole the groundnuts just like Hyena**, showing that both characters engaged in trickery and theft.

* **Why other options are incorrect:**
  * **Hare was a true friend of the farmer.:** False; Hare stole crops from the farmer's field.
  * **Hare was not able to cheat Hyena.:** False; Hare successfully tricked Hyena into taking all the blame.
  * **Hare buried one of his legs in the ground.:** False; Hare pretended to have his leg stuck or buried, but this was a trick.

💡 **Key Takeaway:** Comprehension questions test factual details directly stated or implied in the narrative.""",

    14: """Throughout trickster tales in African folklore, Hare is depicted as **tricky** because he uses clever cunning to outsmart other animals.

* **Why other options are incorrect:**
  * **friendly:** Hare's actions were deceptive rather than motivated by genuine goodwill or friendship.
  * **funny:** While his antics may be entertaining, his primary character trait is cunning trickery.
  * **busy:** Hare was focused on scheme execution rather than hardworking labor.

💡 **Key Takeaway:** Traditional folklore character archetypes portray the Hare as the ultimate clever trickster.""",

    15: """The story warns us against blind trust in deceptive companions, teaching us that **We should keep the right friends**.

* **Why other options are incorrect:**
  * **People need to share what they have.:** Sharing stolen food is not the moral lesson of the fable.
  * **Farmers should beat all Hyenas.:** Excessive violence against animals is not the educational lesson of the story.
  * **We should always do what we are told.:** Uncritical obedience to bad advice (like Hyena obeying Hare) leads to trouble.

💡 **Key Takeaway:** Choose wise and trustworthy companions to avoid being led into deceptive schemes.""",

    16: """The correct possessive determiner for a female subject (Asha) is **her**. "Asha... a gift from **her** grandfather."

* **Why other options are incorrect:**
  * **his:** Masculine possessive determiner; Asha is female.
  * **hers:** Possessive pronoun (e.g., *the garden is hers*), which cannot modify the noun 'grandfather' directly.
  * **him:** Objective masculine pronoun, grammatically incorrect as a possessive modifier.

💡 **Key Takeaway:** Use 'her' as the possessive adjective for female singular nouns (her book, her grandfather).""",

    17: """The sentence describes variety in Asha's vegetable garden, making **different** the correct adjective ("grows **different** vegetables").

* **Why other options are incorrect:**
  * **dry:** Vegetables in a thriving garden are fresh and green, not dry.
  * **cooked:** Crops grow raw in a garden; they are only cooked after harvesting.
  * **plenty:** 'Plenty' is a noun/determiner that requires 'of' (*plenty of*) to modify vegetables.

💡 **Key Takeaway:** Choose adjectives that make logical and grammatical sense within the context of farming and gardening.""",

    18: """The sentence describes Asha's joy in tending her garden: "She **enjoys** taking care of her vegetables."

* **Why other options are incorrect:**
  * **begins:** Means starts; fails to convey her continuous love and passion for garden care.
  * **accepts:** Means agrees to; implies reluctance or obligation rather than delight.
  * **admires:** Means respects or looks at with wonder; requires a direct object without the gerund structure 'taking care'.

💡 **Key Takeaway:** Select verbs that accurately express emotional enthusiasm and fit the gerund pattern (*enjoys doing*).""",

    19: """The conjunction **and** joins two coordinate clauses or activities in a affirmative list: "sit in the house **and** play games".

* **Why other options are incorrect:**
  * **also:** An adverb that requires a connecting conjunction when joining verbs directly.
  * **yet:** An adverse conjunction showing contrast, which does not fit linking two parallel indoor activities.
  * **because:** Explains a cause or reason rather than linking two parallel activities.

💡 **Key Takeaway:** Use 'and' to connect similar, parallel actions in a compound predicate.""",

    20: """The temporal adjective **next** correctly modifies 'month' to indicate the upcoming time period ("sell her harvest **next** month").

* **Why other options are incorrect:**
  * **future:** Requires a prepositional phrase (e.g., *in the future*), cannot directly modify 'month' here.
  * **new:** Describes something recently created or unused, not an upcoming time period (*next month*).
  * **later:** An adverb of time used after time expressions (*two weeks later*), not directly before 'month'.

💡 **Key Takeaway:** Use 'next' to refer to the time period immediately following the present (next week, next month).""",

    21: """The spatial preposition **in** indicates being inside an enclosed space like a room ("in the classroom").

* **Why other options are incorrect:**
  * **to:** Indicates direction or movement toward a destination, not location inside a room.
  * **on:** Indicates position on a surface (e.g., *on the floor*), not enclosed inside a room.
  * **over:** Indicates position above or higher than something, not inside a room.

💡 **Key Takeaway:** Use 'in' for enclosed spaces (in the room, in the car, in the box).""",

    22: """The preposition **on** indicates resting upon a flat surface: "left the book **on** the table".

* **Why other options are incorrect:**
  * **with:** Indicates possession or accompaniment, not physical resting position on a surface.
  * **in:** Indicates inside an enclosed volume, whereas a table is a flat surface.
  * **from:** Indicates origin or point of departure, not stationary placement.

💡 **Key Takeaway:** Use 'on' to denote location on top of flat surfaces (on the table, on the desk).""",

    23: """Question tag rule: Positive statement takes a negative tag. "The children are planting trees" (positive, plural pronoun *they*, verb *are*) -> tag is **aren't they?**

* **Why other options are incorrect:**
  * **aren't we?:** Changes the subject pronoun from third person plural (*they*) to first person plural (*we*).
  * **are they?:** Positive tag used for negative statements, but the main statement here is positive.
  * **are we?:** Positive tag with an incorrect subject pronoun.

💡 **Key Takeaway:** Match the question tag auxiliary verb and subject pronoun to the main sentence (Positive statement -> Negative tag).""",

    24: """In negative sentences indicating the action of an unidentified person, **somebody** is used to refer to an indefinite person: "because **somebody** had taken it."

* **Why other options are incorrect:**
  * **anybody:** Used in questions and negative statements with explicit negation (*did not find... anybody*), but here 'somebody' specifies an unknown individual who took the book.
  * **everybody:** Refers to all people, which would mean everyone collectively took one book.
  * **nobody:** Double negative when used after 'did not find', creating grammatical error.

💡 **Key Takeaway:** Indefinite pronouns (somebody, anybody, nobody) must agree with the sentence structure and affirmative/negative logic.""",

    25: """The reflex pronoun for the first-person plural 'us' (we) is **ourselves**: "take care of **ourselves**".

* **Why other options are incorrect:**
  * **themselves:** Reflexive pronoun for 'they' / 'them'.
  * **yourself:** Reflexive pronoun for singular 'you'.
  * **yourselves:** Reflexive pronoun for plural 'you'.

💡 **Key Takeaway:** Match reflexive pronouns to their antecedent: *we/us -> ourselves*, *they/them -> themselves*.""",

    26: """The correct prepositional idiom for using coercion or violence is **by force**.

* **Why other options are incorrect:**
  * **with:** Incorrect preposition for this specific idiom (*by force*).
  * **at:** Used for points in time or location, not modal force.
  * **under:** Used in phrases like *under duress* or *under pressure*, but the standard idiom is *by force*.

💡 **Key Takeaway:** Idiomatic expressions use fixed prepositions; always use 'by force' to describe coerced actions.""",

    27: """The relative pronoun **whose** expresses possession (belonging to the hen: "whose egg broke").

* **Why other options are incorrect:**
  * **who:** Subject pronoun used only for humans (*the girl who won*).
  * **whom:** Object pronoun used only for humans (*the boy whom I met*).
  * **which:** Relative pronoun for things/animals, but fails to show possession (*whose*).

💡 **Key Takeaway:** Use 'whose' as the relative possessive pronoun for people, animals, and objects.""",

    28: """After the modal auxiliary verb 'will', the main verb must be in its base infinitive form **give** ("will **give** us a present").

* **Why other options are incorrect:**
  * **given:** Past participle form; cannot follow 'will' directly without 'have' (*will have given*).
  * **gives:** Third-person singular present tense; cannot follow modal auxiliary 'will'.
  * **gave:** Simple past tense; cannot follow modal auxiliary 'will'.

💡 **Key Takeaway:** Modal auxiliaries (will, shall, can, may, must) are always followed by the bare infinitive form of the verb.""",

    29: """The correlative conjunction 'Neither... nor...' excludes both subjects, meaning **Both Kalusi and Sofia did not come late to class**.

* **Why other options are incorrect:**
  * **Only Kalusi came late to class.:** Incorrect; 'neither' applies negation to Kalusi as well.
  * **Only Sofia came late to class.:** Incorrect; 'nor' applies negation to Sofia too.
  * **Both Kalusi and Sofia came late to class.:** Reverses the meaning entirely; 'neither... nor' negates both individuals.

💡 **Key Takeaway:** 'Neither... nor...' means "not one and not the other" (both are excluded/negated).""",

    30: """According to the text passage, **Banda** is the only person who plays football exclusively.

* **Why other options are incorrect:**
  * **Nasir.:** Plays multiple sports or a different sport according to the passage.
  * **Lona.:** Participates in other athletics or activities mentioned in the text.
  * **All of them.:** Incorrect because only Banda plays football exclusively.

💡 **Key Takeaway:** Read comprehension texts carefully to identify specific details assigned to individual characters."""
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

print("Successfully updated all 30 explanations in English (kpsea-english-2023.js)!")
