import json
import re
import os

# 1. Append 38-40 to part A
file_path_parta = 'src/data/kpsea-sst-parta-2024.js'
with open(file_path_parta, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = re.sub(r'^export const [a-zA-Z0-9_]+ = ', '', content)
json_str = re.sub(r';\s*$', '', json_str)
parta = json.loads(json_str)

parta['sectionA'].extend([
    {
      "id": "q38",
      "questionNumber": 38,
      "questionText": "Jamol often asks his children to stay at home and assist in weeding the farm during school days. By doing this, he denies his children the right to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "movement", "isCorrect": False },
        { "text": "play", "isCorrect": False },
        { "text": "education", "isCorrect": True },
        { "text": "protection.", "isCorrect": False }
      ],
      "explanation": "Keeping children at home to work during school days denies them their fundamental right to education."
    },
    {
      "id": "q39",
      "questionNumber": 39,
      "questionText": "Political candidates who reject election results take their complaints to court. This method of solving conflicts is known as",
      "questionType": "multiple-choice",
      "options": [
        { "text": "negotiation", "isCorrect": False },
        { "text": "reconciliation", "isCorrect": False },
        { "text": "adjudication", "isCorrect": True },
        { "text": "arbitration.", "isCorrect": False }
      ],
      "explanation": "Adjudication involves taking a dispute to a court of law where a judge or magistrate makes a formal, binding decision."
    },
    {
      "id": "q40",
      "questionNumber": 40,
      "questionText": "During a library search on national symbols of Kenya, a learner came across the following statements.\n(i) It has two lions holding spears\n(ii) Has images of some crops\n(iii) It is the logo of our country\n(iv) Has a cock holding an axe\n\nThe symbol described above is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "National flag", "isCorrect": False },
        { "text": "The public seal", "isCorrect": False },
        { "text": "The Kenyan shield", "isCorrect": False },
        { "text": "Coat of arms.", "isCorrect": True }
      ],
      "explanation": "The Kenyan Coat of Arms features two lions holding spears and a shield, Mount Kenya in the background with crops, and a cockerel holding an axe."
    }
])

