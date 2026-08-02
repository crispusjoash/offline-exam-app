import json
import re

file_path = 'src/data/kjsea-sst-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'export const kjseaSst2025 = (\{.*\});', text, re.DOTALL)
if not match:
    print("Could not find JSON object")
    exit()
    
data = json.loads(match.group(1))

# Add shared contexts for Section B maps
data["sharedContexts"]["ctx-sst-q30"] = {
    "type": "image",
    "imagePath": "/assets/kjsea_sst_2025_q30.png",
    "title": "Map of Kapas Area for Question 30"
}

data["sharedContexts"]["ctx-sst-q33"] = {
    "type": "image",
    "imagePath": "/assets/kjsea_sst_2025_q33.png",
    "title": "Map of Africa for Question 33"
}

section_b = [
    {
        "id": "kjsea-sst-2025-b-21",
        "questionNumber": 21,
        "questionText": "In groups, Grade 8 learners discussed barriers to conflict resolution in a family and shared their findings in class. Outline five barriers they included in their findings. (5 marks)",
        "maxScore": 5
    },
    {
        "id": "kjsea-sst-2025-b-22",
        "questionNumber": 22,
        "questionText": "Grade 8 learners displayed flash cards containing ways of building healthy relationships in a school community. Highlight three ways which were captured on the flash cards. (3 marks)",
        "maxScore": 3
    },
    {
        "id": "kjsea-sst-2025-b-23",
        "questionNumber": 23,
        "questionText": "Pauline, a Grade 9 learner, is interested in a career in languages while the parents are in favour of Performing Arts. State three factors that she should consider before making the final decision. (3 marks)",
        "maxScore": 3
    },
    {
        "id": "kjsea-sst-2025-b-24",
        "questionNumber": 24,
        "questionText": "An article by a resource person in the daily newspaper contained information on child theft in Kenya and ways of preventing it. Outline three ways of preventing child theft that must have been highlighted in the article. (3 marks)",
        "maxScore": 3
    },
    {
        "id": "kjsea-sst-2025-b-25",
        "questionNumber": 25,
        "parentQuestionText": "Grade 9 learners from a Junior School made an educational visit to the Kenya National Assembly to learn about its operations.",
        "subQuestions": [
            {
                "id": "kjsea-sst-2025-b-25-a-i",
                "subNumber": "(a) (i)",
                "questionText": "Name two groups of members of the National Assembly who are elected during general elections that they learnt about. (2 marks)",
                "maxScore": 2
            },
            {
                "id": "kjsea-sst-2025-b-25-a-ii",
                "subNumber": "(a) (ii)",
                "questionText": "Identify two offices in the National Assembly whose holders are elected during the first sitting that they learnt about. (2 marks)",
                "maxScore": 2
            },
            {
                "id": "kjsea-sst-2025-b-25-b",
                "subNumber": "(b)",
                "questionText": "Explain three roles of members of the National Assembly that they learnt about during the visit. (6 marks)",
                "maxScore": 6
            }
        ]
    },
    {
        "id": "kjsea-sst-2025-b-26",
        "questionNumber": 26,
        "parentQuestionText": "Grade 7 learners engaged a resource person on Africans in Diaspora to discuss the reasons for migration, opportunities and challenges facing them.",
        "subQuestions": [
            {
                "id": "kjsea-sst-2025-b-26-a",
                "subNumber": "(a)",
                "questionText": "Outline four social reasons for the migration of Africans to the Diaspora in today's society that were highlighted. (4 marks)",
                "maxScore": 4
            },
            {
                "id": "kjsea-sst-2025-b-26-b",
                "subNumber": "(b)",
                "questionText": "Explain two economic contributions of the Africans in the Diaspora to their home countries. (4 marks)",
                "maxScore": 4
            }
        ]
    },
    {
        "id": "kjsea-sst-2025-b-27",
        "questionNumber": 27,
        "questionText": "Sarah and her friend came across an article on how items were used in the ancient times as a media of exchange and the invention of money which is a more convenient medium of exchange. State five ways through which the invention of money promoted trade in Africa. (5 marks)",
        "maxScore": 5
    },
    {
        "id": "kjsea-sst-2025-b-28",
        "questionNumber": 28,
        "questionText": "A Kenyan ambassador was invited by a teacher of Social Studies to enlighten the learners on globalization of Kenya's cultural elements. Give five elements of cultural globalization that the ambassador highlighted. (5 marks)",
        "maxScore": 5
    },
    {
        "id": "kjsea-sst-2025-b-29",
        "questionNumber": 29,
        "questionText": "During a group activity, learners researched on the national values provided in the Constitution of Kenya and how they promote good governance. Highlight five national values that they are likely to have found during their research. (5 marks)",
        "maxScore": 5
    },
    {
        "id": "kjsea-sst-2025-b-30",
        "questionNumber": 30,
        "contextRef": "ctx-sst-q30",
        "parentQuestionText": "Study the map of Kapas area provided and answer questions (a), (b), (c), (d) and (e).",
        "subQuestions": [
            {
                "id": "kjsea-sst-2025-b-30-a",
                "subNumber": "(a)",
                "questionText": "Identify two types of vegetation found in Kapas area? (2 marks)",
                "maxScore": 2
            },
            {
                "id": "kjsea-sst-2025-b-30-b",
                "subNumber": "(b)",
                "questionText": "Learners from Kora School walked along the dry-weather road up to the church. What distance did they cover? (Give your answer in kilometres) (2 marks)",
                "maxScore": 2
            },
            {
                "id": "kjsea-sst-2025-b-30-c",
                "subNumber": "(c)",
                "questionText": "Members of the Social Studies club carried out a field study on economic activities in Kapas area. Give four economic activities that they identified. (4 marks)",
                "maxScore": 4
            },
            {
                "id": "kjsea-sst-2025-b-30-d",
                "subNumber": "(d)",
                "questionText": "The main form of transport used in Kapas area is (1 mark)",
                "maxScore": 1
            },
            {
                "id": "kjsea-sst-2025-b-30-e",
                "subNumber": "(e)",
                "questionText": "Scola, a Grade 8 learner at Kapas School was asked by the teacher to give the direction of Kon Hill from the school. State the direction that she gave. (1 mark)",
                "maxScore": 1
            }
        ]
    },
    {
        "id": "kjsea-sst-2025-b-31",
        "questionNumber": 31,
        "questionText": "A meteorologist gave a talk on the effects of climate change on human activities to Grade 8 learners. State eight effects of climate change that the meteorologist talked about. (8 marks)",
        "maxScore": 8
    },
    {
        "id": "kjsea-sst-2025-b-32",
        "questionNumber": 32,
        "questionText": "Learners from a Junior School researched on the causes and effects of environmental degradation in the local community and wrote a report. Outline five causes of environmental degradation that they included in their report. (5 marks)",
        "maxScore": 5
    },
    {
        "id": "kjsea-sst-2025-b-33",
        "questionNumber": 33,
        "contextRef": "ctx-sst-q33",
        "parentQuestionText": "Learners in Grade 9 used the following map of Africa to study climatic regions, population distribution and economic activities in Africa. Use the map to answer questions (a), (b) and (c).",
        "subQuestions": [
            {
                "id": "kjsea-sst-2025-b-33-a",
                "subNumber": "(a)",
                "questionText": "The type of climate experienced in the region marked X is (1 mark)",
                "maxScore": 1
            },
            {
                "id": "kjsea-sst-2025-b-33-b",
                "subNumber": "(b)",
                "questionText": "Explain the main factor that has influenced high population density in the region marked Y. (2 marks)",
                "maxScore": 2
            },
            {
                "id": "kjsea-sst-2025-b-33-c",
                "subNumber": "(c)",
                "questionText": "State two economic uses of the multi-purpose project marked Z. (2 marks)",
                "maxScore": 2
            }
        ]
    },
    {
        "id": "kjsea-sst-2025-b-34",
        "questionNumber": 34,
        "questionText": "In groups, learners discussed factors for the scramble and partition of Africa by the European powers and presented their findings in class. Outline five factors that were contained in their findings. (5 marks)",
        "maxScore": 5
    }
]

data["sectionB"] = section_b

js_content = f"export const kjseaSst2025 = {json.dumps(data, indent=2, ensure_ascii=False)};\n"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Successfully added Section B to KJSEA Social Studies 2025.")
