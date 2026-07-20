import sys

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert new contexts
context_insert_str = '        "ctx-eng-q13-15": {'
new_context_str = """        "ctx-eng-q16-20": {
          title: "Questions 16 to 20\\nRead the passage below. It contains blank spaces numbered 16 to 20. For each blank space, select the best alternative from the choices given.",
          type: "text",
          text: "Asha has a small garden at home. She likes it because it is a gift from ____16____ grandfather. Asha grows ____17____ vegetables in her garden. She ____18____ taking care of her vegetables. She does not like to sit in the house ____19____ play games on the phone. She hopes to sell her harvest ____20____ month."
        },
        "ctx-eng-q30": {
          title: "Question 30\\nRead the following paragraph and answer question 30.",
          type: "text",
          text: "Nasir, Banda and Lona are friends. They all play football. Nasir also plays volleyball. Lona also plays netball."
        },
        "ctx-eng-q13-15": {"""

if 'ctx-eng-q16-20' not in content:
    content = content.replace(context_insert_str, new_context_str)

# 2. Insert questions 16-30
q_insert_target = """          explanation: "Hyena thought Hare was his friend and partner in crime, but Hare completely betrayed him and left him to be beaten by the farmer.\\nThe story teaches us a valuable lesson: be careful who you trust, and make sure you keep the right friends!"
        }
      ]
    }
  ],
  KJSEA: []"""

