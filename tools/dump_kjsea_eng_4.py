import json
import re

with open("src/data/kjsea-english-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaEnglish2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

data["sharedContexts"]["ctx-eng-2025-q36-42"] = {
  "title": "Questions 36 to 42\nFor questions 36 to 42, select the best alternative to complete the sentence.",
  "type": "text",
  "text": ""
}

data["sharedContexts"]["ctx-eng-2025-q44"] = {
  "title": "Question 44\nChoose the alternative that best replaces the underlined words.",
  "type": "text",
  "text": ""
}

data["sharedContexts"]["ctx-eng-2025-q45-48"] = {
  "title": "Questions 45 to 48\nFor questions 45 to 48, choose the alternative that means the same as the underlined sentence.",
  "type": "text",
  "text": ""
}

new_qs = [
  {
    "id": "q30", "questionNumber": 30,
    "questionText": "...a doctor who turns ----30---- to be no show?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "up", "isCorrect": False},
      {"text": "off", "isCorrect": False},
      {"text": "on", "isCorrect": False},
      {"text": "out", "isCorrect": False}
    ]
  },
  {
    "id": "q31", "questionNumber": 31,
    "questionText": "To ----31---- the anxiety associated with waiting...",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "discourage", "isCorrect": False},
      {"text": "spoil", "isCorrect": False},
      {"text": "finish", "isCorrect": False},
      {"text": "reduce", "isCorrect": False}
    ]
  },
  {
    "id": "q32", "questionNumber": 32,
    "questionText": "...advised to carry a book with you ----32---- you go.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "wherever", "isCorrect": False},
      {"text": "since", "isCorrect": False},
      {"text": "unless", "isCorrect": False},
      {"text": "whenever", "isCorrect": False}
    ]
  },
  {
    "id": "q33", "questionNumber": 33,
    "questionText": "----33---- time spent on the waiting bench can be put to...",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "All", "isCorrect": False},
      {"text": "A", "isCorrect": False},
      {"text": "The", "isCorrect": False},
      {"text": "No", "isCorrect": False}
    ]
  },
  {
    "id": "q34", "questionNumber": 34,
    "questionText": "...can be put to ----34---- use by reading a captivating novel...",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "best", "isCorrect": False},
      {"text": "good", "isCorrect": False},
      {"text": "well", "isCorrect": False},
      {"text": "more", "isCorrect": False}
    ]
  },
  {
    "id": "q35", "questionNumber": 35,
    "questionText": "Waiting ----35---- not be a painful experience after all.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q26-35",
    "options": [
      {"text": "need", "isCorrect": False},
      {"text": "can", "isCorrect": False},
      {"text": "may", "isCorrect": False},
      {"text": "could", "isCorrect": False}
    ]
  },
  {
    "id": "q36", "questionNumber": 36,
    "questionText": "Makau has two beautiful ____________.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q36-42",
    "options": [
      {"text": "sisters-in-laws", "isCorrect": False},
      {"text": "sister-in-laws", "isCorrect": False},
      {"text": "sisters-in-law", "isCorrect": False},
      {"text": "sister-in-law", "isCorrect": False}
    ]
  },
  {
    "id": "q37", "questionNumber": 37,
    "questionText": "____________ the comedian's jokes were extremely funny, few of us laughed.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q36-42",
    "options": [
      {"text": "As", "isCorrect": False},
      {"text": "Unless", "isCorrect": False},
      {"text": "Since", "isCorrect": False},
      {"text": "Though", "isCorrect": False}
    ]
  },
  {
    "id": "q38", "questionNumber": 38,
    "questionText": "During the nutrition lesson, we watched a ____________ preparing delicious chapati on television.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q36-42",
    "options": [
      {"text": "cook", "isCorrect": False},
      {"text": "cooker", "isCorrect": False},
      {"text": "cookery", "isCorrect": False},
      {"text": "cooking", "isCorrect": False}
    ]
  },
  {
    "id": "q39", "questionNumber": 39,
    "questionText": "Mariam and Kemboi have been good friends since Grade 6 and they get ____________ really well.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q36-42",
    "options": [
      {"text": "across", "isCorrect": False},
      {"text": "along", "isCorrect": False},
      {"text": "about", "isCorrect": False},
      {"text": "around", "isCorrect": False}
    ]
  },
  {
    "id": "q40", "questionNumber": 40,
    "questionText": "My aunt says that we should ____________ disrespect ____________ shout at people.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q36-42",
    "options": [
      {"text": "both, or", "isCorrect": False},
      {"text": "not only, but also", "isCorrect": False},
      {"text": "neither, nor", "isCorrect": False},
      {"text": "either, or", "isCorrect": False}
    ]
  },
  {
    "id": "q41", "questionNumber": 41,
    "questionText": "The girl ____________ I told you about is very friendly.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q36-42",
    "options": [
      {"text": "which", "isCorrect": False},
      {"text": "whose", "isCorrect": False},
      {"text": "whom", "isCorrect": False},
      {"text": "who", "isCorrect": False}
    ]
  },
  {
    "id": "q42", "questionNumber": 42,
    "questionText": "Which one of these five books do you like ____________?",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q36-42",
    "options": [
      {"text": "most", "isCorrect": False},
      {"text": "better", "isCorrect": False},
      {"text": "more", "isCorrect": False},
      {"text": "less", "isCorrect": False}
    ]
  },
  {
    "id": "q43", "questionNumber": 43,
    "questionText": "Red Cross officials met the <u>needy</u> families. The **opposite** of the underlined word is",
    "questionType": "multiple-choice",
    "options": [
      {"text": "poor", "isCorrect": False},
      {"text": "hungry", "isCorrect": False},
      {"text": "affected", "isCorrect": False},
      {"text": "wealthy", "isCorrect": False}
    ]
  },
  {
    "id": "q44", "questionNumber": 44,
    "questionText": "The teacher asked the students if <u>the students</u> had submitted <u>the students'</u> projects.",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q44",
    "options": [
      {"text": "they, our", "isCorrect": False},
      {"text": "we, our", "isCorrect": False},
      {"text": "they, their", "isCorrect": False},
      {"text": "we, their", "isCorrect": False}
    ]
  },
  {
    "id": "q45", "questionNumber": 45,
    "questionText": "<u>The school bus was repaired by the mechanic.</u>",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q45-48",
    "options": [
      {"text": "The mechanic repaired the school bus.", "isCorrect": False},
      {"text": "The mechanic is repairing the school bus.", "isCorrect": False},
      {"text": "The mechanic has been repairing the school bus.", "isCorrect": False},
      {"text": "The mechanic was repairing the school bus.", "isCorrect": False}
    ]
  },
  {
    "id": "q46", "questionNumber": 46,
    "questionText": "<u>Monica said, \"I work here every day.\"</u>",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q45-48",
    "options": [
      {"text": "Monica said that she worked here every day.", "isCorrect": False},
      {"text": "Monica said that she worked there every day.", "isCorrect": False},
      {"text": "Monica said that she works here every day.", "isCorrect": False},
      {"text": "Monica said that she works there every day.", "isCorrect": False}
    ]
  },
  {
    "id": "q47", "questionNumber": 47,
    "questionText": "<u>I can hardly wait to hear the story.</u>",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q45-48",
    "options": [
      {"text": "I am not interested in listening to the story.", "isCorrect": False},
      {"text": "I am eager to listen to the story.", "isCorrect": False},
      {"text": "I am able to listen to the story.", "isCorrect": False},
      {"text": "I am not waiting to listen to the story.", "isCorrect": False}
    ]
  },
  {
    "id": "q48", "questionNumber": 48,
    "questionText": "<u>If it rains, we will not come.</u>",
    "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q45-48",
    "options": [
      {"text": "Unless it rains, we will come.", "isCorrect": False},
      {"text": "Unless it rains, we will not come.", "isCorrect": False},
      {"text": "Unless it does not rain, we will come.", "isCorrect": False},
      {"text": "Unless it does not rain, we will not come.", "isCorrect": False}
    ]
  },
  {
    "id": "q49", "questionNumber": 49,
    "questionText": "Which one of the following sentences is **correctly** punctuated?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "What? A beautiful place this is!", "isCorrect": False},
      {"text": "What! A beautiful place this is?", "isCorrect": False},
      {"text": "What a beautiful place this is!", "isCorrect": False},
      {"text": "What a beautiful place this is?", "isCorrect": False}
    ]
  },
  {
    "id": "q50", "questionNumber": 50,
    "questionText": "We can always **bank on** our new governor. This means that the new governor is",
    "questionType": "multiple-choice",
    "options": [
      {"text": "wise.", "isCorrect": False},
      {"text": "strong.", "isCorrect": False},
      {"text": "healthy.", "isCorrect": False},
      {"text": "reliable.", "isCorrect": False}
    ]
  }
]

data["sectionA"].extend(new_qs)

with open("src/data/kjsea-english-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaEnglish2025 = {json.dumps(data, indent=2)};\n")
