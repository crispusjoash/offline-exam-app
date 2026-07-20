import sys

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert the new sharedContext
context_insert_str = '        "ctx-eng-q10-12": {'
new_context_str = """        "ctx-eng-q13-15": {
          title: "Questions 13 to 15\\nRead the story below and then answer questions 13 to 15.",
          type: "text",
          text: "Many afternoons, Hyena and Hare spent hours in a field eating the farmer's groundnuts. One day, Hare heard that the farmer was complaining that his groundnuts were being stolen. Hare went to him and said, \\"I will catch the thief for you.\\"\\n\\nOne afternoon, Hare told Hyena that groundnuts are sweeter when you eat them with your legs buried in the ground. Hyena buried his four legs in the ground. He looked at the Hare and asked him, \\"Hare, why have you not buried your four legs?\\" Hare replied, \\"My legs are very short.\\" Hyena was happy with Hare's answer, and he continued eating groundnuts. Hare watched carefully and when he saw the farmer coming, he quickly ran away. Hyena too saw the farmer, and tried to escape, but his legs were stuck in the ground. The farmer caught him and gave him a thorough beating."
        },
        "ctx-eng-q10-12": {"""

if 'ctx-eng-q13-15' not in content:
    content = content.replace(context_insert_str, new_context_str)

# 2. Insert questions 13-15
q_insert_target = """          explanation: "Hassan found himself with extra money that wasn't his. Even though he wanted to spend it, he remembered his father's advice and did the right thing by returning it.\\nThis classic moral lesson teaches us that being honest is always the best choice!"
        }
      ]
    }
  ],
  KJSEA: []"""

new_qs = """          explanation: "Hassan found himself with extra money that wasn't his. Even though he wanted to spend it, he remembered his father's advice and did the right thing by returning it.\\nThis classic moral lesson teaches us that being honest is always the best choice!"
        },
        {
          id: "eq13",
          questionNumber: 13,
          questionText: "13. Which one of the following is **true** according to the story?",
          questionType: "mcq",
          contextRef: "ctx-eng-q13-15",
          options: [
            { text: "Hare stole the groundnuts just like Hyena.", isCorrect: true },
            { text: "Hare was a true friend of the farmer.", isCorrect: false },
            { text: "Hare was not able to cheat Hyena.", isCorrect: false },
            { text: "Hare buried one of his legs in the ground.", isCorrect: false }
          ],
          explanation: "In the very first sentence, the story says, 'Many afternoons, Hyena and Hare spent hours in a field eating the farmer\\'s groundnuts.' This means they were both stealing the groundnuts together!"
        },
        {
          id: "eq14",
          questionNumber: 14,
          questionText: "14. From the story, Hare is _________.",
          questionType: "mcq",
          contextRef: "ctx-eng-q13-15",
          options: [
            { text: "friendly", isCorrect: false },
            { text: "funny", isCorrect: false },
            { text: "busy", isCorrect: false },
            { text: "tricky", isCorrect: true }
          ],
          explanation: "Hare came up with a cunning lie, telling Hyena that groundnuts are sweeter when your legs are buried, just so Hyena would get stuck and caught by the farmer.\\nSomeone who uses clever lies to deceive others is definitely tricky!"
        },
        {
          id: "eq15",
          questionNumber: 15,
          questionText: "15. What do we learn from this story?",
          questionType: "mcq",
          contextRef: "ctx-eng-q13-15",
          options: [
            { text: "People need to share what they have.", isCorrect: false },
            { text: "We should keep the right friends.", isCorrect: true },
            { text: "Farmers should beat all Hyenas.", isCorrect: false },
            { text: "We should always do what we are told.", isCorrect: false }
          ],
          explanation: "Hyena thought Hare was his friend and partner in crime, but Hare completely betrayed him and left him to be beaten by the farmer.\\nThe story teaches us a valuable lesson: be careful who you trust, and make sure you keep the right friends!"
        }
      ]
    }
  ],
  KJSEA: []"""

if 'id: "eq13"' not in content:
    content = content.replace(q_insert_target, new_qs)

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added questions 13-15!")
