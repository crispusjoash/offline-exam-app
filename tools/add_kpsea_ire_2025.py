import json

paper_structure = {
  "id": "kpsea-sst-ire-2025",
  "title": "KPSEA 2025 Social Studies & Creative Arts (IRE)",
  "subject": "IRE",
  "year": "2025",
  "isSubPaper": True,
  "durationMinutes": 0,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "Grade 4 learners recited the verse, 'Al-ladhy yuwaswisu fi sudurin naas'.\nThe meaning of the verse is:",
      "questionType": "multiple-choice",
      "options": [
        { "text": "'who whispers evil into the heart of mankind'", "isCorrect": True },
        { "text": "'from among the Jinn and mankind'", "isCorrect": False },
        { "text": "'from the evil of the whisperer'", "isCorrect": False },
        { "text": "'the God of mankind'.", "isCorrect": False }
      ],
      "explanation": "This is verse 5 from Surah An-Nas. It translates to 'Who whispers [evil] into the breasts (hearts) of mankind'."
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "As Muslims, we learn that gathering a lot of wealth and concentrating on worldly things will not benefit us. This lesson is found in Surah",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Al-Kauthar and Al-Maun", "isCorrect": False },
        { "text": "Al-Kauthar and At-Takathur", "isCorrect": False },
        { "text": "Al-Humazah and At-Takathur", "isCorrect": True },
        { "text": "Al-Humazah and Al-Qariah.", "isCorrect": False }
      ],
      "explanation": "Surah At-Takathur warns against the mutual rivalry for piling up worldly things. Surah Al-Humazah warns against gathering wealth and thinking it will make one immortal."
    },
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "A teacher observed the following as his learners took lunch:\nAli: said Bismillah before eating\nMusa: ate with his right hand\nSaid: ate while the food was very hot\nSalim: ate what was nearest to him on the plate\nWho among the learners did not apply the etiquette of eating according to the Hadith of the Prophet (P.b.u.h)?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Ali.", "isCorrect": False },
        { "text": "Musa.", "isCorrect": False },
        { "text": "Said.", "isCorrect": True },
        { "text": "Salim.", "isCorrect": False }
      ],
      "explanation": "According to the Sunnah, one should wait for the food to cool down before eating. Eating food while it is very hot goes against the etiquette. Ali, Musa, and Salim applied correct etiquettes."
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "Grade 5 learners were searching for information about miracles of the prophets from the internet. Which of the following miracles they found was performed by Prophet Isa?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Surviving a blazing fire.", "isCorrect": False },
        { "text": "Changing a stick into a snake.", "isCorrect": False },
        { "text": "Splitting the sea into two.", "isCorrect": False },
        { "text": "Bringing the dead to life.", "isCorrect": True }
      ],
      "explanation": "By the permission of Allah, Prophet Isa (Jesus) performed the miracle of bringing the dead back to life."
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "The Zakat Foundation in your community can give zakat to the following people except",
      "questionType": "multiple-choice",
      "options": [
        { "text": "old people", "isCorrect": True },
        { "text": "converts", "isCorrect": False },
        { "text": "those in debt", "isCorrect": False },
        { "text": "the poor.", "isCorrect": False }
      ],
      "explanation": "The categories of people eligible to receive Zakat are explicitly mentioned in the Quran, including the poor, converts, and those in debt. 'Old people' is not a category unless they also fall under the poor or needy."
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "questionText": "Teacher Amina displayed flash cards showing the following acts:\n(i) talking\n(ii) intentional vomiting\n(iii) passing wind\n(iv) menstruation\nWhich two of the acts nullify both Swalah and Saum?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "(ii) and (iii).", "isCorrect": False },
        { "text": "(ii) and (iv).", "isCorrect": True },
        { "text": "(i) and (iv).", "isCorrect": False },
        { "text": "(i) and (iii).", "isCorrect": False }
      ],
      "explanation": "Menstruation invalidates both prayer (Swalah) and fasting (Saum). Intentional vomiting invalidates fasting and, as an impurity that breaks wudhu in some madhabs, also invalidates prayer."
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "questionText": "Amina was annoyed by her classmate while performing a group assignment. She remained calm and continued doing the assignment. The virtue that Amina demonstrated is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "sabr", "isCorrect": True },
        { "text": "adala", "isCorrect": False },
        { "text": "taqwa", "isCorrect": False },
        { "text": "tawakkul.", "isCorrect": False }
      ],
      "explanation": "Sabr means patience, perseverance, and self-control. By remaining calm when annoyed, Amina demonstrated sabr."
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "Salima left home for school. Which of the following is the correct dua that she recited before leaving?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "In the name of Allah the Most Merciful the Most Beneficent.", "isCorrect": False },
        { "text": "Glory to Him who has brought this under our control.", "isCorrect": False },
        { "text": "In the name of Allah we leave, enter and upon Him we depend.", "isCorrect": True },
        { "text": "Oh Allah make what you teach me beneficial.", "isCorrect": False }
      ],
      "explanation": "The dua specifically for entering/leaving the house involves mentioning the name of Allah and placing trust in Him. This option best matches the combined supplications taught in the syllabus for entering and leaving the home."
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "An obligation that your father should fulfil towards you is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "visit you in school", "isCorrect": False },
        { "text": "pay your school fees", "isCorrect": True },
        { "text": "buy for you new shoes", "isCorrect": False },
        { "text": "buy for you presents.", "isCorrect": False }
      ],
      "explanation": "Providing for basic needs, including education (paying school fees), is a fundamental obligation of a parent towards their child in Islam."
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "questionText": "The second pledge of Aqabah played an important role in the development of Islam because it led to the",
      "questionType": "multiple-choice",
      "options": [
        { "text": "migration to Abbysinia", "isCorrect": False },
        { "text": "conquest of Makkah", "isCorrect": False },
        { "text": "peace treaty of Hudaibiyya", "isCorrect": False },
        { "text": "migration to Madina.", "isCorrect": True }
      ],
      "explanation": "During the Second Pledge of Aqabah, the people of Yathrib (Madina) pledged their allegiance and protection to the Prophet, which paved the way for the Hijrah (migration) to Madina."
    }
  ]
}

file_path = 'src/data/kpsea-sst-ire-2025.js'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstIre2025 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print("KPSEA SST IRE 2025 generated!")
