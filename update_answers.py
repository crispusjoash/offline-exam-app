import json
import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

# I will use string replacements to update the specific questions.

# Update Question 11
q11_old = '''        {
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
        },'''

q11_new = '''        {
          id: "eq11",
          questionNumber: 11,
          questionText: "11. The shopkeeper was surprised to see Hassan back because _________",
          questionType: "mcq",
          contextRef: "ctx-eng-q10-12",
          options: [
            { text: "Hassan returned the money.", isCorrect: true },
            { text: "the shopkeeper was very busy that day.", isCorrect: false },
            { text: "Hassan had just left the shop.", isCorrect: false },
            { text: "the shopkeeper had given him the balance.", isCorrect: false }
          ],
          explanation: "Hassan came back to the shop specifically to return the extra money. The shopkeeper was very surprised because it is very rare for someone to honestly return money they were overpaid. She was so amazed by this action that she even called him an angel!"
        },'''

# Update Question 13
q13_old = '''        {
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
        },'''

q13_new = '''        {
          id: "eq13",
          questionNumber: 13,
          questionText: "13. Which one of the following is **true** according to the story?",
          questionType: "mcq",
          contextRef: "ctx-eng-q13-15",
          options: [
            { text: "Hare stole the groundnuts just like Hyena.", isCorrect: false },
            { text: "Hare was a true friend of the farmer.", isCorrect: false },
            { text: "Hare was not able to cheat Hyena.", isCorrect: false },
            { text: "Hare buried one of his legs in the ground.", isCorrect: true }
          ],
          explanation: "According to the official marking scheme, Hare buried one of his legs in the ground. While Hyena foolishly buried all four of his legs and got stuck, Hare used the tricky excuse that his legs were 'very short', keeping himself free enough to quickly run away when the farmer arrived!"
        },'''

# Update Question 30
q30_old = '''        {
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
        }'''

q30_new = '''        {
          id: "eq30",
          questionNumber: 30,
          questionText: "30. According to the story, who plays football only?",
          questionType: "mcq",
          contextRef: "ctx-eng-q30",
          options: [
            { text: "Nasir.", isCorrect: true },
            { text: "Banda.", isCorrect: false },
            { text: "Lona.", isCorrect: false },
            { text: "All of them.", isCorrect: false }
          ],
          explanation: "According to the official marking scheme, the correct answer is Nasir. (Note: While reading the text literally suggests Banda plays football only since Nasir also plays volleyball, we always follow the official KNEC marking scheme answers for exams!)"
        }'''

content = content.replace(q11_old, q11_new)
content = content.replace(q13_old, q13_new)
content = content.replace(q30_old, q30_new)

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Q11, Q13, Q30 based on marking scheme.")
