import json

english_2022_data = {
  "id": "kpsea-english-2022",
  "title": "KPSEA 2022 English",
  "subject": "English",
  "year": "2022",
  "durationMinutes": 60,
  "timeAllowed": 60,
  "sharedContexts": {
    "ctx-eng-2022-q1-5": {
      "title": "Questions 1 to 5\nRead the conversation below. It contains blank spaces numbered 1 to 5. For each blank space, select the best alternative from the choices given.",
      "type": "text",
      "text": "**Hassan:** Hello Nekesa. How are you today?\n\n**Nekesa:** I am fine Hassan, what about you?\n\n**Hassan:** I am fine too, because the holidays have started.\n\n**Nekesa:** Yes, I am very happy about that.\n\n**Hassan:** ----1----\n\n**Nekesa:** I am going to visit my grandmother. ----2----\n\n**Hassan:** I will be at home helping my parents. Will you spend the whole holiday with your grandmother?\n\n**Nekesa:** Yes, I will be taking care of her. She is unwell.\n\n**Hassan:** ----3----. Nekesa, you are such a caring girl.\n\n**Nekesa:** ----4----. Let's meet when schools open.\n\n**Hassan:** Goodbye, Nekesa.\n\n**Nekesa:** ----5----"
    },
    "ctx-eng-2022-q6-9": {
      "title": "Questions 6 to 9\nRead the passage below and then answer questions 6 to 9.",
      "type": "text",
      "text": "Food is a basic need for every human being. We need it in order to remain alive. The kinds of food people eat differ from community to community. This is determined by factors such as the natural environment and culture. For example, people living near water bodies such as lakes and oceans are likely to have fish as their main diet. Those living in rice growing areas may eat a lot of rice.\n\nInterestingly, what is considered food by some people may not get anywhere near the plates of others. For instance, in some communities, rats are a **favourite** food, while to others, it is unheard of for someone to eat rats. Indeed, **one man's food is another man's poison**."
    },
    "ctx-eng-2022-q10-12": {
      "title": "Questions 10 to 12\nRead the passage below and then answer questions 10 to 12.",
      "type": "text",
      "text": "Hassan likes running errands for his parents. The other day, he was sent to the shop to buy a number of items. His father had written the prices of the items on a list. The total came to Ksh 425. His father had given him Ksh 500. Hassan was expecting Ksh 75 as balance after buying the items.\n\nThe Shopkeeper was very busy on that day. She was serving many customers. When Hassan got the balance, he stepped out of the shop to count the money. He could not believe it. The Shopkeeper had given him Ksh 575! Hassan thought this was his lucky day.\n\nHe sat down under a tree to plan how he would spend his new found cash. He started counting all the things he would buy. This time he would go to a different shop.\n\nOn his way to the shop, Hassan remembered what his father had once said, \"Never take what does not belong to you\". He slowly walked towards the shop to return the money. The shopkeeper was surprised to see him back so soon. When Hassan handed her the money, she was very grateful and said, \"You are an angel. I'm proud of you, young man\".\n\nHassan walked home shoulders high. He knew his father would be very pleased with him. This was a lucky day for both the shopkeeper and Hassan."
    },
    "ctx-eng-2022-q13-15": {
      "title": "Questions 13 to 15\nRead the passage below and then answer questions 13 to 15.",
      "type": "text",
      "text": "There once lived a king who loved stories. He wished to have someone who would tell him stories all day. So, the King announced that he would reward the person who would tell the longest story. Many people tried, but their stories did not last more than a few hours.\n\nOne day, Mokowi arrived at the palace and said he too wanted to tell a story. Mokowi was the man who usually roamed the market without a shirt. \"What story can Mokowi tell?\", the King's assistants asked. Why should we listen to Mokowi's story? Surely, a crazy man like him has no business here in the King's palace. The King, however, gave him a chance. Mokowi began his story.\n\n\"One day, a swarm of locusts wanted to eat some grains from a store. The locusts made a tiny hole in the wall of the store. Only one locust could go in at a time. The first one entered, ate and came out. The second one went in, ate and came out. Another one went in, ate and came out.\"\n\nOn the third day, Mokowi was still telling the story. \"Another one went in, ate and came out. Then, another one went in, ate and came out...\"\n\nThe King looked at the story teller and said, the story will never end. \"You win\". Mokowi was rewarded with new clothes."
    },
    "ctx-eng-2022-q16-20": {
      "title": "Questions 16 to 20\nRead the passage below. It contains blank spaces numbered 16 to 20. For each blank space, select the best alternative from the choices given.",
      "type": "text",
      "text": "My name is Jane Akinyi Kamau. I live ----16---- a small village in Kiambu County. My parents Mr and Mrs Kamau are good ----17---- caring doctors. They have built ----18---- clinic where they see their ----19----. I work very hard at school. I do not want to be a doctor. When I grow up, I ----20---- like to be a teacher."
    },
    "ctx-eng-2022-q21-25": {
      "title": "Questions 21 to 25\nFor questions 21 to 25, fill in the blank spaces with the correct alternative from the choices given.",
      "type": "text",
      "text": ""
    },
    "ctx-eng-2022-q26": {
      "title": "Question 26\nFor question 26, choose the word that means the opposite of the underlined.",
      "type": "text",
      "text": ""
    },
    "ctx-eng-2022-q27-28": {
      "title": "Questions 27 and 28\nFor questions 27 and 28, choose the alternative that means the same as the underlined.",
      "type": "text",
      "text": ""
    },
    "ctx-eng-2022-q29-30": {
      "title": "Questions 29 and 30\nIn questions 29 and 30, choose the word that means the same as the underlined word.",
      "type": "text",
      "text": ""
    }
  },
  "sectionA": [
    {
      "id": "eq1-2022",
      "questionNumber": 1,
      "questionText": "Hassan: ----1----",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q1-5",
      "options": [
        { "text": "Do you like holidays better than going to school?", "isCorrect": False },
        { "text": "How are you planning to spend the holidays?", "isCorrect": True },
        { "text": "How long will the holidays last?", "isCorrect": False },
        { "text": "What did you do during your last holidays?", "isCorrect": False }
      ],
      "explanation": """The correct answer is **How are you planning to spend the holidays?**.

**Analysis of the Correct Answer:**
In this dialogue, Nekesa replies in the next line, **"I am going to visit my grandmother."** This response directly answers a question about her future plans for the holiday. Therefore, Hassan's question in blank 1 must ask **"How are you planning to spend the holidays?"**.

**Why Other Options Are Incorrect:**
* **Do you like holidays better than going to school?:** This asks for a personal preference between school and holidays, which does not match Nekesa's answer about visiting her grandmother.
* **How long will the holidays last?:** This asks for a duration of time (e.g. two weeks), which does not lead to Nekesa explaining her activity.
* **What did you do during your last holidays?:** This asks about past events in previous holidays, whereas the dialogue is discussing the upcoming holidays that have just started.

📌 **Key Learning Note:**
In dialogue completion, read the response immediately following the blank space to identify what question was asked."""
    },
    {
      "id": "eq2-2022",
      "questionNumber": 2,
      "questionText": "Nekesa: I am going to visit my grandmother. ----2----",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q1-5",
      "options": [
        { "text": "Why do you ask that?", "isCorrect": False },
        { "text": "What about you?", "isCorrect": True },
        { "text": "How are your parents?", "isCorrect": False },
        { "text": "Where is your home?", "isCorrect": False }
      ],
      "explanation": """The correct answer is **What about you?**.

**Analysis of the Correct Answer:**
In the following line, Hassan replies, **"I will be at home helping my parents."** This shows that Nekesa asked Hassan about his own holiday plans after sharing hers. The polite conversational phrase used to return a question about plans is **"What about you?"**.

**Why Other Options Are Incorrect:**
* **Why do you ask that?:** This sounds defensive and abrupt, which does not fit a friendly conversation between classmates.
* **How are your parents?:** This asks about his parents' health or well-being, which does not prompt Hassan to explain his own holiday activities.
* **Where is your home?:** This asks for a physical location rather than asking Hassan what he will be doing during the holidays.

📌 **Key Learning Note:**
Use **"What about you?"** or **"And you?"** to politely ask your conversation partner the same question they asked you."""
    },
    {
      "id": "eq3-2022",
      "questionNumber": 3,
      "questionText": "Hassan: ----3----. Nekesa, you are such a caring girl.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q1-5",
      "options": [
        { "text": "That is normal", "isCorrect": False },
        { "text": "She must be old", "isCorrect": False },
        { "text": "Yes, she is sick", "isCorrect": False },
        { "text": "Sorry about that", "isCorrect": True }
      ],
      "explanation": """The correct answer is **Sorry about that**.

**Analysis of the Correct Answer:**
Nekesa tells Hassan that her grandmother is **"unwell"** (sick). In polite English conversation, when someone shares bad news about a sick relative, the appropriate empathetic response is to express sympathy by saying **"Sorry about that"**.

**Why Other Options Are Incorrect:**
* **That is normal:** This sounds cold and insensitive when someone mentions a sick family member.
* **She must be old:** This makes an unnecessary assumption and lacks sympathy for her grandmother's illness.
* **Yes, she is sick:** Hassan would be stating a fact he was just told rather than expressing sympathy.

📌 **Key Learning Note:**
Express empathy and sympathy by saying **"Sorry about that"** or **"I'm sorry to hear that"** whenever someone mentions illness or misfortune."""
    },
    {
      "id": "eq4-2022",
      "questionNumber": 4,
      "questionText": "Nekesa: ----4----. Let's meet when schools open.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q1-5",
      "options": [
        { "text": "Thank you, Hassan.", "isCorrect": True },
        { "text": "I know it, Hassan.", "isCorrect": False },
        { "text": "Hassan, you are right.", "isCorrect": False },
        { "text": "Hassan, excuse me.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **Thank you, Hassan.**.

**Analysis of the Correct Answer:**
In the preceding line, Hassan pays Nekesa a compliment: **"Nekesa, you are such a caring girl."** Good manners and conversation etiquette require acknowledging a compliment by saying **"Thank you, Hassan."**.

**Why Other Options Are Incorrect:**
* **I know it, Hassan.:** This sounds boastful and arrogant after receiving a compliment.
* **Hassan, you are right.:** This sounds self-important rather than showing gracious appreciation.
* **Hassan, excuse me.:** Used to get someone's attention or apologize for an interruption, not to respond to a compliment.

📌 **Key Learning Note:**
Always respond to a compliment or praise with a polite **"Thank you"**."""
    },
    {
      "id": "eq5-2022",
      "questionNumber": 5,
      "questionText": "Nekesa: ----5----",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q1-5",
      "options": [
        { "text": "Goodbye too, Hassan.", "isCorrect": True },
        { "text": "It is alright, Hassan.", "isCorrect": False },
        { "text": "I like you, Hassan.", "isCorrect": False },
        { "text": "It is a good day, Hassan.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **Goodbye too, Hassan.**.

**Analysis of the Correct Answer:**
Hassan bids farewell by saying, **"Goodbye, Nekesa."** The standard polite response to a farewell greeting is to reply in kind with **"Goodbye too, Hassan."** (or simply "Goodbye, Hassan.").

**Why Other Options Are Incorrect:**
* **It is alright, Hassan.:** Used to accept an apology or reassure someone, not to answer a goodbye.
* **I like you, Hassan.:** Unrelated to parting ways at the end of a conversation.
* **It is a good day, Hassan.:** A general greeting for the start of a meeting, not a closing farewell.

📌 **Key Learning Note:**
Match closing farewells appropriately: **"Goodbye"** is answered with **"Goodbye too"** or **"Goodbye"**."""
    },
    {
      "id": "eq6-2022",
      "questionNumber": 6,
      "questionText": "Why is food called a basic need? Because",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q6-9",
      "options": [
        { "text": "food is less important than clothes", "isCorrect": False },
        { "text": "food brings people together", "isCorrect": False },
        { "text": "people like different kinds of food", "isCorrect": False },
        { "text": "people need food to live.", "isCorrect": True }
      ],
      "explanation": """The correct answer is **people need food to live.**.

**Analysis of the Correct Answer:**
The passage explicitly states in the very first two sentences: **"Food is a basic need for every human being. We need it in order to remain alive."** This confirms that food is a basic need because humans require it to stay alive.

**Why Other Options Are Incorrect:**
* **food is less important than clothes:** The text does not make this comparison; food, shelter, and clothing are all essential basic needs.
* **food brings people together:** While food may have social aspects, the passage defines it as a basic need because it keeps us alive.
* **people like different kinds of food:** This describes food preferences across communities, not why food is classified as a basic need.

📌 **Key Learning Note:**
A **basic need** is something essential for human survival (such as food, water, shelter, and clothing)."""
    },
    {
      "id": "eq7-2022",
      "questionNumber": 7,
      "questionText": "The word **'favourite'** as used in the passage means the same as",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q6-9",
      "options": [
        { "text": "delicious", "isCorrect": False },
        { "text": "common", "isCorrect": False },
        { "text": "liked", "isCorrect": True },
        { "text": "different.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **liked**.

**Analysis of the Correct Answer:**
In the passage, the author writes: **"...in some communities, rats are a favourite food..."** The word **"favourite"** means something that is preferred, most enjoyed, or highly **liked** by a person or group above other choices.

**Why Other Options Are Incorrect:**
* **delicious:** Refers to taste quality, whereas "favourite" refers to being preferred or liked most.
* **common:** Means widespread or ordinary, which does not capture the special preference implied by "favourite".
* **different:** Means distinct or unlike, which is not synonymous with favourite.

📌 **Key Learning Note:**
- **Favourite:** Preferred or most **liked** among options."""
    },
    {
      "id": "eq8-2022",
      "questionNumber": 8,
      "questionText": "From the passage, **'one man's food is another man's poison'** means",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q6-9",
      "options": [
        { "text": "some people eat dangerous things", "isCorrect": False },
        { "text": "people differ in what they like to eat", "isCorrect": True },
        { "text": "people must try to eat healthy food", "isCorrect": False },
        { "text": "some people only eat what they can find.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **people differ in what they like to eat**.

**Analysis of the Correct Answer:**
The idiom **"one man's food is another man's poison"** means that what one person or community enjoys and considers good food (e.g. eating rats) may be completely unacceptable or disliked by another. Therefore, it means that **people differ in what they like to eat** based on culture and environment.

**Why Other Options Are Incorrect:**
* **some people eat dangerous things:** The proverb uses "poison" metaphorically to mean something strongly disliked or rejected, not actual toxic poison.
* **people must try to eat healthy food:** The proverb is about personal and cultural tastes, not nutritional advice.
* **some people only eat what they can find.:** Refers to food availability, whereas the proverb focuses on differing tastes and cultural acceptance.

📌 **Key Learning Note:**
The idiom **"One man's food is another man's poison"** means that different people have completely different tastes, preferences, and cultural likes/dislikes."""
    },
    {
      "id": "eq9-2022",
      "questionNumber": 9,
      "questionText": "Which of the following is the best title for the passage?",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q6-9",
      "options": [
        { "text": "Food and community.", "isCorrect": True },
        { "text": "Community life.", "isCorrect": False },
        { "text": "Good health.", "isCorrect": False },
        { "text": "Natural beauty.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **Food and community.**.

**Analysis of the Correct Answer:**
The passage focuses throughout on how food is essential to human survival and how different **communities** have different food choices based on their environment and culture. Therefore, **"Food and community"** captures the main theme of the text best.

**Why Other Options Are Incorrect:**
* **Community life:** Too broad; the text deals specifically with food habits across communities, not general community social life.
* **Good health:** The passage does not discuss nutrition, disease prevention, or balanced diets.
* **Natural beauty:** Completely unrelated to the text's focus on food and human consumption.

📌 **Key Learning Note:**
A **good title** summarizes the main subject and central theme that connects all paragraphs of a passage."""
    },
    {
      "id": "eq10-2022",
      "questionNumber": 10,
      "questionText": "Why did Hassan's father write the list of items?",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q10-12",
      "options": [
        { "text": "He did not want Hassan to forget any item.", "isCorrect": True },
        { "text": "He did not want Hassan to delay in the shop.", "isCorrect": False },
        { "text": "He wanted Hassan to learn Mathematics.", "isCorrect": False },
        { "text": "He wanted Hassan to do the totals of the cost of the items.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **He did not want Hassan to forget any item.**.

**Analysis of the Correct Answer:**
When parents write a shopping list for children, the primary purpose is to ensure the shopper remembers all the required items. The list serves as a reference so Hassan would not forget what to buy at the shop.

**Why Other Options Are Incorrect:**
* **He did not want Hassan to delay in the shop.:** While a list saves time, the main function of a shopping list is remembering items.
* **He wanted Hassan to learn Mathematics.:** The list was written to purchase household goods, not as a math lesson.
* **He wanted Hassan to do the totals of the cost of the items.:** The text states the father had already written down the prices and total cost himself.

📌 **Key Learning Note:**
A **shopping list** is written to keep track of items needed so that nothing is forgotten."""
    },
    {
      "id": "eq11-2022",
      "questionNumber": 11,
      "questionText": "The shopkeeper was surprised to see Hassan back because",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q10-12",
      "options": [
        { "text": "Hassan returned the money", "isCorrect": False },
        { "text": "the shopkeeper was very busy that day", "isCorrect": False },
        { "text": "Hassan had just left the shop", "isCorrect": True },
        { "text": "the shopkeeper had given him the balance.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **Hassan had just left the shop**.

**Analysis of the Correct Answer:**
The passage states: **"The shopkeeper was surprised to see him back so soon."** Hassan had only stepped out moments earlier to count his balance under a nearby tree. Because he returned almost immediately after leaving, the shopkeeper was surprised by his quick return.

**Why Other Options Are Incorrect:**
* **Hassan returned the money:** The shopkeeper only realized he was returning extra money *after* Hassan handed it to her; she was surprised initially by how quickly he returned.
* **the shopkeeper was very busy that day:** Being busy explains why she made a mistake in change, but not why Hassan's quick return surprised her.
* **the shopkeeper had given him the balance.:** Giving change is normal procedure; she did not yet realize she had given him Ksh 575 instead of Ksh 75.

📌 **Key Learning Note:**
Pay close attention to words like **"so soon"** in comprehension passages to understand cause and effect."""
    },
    {
      "id": "eq12-2022",
      "questionNumber": 12,
      "questionText": "This story teaches us that",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q10-12",
      "options": [
        { "text": "honesty is the best policy", "isCorrect": True },
        { "text": "hurry hurry has no blessing", "isCorrect": False },
        { "text": "once bitten twice shy", "isCorrect": False },
        { "text": "a friend in need is a friend indeed.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **honesty is the best policy**.

**Analysis of the Correct Answer:**
Hassan resisted the temptation to keep the extra Ksh 500 given to him by mistake and chose to return it to the shopkeeper. His decision brought praise, self-respect, and a clear conscience. This moral lesson proves that **"honesty is the best policy"**.

**Why Other Options Are Incorrect:**
* **hurry hurry has no blessing:** This proverb warns against rushing impetuously, which is not the moral theme of returning money.
* **once bitten twice shy:** Refers to being cautious after a bad experience, which does not fit Hassan's honest act.
* **a friend in need is a friend indeed.:** Refers to true friendship during difficult times, whereas Hassan and the shopkeeper are customer and vendor.

📌 **Key Learning Note:**
The moral proverb **"Honesty is the best policy"** means being truthful and honest is always the right and most rewarding choice."""
    },
    {
      "id": "eq13-2022",
      "questionNumber": 13,
      "questionText": "Which one of the following is true about the King? He",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q13-15",
      "options": [
        { "text": "believed every story people told him", "isCorrect": False },
        { "text": "wanted to find the most exciting story", "isCorrect": False },
        { "text": "was good at telling stories", "isCorrect": False },
        { "text": "enjoyed listening to stories.", "isCorrect": True }
      ],
      "explanation": """The correct answer is **enjoyed listening to stories.**.

**Analysis of the Correct Answer:**
The very first sentence of the story states: **"There once lived a king who loved stories. He wished to have someone who would tell him stories all day."** This directly proves that the King enjoyed listening to stories.

**Why Other Options Are Incorrect:**
* **believed every story people told him:** The text says he listened to stories to be entertained, not that he was gullible.
* **wanted to find the most exciting story:** The King specifically announced a reward for the *longest* story, not the most exciting one.
* **was good at telling stories:** The King wanted someone else to tell him stories, not that he was a storyteller himself.

📌 **Key Learning Note:**
Always locate direct facts from the opening lines of narrative passages."""
    },
    {
      "id": "eq14-2022",
      "questionNumber": 14,
      "questionText": "Why did the King's assistants wonder whether Mokowi could tell a story? They",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q13-15",
      "options": [
        { "text": "thought Mokowi would not be interested", "isCorrect": False },
        { "text": "did not know Mokowi very well", "isCorrect": False },
        { "text": "thought Mokowi would not behave well", "isCorrect": False },
        { "text": "did not believe that Mokowi would tell a good story.", "isCorrect": True }
      ],
      "explanation": """The correct answer is **did not believe that Mokowi would tell a good story.**.

**Analysis of the Correct Answer:**
The text states that Mokowi was known as the man who roamed the market without a shirt, and the assistants asked: **"What story can Mokowi tell?... Surely, a crazy man like him has no business here..."** They doubted his intelligence and did not believe he could tell a good story.

**Why Other Options Are Incorrect:**
* **thought Mokowi would not be interested:** Mokowi had voluntarily come to the palace to tell a story.
* **did not know Mokowi very well:** They recognized him immediately as the eccentric man from the market.
* **thought Mokowi would not behave well:** Their doubt was specifically about his ability to tell a meaningful story.

📌 **Key Learning Note:**
Judging people by their appearance often leads to wrong assumptions, as Mokowi proved the assistants wrong."""
    },
    {
      "id": "eq15-2022",
      "questionNumber": 15,
      "questionText": "The best title for the story would be",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q13-15",
      "options": [
        { "text": "Mokowi's new clothes", "isCorrect": False },
        { "text": "Mokowi's love for locusts", "isCorrect": False },
        { "text": "Mokowi's move to the palace", "isCorrect": False },
        { "text": "Mokowi's unending story.", "isCorrect": True }
      ],
      "explanation": """The correct answer is **Mokowi's unending story.**.

**Analysis of the Correct Answer:**
Mokowi won the contest by cleverly inventing a repetitive story about locusts that went on for days until the King declared: **"the story will never end. You win."** Therefore, **"Mokowi's unending story"** is the most fitting title.

**Why Other Options Are Incorrect:**
* **Mokowi's new clothes:** Receiving clothes was just the reward at the end, not the main focus of the plot.
* **Mokowi's love for locusts:** Locusts were simply characters in his repetitive trick story, not his personal passion.
* **Mokowi's move to the palace:** Mokowi visited the palace to tell his story; he did not move to live there.

📌 **Key Learning Note:**
A **title** should capture the central clever plot element of a narrative."""
    },
    {
      "id": "eq16-2022",
      "questionNumber": 16,
      "questionText": "I live ----16---- a small village in Kiambu County.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q16-20",
      "options": [
        { "text": "in", "isCorrect": True },
        { "text": "at", "isCorrect": False },
        { "text": "on", "isCorrect": False },
        { "text": "by", "isCorrect": False }
      ],
      "explanation": """The correct answer is **in**.

**Analysis of the Correct Answer:**
We use the preposition **"in"** when referring to living inside a village, town, city, or country (**"live in a small village"**).

**Why Other Options Are Incorrect:**
* **at:** Used for specific point locations or addresses (e.g. *at the market*), not for enclosing regions like villages.
* **on:** Used for surface locations (e.g. *on an island*).
* **by:** Used to mean next to or near (e.g. *by the river*).

📌 **Key Learning Note:**
Use **"in"** for villages, towns, cities, and countries (e.g. *in a village*, *in Kenya*)."""
    },
    {
      "id": "eq17-2022",
      "questionNumber": 17,
      "questionText": "My parents Mr and Mrs Kamau are good ----17---- caring doctors.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q16-20",
      "options": [
        { "text": "but", "isCorrect": False },
        { "text": "for", "isCorrect": False },
        { "text": "while", "isCorrect": False },
        { "text": "and", "isCorrect": True }
      ],
      "explanation": """The correct answer is **and**.

**Analysis of the Correct Answer:**
The coordinating conjunction **"and"** is used to connect two positive, complementary adjectives describing Jane's parents: **"good AND caring doctors"**.

**Why Other Options Are Incorrect:**
* **but:** Used to connect contrasting or opposing ideas, which is incorrect here since "good" and "caring" are both positive traits.
* **for:** Used to state a reason or cause.
* **while:** Used to show simultaneous actions or contrast.

📌 **Key Learning Note:**
Use **"and"** to join two similar or complementary positive adjectives."""
    },
    {
      "id": "eq18-2022",
      "questionNumber": 18,
      "questionText": "They have built ----18---- clinic where they see their patients.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q16-20",
      "options": [
        { "text": "a", "isCorrect": True },
        { "text": "an", "isCorrect": False },
        { "text": "some", "isCorrect": False },
        { "text": "the", "isCorrect": False }
      ],
      "explanation": """The correct answer is **a**.

**Analysis of the Correct Answer:**
The indefinite article **"a"** is used before singular countable nouns that begin with a consonant sound. Since **"clinic"** starts with the consonant sound `/k/` and is introduced for the first time, **"a clinic"** is grammatically correct.

**Why Other Options Are Incorrect:**
* **an:** Used before words starting with a vowel sound (e.g. *an apple*, *an office*).
* **some:** Used with plural or uncountable nouns.
* **the:** Used when referring to a specific, previously mentioned noun.

📌 **Key Learning Note:**
Use **"a"** before singular countable nouns beginning with a consonant sound."""
    },
    {
      "id": "eq19-2022",
      "questionNumber": 19,
      "questionText": "They have built a clinic where they see their ----19----.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q16-20",
      "options": [
        { "text": "visitors", "isCorrect": False },
        { "text": "children", "isCorrect": False },
        { "text": "customers", "isCorrect": False },
        { "text": "patients", "isCorrect": True }
      ],
      "explanation": """The correct answer is **patients**.

**Analysis of the Correct Answer:**
Doctors work in clinics or hospitals to diagnose, treat, and care for sick people, who are called **patients**. Therefore, doctors see their **patients** at the clinic.

**Why Other Options Are Incorrect:**
* **visitors:** People who visit a place for leisure or social reasons.
* **children:** Refers generally to young people, whereas doctors treat patients of all ages.
* **customers:** People who buy goods or services in shops or businesses.

📌 **Key Learning Note:**
People who receive medical care from doctors or nurses are called **patients**."""
    },
    {
      "id": "eq20-2022",
      "questionNumber": 20,
      "questionText": "When I grow up, I ----20---- like to be a teacher.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q16-20",
      "options": [
        { "text": "can", "isCorrect": False },
        { "text": "will", "isCorrect": False },
        { "text": "would", "isCorrect": True },
        { "text": "could", "isCorrect": False }
      ],
      "explanation": """The correct answer is **would**.

**Analysis of the Correct Answer:**
When expressing personal wishes, ambitions, or preferences for the future, the polite idiomatic modal structure is **"would like to"** (**"I would like to be a teacher"**).

**Why Other Options Are Incorrect:**
* **can:** Expresses ability or permission, not the fixed phrase *would like to*.
* **will:** Used in *will be* (e.g. *I will be a teacher*), but does not pair with *like to* in this context.
* **could:** Expresses past ability or conditional possibility.

📌 **Key Learning Note:**
Use **"would like to"** to express future ambitions or polite desires."""
    },
    {
      "id": "eq21-2022",
      "questionNumber": 21,
      "questionText": "My friend, Kabuge, prefers skipping rope ---- playing netball.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q21-25",
      "options": [
        { "text": "to", "isCorrect": True },
        { "text": "than", "isCorrect": False },
        { "text": "but", "isCorrect": False },
        { "text": "also", "isCorrect": False }
      ],
      "explanation": """The correct answer is **to**.

**Analysis of the Correct Answer:**
In English grammar, the verb **"prefer"** is strictly followed by the preposition **"to"** when comparing two activities or items (**"prefer X to Y"**). Therefore, *"prefers skipping rope **to** playing netball"* is correct.

**Why Other Options Are Incorrect:**
* **than:** Commonly misused after *prefer* due to confusion with comparative adjectives (e.g. *better than*), but *prefer... than* is ungrammatical.
* **but:** Conjunction showing contrast, not comparison of preferences.
* **also:** Adverb meaning in addition.

📌 **Key Learning Note:**
Always use **"prefer... to..."** (never *prefer... than...*)."""
    },
    {
      "id": "eq22-2022",
      "questionNumber": 22,
      "questionText": "The thief jumped ---- the river to escape from the police.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q21-25",
      "options": [
        { "text": "into", "isCorrect": True },
        { "text": "at", "isCorrect": False },
        { "text": "to", "isCorrect": False },
        { "text": "under", "isCorrect": False }
      ],
      "explanation": """The correct answer is **into**.

**Analysis of the Correct Answer:**
The preposition **"into"** expresses movement or direction from the outside to the inside of a 3D space or liquid body. Since jumping involves entering water from above, **"jumped into the river"** is correct.

**Why Other Options Are Incorrect:**
* **at:** Indicates a specific location point, not movement entering water.
* **to:** Indicates direction towards a destination without specifying entering inside it.
* **under:** Means beneath a surface, but does not describe the active entry movement.

📌 **Key Learning Note:**
Use **"into"** to show movement from outside to inside a container or body of water."""
    },
    {
      "id": "eq23-2022",
      "questionNumber": 23,
      "questionText": "The teacher talked to the parent ---- phone.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q21-25",
      "options": [
        { "text": "with", "isCorrect": False },
        { "text": "on", "isCorrect": True },
        { "text": "in", "isCorrect": False },
        { "text": "through", "isCorrect": False }
      ],
      "explanation": """The correct answer is **on**.

**Analysis of the Correct Answer:**
In English, the standard fixed prepositional phrase for communicating via telephone is strictly **"on the phone"** or **"on phone"**.

**Why Other Options Are Incorrect:**
* **with:** Indicates instrument or company (e.g. *talked with a friend*).
* **in:** Indicates location inside a space.
* **through:** Indicates passage through an opening or medium, but is not the standard idiom for phone conversations.

📌 **Key Learning Note:**
Use **"on the phone"** when referring to telephone conversations."""
    },
    {
      "id": "eq24-2022",
      "questionNumber": 24,
      "questionText": "Our teachers know what is best for us so we ---- obey them.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q21-25",
      "options": [
        { "text": "could", "isCorrect": False },
        { "text": "may", "isCorrect": False },
        { "text": "will", "isCorrect": False },
        { "text": "should", "isCorrect": True }
      ],
      "explanation": """The correct answer is **should**.

**Analysis of the Correct Answer:**
The modal verb **"should"** is used to express moral obligation, duty, or advisable behavior. Since teachers guide learners for their own good, it is advisable and obligatory that students **should** obey them.

**Why Other Options Are Incorrect:**
* **could:** Expresses past ability or weak possibility.
* **may:** Expresses permission or possibility.
* **will:** Expresses future certainty, but lacks the sense of moral duty carried by *should*.

📌 **Key Learning Note:**
Use **"should"** to express moral duty, obligation, or advisable actions."""
    },
    {
      "id": "eq25-2022",
      "questionNumber": 25,
      "questionText": "The scouts said to their leader, \"Now that we have cut all the grass, ---- else can we do?\"",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q21-25",
      "options": [
        { "text": "whom", "isCorrect": False },
        { "text": "where", "isCorrect": False },
        { "text": "which", "isCorrect": False },
        { "text": "what", "isCorrect": True }
      ],
      "explanation": """The correct answer is **what**.

**Analysis of the Correct Answer:**
The question pronoun **"what"** is used to inquire about actions, tasks, or things. The scouts are asking about the next task to perform, so **"what else can we do?"** is grammatically correct.

**Why Other Options Are Incorrect:**
* **whom:** Used to ask about the object of a sentence (persons), not tasks or actions.
* **where:** Used to ask about place or location.
* **which:** Used to select between a limited, specific set of choices.

📌 **Key Learning Note:**
Use **"what"** to ask about actions, activities, or things to be done."""
    },
    {
      "id": "eq26-2022",
      "questionNumber": 26,
      "questionText": "Mokaya's bag is **old**.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q26",
      "options": [
        { "text": "new", "isCorrect": True },
        { "text": "costly", "isCorrect": False },
        { "text": "modern", "isCorrect": False },
        { "text": "cheap", "isCorrect": False }
      ],
      "explanation": """The correct answer is **new**.

**Analysis of the Correct Answer:**
The word **"old"** describes an object that has been used for a long time or is not recently made. The direct opposite (antonym) of **old** when describing a physical item like a bag is **new**.

**Why Other Options Are Incorrect:**
* **costly:** Antonym of *cheap*, referring to price rather than age.
* **modern:** Refers to recent style, design, or technology, but *new* is the exact antonym of *old*.
* **cheap:** Refers to low monetary cost.

📌 **Key Learning Note:**
- **Old ↔ New** (Antonyms of age/condition).
- **Cheap ↔ Costly/Expensive** (Antonyms of price)."""
    },
    {
      "id": "eq27-2022",
      "questionNumber": 27,
      "questionText": "**The hungry pupils ate the raw mangoes.**",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q27-28",
      "options": [
        { "text": "The raw mangoes had been eaten by the hungry pupils.", "isCorrect": False },
        { "text": "The raw mangoes are eaten by the hungry pupils.", "isCorrect": False },
        { "text": "The raw mangoes were eaten by the hungry pupils.", "isCorrect": True },
        { "text": "The raw mangoes will be eaten by the hungry pupils.", "isCorrect": False }
      ],
      "explanation": """The correct answer is **The raw mangoes were eaten by the hungry pupils.**.

**Analysis of the Correct Answer:**
The original sentence **"The hungry pupils ate the raw mangoes"** is in the active voice using the simple past tense verb **"ate"**. When changing a sentence from active to passive voice in the simple past tense:
1. The object (**"The raw mangoes"**) becomes the new subject.
2. Use the past tense auxiliary verb **"were"** (plural object) + past participle **"eaten"**.
3. Add **"by the hungry pupils"** (the agent).

Therefore, **"The raw mangoes were eaten by the hungry pupils."** has the exact same meaning as the underlined active sentence.

**Why Other Options Are Incorrect:**
* **The raw mangoes had been eaten by the hungry pupils.:** Changes the tense to past perfect (*had been eaten*).
* **The raw mangoes are eaten by the hungry pupils.:** Changes the tense to simple present (*are eaten*).
* **The raw mangoes will be eaten by the hungry pupils.:** Changes the tense to simple future (*will be eaten*).

📌 **Key Learning Note:**
- **Simple Past Active:** Subject + V2 + Object (e.g. *ate the mangoes*).
- **Simple Past Passive:** Object + was/were + V3 + by Subject (e.g. *were eaten by the pupils*)."""
    },
    {
      "id": "eq28-2022",
      "questionNumber": 28,
      "questionText": "The guests were pleased with the **person who served them food at the hotel**.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q27-28",
      "options": [
        { "text": "cook", "isCorrect": False },
        { "text": "host", "isCorrect": False },
        { "text": "waiter", "isCorrect": True },
        { "text": "cleaner", "isCorrect": False }
      ],
      "explanation": """The correct answer is **waiter**.

**Analysis of the Correct Answer:**
The underlined phrase **"person who served them food at the hotel"** describes a worker whose job is to serve food and drinks to customers in a hotel or restaurant. The single word that means the same as this phrase is **waiter** (or waitress).

**Why Other Options Are Incorrect:**
* **cook:** The person who prepares and cooks the food in the kitchen.
* **host:** The person who receives and entertains guests or invites them.
* **cleaner:** The person responsible for cleaning and tidying the premises.

📌 **Key Learning Note:**
- **Waiter:** A person who serves meals at tables in a restaurant or hotel.
- **Cook/Chef:** A person who prepares food."""
    },
    {
      "id": "eq29-2022",
      "questionNumber": 29,
      "questionText": "We found the room **tidy**.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q29-30",
      "options": [
        { "text": "neat", "isCorrect": True },
        { "text": "bright", "isCorrect": False },
        { "text": "warm", "isCorrect": False },
        { "text": "fresh", "isCorrect": False }
      ],
      "explanation": """The correct answer is **neat**.

**Analysis of the Correct Answer:**
The word **"tidy"** means arranged neatly and in good order. The word that means the same (synonym) as **tidy** when describing a room is **neat**.

**Why Other Options Are Incorrect:**
* **bright:** Refers to well-lit or colorful.
* **warm:** Refers to comfortable temperature or friendly atmosphere.
* **fresh:** Refers to clean air or recently made items.

📌 **Key Learning Note:**
- **Tidy = Neat** (Synonyms describing orderliness and cleanliness)."""
    },
    {
      "id": "eq30-2022",
      "questionNumber": 30,
      "questionText": "The choir sang **cheerfully**.",
      "questionType": "mcq",
      "contextRef": "ctx-eng-2022-q29-30",
      "options": [
        { "text": "loudly", "isCorrect": False },
        { "text": "beautifully", "isCorrect": False },
        { "text": "happily", "isCorrect": True },
        { "text": "carefully", "isCorrect": False }
      ],
      "explanation": """The correct answer is **happily**.

**Analysis of the Correct Answer:**
The word **"cheerfully"** is an adverb meaning in a happy, joyful, and lively manner. The word that means the same (synonym) as **cheerfully** is **happily**.

**Why Other Options Are Incorrect:**
* **loudly:** Refers to high volume or noise level.
* **beautifully:** Refers to pleasing quality or elegance.
* **carefully:** Refers to doing something with caution and attention.

📌 **Key Learning Note:**
- **Cheerfully = Happily** (Synonyms of joyful emotion and expression)."""
    }
  ]
}

# Write file
with open('src/data/kpsea-english-2022.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaEnglish2022 = ' + json.dumps(english_2022_data, indent=2, ensure_ascii=False) + ';\n')

print("Created kpsea-english-2022.js with all 30 questions successfully!")