with open(file_path_parta, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstParta2024 = ' + json.dumps(parta, indent=2) + ';\n')


# 2. Create CRE 2024
cre_data = {
  "id": "kpsea-sst-cre-2024",
  "title": "KPSEA 2024 Social Studies & Creative Arts (CRE)",
  "subject": "CRE",
  "year": "2024",
  "isSubPaper": True,
  "durationMinutes": 0,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "According to the stories of creation in the Bible, human beings are considered special among God's creation. This is because",
      "questionType": "multiple-choice",
      "options": [
        { "text": "they were created male and female", "isCorrect": False },
        { "text": "God gave them all types of food", "isCorrect": False },
        { "text": "God put them in the Garden of Eden", "isCorrect": False },
        { "text": "they were made in the image of God.", "isCorrect": True }
      ],
      "explanation": "Genesis states that humans are unique because they were created in the image and likeness of God."
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "Your cousin got married in the office of the registrar of marriages. This type of marriage is called",
      "questionType": "multiple-choice",
      "options": [
        { "text": "customary marriage", "isCorrect": False },
        { "text": "civil marriage", "isCorrect": True },
        { "text": "polygamous marriage", "isCorrect": False },
        { "text": "christian marriage.", "isCorrect": False }
      ],
      "explanation": "A marriage officiated by a government official (registrar) at a registrar's office is known as a civil marriage."
    },
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "The Bible has been translated into the languages of communities found in Kenya today. The main advantage of this is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "create job opportunities", "isCorrect": False },
        { "text": "promote local languages", "isCorrect": False },
        { "text": "spread good news to many people", "isCorrect": True },
        { "text": "set up bookshops for selling Christian books.", "isCorrect": False }
      ],
      "explanation": "The primary purpose of Bible translation is to make the Word of God accessible to people in their native languages so they can understand the gospel."
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "King Solomon of Israel settled a dispute between two women who claimed to own one baby. The lesson Christians learn from this story is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "use wisdom in solving conflicts", "isCorrect": True },
        { "text": "avoid sharing a room with other people", "isCorrect": False },
        { "text": "report difficult cases to their leaders", "isCorrect": False },
        { "text": "consult their relatives whenever they have problems.", "isCorrect": False }
      ],
      "explanation": "Solomon used God-given wisdom to determine the real mother, teaching Christians the value of wisdom and discernment in resolving disputes."
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "Which one of the following events took place during the baptism of Jesus?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "There was an earthquake.", "isCorrect": False },
        { "text": "The appearance of Jesus was changed.", "isCorrect": False },
        { "text": "The disciples praised God.", "isCorrect": False },
        { "text": "A voice was heard from heaven.", "isCorrect": True }
      ],
      "explanation": "During Jesus' baptism, the heavens opened, the Spirit descended like a dove, and a voice from heaven said, 'This is my Son, whom I love; with him I am well pleased.'"
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "questionText": "The lesson that Jesus wanted to pass to his listeners through the parable of the lost son and the lost coin is that people should",
      "questionType": "multiple-choice",
      "options": [
        { "text": "take good care of their properties", "isCorrect": False },
        { "text": "work hard in their lives", "isCorrect": False },
        { "text": "bring sinners to God", "isCorrect": True },
        { "text": "tell others what God has done for them.", "isCorrect": False }
      ],
      "explanation": "These parables illustrate God's immense joy when a sinner repents, encouraging believers to seek the lost and bring them to God."
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "questionText": "A lesson Christians learn from the miracle in which a woman who had been bleeding for twelve years was healed by touching the cloth of Jesus is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "hide sickness from other people", "isCorrect": False },
        { "text": "always have faith in God", "isCorrect": True },
        { "text": "build hospitals for the sick people", "isCorrect": False },
        { "text": "touch the clothes of pastors when sick.", "isCorrect": False }
      ],
      "explanation": "Jesus told the woman, 'Your faith has healed you.' This teaches Christians the importance of having unwavering faith in God's healing power."
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "Your classmate was injured by his friend while playing in the field. Your classmate forgave his friend. Select the fruit of the Holy Spirit that your classmate demonstrated.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Self-control.", "isCorrect": False },
        { "text": "Faithfulness.", "isCorrect": False },
        { "text": "Patience.", "isCorrect": True },
        { "text": "Joy.", "isCorrect": False }
      ],
      "explanation": "Forgiveness involves forbearance and patience, choosing not to retaliate when wronged."
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "Your friend told you a story about a man who was stoned to death by a crowd for snatching a mobile phone from someone. Which commandment did the crowd break. Do not",
      "questionType": "multiple-choice",
      "options": [
        { "text": "accuse anyone falsely", "isCorrect": False },
        { "text": "steal another person's property", "isCorrect": False },
        { "text": "commit murder", "isCorrect": True },
        { "text": "desire another person's property.", "isCorrect": False }
      ],
      "explanation": "Taking someone's life through mob justice is a violation of the commandment 'Do not commit murder'."
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "questionText": "Your teacher gave you an assignment to search for information about the miracles of Jesus from the internet. Which of the following digital devices would you use?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Camera.", "isCorrect": False },
        { "text": "Radio.", "isCorrect": False },
        { "text": "Projector.", "isCorrect": False },
        { "text": "Tablet.", "isCorrect": True }
      ],
      "explanation": "A tablet is a digital device that can connect to the internet to search for information. The others are not typically used for web browsing."
    }
  ]
}

with open('src/data/kpsea-sst-cre-2024.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstCre2024 = ' + json.dumps(cre_data, indent=2) + ';\n')

