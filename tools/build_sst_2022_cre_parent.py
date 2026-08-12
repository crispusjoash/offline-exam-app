import json

cre_template = {
  "id": "kpsea-sst-cre-2022",
  "title": "KPSEA 2022 Social Studies & Creative Arts (CRE)",
  "subject": "CRE",
  "year": "2022",
  "isSubPaper": True,
  "durationMinutes": 0,
  "sharedContexts": {},
  "sectionA": [
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "Your class teacher asked four learners who have the talent of singing to write ways of developing their talent during their free time. They gave the following:\n\nKen - Listening to gospel songs.\nBetty - Talking with friends about singing.\nTom - Drawing pictures of great musicians.\nJoan - Practising in a church choir\n\nWho among those learners gave the **best** way?",
      "questionType": "multiple-choice",
      "options": [
        {"text": "Ken", "isCorrect": False},
        {"text": "Betty", "isCorrect": False},
        {"text": "Tom", "isCorrect": False},
        {"text": "Joan", "isCorrect": True}
      ],
      "explanation": "The correct answer is **Joan.**\n\n**Analysis of the Correct Answer:**\nGod-given talents, like singing, need to be actively nurtured and developed. The most effective way to improve a singing talent is through consistent, active practice. By joining and practising in a church choir, Joan is actively using and improving her vocal skills in a structured environment.\n\n**Why Other Options Are Incorrect:**\n- **Ken (Listening):** While it helps with appreciation, passive listening doesn't train vocal cords.\n- **Betty (Talking):** Talking about it doesn't improve the actual skill.\n- **Tom (Drawing):** Drawing is a completely different talent (Art) and does not develop singing."
    },
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "After learning about child labour, your class teacher told learners to summarise two forms of child labour. Choose a **correct** response from the choices given below.",
      "questionType": "multiple-choice",
      "options": [
        {"text": "Washing utensils at home. Taking care of a younger brother.", "isCorrect": False},
        {"text": "Looking after sheep at home. Tilling the farm at home.", "isCorrect": False},
        {"text": "Selling fruits in the market. Harvesting coffee to get money.", "isCorrect": True},
        {"text": "Cooking for the family. Fetching water at home.", "isCorrect": False}
      ],
      "explanation": "The correct answer is **Selling fruits in the market. Harvesting coffee to get money.**\n\n**Analysis of the Correct Answer:**\nChild labour involves work that exploits children for economic gain, often forcing them to drop out of school or exposing them to harsh, adult-level working conditions. Selling items in a public market and working on commercial plantations for wages are illegal forms of child labour.\n\n**Why Other Options Are Incorrect:**\n- **A, B, D:** These describe light, age-appropriate household chores that children are expected to do to help their families, provided they do not interfere with schooling."
    }
  ]
}

with open("src/data/kpsea-sst-cre-2022.js", "w", encoding="utf-8") as f:
    f.write(f"export const kpseaSstCre2022 = {json.dumps(cre_template, indent=2)};\n")

print("Created kpsea-sst-cre-2022.js successfully.")

parent_template = {
  "id": "kpsea-sst-2022",
  "title": "KPSEA 2022 Social Studies & Creative Arts",
  "subject": "Social Studies & Creative Arts",
  "year": "2022",
  "isParentPaper": True,
  "durationMinutes": 100,
  "timeAllowed": 100,
  "sectionA": []
}

with open("src/data/kpsea-sst-2022.js", "w", encoding="utf-8") as f:
    f.write(f"export const kpseaSst2022 = {json.dumps(parent_template, indent=2)};\n")

print("Created kpsea-sst-2022.js successfully.")
