import json
import os
import shutil

section_a_data = {
  "id": "kjsea-cre-sectiona-2025",
  "title": "KJSEA 2025 Christian Religious Education (Section A)",
  "subject": "Christian Religious Education (Section A)",
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "There are many benefits of learning Christian Religious Education in school today. Which of the following is one of the benefits?",
      "options": [
        { "text": "It helps learners to know their church leaders.", "isCorrect": False },
        { "text": "It makes parents buy CRE textbooks for learners.", "isCorrect": False },
        { "text": "It helps learners to grow spiritually.", "isCorrect": True },
        { "text": "It makes the parents of the learners happy.", "isCorrect": False }
      ],
      "explanation": "Learning CRE equips learners with moral values and spiritual guidance, helping them to grow spiritually. It is not merely about knowing church leaders or making parents happy."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "You read the Bible on the two accounts of creation in Genesis 1 and 2 and noted that they have similarities. One of the similarities is that",
      "options": [
        { "text": "God gave human beings duties to perform", "isCorrect": True },
        { "text": "God chased human beings out of the Garden of Eden", "isCorrect": False },
        { "text": "human beings gave names to all the animals", "isCorrect": False },
        { "text": "human beings made clothes for themselves.", "isCorrect": False }
      ],
      "explanation": "In both Genesis 1 and 2, God gave humans duties. In Genesis 1:28, they are told to rule over the earth, and in Genesis 2:15, man is put in the garden to work it and take care of it."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "One way in which God showed his love for Adam and Eve after they ate the fruit from the tree in the middle of the garden was by",
      "options": [
        { "text": "cursing the snake in the garden", "isCorrect": False },
        { "text": "putting a Cherubim to protect the garden", "isCorrect": False },
        { "text": "giving man power to rule over the woman", "isCorrect": False },
        { "text": "looking for them in the garden.", "isCorrect": True }
      ],
      "explanation": "Despite their disobedience, God went looking for Adam and Eve in the garden (Genesis 3:8-9), showing His continuous love and care for humanity even in sin."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "A resource person gave a talk to Grade 7 learners on ways of maintaining a healthy environment in the school. Which of the following is the best way to demonstrate what was learnt from the talk?",
      "options": [
        { "text": "Reporting those who throw waste paper carelessly.", "isCorrect": False },
        { "text": "Collecting litter in the compound every day.", "isCorrect": True },
        { "text": "Reminding the classmates to take their cleaning duties seriously.", "isCorrect": False },
        { "text": "Avoiding stepping on the grass in the school compound.", "isCorrect": False }
      ],
      "explanation": "Demonstrating what was learnt implies taking practical action. Collecting litter actively contributes to maintaining a healthy environment, rather than just reporting others or talking about it."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "The Bible has been translated into many languages from its original language. What was the original language of the Old testament?",
      "options": [
        { "text": "Hebrew", "isCorrect": True },
        { "text": "Latin", "isCorrect": False },
        { "text": "English", "isCorrect": False },
        { "text": "Greek", "isCorrect": False }
      ],
      "explanation": "The Old Testament was originally written predominantly in Hebrew (with a few portions in Aramaic). The New Testament was originally written in Greek."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "The following are ways in which Christians can make good use of the Bible except to",
      "options": [
        { "text": "accumulate riches", "isCorrect": True },
        { "text": "live a Christian life", "isCorrect": False },
        { "text": "guide new converts", "isCorrect": False },
        { "text": "form new churches.", "isCorrect": False }
      ],
      "explanation": "The Bible is intended for spiritual guidance, living a godly life, evangelism, and doctrine. It is not intended to be used as a means to accumulate material wealth."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "A lesson that Christians learn from the leadership of Deborah as a Judge in Israel is that they should",
      "options": [
        { "text": "fight their enemies", "isCorrect": False },
        { "text": "be courageous in their undertakings", "isCorrect": True },
        { "text": "make themselves famous", "isCorrect": False },
        { "text": "reward the people who work hard.", "isCorrect": False }
      ],
      "explanation": "Deborah demonstrated immense courage and faith in God when she commanded Barak to fight the Canaanites and even accompanied him to the battlefield."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "King Solomon was a great leader in Israel. However, God was displeased with him towards the end of his rule. The main reason for this was because he",
      "options": [
        { "text": "built his own palace for 13 years", "isCorrect": False },
        { "text": "allowed the worship of foreign gods in Israel", "isCorrect": True },
        { "text": "sold part of Israel's land to settle his debts", "isCorrect": False },
        { "text": "introduced forced labour in Israel.", "isCorrect": False }
      ],
      "explanation": "God was most displeased with Solomon because his many foreign wives led him to turn away from God and allow idolatry (the worship of foreign gods) in Israel."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "Jesus used the parable of the lost sheep to teach his audience. The main lesson that Christians learn from this parable is to",
      "options": [
        { "text": "take good care of their God-given property", "isCorrect": False },
        { "text": "seek the people lost in sin", "isCorrect": True },
        { "text": "employ good servants to care for their sheep", "isCorrect": False },
        { "text": "avoid keeping many sheep.", "isCorrect": False }
      ],
      "explanation": "The Parable of the Lost Sheep teaches about God's great love for sinners and the joy in heaven over one sinner who repents, encouraging Christians to seek out those lost in sin."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "During his earthly ministry, Jesus performed many miracles. Which of the following miracles teaches Christians to be thankful?",
      "options": [
        { "text": "Healing of the ten lepers.", "isCorrect": True },
        { "text": "Feeding of the five thousand.", "isCorrect": False },
        { "text": "Raising of Lazarus to life.", "isCorrect": False },
        { "text": "Calming of the storm.", "isCorrect": False }
      ],
      "explanation": "In the healing of the ten lepers, only one returned to give thanks to Jesus. This miracle emphasizes the importance of gratitude and thankfulness to God."
    },
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "After Jesus entered Jerusalem, he went to the temple and cleansed it because",
      "options": [
        { "text": "he was requested by the religious leaders to do so", "isCorrect": False },
        { "text": "people had stopped cleaning the temple", "isCorrect": False },
        { "text": "it was being misused by the people", "isCorrect": True },
        { "text": "he was requested by his followers to do so.", "isCorrect": False }
      ],
      "explanation": "Jesus cleansed the temple because merchants and money changers were misusing it, turning a 'house of prayer' into a 'den of thieves'."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "\"This is my body which is given for you\" (Luke 22:19). When did Jesus speak these words to his disciples?",
      "options": [
        { "text": "When he was praying on Mount Olives.", "isCorrect": False },
        { "text": "During his crucifixion.", "isCorrect": False },
        { "text": "When he was in the house of Zaccheaus.", "isCorrect": False },
        { "text": "During the Last Supper.", "isCorrect": True }
      ],
      "explanation": "Jesus spoke these words during the Last Supper when He instituted the Holy Communion, breaking bread and sharing it with His disciples."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "According to the teachings of Jesus on prayer, Christians learn that they should",
      "options": [
        { "text": "pray on mountains", "isCorrect": False },
        { "text": "make long prayers daily", "isCorrect": False },
        { "text": "have faith when praying", "isCorrect": True },
        { "text": "pray in a loud voice.", "isCorrect": False }
      ],
      "explanation": "Jesus emphasized having faith, sincerity, and praying in secret rather than making long, showy prayers or simply praying loudly on mountains."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "Who among the following apostles of the Early Church healed a lame man at the Beautiful Gate of the temple?",
      "options": [
        { "text": "James", "isCorrect": False },
        { "text": "Peter", "isCorrect": True },
        { "text": "Andrew", "isCorrect": False },
        { "text": "Philip", "isCorrect": False }
      ],
      "explanation": "Peter (along with John) healed the lame man at the Beautiful Gate, telling him 'Silver or gold I do not have, but what I do have I give you. In the name of Jesus Christ of Nazareth, walk' (Acts 3:6)."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "You are asked to use examples to show the differences between the gifts and fruits of the Holy Spirit. Select the option that only contains the gifts of the Holy Spirit.",
      "options": [
        { "text": "Peace, Self-control", "isCorrect": False },
        { "text": "Knowledge, Wisdom", "isCorrect": True },
        { "text": "Patience, Prophecy", "isCorrect": False },
        { "text": "Healing, Goodness", "isCorrect": False }
      ],
      "explanation": "Knowledge and Wisdom are gifts of the Holy Spirit (1 Corinthians 12:8). Peace, self-control, patience, and goodness are fruits of the Holy Spirit (Galatians 5:22-23)."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "Grade 9 learners discussed the consequences of early marriage. One of the consequences likely to have been discussed is that it",
      "options": [
        { "text": "reduces wealth for the man's family", "isCorrect": False },
        { "text": "prevents cases of single parenthood", "isCorrect": False },
        { "text": "expands family relationships", "isCorrect": False },
        { "text": "increases chances of school drop outs.", "isCorrect": True }
      ],
      "explanation": "Early marriage typically interrupts a child's education, significantly increasing the likelihood that they will drop out of school."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "You attended a church service where the sermon was on the story of Paul and Silas in jail. From the sermon, what is the main lesson you learnt as a Christian?",
      "options": [
        { "text": "To cast out evil spirits from people.", "isCorrect": False },
        { "text": "To speak the truth at all times.", "isCorrect": False },
        { "text": "To endure suffering for the sake of Christ.", "isCorrect": True },
        { "text": "To cooperate with others in serving God.", "isCorrect": False }
      ],
      "explanation": "Paul and Silas praised God while in chains, teaching Christians to patiently endure suffering and remain faithful during trials for the sake of Christ."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "You conducted a library search on healthy family relationships. Which of the following is the best practice to observe to maintain a healthy Christian family?",
      "options": [
        { "text": "Solving conflicts peacefully.", "isCorrect": True },
        { "text": "Family members working to get wealth.", "isCorrect": False },
        { "text": "Taking children to school.", "isCorrect": False },
        { "text": "Buying food for the family.", "isCorrect": False }
      ],
      "explanation": "While providing basics like food and education is important, maintaining healthy relationships relies heavily on peaceful conflict resolution, love, and understanding within the family."
    },
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "There are many leisure activities that individuals engage in today. Which of the following leisure activities is common in both the Christian and secular world?",
      "options": [
        { "text": "Gambling", "isCorrect": False },
        { "text": "Prayer retreats", "isCorrect": False },
        { "text": "Sports", "isCorrect": True },
        { "text": "Attending discos", "isCorrect": False }
      ],
      "explanation": "Sports is a healthy leisure activity commonly enjoyed by both Christians and non-Christians alike. Gambling and discos are generally discouraged for Christians, and prayer retreats are primarily a Christian activity."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "Your class brainstormed on the electronic gadgets that are found both at home and in school. From the gadgets they mentioned, select one that is most suitable for learning CRE at home.",
      "options": [
        { "text": "Microphone.", "isCorrect": False },
        { "text": "Projector.", "isCorrect": False },
        { "text": "Amplifier.", "isCorrect": False },
        { "text": "Mobile phone.", "isCorrect": True }
      ],
      "explanation": "A mobile phone (smartphone) can access digital Bibles, CRE apps, educational videos, and e-learning resources, making it the most suitable gadget among the options for learning at home."
    }
  ],
  "sectionB": [],
  "sharedContexts": {}
}

