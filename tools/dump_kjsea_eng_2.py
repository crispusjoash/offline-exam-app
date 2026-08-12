import json
import re

with open("src/data/kjsea-english-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaEnglish2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

data["sharedContexts"]["ctx-eng-2025-q11-16"] = {
  "title": "Questions 11 to 16\nRead the following passage and then answer questions 11 to 16.",
  "type": "text",
  "text": "When the headteacher, Mr. Mutandi walked into our classroom carrying a book and two medium-sized sticks, the class went dead silent. We had never seen our headteacher walk around with sticks. Earlier in the day during the morning assembly, he had warned us against sneaking mobile phones into school. \"It is an offence for learners to have phones in school. Anybody found with one will face dire consequences,\" Mr. Mutandi had emphasised.\n\nWe were therefore worried when the headteacher came to class carrying the sticks. \"Who could be having a phone? When was he or she found? Where was the phone?\" These were the questions running through our minds. Mr. Mutandi placed the sticks on the table and opened the book. Mwajuma, one of the girls in the class swiftly stood up.\n\n\"Sir, please forgive the offender,\" she said. The headteacher looked surprised. \"What is it, Mwajuma? Who do I forgive?\" He inquired. \"The person who came with the phone,\" Mwajuma said in a trembling voice. \"Oh, did someone come to school with a phone? And after the warnings I gave?\" There was pin-drop silence in the room.\n\n\"Anyway, we will handle that after our lesson today. I am standing in for your Creative Arts teacher, Madam Sitati, who is unwell. And these two sticks will be used to **demonstrate** how we can make a sailing boat using material available in our immediate environment. Now get your exercise books out.\" We smiled at one another. All of us were ready for the lesson."
}

data["sharedContexts"]["ctx-eng-2025-q17-20"] = {
  "title": "Questions 17 to 20\nRead the following passage and then answer questions 17 to 20.",
  "type": "text",
  "text": "Four students, Sarah, Naipanoi, Mokua and Omar are working on a project. Apart from the fact that they are all curious, they have different personalities. Sarah and Mokua are both creative. They are different from Naipanoi who is organised, like Omar. Of the four students, Sarah and Omar find pleasure in helping others though Sarah is not relaxed like Omar. Mokua and Naipanoi are keen, while Omar is time-conscious just like Naipanoi. Despite their differences, the students understand the need to work together for the success of the project."
}

new_qs = [
  {
    "id": "q11", "questionNumber": 11,
    "questionText": "Why were the pupils worried when Mr. Mutandi walked into the class?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q11-16",
    "options": [
      {"text": "They feared the sizes of the sticks the headteacher had.", "isCorrect": False},
      {"text": "The headteacher had never been to their class with sticks.", "isCorrect": False},
      {"text": "They thought the headteacher had come to punish an offender.", "isCorrect": False},
      {"text": "The headteacher had just warned them during assembly.", "isCorrect": False}
    ]
  },
  {
    "id": "q12", "questionNumber": 12,
    "questionText": "Mwajuma can be said to be caring because she",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q11-16",
    "options": [
      {"text": "does not wish that someone is punished.", "isCorrect": False},
      {"text": "does not want the headteacher to be upset.", "isCorrect": False},
      {"text": "stands up when addressing the headteacher.", "isCorrect": False},
      {"text": "talks to the headteacher in a trembling voice.", "isCorrect": False}
    ]
  },
  {
    "id": "q13", "questionNumber": 13,
    "questionText": "What does the word '**demonstrate**' mean as used in the passage?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q11-16",
    "options": [
      {"text": "guide", "isCorrect": False},
      {"text": "plan", "isCorrect": False},
      {"text": "find", "isCorrect": False},
      {"text": "show", "isCorrect": False}
    ]
  },
  {
    "id": "q14", "questionNumber": 14,
    "questionText": "Which word **best** describes the feeling in the class at the end of the story?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q11-16",
    "options": [
      {"text": "Fear", "isCorrect": False},
      {"text": "Relief", "isCorrect": False},
      {"text": "Happiness", "isCorrect": False},
      {"text": "Confusion", "isCorrect": False}
    ]
  },
  {
    "id": "q15", "questionNumber": 15,
    "questionText": "According to the passage, it is **true** to say that",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q11-16",
    "options": [
      {"text": "some learners had mobile phones in the class.", "isCorrect": False},
      {"text": "Mr. Mutandi is a good Creative Arts teacher.", "isCorrect": False},
      {"text": "Mr. Mutandi always carried sticks for beating learners.", "isCorrect": False},
      {"text": "Mwajuma is the class prefect in charge of discipline.", "isCorrect": False}
    ]
  },
  {
    "id": "q16", "questionNumber": 16,
    "questionText": "Which one of the following **best** summarises the message of the story?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q11-16",
    "options": [
      {"text": "Hurry hurry has no blessing.", "isCorrect": False},
      {"text": "Do not put all your eggs in one basket.", "isCorrect": False},
      {"text": "Do not put the cart before the horse.", "isCorrect": False},
      {"text": "A stitch in time saves nine.", "isCorrect": False}
    ]
  },
  {
    "id": "q17", "questionNumber": 17,
    "questionText": "Part of the project required keenness and curiosity. Who are the **best** suited for this role?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q17-20",
    "options": [
      {"text": "Naipanoi and Omar.", "isCorrect": False},
      {"text": "Sarah and Naipanoi.", "isCorrect": False},
      {"text": "Omar and Mokua.", "isCorrect": False},
      {"text": "Mokua and Naipanoi.", "isCorrect": False}
    ]
  },
  {
    "id": "q18", "questionNumber": 18,
    "questionText": "Which student will be happy helping the group to keep time?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q17-20",
    "options": [
      {"text": "Omar", "isCorrect": False},
      {"text": "Naipanoi", "isCorrect": False},
      {"text": "Mokua", "isCorrect": False},
      {"text": "Sarah", "isCorrect": False}
    ]
  },
  {
    "id": "q19", "questionNumber": 19,
    "questionText": "Sarah and Mokua are **both**",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q17-20",
    "options": [
      {"text": "organised and keen.", "isCorrect": False},
      {"text": "helpful and organised.", "isCorrect": False},
      {"text": "creative and curious.", "isCorrect": False},
      {"text": "relaxed and time-conscious.", "isCorrect": False}
    ]
  },
  {
    "id": "q20", "questionNumber": 20,
    "questionText": "Which one of the following students has a personality that no other student has?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q17-20",
    "options": [
      {"text": "Sarah", "isCorrect": False},
      {"text": "Naipanoi", "isCorrect": False},
      {"text": "Omar", "isCorrect": False},
      {"text": "Mokua", "isCorrect": False}
    ]
  }
]

data["sectionA"].extend(new_qs)

with open("src/data/kjsea-english-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaEnglish2025 = {json.dumps(data, indent=2)};\n")
