import json
import os

data = {
  "id": "kjsea-english-2025",
  "title": "KJSEA 2025 English Language",
  "subject": "English",
  "year": "2025",
  "durationMinutes": 120,
  "timeAllowed": 120,
  "sharedContexts": {
    "ctx-eng-2025-q1-5": {
      "title": "Questions 1 to 5\nRead the following passage and then answer questions 1 to 5.",
      "type": "text",
      "text": "Many people do not have enough time to rest adequately. However, it is important to prioritise rest and quality sleep every day. Rest and sleep are two different things, but both are equally important for our mental, emotional and physical health. Actually, prioritising rest can improve one's quality of sleep.\n\nRest can be difficult to define because it can mean different things to different people. It can be active, such as going for a walk outside, or passive, such as taking a moment to sit down and breathe deeply. Regardless of how you choose to rest, these actions can help you recover and recharge from physical and mental effort. That is why quality rest is linked to improved physical and mental health.\n\nSleep on the other hand is a state in which individuals are mentally detached from their surroundings. It is an essential part of the body's well being. Quality sleep can help us to reset, recover and recharge our bodies. Unlike rest, sleep is something the body cannot function without. In fact, if you are deprived of sleep, your body will force you to sleep, no matter what you are in the middle of doing."
    },
    "ctx-eng-2025-q6-10": {
      "title": "Questions 6 to 10\nRead the following passage and then answer questions 6 to 10.",
      "type": "text",
      "text": "Laughter is normally an expression of happiness. This is probably because when we laugh, our faces brighten up. We generally laugh when we are amused. When we hear a joke, the natural response is to let out a laugh. However, not all people laugh at the same things. What one person finds amusing may be ordinary or even unpleasant to another.\n\nLaughter is not always a sign of delight. Most of us have, without doubt, seen people laughing when there is nothing really funny. Such laughter could be out of nervousness or even politeness. A saying goes, “A rich man's joke is always funny”. This means people are expected to laugh when a person of high status cracks a joke, however flat. Sometimes people laugh to mock others with the intention of making the victim feel bad. Such **derisive** laughter is unfortunate. Genuine laughter is thought to be healthy. No wonder, someone said that **laughter is the best medicine**."
    }
  },
  "sectionA": [
    {
      "id": "q1", "questionNumber": 1,
      "questionText": "According to the passage, passive rest involves",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q1-5",
      "options": [
        {"text": "little movement of the body.", "isCorrect": False},
        {"text": "going to a place nearby.", "isCorrect": False},
        {"text": "taking a short break.", "isCorrect": False},
        {"text": "indoor activities.", "isCorrect": False}
      ]
    },
    {
      "id": "q2", "questionNumber": 2,
      "questionText": "Which one of the following statements is **true** about sleep according to the passage? It",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q1-5",
      "options": [
        {"text": "cannot be defined.", "isCorrect": False},
        {"text": "improves the quality of rest.", "isCorrect": False},
        {"text": "cannot be avoided.", "isCorrect": False},
        {"text": "helps one to recover time.", "isCorrect": False}
      ]
    },
    {
      "id": "q3", "questionNumber": 3,
      "questionText": "The last sentence in the passage suggests that",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q1-5",
      "options": [
        {"text": "sleep comes when it is not wanted.", "isCorrect": False},
        {"text": "one can fall asleep while in action.", "isCorrect": False},
        {"text": "no activity is more important than sleep.", "isCorrect": False},
        {"text": "sleep cannot be forced.", "isCorrect": False}
      ]
    },
    {
      "id": "q4", "questionNumber": 4,
      "questionText": "The following statements are true according to the passage **except** that",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q1-5",
      "options": [
        {"text": "rest can remove us from our surrounding.", "isCorrect": False},
        {"text": "physical and mental energy can be regained.", "isCorrect": False},
        {"text": "adequate rest may not be common nowadays.", "isCorrect": False},
        {"text": "rest and sleep are not the same thing.", "isCorrect": False}
      ]
    },
    {
      "id": "q5", "questionNumber": 5,
      "questionText": "Which one of the following sayings **best** reflects the message in the passage?",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q1-5",
      "options": [
        {"text": "Prevention is better than cure.", "isCorrect": False},
        {"text": "Let the sleeping dogs lie.", "isCorrect": False},
        {"text": "All work and no play makes Jack a dull boy.", "isCorrect": False},
        {"text": "If you make a bed, you must lie on it.", "isCorrect": False}
      ]
    },
    {
      "id": "q6", "questionNumber": 6,
      "questionText": "Laughter is not always a sign of delight because",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q6-10",
      "options": [
        {"text": "some people make flat jokes.", "isCorrect": False},
        {"text": "there are other reasons why some people may laugh.", "isCorrect": False},
        {"text": "there are other ways of showing that one is happy.", "isCorrect": False},
        {"text": "some people doubt what others say.", "isCorrect": False}
      ]
    },
    {
      "id": "q7", "questionNumber": 7,
      "questionText": "The word '**derisive**' means the same as",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q6-10",
      "options": [
        {"text": "insulting.", "isCorrect": False},
        {"text": "funny.", "isCorrect": False},
        {"text": "crazy.", "isCorrect": False},
        {"text": "interesting.", "isCorrect": False}
      ]
    },
    {
      "id": "q8", "questionNumber": 8,
      "questionText": "From the passage we can conclude that some people like to",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q6-10",
      "options": [
        {"text": "please the rich.", "isCorrect": False},
        {"text": "obey the rich.", "isCorrect": False},
        {"text": "admire the rich.", "isCorrect": False},
        {"text": "praise the rich.", "isCorrect": False}
      ]
    },
    {
      "id": "q9", "questionNumber": 9,
      "questionText": "The expression '**laughter is the best medicine**' means that",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q6-10",
      "options": [
        {"text": "laughing protects us from being sick.", "isCorrect": False},
        {"text": "there is no medicine as good as laughter.", "isCorrect": False},
        {"text": "genuine laughter gives us a feeling of well-being.", "isCorrect": False},
        {"text": "there is no need to take medicine when we can laugh.", "isCorrect": False}
      ]
    },
    {
      "id": "q10", "questionNumber": 10,
      "questionText": "What does the writer of the passage intend to achieve? To",
      "questionType": "multiple-choice", "contextRef": "ctx-eng-2025-q6-10",
      "options": [
        {"text": "explain why people should make good use of laughter.", "isCorrect": False},
        {"text": "describe how people laugh during various occasions.", "isCorrect": False},
        {"text": "encourage the readers to laugh all the time.", "isCorrect": False},
        {"text": "motivate people to think first before they laugh.", "isCorrect": False}
      ]
    }
  ]
}

js_content = f"export const kjseaEnglish2025 = {json.dumps(data, indent=2)};"

with open("src/data/kjsea-english-2025.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Created src/data/kjsea-english-2025.js")