# 3. Create IRE 2024
ire_data = {
  "id": "kpsea-sst-ire-2024",
  "title": "KPSEA 2024 Social Studies & Creative Arts (IRE)",
  "subject": "IRE",
  "year": "2024",
  "isSubPaper": True,
  "durationMinutes": 0,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "While performing swalatul Dhuhr, Ali recited the verse: 'Kalla saufa taalamun'. The verse is found in surah",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Al-Qariah", "isCorrect": False },
        { "text": "Al-Humazah", "isCorrect": False },
        { "text": "At-Takathur", "isCorrect": True },
        { "text": "Al-Kawthar.", "isCorrect": False }
      ],
      "explanation": "The verse 'Kallaa sawfa ta'lamoon' (No! You are going to know) is Ayah 3 of Surah At-Takathur."
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "At break time, Mariam called her friends to show off her new watch that her mother had bought her. The surah that discourages this behaviour is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "An-Naas", "isCorrect": False },
        { "text": "An-Nasr", "isCorrect": False },
        { "text": "Al-Falaq", "isCorrect": False },
        { "text": "Al-Maun.", "isCorrect": True }
      ],
      "explanation": "Surah Al-Maun condemns those who make a show of their deeds (showing off)."
    },
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "Choose the phrase that completes the following Hadith: 'Allah does not look at your appearance or wealth, but rather he looks at your _____'",
      "questionType": "multiple-choice",
      "options": [
        { "text": "heart and actions", "isCorrect": True },
        { "text": "heart and intentions", "isCorrect": False },
        { "text": "strength and actions", "isCorrect": False },
        { "text": "strength and intentions.", "isCorrect": False }
      ],
      "explanation": "The famous Hadith narrated by Muslim says: 'Allah does not look at your forms and wealth, but He looks at your hearts and your deeds (actions).'"
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "Halima's father is travelling and wants to make a dua asking for protection during his journey. The attribute of Allah that he will use in his dua is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Al-Ghaffar", "isCorrect": False },
        { "text": "Al-Waahid", "isCorrect": False },
        { "text": "Al-Haafidh", "isCorrect": True },
        { "text": "Al-Hakam.", "isCorrect": False }
      ],
      "explanation": "Al-Haafidh means The Protector or The Preserver, which is the attribute used when seeking protection."
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "Athman, a Grade 4 learner had started performing Dhuhr prayer. He realized that his wudhu was nullified. Which one of the following acts could have nullified his wudhu?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Swallowing saliva.", "isCorrect": False },
        { "text": "Passing wind.", "isCorrect": True },
        { "text": "Eating.", "isCorrect": False },
        { "text": "Laughing.", "isCorrect": False }
      ],
      "explanation": "Passing wind breaks wudhu (ablution). Laughing loudly breaks the prayer but not the wudhu. Eating breaks the prayer but not wudhu."
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "questionText": "During IRE group discussions, Grade 6 learners presented items liable for Zakat payment as follows:\n\nGroup 1: Residential house\nGroup 2: Personal books\nGroup 3: Gold for trade\nGroup 4: Household furniture\n\nThe group that presented the correct item is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Group 1", "isCorrect": False },
        { "text": "Group 2", "isCorrect": False },
        { "text": "Group 3", "isCorrect": True },
        { "text": "Group 4.", "isCorrect": False }
      ],
      "explanation": "Zakat is payable on trade goods and precious metals like gold and silver. Personal items like houses, furniture, and books are exempt from Zakat."
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "questionText": "Adan found his friends betting on football matches. The best action that he should take is to",
      "questionType": "multiple-choice",
      "options": [
        { "text": "warn them that he will report to the teacher", "isCorrect": False },
        { "text": "advise them on the harmful effects of betting", "isCorrect": True },
        { "text": "pray for them to stop the behaviour", "isCorrect": False },
        { "text": "ignore them and mind his own business.", "isCorrect": False }
      ],
      "explanation": "Islam teaches believers to actively forbid evil by advising gently and explaining its harms."
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "Which among the following acts performed by Grade 6 learners will guard against Israf?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Switching off the lights when there is no one in the classroom.", "isCorrect": True },
        { "text": "Performing wudhu using plenty of water.", "isCorrect": False },
        { "text": "Serving a lot of food at lunch time.", "isCorrect": False },
        { "text": "Using new exercise books while the old ones are not filled up.", "isCorrect": False }
      ],
      "explanation": "Israf means wastefulness or extravagance. Switching off unused lights conserves resources, preventing Israf."
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "Children should respect other family members because",
      "questionType": "multiple-choice",
      "options": [
        { "text": "it is an act of ibadah", "isCorrect": True },
        { "text": "it is a form of sadaqah", "isCorrect": False },
        { "text": "it prepares them for adulthood", "isCorrect": False },
        { "text": "it shows responsibility.", "isCorrect": False }
      ],
      "explanation": "In Islam, treating parents and family with respect is an act of worship (ibadah) mandated by Allah."
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "questionText": "The virtue that Muslims learn from the Prophet's journey to Taif is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "generosity", "isCorrect": False },
        { "text": "honesty", "isCorrect": False },
        { "text": "justice", "isCorrect": False },
        { "text": "forgiveness.", "isCorrect": True }
      ],
      "explanation": "Even though the people of Taif stoned and rejected him, the Prophet (PBUH) chose to forgive them rather than have them destroyed, demonstrating immense forgiveness and mercy."
    }
  ]
}

