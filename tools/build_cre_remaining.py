import json
import os

filepath = "src/data/kpsea-sst-cre-2022.js"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kpseaSstCre2022 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

q38_to_50 = [
  {
    "id": "q38",
    "questionNumber": 38,
    "questionText": "In a Sunday school class four children told their parents why they honour their parents:\n\nMartha - they give me food.\nTitus - they do not curse me.\nDorcas - they pay my school fees.\nDan - I can live long on earth.\n\nWho among them gave a **correct** answer according to the Biblical teaching?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Martha", "isCorrect": False},
      {"text": "Titus", "isCorrect": False},
      {"text": "Dorcas", "isCorrect": False},
      {"text": "Dan", "isCorrect": True}
    ],
    "explanation": "The correct answer is **Dan.**\n\n**Analysis of the Correct Answer:**\nAccording to Ephesians 6:2-3, \"Honor your father and mother... so that it may go well with you and that you may enjoy long life on the earth.\" Dan's reason directly quotes this biblical promise associated with the commandment to honor parents.\n\n**Why Other Options Are Incorrect:**\n- **Martha, Titus, Dorcas:** While providing food and school fees are good things parents do, honoring them simply to get these benefits is not the primary biblical reason given in the commandments."
  },
  {
    "id": "q39",
    "questionNumber": 39,
    "questionText": "\"Do not accuse anyone falsely\" (Exodus 20:16).\n\nA lesson Christians learn from this commandment given by God is that they should",
    "questionType": "multiple-choice",
    "options": [
      {"text": "practice tolerance in their lives", "isCorrect": False},
      {"text": "be patient with one another", "isCorrect": False},
      {"text": "speak the truth", "isCorrect": True},
      {"text": "help others.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **speak the truth.**\n\n**Analysis of the Correct Answer:**\nThe commandment \"Do not accuse anyone falsely\" (also known as \"You shall not bear false witness\") forbids lying, perjury, and spreading false rumors about others. The positive lesson to be learned from this is to always be honest and speak the truth.\n\n**Why Other Options Are Incorrect:**\n- **practice tolerance, be patient, help others:** While these are good Christian virtues, they are not the direct lesson derived from the commandment against false accusations."
  },
  {
    "id": "q40",
    "questionNumber": 40,
    "questionText": "From the Biblical story of creation in Genesis chapter two, God created the woman in order for her to",
    "questionType": "multiple-choice",
    "options": [
      {"text": "till the Garden of Eden", "isCorrect": False},
      {"text": "be a suitable helper for the man", "isCorrect": True},
      {"text": "name the animals in the Garden", "isCorrect": False},
      {"text": "make food for the man.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **be a suitable helper for the man.**\n\n**Analysis of the Correct Answer:**\nIn Genesis 2:18, God says, \"It is not good for the man to be alone. I will make a helper suitable for him.\" This was the primary stated reason for the creation of woman in this account.\n\n**Why Other Options Are Incorrect:**\n- **till the Garden of Eden:** Man was placed in the garden to work it and take care of it.\n- **name the animals:** God brought the animals to Adam (the man) to see what he would name them.\n- **make food for the man:** This is a traditional gender role, not the Biblical reason for creation."
  },
  {
    "id": "q41",
    "questionNumber": 41,
    "questionText": "A lesson Christians learn from the contest at Mount Carmel in which prophet Elijah challenged the Baal prophets is that they should",
    "questionType": "multiple-choice",
    "options": [
      {"text": "slaughter animals during worship", "isCorrect": False},
      {"text": "worship God on mountains", "isCorrect": False},
      {"text": "pray loudly to God", "isCorrect": False},
      {"text": "worship the true God.", "isCorrect": True}
    ],
    "explanation": "The correct answer is **worship the true God.**\n\n**Analysis of the Correct Answer:**\nThe contest at Mount Carmel (1 Kings 18) was a showdown to prove who the real God was in Israel. When God sent fire to consume Elijah's sacrifice, the people realized the Lord is God and Baal was false. The core lesson is rejecting idolatry and worshipping the one true God.\n\n**Why Other Options Are Incorrect:**\n- **slaughter animals:** Animal sacrifice was an Old Testament practice, not the main spiritual lesson for Christians today.\n- **worship God on mountains:** God can be worshipped anywhere.\n- **pray loudly:** The Baal prophets prayed loudly and frantically to no avail, while Elijah prayed a simple, trusting prayer."
  },
  {
    "id": "q42",
    "questionNumber": 42,
    "questionText": "The **main** lesson learners can share with their parents after learning about the temptations of Jesus Christ in the wilderness is to",
    "questionType": "multiple-choice",
    "options": [
      {"text": "depend on bread for their survival", "isCorrect": False},
      {"text": "avoid praying to God in lonely places", "isCorrect": False},
      {"text": "use the word of God in their lives", "isCorrect": True},
      {"text": "give their possessions to others.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **use the word of God in their lives.**\n\n**Analysis of the Correct Answer:**\nDuring the temptations in the wilderness, Jesus countered every single trick and temptation from Satan by quoting Scripture (saying \"It is written...\"). The lesson for Christians is to know and use the word of God to overcome daily challenges and temptations.\n\n**Why Other Options Are Incorrect:**\n- **depend on bread:** Jesus actually said, \"Man shall not live on bread alone, but on every word that comes from the mouth of God.\"\n- **avoid praying in lonely places:** Jesus frequently went to lonely places to pray.\n- **give their possessions:** This is a lesson from other teachings (like the rich young ruler), not the wilderness temptations."
  },
  {
    "id": "q43",
    "questionNumber": 43,
    "questionText": "The main reason why Jesus healed the servant of the Roman officer was because",
    "questionType": "multiple-choice",
    "options": [
      {"text": "The Roman Officer was senior in the government", "isCorrect": False},
      {"text": "The Roman Officer had faith in Jesus", "isCorrect": True},
      {"text": "The Roman Officer gave Jesus money", "isCorrect": False},
      {"text": "The Roman officer was a friend of Jesus.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **The Roman Officer had faith in Jesus.**\n\n**Analysis of the Correct Answer:**\nIn the story of the Roman Centurion (Luke 7), the officer tells Jesus he doesn't even need to come to his house, just say the word and his servant will be healed. Jesus was amazed and said, \"I have not found such great faith even in Israel.\" The healing was a direct result of the officer's immense faith.\n\n**Why Other Options Are Incorrect:**\n- **was senior in the government / gave money / was a friend:** Jesus did not heal based on social status, bribery, or personal favoritism."
  },
  {
    "id": "q44",
    "questionNumber": 44,
    "questionText": "Choose an instruction that John the Baptist gave to the people as a way of preparing for the coming of the messiah",
    "questionType": "multiple-choice",
    "options": [
      {"text": "keep the sabbath day holy.", "isCorrect": False},
      {"text": "maintain harmonious relations.", "isCorrect": False},
      {"text": "listen to his teachings carefully.", "isCorrect": False},
      {"text": "share your food with others.", "isCorrect": True}
    ],
    "explanation": "The correct answer is **share your food with others.**\n\n**Analysis of the Correct Answer:**\nWhen the crowds asked John the Baptist what they should do to prepare and show their repentance, he replied in Luke 3:11, \"Anyone who has two shirts should share with the one who has none, and anyone who has food should do the same.\"\n\n**Why Other Options Are Incorrect:**\n- **keep the sabbath day holy:** This is one of the Ten Commandments given by Moses, not John's specific instruction to the crowds.\n- **maintain harmonious relations / listen carefully:** While generally good, sharing possessions and food was his explicit, practical instruction for repentance."
  },
  {
    "id": "q45",
    "questionNumber": 45,
    "questionText": "Select the option which contains **only** the gifts of the holy spirit",
    "questionType": "multiple-choice",
    "options": [
      {"text": "A (Healing, Success)", "isCorrect": False},
      {"text": "B (Richness, Goodness)", "isCorrect": False},
      {"text": "C (Wisdom, Knowledge)", "isCorrect": True},
      {"text": "D (Arrogance, Ignorance)", "isCorrect": False}
    ],
    "explanation": "The correct answer is **C (Wisdom, Knowledge).**\n\n**Analysis of the Correct Answer:**\nAccording to 1 Corinthians 12, the spiritual gifts given by the Holy Spirit include the message of wisdom, the message of knowledge, faith, gifts of healing, miraculous powers, prophecy, distinguishing between spirits, speaking in tongues, and interpretation of tongues. Option C contains two of these explicitly.\n\n**Why Other Options Are Incorrect:**\n- **A:** Healing is a gift, but \"Success\" is not a Biblical gift of the Spirit.\n- **B:** Goodness is a *fruit* of the Spirit (Galatians 5:22), not a gift. Richness is neither.\n- **D:** Arrogance and Ignorance are negative traits, not gifts from God."
  },
  {
    "id": "q46",
    "questionNumber": 46,
    "questionText": "A Grade Six class is composed of learners from different ethnic groups. In which way can they promote unity among themselves?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Speaking a national language in school.", "isCorrect": True},
      {"text": "Choosing desk mates who belong to their community.", "isCorrect": False},
      {"text": "Playing with friends from their own community.", "isCorrect": False},
      {"text": "Making fun of members of other communities.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Speaking a national language in school.**\n\n**Analysis of the Correct Answer:**\nSpeaking a national language (like Kiswahili or English in Kenya) ensures that everyone can understand each other, bridging ethnic divides and promoting inclusivity and national unity within the diverse classroom.\n\n**Why Other Options Are Incorrect:**\n- **Choosing desk mates / Playing with friends from their own community:** This promotes segregation and tribalism, destroying unity.\n- **Making fun of members of other communities:** This is bullying and creates hostility and division."
  },
  {
    "id": "q47",
    "questionNumber": 47,
    "questionText": "During lunch break, you notice a Grade Two boy sitting alone and crying. You ask him what is the problem, and he tells you that he is hungry. Which one of the following is the **best** way to express your love for the boy?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Give him some food to eat.", "isCorrect": True},
      {"text": "Tell him \"sorry\" and walk away.", "isCorrect": False},
      {"text": "Take him to his class teacher.", "isCorrect": False},
      {"text": "Ask him to go and look for food.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Give him some food to eat.**\n\n**Analysis of the Correct Answer:**\nTrue Christian love and compassion are shown through practical action. If someone is hungry and you have the means to help, the most direct and loving response is to share your food with them to solve their immediate problem.\n\n**Why Other Options Are Incorrect:**\n- **Tell him \"sorry\" / Ask him to look for food:** These show a lack of care and do nothing to solve his hunger.\n- **Take him to his class teacher:** While this is a responsible secondary action, giving him food immediately is the *best* direct expression of love and empathy."
  },
  {
    "id": "q48",
    "questionNumber": 48,
    "questionText": "While walking home in the evening Jebet, a Grade Five learner, meets with a young man she does not know who offers to assist her to carry her bag. The **correct** advice to give Grace is to tell her to",
    "questionType": "multiple-choice",
    "options": [
      {"text": "give her bag to the young man to assist her", "isCorrect": False},
      {"text": "tell the young man no thank you and continue walking", "isCorrect": True},
      {"text": "give her bag to the young man and tell him thank you", "isCorrect": False},
      {"text": "get out of the road and hide in a nearby home till the man leaves the road.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **tell the young man no thank you and continue walking.**\n\n**Analysis of the Correct Answer:**\nChildren are taught never to trust or accept help/gifts from strangers, as this could be a tactic used by kidnappers or abusers. The safest and most polite response is to firmly decline (\"no thank you\") and continue walking to a safe destination without engaging further.\n\n**Why Other Options Are Incorrect:**\n- **give her bag:** This is extremely dangerous as the stranger could steal it or use it to lure her away.\n- **hide in a nearby home:** While she should seek safety if actively threatened, hiding unnecessarily might put her in an isolated situation. Assertively declining and moving on is the standard safety advice for unsolicited offers from strangers."
  },
  {
    "id": "q49",
    "questionNumber": 49,
    "questionText": "Onyango, a Grade Four learner has a habit of collecting textbooks that are left on top of the desks in the evening and putting them in a shelf in the classroom. Select the value that Onyango demonstrates.",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Courage.", "isCorrect": False},
      {"text": "Honesty.", "isCorrect": False},
      {"text": "Responsibility.", "isCorrect": True},
      {"text": "Holiness.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Responsibility.**\n\n**Analysis of the Correct Answer:**\nResponsibility involves taking ownership of tasks, being dependable, and caring for shared property. By voluntarily collecting left-out books and safely storing them to prevent loss or damage, Onyango is showing a high level of responsibility for school property.\n\n**Why Other Options Are Incorrect:**\n- **Courage:** Involves facing fear or danger.\n- **Honesty:** Involves telling the truth and not stealing (he is storing them, not necessarily returning stolen goods).\n- **Holiness:** Refers to religious piety and spiritual purity."
  },
  {
    "id": "q50",
    "questionNumber": 50,
    "questionText": "Which one of the following ways is an inappropriate use of the social media by a Christian?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Posting indecent pictures.", "isCorrect": True},
      {"text": "Searching information for personal development.", "isCorrect": False},
      {"text": "Sending greetings to friends.", "isCorrect": False},
      {"text": "Posting Christian messages.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Posting indecent pictures.**\n\n**Analysis of the Correct Answer:**\nChristians are taught to uphold moral purity, modesty, and decency in all aspects of life, including the digital world. Posting indecent (immodest or sexually explicit) pictures goes against these Biblical teachings and is an inappropriate use of social media.\n\n**Why Other Options Are Incorrect:**\n- **Searching information, Sending greetings, Posting Christian messages:** These are all positive, constructive, and appropriate ways to use social media."
  }
]

data["sectionA"].extend(q38_to_50)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(f"export const kpseaSstCre2022 = {json.dumps(data, indent=2)};\n")

print("Updated kpsea-sst-cre-2022.js with Q38-Q50 successfully.")