section_b_data = {
  "id": "kjsea-cre-sectionb-2025",
  "title": "KJSEA 2025 Christian Religious Education (Section B)",
  "subject": "Christian Religious Education (Section B)",
  "sectionA": [],
  "sectionB": [
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "After Adam and Eve disobeyed God in the Garden of Eden, it led to serious consequences. State any five of those consequences.",
      "questionType": "structured",
      "maxScore": 5,
      "modelAnswer": "1. They were chased out of the Garden of Eden.\n2. The woman would experience pain in childbirth.\n3. The man would have to toil and sweat to get food from the ground.\n4. The snake was cursed to crawl on its belly.\n5. Enmity was established between the woman's offspring and the snake.\n6. Death was introduced (they became mortal/would return to dust).",
      "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct consequence stated (Max 5 marks).\n* **Flexibility:** Accept any accurately paraphrased consequences from Genesis 3."
    },
    {
      "id": "q22",
      "questionNumber": 22,
      "parentQuestionText": "God provided human beings with various natural resources. However, these resources are being misused.",
      "subQuestions": [
        {
          "id": "q22a",
          "subNumber": "(a)",
          "questionText": "Outline five ways in which natural resources are misused in Kenya today.",
          "questionType": "structured",
          "maxScore": 5,
          "modelAnswer": "1. Deforestation / cutting down trees without replacing them.\n2. Pollution of water bodies (e.g., releasing industrial waste into rivers).\n3. Overfishing or poaching of wildlife.\n4. Poor farming methods leading to soil erosion.\n5. Illegal mining and unregulated sand harvesting.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct way outlined (Max 5 marks).\n* **Flexibility:** Accept any reasonable and valid way natural resources are misused in Kenya."
        },
        {
          "id": "q22b",
          "subNumber": "(b)",
          "questionText": "In groups, you discussed the effects of misusing natural resources. State five effects of misusing natural resources.",
          "questionType": "structured",
          "maxScore": 5,
          "modelAnswer": "1. Soil erosion and loss of soil fertility.\n2. Drought and famine due to unpredictable weather patterns.\n3. Death of aquatic life and terrestrial animals.\n4. Global warming and climate change.\n5. Shortage of clean water.",
          "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correct effect stated (Max 5 marks).\n* **Flexibility:** Accept any valid environmental, economic, or health effects caused by misuse of resources."
        }
      ]
    }
  ],
  "sharedContexts": {}
}

import os
os.makedirs('public/data', exist_ok=True)
os.makedirs('electron/app/data', exist_ok=True)

with open('public/data/kjsea-cre-sectiona-2025.json', 'w', encoding='utf-8') as f:
    json.dump(section_a_data, f, indent=2, ensure_ascii=False)
with open('public/data/kjsea-cre-sectionb-2025.json', 'w', encoding='utf-8') as f:
    json.dump(section_b_data, f, indent=2, ensure_ascii=False)

shutil.copy('public/data/kjsea-cre-sectiona-2025.json', 'electron/app/data/kjsea-cre-sectiona-2025.json')
shutil.copy('public/data/kjsea-cre-sectionb-2025.json', 'electron/app/data/kjsea-cre-sectionb-2025.json')
print('Successfully generated CRE Batch 1 JSON files.')
