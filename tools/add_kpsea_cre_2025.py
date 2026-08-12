import json

paper_structure = {
  "id": "kpsea-sst-cre-2025",
  "title": "KPSEA 2025 Social Studies & Creative Arts (CRE)",
  "subject": "CRE",
  "year": "2025",
  "isSubPaper": True,
  "durationMinutes": 0,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "Children participate in different activities at home. Which of the following activities is likely to promote unity in the family?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Visiting friends in their homes.", "isCorrect": False },
        { "text": "Watching television with their classmates.", "isCorrect": False },
        { "text": "Looking after younger brothers or sisters.", "isCorrect": True },
        { "text": "Playing games with their friends.", "isCorrect": False }
      ],
      "explanation": "Looking after younger siblings involves taking responsibility within the family and working together, which promotes family unity."
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "You read a story in the Bible in which Samson defeated the Philistines using a donkey's jawbone. What made Samson to defeat the Philistines?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "The power of God was upon him.", "isCorrect": True },
        { "text": "He was a skilled fighter.", "isCorrect": False },
        { "text": "He had a strong army.", "isCorrect": False },
        { "text": "His enemies did not resist him.", "isCorrect": False }
      ],
      "explanation": "Samson's incredible strength to defeat the Philistines came directly from the Spirit and power of God being upon him."
    },
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "You read the Bible about King Belshazzar's party and the strange writing on the wall. Who among the following prophets interpreted the writing on the wall for the King?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Elijah", "isCorrect": False },
        { "text": "Isaiah", "isCorrect": False },
        { "text": "Jeremiah", "isCorrect": False },
        { "text": "Daniel", "isCorrect": True }
      ],
      "explanation": "Prophet Daniel was the one who was called and successfully interpreted the writing on the wall for King Belshazzar (Daniel 5)."
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "The raising of Lazarus from the dead was one of the miracles that Jesus performed. Why did Jesus perform this miracle? To",
      "questionType": "multiple-choice",
      "options": [
        { "text": "comfort mourners", "isCorrect": False },
        { "text": "reveal the glory of God", "isCorrect": True },
        { "text": "please Mary and Martha", "isCorrect": False },
        { "text": "show that he loved Lazarus.", "isCorrect": False }
      ],
      "explanation": "Jesus stated that Lazarus's sickness was not unto death, but for the glory of God, so that the Son of God might be glorified through it (John 11:4)."
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "A christian value that learners acquire from the miracle in which Jesus healed the ten lepers is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "unity", "isCorrect": False },
        { "text": "faithfulness", "isCorrect": False },
        { "text": "thankfulness", "isCorrect": True },
        { "text": "self-control.", "isCorrect": False }
      ],
      "explanation": "Only one of the ten healed lepers returned to thank Jesus, teaching us the important value of thankfulness and gratitude."
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "questionText": "Jesus shared the Last Supper with his disciples mainly to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "prepare the disciples for his death", "isCorrect": True },
        { "text": "identify the disciple who would betray him", "isCorrect": False },
        { "text": "warn the disciples of the coming persecution", "isCorrect": False },
        { "text": "choose a leader from among them.", "isCorrect": False }
      ],
      "explanation": "The Last Supper was a crucial final meal where Jesus instituted the New Covenant and prepared his disciples for his impending suffering, death, and departure."
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "questionText": "Christians should bear the fruits of the Holy Spirit in order to live a Godly life. Which of the following is one of the fruits that a Christian should bear?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Courage", "isCorrect": False },
        { "text": "Wisdom", "isCorrect": False },
        { "text": "Healing", "isCorrect": False },
        { "text": "Gentleness", "isCorrect": True }
      ],
      "explanation": "Gentleness is listed as one of the fruits of the Holy Spirit in Galatians 5:22-23. Wisdom and healing are considered gifts of the Holy Spirit."
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "A common practice that was carried out in the Early Church and is still being practised in the church in Kenya today is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "making sacrifices", "isCorrect": False },
        { "text": "helping the needy", "isCorrect": True },
        { "text": "building schools", "isCorrect": False },
        { "text": "giving loans to Christians.", "isCorrect": False }
      ],
      "explanation": "The Early Church was known for sharing their possessions and helping the needy (like widows and orphans), a practice of charity that continues in the modern church."
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "Your classmate is becoming shy due to the changes occurring in her body as a result of adolescence. Choose the best groups of people she can seek advice from.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Classmates and friends.", "isCorrect": False },
        { "text": "Doctors and nurses.", "isCorrect": False },
        { "text": "House helps and neighbours.", "isCorrect": False },
        { "text": "Parents and teachers.", "isCorrect": True }
      ],
      "explanation": "Parents, teachers, or designated school counselors are the most trusted, experienced, and appropriate adults to provide sound advice and guidance during adolescence."
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "questionText": "You saw some boys from your class smoking cigarettes as they went home in the evening. What is the best action for you to take?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Report them to the chief.", "isCorrect": False },
        { "text": "Tell your classmates about it.", "isCorrect": False },
        { "text": "Tell them the dangers of their habit.", "isCorrect": True },
        { "text": "Warn them that cigarettes are expensive.", "isCorrect": False }
      ],
      "explanation": "As a responsible peer and Christian, gently warning them about the health dangers of smoking is the most constructive and caring immediate action to take."
    }
  ]
}

file_path = 'src/data/kpsea-sst-cre-2025.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstCre2025 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print("KPSEA SST CRE 2025 generated!")
