import json
import os
import shutil

filepath = 'public/data/kjsea-cre-sectionb-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

updates = {
    "q21": {
        "modelAnswer": "Here is an exhaustive list of acceptable consequences of Adam and Eve's disobedience:\n\n1. **Expulsion from Eden:** They were chased out of the Garden of Eden.\n2. **Pain in Childbirth:** The woman would experience severe pain during childbirth.\n3. **Toil for Food:** The man would have to toil and sweat to get food from the ground.\n4. **Curse on the Snake:** The snake was cursed to crawl on its belly and eat dust.\n5. **Enmity:** Enmity was established between the woman's offspring and the snake.\n6. **Introduction of Death:** They became mortal and would eventually return to dust.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid consequence stated (Max 5 marks).\n* **Flexibility:** Accept any accurately paraphrased consequences from Genesis 3."
    },
    "q22a": {
        "modelAnswer": "Here is an exhaustive list of acceptable ways in which natural resources are misused in Kenya:\n\n1. **Deforestation:** Cutting down trees for timber, charcoal, or settlement without replacing them.\n2. **Water Pollution:** Releasing untreated industrial waste, sewage, or agricultural chemicals into rivers and lakes.\n3. **Overfishing and Poaching:** Illegal hunting of wildlife and unsustainable harvesting of fish.\n4. **Poor Farming Methods:** Overstocking or cultivating on steep slopes leading to severe soil erosion.\n5. **Illegal Mining:** Unregulated sand harvesting and mining that destroys landscapes.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid way natural resources are misused (Max 5 marks).\n* **Flexibility:** Accept any reasonable, practical example of environmental degradation or resource misuse in Kenya."
    },
    "q22b": {
        "modelAnswer": "Here is an exhaustive list of acceptable effects of misusing natural resources:\n\n1. **Soil Erosion and Infertility:** Loss of topsoil leading to poor agricultural yields.\n2. **Drought and Famine:** Deforestation causing unpredictable weather patterns and lack of food.\n3. **Loss of Biodiversity:** Death of aquatic life and extinction of terrestrial animals due to habitat destruction.\n4. **Climate Change:** Global warming resulting from greenhouse gas emissions and loss of forest cover.\n5. **Water Shortage:** Drying up of rivers and shortage of clean drinking water for humans and livestock.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid effect of resource misuse stated (Max 5 marks).\n* **Flexibility:** Accept any valid environmental, economic, or health effects caused by the degradation of natural resources."
    },
    "q23": {
        "modelAnswer": "Here is an exhaustive list of acceptable poetic books of the Old Testament:\n\n1. **Job:** A book exploring the theme of human suffering and God's sovereignty.\n2. **Psalms:** A collection of sacred songs, prayers, and hymns used in worship.\n3. **Proverbs:** A collection of wise sayings and instructions for living a godly life.\n4. **Ecclesiastes:** A philosophical reflection on the meaning and purpose of life.\n5. **Song of Solomon (Song of Songs):** A poetic celebration of love and marriage.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each correctly identified poetic book (Max 5 marks).\n* **Flexibility:** Accept 'Song of Songs' in place of 'Song of Solomon'."
    },
    "q24": {
        "modelAnswer": "Here is an exhaustive list of acceptable effects of Bible translations into local African languages:\n\n1. **Better Understanding:** It enabled more people to read, comprehend, and internalize the word of God in their mother tongue.\n2. **Spread of Christianity:** It accelerated evangelism and the rapid expansion of the Church across Africa.\n3. **Literacy and Education:** It promoted the development of local languages (reading and writing) and the establishment of formal schools.\n4. **African Leadership:** It empowered Africans to participate actively in evangelism, preaching, and church leadership.\n5. **Independent Churches:** It led to the emergence of African Independent Churches as locals interpreted scriptures for themselves.\n6. **Cultural Preservation:** It helped in preserving and standardizing African languages through written texts.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid effect of Bible translation stated (Max 5 marks).\n* **Flexibility:** Accept any historically or socially accurate impact of vernacular Bible translations on African societies."
    },
    "q25": {
        "modelAnswer": "Here is an exhaustive list of acceptable leadership qualities demonstrated by King David:\n\n1. **Courageous / Brave:** He fearlessly led his army into battle and defeated giants like Goliath.\n2. **God-fearing / Prayerful:** He constantly sought God's guidance before making major decisions.\n3. **Repentant / Humble:** He was quick to admit his mistakes and genuinely ask God for forgiveness (e.g., after the incident with Bathsheba).\n4. **Just / Fair:** He administered justice and equity to all his people.\n5. **Wise:** He used divine wisdom in ruling and uniting the tribes of Israel.\n6. **Merciful / Forgiving:** He spared the life of King Saul multiple times despite Saul trying to kill him.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid leadership quality stated (Max 5 marks).\n* **Flexibility:** Accept descriptive phrases (e.g., \"He was brave\") or single adjectives (e.g., \"Brave\")."
    },
    "q29a": {
        "modelAnswer": "Here is an exhaustive list of acceptable roles played by Christian parents:\n\n1. **Provision of Basic Needs:** Supplying food, clothing, shelter, and healthcare.\n2. **Spiritual Nurturing:** Teaching children the word of God, Christian values, and praying for/with them.\n3. **Church Involvement:** Taking children to church, Sunday school, and presenting them for baptism/dedication.\n4. **Loving Discipline:** Correcting and guiding children lovingly when they make mistakes.\n5. **Role Modeling:** Setting a positive example of a Christ-like life for children to emulate.\n6. **Education:** Taking children to school and supporting their academic development.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid role of a Christian parent identified (Max 5 marks).\n* **Flexibility:** Accept roles related to physical provision, spiritual guidance, emotional support, and education."
    },
    "q29b": {
        "modelAnswer": "Here is an exhaustive list of acceptable factors contributing to teenage pregnancies:\n\n1. **Peer Pressure:** Negative influence from friends leading to premature sexual activity.\n2. **Drug and Substance Abuse:** Impairs judgment and increases risky sexual behaviors.\n3. **Poverty:** Leading some teenagers to engage in transactional sex for basic needs or favors.\n4. **Lack of Parental Guidance:** Parental negligence or lack of open communication about sexuality.\n5. **Negative Media Influence:** Exposure to inappropriate content on the internet, television, and social media.\n6. **Idleness:** Lack of constructive leisure activities leaving teenagers with too much unsupervised free time.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid contributing factor stated (Max 5 marks).\n* **Flexibility:** Accept any reasonable social, economic, or psychological factor that leads to teenage pregnancies."
    },
    "q30a": {
        "modelAnswer": "Here is an exhaustive list of acceptable constructive leisure activities for youths:\n\n1. **Spiritual Growth:** Reading the Bible, Christian literature, or attending prayer retreats.\n2. **Church Participation:** Joining the church choir, youth groups, or drama clubs.\n3. **Physical Fitness:** Engaging in healthy sports, athletics, and games.\n4. **Community Service:** Volunteering to help the needy, visiting the sick, or environmental clean-ups.\n5. **Skill Development:** Attending Christian camps, seminars, or learning a new craft/hobby.\n6. **Family Time:** Spending quality time helping parents with chores or bonding with siblings.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid constructive leisure activity stated (Max 5 marks).\n* **Flexibility:** Accept any positive, productive, and morally upright activity suitable for a Christian youth."
    },
    "q30b": {
        "modelAnswer": "Here is an exhaustive list of acceptable effects of drug and substance abuse on school-going children:\n\n1. **Academic Decline:** Poor academic performance, lack of concentration, and eventually dropping out of school.\n2. **Health Issues:** Physical health deterioration, mental disorders, and risk of fatal overdoses.\n3. **Behavioral Problems:** Indiscipline, rebelliousness, aggression, and lack of respect for authority.\n4. **Criminal Activities:** Engaging in theft or violence to fund their drug habit.\n5. **Strained Relationships:** Constant conflicts with parents, teachers, and well-meaning friends.\n6. **Risky Behaviors:** Increased risk of contracting sexually transmitted diseases like HIV/AIDS due to impaired judgment.",
        "rubric": "📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid effect of drug abuse outlined (Max 5 marks).\n* **Flexibility:** Accept any valid physiological, psychological, academic, or social consequence of substance abuse."
    }
}

for q in data.get('sectionB', []):
    qid = q.get('id')
    if qid in updates:
        q['modelAnswer'] = updates[qid]['modelAnswer']
        q['rubric'] = updates[qid]['rubric']
    
    if 'subQuestions' in q:
        for sub in q['subQuestions']:
            sub_id = sub.get('id')
            if sub_id in updates:
                sub['modelAnswer'] = updates[sub_id]['modelAnswer']
                sub['rubric'] = updates[sub_id]['rubric']

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-cre-sectionb-2025.json')
print('Successfully updated CRE Section B model answers and rubrics to PreTech style.')
