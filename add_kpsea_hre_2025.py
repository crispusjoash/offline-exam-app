import json

paper_structure = {
  "id": "kpsea-sst-hre-2025",
  "title": "KPSEA 2025 Social Studies & Creative Arts (HRE)",
  "subject": "HRE",
  "year": "2025",
  "isSubPaper": True,
  "durationMinutes": 0,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "Grade 6 learners visited a Sanatan mandir and witnessed the ceremony of Havan being performed. The most important element of Panch mahabhoot in performing Hawan is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Jal", "isCorrect": False },
        { "text": "Vayu", "isCorrect": False },
        { "text": "Agni", "isCorrect": True },
        { "text": "Akash.", "isCorrect": False }
      ],
      "explanation": "Havan (or Yajna) is a fire ritual in Hinduism, making Agni (fire) the most essential element among the Panch Mahabhootas (five great elements) for its performance."
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "Grade 6 learners painted a lotus flower as an important creation of Parmatma. Lotus flower is a symbol of",
      "questionType": "multiple-choice",
      "options": [
        { "text": "detachment", "isCorrect": True },
        { "text": "beauty", "isCorrect": False },
        { "text": "colour", "isCorrect": False },
        { "text": "adaptability.", "isCorrect": False }
      ],
      "explanation": "In Hinduism, the lotus flower represents purity and detachment because it grows in muddy water but remains beautiful and unstained by the mud."
    },
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "Guru Arjan Devji played a very significant part in the Sikh faith as he",
      "questionType": "multiple-choice",
      "options": [
        { "text": "began the practice of the Guru Langar", "isCorrect": False },
        { "text": "completed the building of the Golden Temple", "isCorrect": True },
        { "text": "showed devotees the correct way to worship", "isCorrect": False },
        { "text": "compiled a code of conduct.", "isCorrect": False }
      ],
      "explanation": "Guru Arjan Dev Ji, the fifth Sikh Guru, significantly contributed by completing the construction of the Harmandir Sahib (Golden Temple) and compiling the Adi Granth."
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "Swami Narayan has made important contributions to the modern society. Which of the following is the most outstanding contribution of Swami Narayan Bhagwan? He",
      "questionType": "multiple-choice",
      "options": [
        { "text": "built many temples", "isCorrect": False },
        { "text": "emphasized that yajnas should be performed", "isCorrect": False },
        { "text": "wrote shikshapatri, a book of social conduct", "isCorrect": True },
        { "text": "promoted education as basic right for all.", "isCorrect": False }
      ],
      "explanation": "Bhagwan Swaminarayan authored the Shikshapatri, a foundational text outlining a strict code of moral and social conduct for his followers."
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "A young man, Eklavya, learnt archery secretly from Guru Dhronacharya and gave reverence to a sculpture of the Guru. Guru Dhronacharya found out that Eklavya was very good in archery and better than his top student, Arjun. To keep his top student, he asked Eklavya for Guru Dakshina which Eklavya willingly gave. What did Eklavya give?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Bow and arrow.", "isCorrect": False },
        { "text": "Ornaments.", "isCorrect": False },
        { "text": "His right hand thumb.", "isCorrect": True },
        { "text": "Robe.", "isCorrect": False }
      ],
      "explanation": "In the Mahabharata, Ekalavya willingly cut off his right thumb and offered it as Guru Dakshina to Dronacharya upon request."
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "questionText": "Devotees of different faiths remove their footwear at the entrance of their places of worship and prayer halls to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "feel comfortable without their footwear", "isCorrect": False },
        { "text": "just follow what others do", "isCorrect": False },
        { "text": "keep shoes from being stolen", "isCorrect": False },
        { "text": "maintain the cleanliness of the place.", "isCorrect": True }
      ],
      "explanation": "Removing footwear is a sign of respect and serves the practical purpose of maintaining the cleanliness and purity of the sacred space."
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "questionText": "A villager lost his cows and was very upset. While searching for them, he came to where Lord Buddha was giving a discourse to his followers. He began shouting at Lord Buddha for no reason. The villager getting no response from Lord Buddha calmed down. By keeping quiet and calm, Lord Buddha practised the principle of right",
      "questionType": "multiple-choice",
      "options": [
        { "text": "concentration", "isCorrect": False },
        { "text": "action", "isCorrect": False },
        { "text": "view", "isCorrect": False },
        { "text": "speech.", "isCorrect": True }
      ],
      "explanation": "Right Speech in the Noble Eightfold Path involves abstaining from abusive or harsh words. By choosing to remain silent in the face of anger, Lord Buddha exemplified Right Speech."
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "One day Sarla was going back home from school with her friends. She noticed an old blind woman waiting to cross the road. She quickly went to the old woman and helped her to cross the road. By doing this, Sarla practised the principle of",
      "questionType": "multiple-choice",
      "options": [
        { "text": "purushartha", "isCorrect": False },
        { "text": "ahinsa", "isCorrect": True },
        { "text": "vande shakhna", "isCorrect": False },
        { "text": "aparigraha.", "isCorrect": False }
      ],
      "explanation": "Ahimsa is commonly known as non-violence, but broadly it means unconditional love, compassion, and not causing harm. Helping the old woman is an act of compassion (Ahimsa)."
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "The following statements describe a festival.\n(i) Prayers are offered to Laxmi Devi.\n(ii) Homes are lighted with deepaks.\n(iii) Places of worship are visited.\n(iv) Donations are given.\n(v) New clothes are worn.\n(vi) Gifts are exchanged.\n(vii) Fun fairs are organized.\nThe festival described is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "janmashtami", "isCorrect": False },
        { "text": "holi", "isCorrect": False },
        { "text": "navratri", "isCorrect": False },
        { "text": "diwali.", "isCorrect": True }
      ],
      "explanation": "Diwali is the festival of lights characterized by lighting deepaks (lamps), exchanging gifts, wearing new clothes, and offering prayers to Goddess Lakshmi (Laxmi Devi) for prosperity."
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "questionText": "A yoga instructor was invited to Karuna Primary School to talk about yoga. During his talk, he emphasized two basic requirements for performing yoga. These are",
      "questionType": "multiple-choice",
      "options": [
        { "text": "new clothes and yoga mat", "isCorrect": False },
        { "text": "soft drinks and light snacks", "isCorrect": False },
        { "text": "balanced diet and right attire", "isCorrect": True },
        { "text": "good lighting and furniture.", "isCorrect": False }
      ],
      "explanation": "Proper physical conditioning through a balanced diet and wearing comfortable right attire that allows freedom of movement are basic requirements for performing yoga effectively."
    }
  ]
}

file_path = 'src/data/kpsea-sst-hre-2025.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstHre2025 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print("KPSEA SST HRE 2025 generated!")
