import sys

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert the new sharedContext
context_insert_str = '        "ctx-eng-q6-9": {'
new_context_str = """        "ctx-eng-q10-12": {
          title: "Questions 10 to 12\\nRead the story below and then answer questions 10 to 12.",
          type: "text",
          text: "Hassan likes running errands for his parents. The other day, he was sent to the shop to buy some items. His father had written the prices of the items on a list. The total cost was four hundred and twenty five shillings. His father had given him five hundred shillings. Hassan was expecting a balance of seventy five shillings.\\n\\nThe shopkeeper was very busy on that day. She was serving many customers. When Hassan got the balance, he stepped out of the shop to count the money. He could not believe it. The shopkeeper had given him five hundred and seventy five shillings! Hassan thought this was his lucky day.\\n\\nHe sat down under a tree to plan how he would spend his new found cash. He started counting all the things he wanted to buy. This time he would go to a different shop.\\n\\nOn his way to the shop, Hassan remembered what his father had once told him, \\"Never take what does not belong to you\\". He realised the five hundred shillings belonged to the shopkeeper. He walked back to the shop to return the money. The shopkeeper was surprised to see him back so soon. When Hassan handed her the money, she was very grateful and said, \\"You are an angel. I'm proud of you, young man\\".\\n\\nHassan walked home shoulder high. He knew his father would be very pleased with him."
        },
        "ctx-eng-q6-9": {"""

if 'ctx-eng-q10-12' not in content:
    content = content.replace(context_insert_str, new_context_str)

# 2. Insert questions 10-12
q_insert_target = """          explanation: "The passage concludes by reminding us that whether animals are kept for pets, work, or food, they 'deserve kind treatment.'\\nThe logical implication here is a simple trade-off: since we get so many benefits from them (like company, transport, and food), failing to treat them kindly means we might lose out on all those wonderful benefits!"
        }
      ]
    }
  ],
  KJSEA: []"""

new_qs = """          explanation: "The passage concludes by reminding us that whether animals are kept for pets, work, or food, they 'deserve kind treatment.'\\nThe logical implication here is a simple trade-off: since we get so many benefits from them (like company, transport, and food), failing to treat them kindly means we might lose out on all those wonderful benefits!"
        },
        {
          id: "eq10",
          questionNumber: 10,
          questionText: "10. Why did Hassan's father write the list of items?",
          questionType: "mcq",
          contextRef: "ctx-eng-q10-12",
          options: [
            { text: "He did not want Hassan to forget any item.", isCorrect: false },
            { text: "He did not want Hassan to delay in the shop.", isCorrect: false },
            { text: "He wanted Hassan to get the right balance from the shopkeeper.", isCorrect: true },
            { text: "He wanted Hassan to do the totals of the cost of the items.", isCorrect: false }
          ],
          explanation: "In the passage, the writer specifically mentions that the father wrote the 'prices' on the list, which helped Hassan know the total cost and expect exactly seventy-five shillings in balance.\\nWhile people often use shopping lists to avoid forgetting items, the emphasis here on prices and calculating the expected balance points to ensuring Hassan gets the correct change from the busy shopkeeper!"
        },
        {
          id: "eq11",
          questionNumber: 11,
          questionText: "11. The shopkeeper was surprised to see Hassan back because _________",
          questionType: "mcq",
          contextRef: "ctx-eng-q10-12",
          options: [
            { text: "Hassan returned the money.", isCorrect: false },
            { text: "the shopkeeper was very busy that day.", isCorrect: false },
            { text: "Hassan had just left the shop.", isCorrect: true },
            { text: "the shopkeeper had given him the balance.", isCorrect: false }
          ],
          explanation: "The story says, 'The shopkeeper was surprised to see him back so soon.'\\nShe was surprised before he even handed her the money. Her surprise was purely because he had just left a few moments ago and was already walking back into the shop!"
        },
        {
          id: "eq12",
          questionNumber: 12,
          questionText: "12. This story teaches us that _________",
          questionType: "mcq",
          contextRef: "ctx-eng-q10-12",
          options: [
            { text: "honesty is the best policy.", isCorrect: true },
            { text: "hurry hurry has no blessing.", isCorrect: false },
            { text: "once bitten twice shy.", isCorrect: false },
            { text: "a friend in need is a friend indeed.", isCorrect: false }
          ],
          explanation: "Hassan found himself with extra money that wasn't his. Even though he wanted to spend it, he remembered his father's advice and did the right thing by returning it.\\nThis classic moral lesson teaches us that being honest is always the best choice!"
        }
      ]
    }
  ],
  KJSEA: []"""

if 'id: "eq12"' not in content:
    content = content.replace(q_insert_target, new_qs)

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added questions 10-12!")