new_qs = """          explanation: "Hyena thought Hare was his friend and partner in crime, but Hare completely betrayed him and left him to be beaten by the farmer.\\nThe story teaches us a valuable lesson: be careful who you trust, and make sure you keep the right friends!"
        },
        {
          id: "eq16",
          questionNumber: 16,
          questionText: "16. Asha has a small garden at home. She likes it because it is a gift from ____16____ grandfather.",
          questionType: "mcq",
          contextRef: "ctx-eng-q16-20",
          options: [
            { text: "his", isCorrect: false },
            { text: "hers", isCorrect: false },
            { text: "him", isCorrect: false },
            { text: "her", isCorrect: true }
          ],
          explanation: "Asha is a girl. When referring to someone related to a female, we use the possessive pronoun 'her'. So it is 'her grandfather'."
        },
        {
          id: "eq17",
          questionNumber: 17,
          questionText: "17. Asha grows ____17____ vegetables in her garden.",
          questionType: "mcq",
          contextRef: "ctx-eng-q16-20",
          options: [
            { text: "different", isCorrect: true },
            { text: "dry", isCorrect: false },
            { text: "cooked", isCorrect: false },
            { text: "plenty", isCorrect: false }
          ],
          explanation: "In a garden, you grow raw, living plants. 'Dry' and 'cooked' don't make sense for growing vegetables. 'Plenty' requires 'of' (plenty of vegetables). 'Different' perfectly describes a variety of vegetables growing in a garden."
        },
        {
          id: "eq18",
          questionNumber: 18,
          questionText: "18. She ____18____ taking care of her vegetables.",
          questionType: "mcq",
          contextRef: "ctx-eng-q16-20",
          options: [
            { text: "begins", isCorrect: false },
            { text: "accepts", isCorrect: false },
            { text: "enjoys", isCorrect: true },
            { text: "admires", isCorrect: false }
          ],
          explanation: "Because she likes her garden, doing the work to take care of it is something she likes doing. The word 'enjoys' shows that she finds pleasure in taking care of her vegetables."
        },
        {
          id: "eq19",
          questionNumber: 19,
          questionText: "19. She does not like to sit in the house ____19____ play games on the phone.",
          questionType: "mcq",
          contextRef: "ctx-eng-q16-20",
          options: [
            { text: "also", isCorrect: false },
            { text: "and", isCorrect: true },
            { text: "yet", isCorrect: false },
            { text: "because", isCorrect: false }
          ],
          explanation: "The sentence links two things she dislikes doing together: sitting in the house, AND playing games on the phone. The conjunction 'and' joins these two similar activities smoothly."
        },
        {
          id: "eq20",
          questionNumber: 20,
          questionText: "20. She hopes to sell her harvest ____20____ month.",
          questionType: "mcq",
          contextRef: "ctx-eng-q16-20",
          options: [
            { text: "future", isCorrect: false },
            { text: "new", isCorrect: false },
            { text: "next", isCorrect: true },
            { text: "later", isCorrect: false }
          ],
          explanation: "When referring to the month that follows the current one, the correct English phrase is 'next month'. We don't say 'future month' or 'later month'."
        },
        {
          id: "eq21",
          questionNumber: 21,
          questionText: "21. The teacher found the learner _______ the classroom.",
          questionType: "mcq",
          options: [
            { text: "to", isCorrect: false },
            { text: "in", isCorrect: true },
            { text: "on", isCorrect: false },
            { text: "over", isCorrect: false }
          ],
          explanation: "A classroom is an enclosed space. When someone is inside an enclosed space, we use the preposition 'in'."
        },
        {
          id: "eq22",
          questionNumber: 22,
          questionText: "22. Ali left the book _______ the table.",
          questionType: "mcq",
          options: [
            { text: "with", isCorrect: false },
            { text: "on", isCorrect: true },
            { text: "in", isCorrect: false },
            { text: "from", isCorrect: false }
          ],
          explanation: "A table has a flat surface. When placing an object atop a surface, the correct preposition is 'on'."
        },
        {
          id: "eq23",
          questionNumber: 23,
          questionText: "23. The children are planting trees, _______",
          questionType: "mcq",
          options: [
            { text: "aren't they?", isCorrect: true },
            { text: "aren't we?", isCorrect: false },
            { text: "are they?", isCorrect: false },
            { text: "are we?", isCorrect: false }
          ],
          explanation: "This is a question tag. The main sentence is positive ('are planting'), so the tag must be negative. 'The children' is plural (they). Therefore, the correct tag is 'aren't they?'"
        },
        {
          id: "eq24",
          questionNumber: 24,
          questionText: "24. Rudisha did not find the story book in his bag because _______ had taken it.",
          questionType: "mcq",
          options: [
            { text: "anybody", isCorrect: false },
            { text: "somebody", isCorrect: true },
            { text: "everybody", isCorrect: false },
            { text: "nobody", isCorrect: false }
          ],
          explanation: "The book is missing because a person took it without Rudisha knowing exactly who it was. The pronoun 'somebody' is used to refer to an unspecified person."
        },
        {
          id: "eq25",
          questionNumber: 25,
          questionText: "25. The teacher told us to take care of _______ during the journey.",
          questionType: "mcq",
          options: [
            { text: "themselves", isCorrect: false },
            { text: "yourself", isCorrect: false },
            { text: "ourselves", isCorrect: true },
            { text: "yourselves", isCorrect: false }
          ],
          explanation: "The pronoun in the sentence is 'us'. The matching reflexive pronoun for 'us' (we) is 'ourselves'. The teacher told us to take care of ourselves."
        },
        {
          id: "eq26",
          questionNumber: 26,
          questionText: "26. The thieves took away our goats _______ force.",
          questionType: "mcq",
          options: [
            { text: "with", isCorrect: false },
            { text: "by", isCorrect: true },
            { text: "at", isCorrect: false },
            { text: "under", isCorrect: false }
          ],
          explanation: "In English, the correct phrase used to describe an action done using violence or against someone's will is 'by force'."
        },
        {
          id: "eq27",
          questionNumber: 27,
          questionText: "27. This is the hen _______ egg broke.",
          questionType: "mcq",
          options: [
            { text: "who", isCorrect: false },
            { text: "whom", isCorrect: false },
            { text: "whose", isCorrect: true },
            { text: "which", isCorrect: false }
          ],
          explanation: "The egg belongs to the hen. To show possession linking a noun to its owner in a relative clause, we use the word 'whose'."
        },
        {
          id: "eq28",
          questionNumber: 28,
          questionText: "28. The class teacher will _______ us a present.",
          questionType: "mcq",
          options: [
            { text: "given", isCorrect: false },
            { text: "gives", isCorrect: false },
            { text: "gave", isCorrect: false },
            { text: "give", isCorrect: true }
          ],
          explanation: "The word 'will' indicates future tense. After modal verbs like 'will', 'shall', or 'can', we must always use the base form of the verb. So 'give' is correct."
        },
        {
          id: "eq29",
          questionNumber: 29,
          questionText: "29. 'Neither Kalusi nor Sofia came late to class'.\\nMeans:",
          questionType: "mcq",
          options: [
            { text: "Only Kalusi came late to class.", isCorrect: false },
            { text: "Only Sofia came late to class.", isCorrect: false },
            { text: "Both Kalusi and Sofia came late to class.", isCorrect: false },
            { text: "Both Kalusi and Sofia did not come late to class.", isCorrect: true }
          ],
          explanation: "The phrase 'Neither... nor' is used to make a negative statement about two things or people. It means 'not one and not the other'. So it means both Kalusi and Sofia did NOT come late."
        },
        {
          id: "eq30",
          questionNumber: 30,
          questionText: "30. According to the story, who plays football only?",
          questionType: "mcq",
          contextRef: "ctx-eng-q30",
          options: [
            { text: "Nasir.", isCorrect: false },
            { text: "Banda.", isCorrect: true },
            { text: "Lona.", isCorrect: false },
            { text: "All of them.", isCorrect: false }
          ],
          explanation: "Let's look at the facts:\\n- Nasir plays football AND volleyball.\\n- Lona plays football AND netball.\\n- All three play football, but Banda is the ONLY one who doesn't have a second sport mentioned. Therefore, Banda plays football only!"
        }
      ]
    }
  ],
  KJSEA: []"""

if 'id: "eq30"' not in content:
    content = content.replace(q_insert_target, new_qs)

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added questions 16-30!")
