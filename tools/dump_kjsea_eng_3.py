import json

with open("src/data/kjsea-english-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaEnglish2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

data["sharedContexts"]["ctx-eng-2025-q21-23"] = {
  "title": "Questions 21 to 23\nRead the following debate and then answer questions 21 to 23.",
  "type": "text",
  "text": "**Hon. Sapota:** Madam Speaker, I rise to support the motion. Indeed, social media has affected many people negatively. Look at the way some people right here are addicted to it. For instance, Honorable Mapinga gets so busy with his phone that he does not even have time to **visit the washroom**! This has affected...\n**Hon. Mapinga:** Objection, Madam Speaker!\n**Speaker:** What is it, Honourable Mapinga?\n**Hon. Mapinga:** This member is a liar.\n**Speaker:** You are out of order, Honourable Mapinga. You are using unacceptable language.\n**Hon. Mapinga:** **I beg your pardon**, Madam Speaker. What should I have said?\n**Speaker:** You should have said that the Honorable member is not truthful.\n**Hon. Sapota:** Thank you Madam Speaker, for saving me from being given a bad name."
}

data["sharedContexts"]["ctx-eng-2025-q26-35"] = {
  "title": "Questions 26 to 35\nRead the passage below and then answer questions 26 to 35.",
  "type": "text",
  "text": "Nobody enjoys waiting. You may be waiting for a friend, a colleague or a boss who is ----26---- for an appointment. You ----27---- as well be forced to idle in a waiting ----28---- for a bus or a flight that is behind schedule. ----29---- can be as upsetting to patients as being kept waiting for a doctor who turns ----30---- to be no show?\nTo ----31---- the anxiety associated with waiting, you are advised to carry a book with you ----32---- you go. ----33---- time spent on the waiting bench can be put to ----34---- use by reading a captivating novel or a motivational book. Waiting ----35---- not be a painful experience after all."
}

new_qs = [
  {
    "id": "q21", "questionNumber": 21,
    "questionText": "The **main** role of the speaker as shown in the debate is to",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q21-23",
    "options": [
      {"text": "teach members good behaviour.", "isCorrect": False},
      {"text": "decide who wins the debate.", "isCorrect": False},
      {"text": "maintain order during debates.", "isCorrect": False},
      {"text": "give members strong warnings.", "isCorrect": False}
    ]
  },
  {
    "id": "q22", "questionNumber": 22,
    "questionText": "Hon. Sapota uses the expression '**visit the washroom**' because she wants to",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q21-23",
    "options": [
      {"text": "be honest.", "isCorrect": False},
      {"text": "sound correct.", "isCorrect": False},
      {"text": "be clear.", "isCorrect": False},
      {"text": "sound polite.", "isCorrect": False}
    ]
  },
  {
    "id": "q23", "questionNumber": 23,
    "questionText": "Why does Hon. Mapinga tell the speaker, \"**I beg your pardon**\"? He wants the speaker to",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q21-23",
    "options": [
      {"text": "repeat what she had said.", "isCorrect": False},
      {"text": "forgive him.", "isCorrect": False},
      {"text": "correct him.", "isCorrect": False},
      {"text": "prove what she had said.", "isCorrect": False}
    ]
  },
  {
    "id": "q24", "questionNumber": 24,
    "questionText": "During a class discussion a student says something that you strongly disagree with. Which of the following statements would be the most appropriate to start your response?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "That argument is completely crazy.", "isCorrect": False},
      {"text": "I don't agree with that crazy argument.", "isCorrect": False},
      {"text": "I disagree with the argument.", "isCorrect": False},
      {"text": "Nobody can agree with that argument.", "isCorrect": False}
    ]
  },
  {
    "id": "q25", "questionNumber": 25,
    "questionText": "You have gone to a school for the first time and you want to go to the office. Which of the following is the **most** suitable way of asking for directions to the office?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Excuse me, can I know where the office is?", "isCorrect": False},
      {"text": "Excuse me, I beg to go to the office.", "isCorrect": False},
      {"text": "Excuse me, could you show me where the office is?", "isCorrect": False},
      {"text": "Excuse me, I want to go to the office.", "isCorrect": False}
    ]
  },
  {
    "id": "q26", "questionNumber": 26,
    "questionText": "Nobody enjoys waiting. You may be waiting for a friend, a colleague or a boss who is ----26---- for an appointment.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "absent", "isCorrect": False},
      {"text": "late", "isCorrect": False},
      {"text": "lost", "isCorrect": False},
      {"text": "called", "isCorrect": False}
    ]
  },
  {
    "id": "q27", "questionNumber": 27,
    "questionText": "You ----27---- as well be forced to idle in a waiting...",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "must", "isCorrect": False},
      {"text": "shall", "isCorrect": False},
      {"text": "should", "isCorrect": False},
      {"text": "could", "isCorrect": False}
    ]
  },
  {
    "id": "q28", "questionNumber": 28,
    "questionText": "...idle in a waiting ----28---- for a bus or a flight...",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "area", "isCorrect": False},
      {"text": "time", "isCorrect": False},
      {"text": "class", "isCorrect": False},
      {"text": "process", "isCorrect": False}
    ]
  },
  {
    "id": "q29", "questionNumber": 29,
    "questionText": "----29---- can be as upsetting to patients...",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "Who", "isCorrect": False},
      {"text": "Which", "isCorrect": False},
      {"text": "What", "isCorrect": False},
      {"text": "Where", "isCorrect": False}
    ]
  }
]

data["sectionA"].extend(new_qs)

with open("src/data/kjsea-english-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaEnglish2025 = {json.dumps(data, indent=2)};\n")