with open('src/data/kpsea-sst-ire-2024.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstIre2024 = ' + json.dumps(ire_data, indent=2) + ';\n')


# 4. Create HRE 2024
hre_data = {
  "id": "kpsea-sst-hre-2024",
  "title": "KPSEA 2024 Social Studies & Creative Arts (HRE)",
  "subject": "HRE",
  "year": "2024",
  "isSubPaper": True,
  "durationMinutes": 0,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q41",
      "questionNumber": 41,
      "questionText": "Grade 4 learners watched video clips on the creation of Parmatma. They discovered that the sun is important to human beings because",
      "questionType": "multiple-choice",
      "options": [
        { "text": "the earth cannot exist without it", "isCorrect": False },
        { "text": "plants need the heat from the sun", "isCorrect": True },
        { "text": "water will not evaporate", "isCorrect": False },
        { "text": "energy will not be available.", "isCorrect": False }
      ],
      "explanation": "The sun is crucial because its light and heat sustain plant life, which forms the basis of food for humans and animals."
    },
    {
      "id": "q42",
      "questionNumber": 42,
      "questionText": "Pavan Guru Pani Pita Mata Dharat Mahat. The panch mahabhoot that is given the highest status from the above verse from Sri Guru Grant Sahibji is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "air", "isCorrect": False },
        { "text": "earth", "isCorrect": True },
        { "text": "fire", "isCorrect": False },
        { "text": "water.", "isCorrect": False }
      ],
      "explanation": "The verse calls the Earth 'Mata Dharat Mahat' (Mother Earth, the great one), elevating it to a high, nurturing status."
    },
    {
      "id": "q43",
      "questionNumber": 43,
      "questionText": "A resource person was invited to school to talk about the four different scriptures found in the four faiths. He told the learners that Bwagwad Gita is part of the epic Mahabharat which is a dialogue between",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Lord Krishna and Sudama", "isCorrect": False },
        { "text": "Lord Krishna and Arjun", "isCorrect": True },
        { "text": "Arjun and Lord Krisha", "isCorrect": False },
        { "text": "Hanuman and Lord Krishna.", "isCorrect": False }
      ],
      "explanation": "The Bhagavad Gita is a profound philosophical dialogue between Lord Krishna and the warrior prince Arjun on the battlefield of Kurukshetra."
    },
    {
      "id": "q44",
      "questionNumber": 44,
      "questionText": "Learners were told about the story of the lion that cleverly trapped several animals and killed them except the fox. The fox used its wisdom and followed the footsteps of animals that kept disappearing at the lions cave. The moral of this story is that we should",
      "questionType": "multiple-choice",
      "options": [
        { "text": "learn from other peoples mistakes", "isCorrect": True },
        { "text": "help those who are sick", "isCorrect": False },
        { "text": "avoid the troublemakers", "isCorrect": False },
        { "text": "associate with wise people.", "isCorrect": False }
      ],
      "explanation": "By observing the tracks of the animals that did not return, the fox learned from their mistakes and avoided the trap."
    },
    {
      "id": "q45",
      "questionNumber": 45,
      "questionText": "Prince Siddhartha cared for a bird which had been injured by his cousin. By doing so, Prince Siddhartha demonstrated the principle of",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Santosh", "isCorrect": False },
        { "text": "Daya", "isCorrect": True },
        { "text": "Dharraj", "isCorrect": False },
        { "text": "Satya.", "isCorrect": False }
      ],
      "explanation": "Daya means compassion or kindness. By saving the injured bird, Prince Siddhartha displayed great compassion."
    },
    {
      "id": "q46",
      "questionNumber": 46,
      "questionText": "Rakesh was watching inappropriate content on YouTube from his phone in class. The class teacher saw him and told him to stop the habit. The principle of Dharma demonstrated by the teacher is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "purushath", "isCorrect": True },
        { "text": "prathana", "isCorrect": False },
        { "text": "pranidaya", "isCorrect": False },
        { "text": "punarjanam.", "isCorrect": False }
      ],
      "explanation": "Guiding a student towards righteous action and responsibility aligns with Purusharth (the goals of human life, encompassing duty and righteous living)."
    },
    {
      "id": "q47",
      "questionNumber": 47,
      "questionText": "Some learners from Bahati school went to Nyayo stadium to celebrate the independence of Kenya. They took part in the following activities. The one that best demonstrated patriotism is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "entertaining the people", "isCorrect": False },
        { "text": "watching the parade of soldiers", "isCorrect": False },
        { "text": "singing the national anthem", "isCorrect": True },
        { "text": "listening to the speeches of leaders.", "isCorrect": False }
      ],
      "explanation": "Singing the national anthem is an active expression of love and devotion to one's country (patriotism)."
    },
    {
      "id": "q48",
      "questionNumber": 48,
      "questionText": "The communal aspect of yoga benefits the society by encouraging environmental conservation. This promotes",
      "questionType": "multiple-choice",
      "options": [
        { "text": "fellowship", "isCorrect": False },
        { "text": "friendship", "isCorrect": False },
        { "text": "citizenship", "isCorrect": True },
        { "text": "mentorship.", "isCorrect": False }
      ],
      "explanation": "Taking responsibility for the environment and the community is a core aspect of good citizenship."
    },
    {
      "id": "q49",
      "questionNumber": 49,
      "questionText": "A festival during which devotees worship Maa Durga to celebrate the victory over evil is called",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Diwali", "isCorrect": False },
        { "text": "Navrattri", "isCorrect": True },
        { "text": "Holi", "isCorrect": False },
        { "text": "Dushera.", "isCorrect": False }
      ],
      "explanation": "Navratri is a nine-night festival dedicated to the worship of the Goddess Durga and her nine forms."
    },
    {
      "id": "q50",
      "questionNumber": 50,
      "questionText": "Linda attended a yoga class and took part in performing an asana which is done by reciting manthras and performing twelve physical asanas. This asana is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "vajra asana", "isCorrect": False },
        { "text": "tadd asana", "isCorrect": False },
        { "text": "surya namaskar", "isCorrect": True },
        { "text": "padam asan.", "isCorrect": False }
      ],
      "explanation": "Surya Namaskar (Sun Salutation) is a sequence of 12 yoga postures performed gracefully along with chanting mantras."
    }
  ]
}

with open('src/data/kpsea-sst-hre-2024.js', 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstHre2024 = ' + json.dumps(hre_data, indent=2) + ';\n')

print("Final batches completed!")
