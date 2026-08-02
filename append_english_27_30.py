import json
filepath = 'src/data/kpsea-english-2022.js'
data = open(filepath, 'r', encoding='utf-8').read().replace('export const kpseaEnglish2022 = ', '').strip(';\n')
js = json.loads(data)

js['sharedContexts']['ctx-eng-2022-q27-28'] = {
    'title': 'For questions 27 and 28, choose the alternative that means the same as the underlined.',
    'type': 'text',
    'text': ''
}
js['sharedContexts']['ctx-eng-2022-q29-30'] = {
    'title': 'In questions 29 and 30, choose the word that means the same as the underlined word.',
    'type': 'text',
    'text': ''
}

new_qs = [
    {
      'id': 'eq27-2022',
      'questionNumber': 27,
      'questionText': '<u>The hungry pupils ate the raw mangoes.</u>',
      'questionType': 'mcq',
      'contextRef': 'ctx-eng-2022-q27-28',
      'options': [
        { 'text': 'The raw mangoes had been eaten by the hungry pupils.', 'isCorrect': False },
        { 'text': 'The raw mangoes are eaten by the hungry pupils.', 'isCorrect': False },
        { 'text': 'The raw mangoes were eaten by the hungry pupils.', 'isCorrect': True },
        { 'text': 'The raw mangoes will be eaten by the hungry pupils.', 'isCorrect': False }
      ],
      'explanation': "The correct answer is **The raw mangoes were eaten by the hungry pupils.**\n\n**Analysis of the Correct Answer:**\nThe original sentence is in the active voice and the past tense (\"ate\"). When converting to the passive voice, the object (\"the raw mangoes\") becomes the subject, and the past tense verb \"ate\" becomes \"were eaten\" (because \"mangoes\" is plural).\n\n**Why Other Options Are Incorrect:**\n* **The raw mangoes had been eaten by the hungry pupils.:** This is the past perfect tense, not the simple past tense.\n* **The raw mangoes are eaten by the hungry pupils.:** This is the present tense.\n* **The raw mangoes will be eaten by the hungry pupils.:** This is the future tense.\n\n📌 **Key Learning Note:**\nWhen changing a sentence from active to passive voice, always maintain the original tense of the verb."
    },
    {
      'id': 'eq28-2022',
      'questionNumber': 28,
      'questionText': 'The guests were pleased with the <u>person who served them food at the hotel</u>.',
      'questionType': 'mcq',
      'contextRef': 'ctx-eng-2022-q27-28',
      'options': [
        { 'text': 'cook', 'isCorrect': False },
        { 'text': 'host', 'isCorrect': False },
        { 'text': 'waiter', 'isCorrect': True },
        { 'text': 'cleaner', 'isCorrect': False }
      ],
      'explanation': "The correct answer is **waiter**.\n\n**Analysis of the Correct Answer:**\nIn a hotel or restaurant, the person whose specific job is to take orders and serve food to guests is called a **waiter** (or waitress for a female).\n\n**Why Other Options Are Incorrect:**\n* **cook:** The person who prepares and cooks the food in the kitchen.\n* **host:** The person who welcomes guests and shows them to their tables.\n* **cleaner:** The person who cleans the hotel or restaurant.\n\n📌 **Key Learning Note:**\nDifferent professions have specific titles. A **waiter** serves food, while a **chef** or **cook** prepares it."
    },
    {
      'id': 'eq29-2022',
      'questionNumber': 29,
      'questionText': 'We found the room <u>tidy</u>.',
      'questionType': 'mcq',
      'contextRef': 'ctx-eng-2022-q29-30',
      'options': [
        { 'text': 'neat', 'isCorrect': True },
        { 'text': 'bright', 'isCorrect': False },
        { 'text': 'warm', 'isCorrect': False },
        { 'text': 'fresh', 'isCorrect': False }
      ],
      'explanation': "The correct answer is **neat**.\n\n**Analysis of the Correct Answer:**\nThe word **tidy** means arranged well, in good order, and clean. The word that means the exact same thing (synonym) is **neat**.\n\n**Why Other Options Are Incorrect:**\n* **bright:** Refers to being full of light or colors.\n* **warm:** Refers to a comfortable or relatively high temperature.\n* **fresh:** Refers to something new or clean air, but not necessarily organized.\n\n📌 **Key Learning Note:**\nSynonyms are words with the same or similar meanings. **Tidy** and **neat** are common synonyms for an organized space."
    },
    {
      'id': 'eq30-2022',
      'questionNumber': 30,
      'questionText': 'The choir sang <u>cheerfully</u>.',
      'questionType': 'mcq',
      'contextRef': 'ctx-eng-2022-q29-30',
      'options': [
        { 'text': 'loudly', 'isCorrect': False },
        { 'text': 'beautifully', 'isCorrect': False },
        { 'text': 'happily', 'isCorrect': True },
        { 'text': 'carefully', 'isCorrect': False }
      ],
      'explanation': "The correct answer is **happily**.\n\n**Analysis of the Correct Answer:**\nThe word **cheerfully** is an adverb that means doing something in a positive, joyful, and happy manner. Its direct synonym is **happily**.\n\n**Why Other Options Are Incorrect:**\n* **loudly:** Refers to high volume or noise, which doesn't mean joyful.\n* **beautifully:** Refers to something pleasing to hear, but doesn't specify the emotion of joy.\n* **carefully:** Refers to doing something with caution to avoid mistakes.\n\n📌 **Key Learning Note:**\nAdverbs ending in \"-ly\" often describe how an action is performed. **Cheerfully** describes a happy emotion, making **happily** the perfect match."
    }
]

js['sectionA'].extend(new_qs)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('export const kpseaEnglish2022 = ' + json.dumps(js, indent=2, ensure_ascii=False) + ';\n')

print('Added Q27-30 to kpsea-english-2022.js successfully.')
