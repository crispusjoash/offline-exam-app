import sys

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert the new sharedContext
context_insert_str = '        "ctx-eng-q1-3": {'
new_context_str = """        "ctx-eng-q6-9": {
          title: "Questions 6 to 9\\nRead the passage below and then answer questions 6 to 9.",
          type: "text",
          text: "Human beings have always kept animals for different purposes. Animals can be kept as pets. A pet is an animal kept for pleasure. We keep pets because we love their company. We play with them. They are just like our friends, so we keep them happy and comfortable. Indeed, the dog, which is a common pet, has been said to be man's best friend.\\n\\nAnimals can also be kept to help human beings do certain tasks. This is because they have special abilities which human beings do not have. For example, donkeys have strength to carry heavy luggage. They can therefore help us in transportation.\\n\\nSome animals are kept as source of food. Animal products such as milk and eggs are a rich source of nutrients. It is important to realise that whether we keep animals as pets, to help in work, or for food, they deserve kind treatment."
        },
        "ctx-eng-q1-3": {"""

if 'ctx-eng-q6-9' not in content:
    content = content.replace(context_insert_str, new_context_str)

# 2. Insert questions 6-9
q_insert_target = """          explanation: "In English, the correct preposition to use when referring to walking as a means of transport is 'on'. We say 'on foot', not 'by foot'."
        }
      ]
    }
  ],
  KJSEA: []"""

new_qs = """          explanation: "In English, the correct preposition to use when referring to walking as a means of transport is 'on'. We say 'on foot', not 'by foot'."
        },
        {
          id: "eq6",
          questionNumber: 6,
          questionText: "6. Why do we keep pets?",
          questionType: "mcq",
          contextRef: "ctx-eng-q6-9",
          options: [
            { text: "To help us carry heavy things.", isCorrect: false },
            { text: "To make us happy.", isCorrect: true },
            { text: "To provide food.", isCorrect: false },
            { text: "To protect the environment.", isCorrect: false }
          ],
          explanation: "When you read the very first paragraph, it clearly says, 'A pet is an animal kept for pleasure. We keep pets because we love their company.'\\nKeeping an animal for pleasure and loving its company are things that directly bring us happiness! So, the best answer is that we keep them to make us happy."
        },
        {
          id: "eq7",
          questionNumber: 7,
          questionText: "7. Which one of the following is **true** about donkeys and dogs?",
          questionType: "mcq",
          contextRef: "ctx-eng-q6-9",
          options: [
            { text: "They are man's best friend.", isCorrect: false },
            { text: "They are better than us.", isCorrect: false },
            { text: "They can do things that we cannot do.", isCorrect: true },
            { text: "They are always comfortable and healthy.", isCorrect: false }
          ],
          explanation: "Let's think about both animals based on the passage! Dogs are great pets and provide loyal company, while donkeys are strong enough to carry heavy luggage.\\nWhat do they both have in common? They both fall under the category of animals that have 'special abilities which human beings do not have.' Because of these unique abilities, they can do things that we simply cannot do on our own."
        },
        {
          id: "eq8",
          questionNumber: 8,
          questionText: "8. The word **'special'** as used in the passage means the same as",
          questionType: "mcq",
          contextRef: "ctx-eng-q6-9",
          options: [
            { text: "strange.", isCorrect: false },
            { text: "unusual.", isCorrect: true },
            { text: "new.", isCorrect: false },
            { text: "unknown.", isCorrect: false }
          ],
          explanation: "When the writer talks about animals having 'special' abilities, they mean abilities that humans don't normally have.\\nIf something isn't common or normal for everyone to have, we can describe it as 'unusual'. It's a unique and exceptional skill!"
        },
        {
          id: "eq9",
          questionNumber: 9,
          questionText: "9. What is likely to happen if we do not treat animals kindly?",
          questionType: "mcq",
          contextRef: "ctx-eng-q6-9",
          options: [
            { text: "They will not live with us.", isCorrect: false },
            { text: "They may not give us enough food.", isCorrect: false },
            { text: "We may not get enough benefits from them.", isCorrect: true },
            { text: "We may not be happy and comfortable.", isCorrect: false }
          ],
          explanation: "The passage concludes by reminding us that whether animals are kept for pets, work, or food, they 'deserve kind treatment.'\\nThe logical implication here is a simple trade-off: since we get so many benefits from them (like company, transport, and food), failing to treat them kindly means we might lose out on all those wonderful benefits!"
        }
      ]
    }
  ],
  KJSEA: []"""

if 'id: "eq9"' not in content:
    content = content.replace(q_insert_target, new_qs)

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added questions 6-9!")
