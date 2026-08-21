import json
import os
import shutil

filepath = 'public/data/kjsea-cre-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_questions = [
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "Grade 7 learners were tasked to classify the books of the Old Testament and make presentations. State five poetic books that they identified.",
      "questionType": "structured",
      "maxScore": 5,
      "modelAnswer": "1. Job\n2. Psalms\n3. Proverbs\n4. Ecclesiastes\n5. Song of Solomon (or Song of Songs)",
      "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correctly identified poetic book (Max 5 marks)."
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "The Bible has been translated into many local African languages. State five effects of these translations.",
      "questionType": "structured",
      "maxScore": 5,
      "modelAnswer": "1. It has enabled more people to read and understand the word of God.\n2. It led to the spread of Christianity and expansion of the Church in Africa.\n3. It promoted the development of local languages (reading and writing).\n4. It led to the establishment of schools/formal education.\n5. It led to the emergence of independent churches.\n6. It allowed Africans to participate actively in evangelism and church leadership.",
      "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct effect stated (Max 5 marks)."
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "King David was a leader in Israel with exemplary leadership qualities that should be emulated by political leaders today. State any five of these qualities.",
      "questionType": "structured",
      "maxScore": 5,
      "modelAnswer": "1. Courageous/Brave.\n2. God-fearing / Prayerful.\n3. Repentant / Humble.\n4. Just / Fair.\n5. Wise.\n6. Merciful / Forgiving.",
      "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct leadership quality (Max 5 marks)."
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "parentQuestionText": "Parents play different roles in the lives of their children.",
      "subQuestions": [
        {
          "id": "q29a",
          "subNumber": "(a)",
          "questionText": "Identify any five roles played by Christian parents in the lives of their children.",
          "questionType": "structured",
          "maxScore": 5,
          "modelAnswer": "1. Providing basic needs (food, shelter, clothing).\n2. Teaching children the word of God / Christian values.\n3. Praying for and with their children.\n4. Taking children to church / for baptism.\n5. Disciplining and correcting children lovingly.\n6. Acting as positive role models.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct role identified (Max 5 marks)."
        },
        {
          "id": "q29b",
          "subNumber": "(b)",
          "questionText": "A resource person talked to your class about the factors contributing to teenage pregnancies in Kenya today. State five factors that the resource person must have talked about.",
          "questionType": "structured",
          "maxScore": 5,
          "modelAnswer": "1. Peer pressure.\n2. Drug and substance abuse.\n3. Poverty.\n4. Lack of parental guidance / parental negligence.\n5. Negative influence from mass media / internet.\n6. Idleness / Lack of constructive leisure activities.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct factor stated (Max 5 marks)."
        }
      ]
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "parentQuestionText": "Issues regarding youth and society.",
      "subQuestions": [
        {
          "id": "q30a",
          "subNumber": "(a)",
          "questionText": "A pastor from your church has requested you to talk to the youth on how to use their leisure time constructively. State five leisure activities you would encourage the youths to participate in.",
          "questionType": "structured",
          "maxScore": 5,
          "modelAnswer": "1. Reading the Bible / Christian literature.\n2. Participating in church choir / youth groups.\n3. Engaging in sports and games.\n4. Doing community service / helping the needy.\n5. Visiting the sick or elderly.\n6. Attending Christian camps / seminars.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct constructive leisure activity (Max 5 marks)."
        },
        {
          "id": "q30b",
          "subNumber": "(b)",
          "questionText": "There is great concern in Kenya today that some school-going children abuse drugs and substances. Outline any five effects of drug and substance abuse on such children.",
          "questionType": "structured",
          "maxScore": 5,
          "modelAnswer": "1. Poor academic performance / dropping out of school.\n2. Health problems / mental disorders.\n3. Indiscipline / rebellious behavior.\n4. Engaging in criminal activities (e.g., stealing to fund the habit).\n5. Strained relationships with parents and teachers.\n6. Risk of contracting HIV/AIDS (due to shared needles or reckless behavior).",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct effect outlined (Max 5 marks)."
        }
      ]
    }
]

data['sectionB'].extend(new_questions)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-cre-sectionb-2025.json')
print('Successfully appended CRE Batch 2 JSON files.')
