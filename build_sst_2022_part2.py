import json
import os

filepath = "src/data/kpsea-sst-parta-2022.js"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kpseaSstParta2022 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

q12_to_20 = [
  {
    "id": "q12",
    "questionNumber": 12,
    "questionText": "The main role of a soloist in a folk song is to",
    "questionType": "multiple-choice",
    "options": [
      {"text": "play musical instruments", "isCorrect": False},
      {"text": "entertain the audience", "isCorrect": False},
      {"text": "lead the performance", "isCorrect": True},
      {"text": "train the choir.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **lead the performance.**\n\n**Analysis of the Correct Answer:**\nIn folk music, the soloist is the lead singer who starts the song, introduces the melody and lyrics, and guides the rest of the group (the chorus) in a call-and-response style. Their primary role is to lead the performance.\n\n**Why Other Options Are Incorrect:**\n- **play musical instruments:** Instrumentalists play instruments; a soloist is primarily a vocalist.\n- **entertain the audience:** While they do entertain, the *main* technical role within the group is leading.\n- **train the choir:** This is the role of a choir director or music teacher, not specifically the soloist during a performance."
  },
  {
    "id": "q13",
    "questionNumber": 13,
    "questionText": "Which of the sentences below is the last line of the first stanza of the Kenya National Anthem?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Firm may we stand to defend", "isCorrect": False},
      {"text": "Fill every heart with thanksgiving", "isCorrect": False},
      {"text": "Plenty be found within our borders", "isCorrect": True},
      {"text": "Service be our earnest endeavour", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Plenty be found within our borders.**\n\n**Analysis of the Correct Answer:**\nThe first stanza of the Kenya National Anthem in English is:\n\"O God of all creation,\nBless this our land and nation.\nJustice be our shield and defender,\nMay we dwell in unity,\nPeace and liberty,\n**Plenty be found within our borders.**\"\n\n**Why Other Options Are Incorrect:**\n- **Firm may we stand to defend:** This is in the second stanza.\n- **Fill every heart with thanksgiving:** This is in the third stanza.\n- **Service be our earnest endeavour:** This is in the third stanza."
  },
  {
    "id": "q14",
    "questionNumber": 14,
    "questionText": "Which of the following is **not** a way of tuning Kenyan indigenous drums?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Tightening laces", "isCorrect": False},
      {"text": "Rubbing the membrane", "isCorrect": True},
      {"text": "Tightening pegs", "isCorrect": False},
      {"text": "Warming the membrane", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Rubbing the membrane.**\n\n**Analysis of the Correct Answer:**\nTuning an indigenous drum involves changing the tension of the membrane (skin). You can increase tension by warming the membrane near a fire (which shrinks it), tightening the laces/cords, or tightening the pegs that hold the skin. Rubbing the membrane produces a sound (friction) but does not tune or change the pitch of the drum.\n\n**Why Other Options Are Incorrect:**\n- **Tightening laces, Tightening pegs, Warming the membrane:** These are all correct methods of tuning an indigenous drum by increasing tension."
  },
  {
    "id": "q15",
    "questionNumber": 15,
    "questionText": "Which of these statements about the descant recorder is **false**?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "It is a wind instrument.", "isCorrect": False},
      {"text": "It should be cleaned before and after playing.", "isCorrect": False},
      {"text": "It is played by bowing.", "isCorrect": True},
      {"text": "It should be properly assembled.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **It is played by bowing.**\n\n**Analysis of the Correct Answer:**\nThe descant recorder is a woodwind instrument. Sound is produced by blowing air into the mouthpiece. It is not a string instrument, so it is never played by bowing (using a bow across strings).\n\n**Why Other Options Are Incorrect:**\n- **It is a wind instrument:** This is true.\n- **It should be cleaned... / It should be properly assembled:** These are true maintenance and preparation steps for playing a recorder."
  },
  {
    "id": "q16",
    "questionNumber": 16,
    "questionText": "Which of the following words best describe how a lullaby should be sung?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Loudly and softly", "isCorrect": False},
      {"text": "Softly and sadly", "isCorrect": False},
      {"text": "Slowly and softly", "isCorrect": True},
      {"text": "Fast and softly", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Slowly and softly.**\n\n**Analysis of the Correct Answer:**\nA lullaby is a soothing song sung to children to help them fall asleep. To achieve a calming effect, it must be sung slowly (gentle tempo) and softly (low volume). \n\n**Why Other Options Are Incorrect:**\n- **Loudly:** Would wake the baby up.\n- **Sadly:** A lullaby is meant to be comforting, not depressing.\n- **Fast:** A fast tempo would excite the baby rather than put them to sleep."
  },
  {
    "id": "q17",
    "questionNumber": 17,
    "questionText": "We can respond to music in the following ways **except**",
    "questionType": "multiple-choice",
    "options": [
      {"text": "dancing to the music", "isCorrect": False},
      {"text": "talking while listening to the music", "isCorrect": True},
      {"text": "talking about the music", "isCorrect": False},
      {"text": "clapping to the rhythm of the music.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **talking while listening to the music.**\n\n**Analysis of the Correct Answer:**\nResponding to music involves actively engaging with it, such as dancing, clapping, or discussing its meaning and feelings (talking *about* it). However, simply chatting or talking over the music while it plays shows a lack of attention and is considered disrespectful rather than an active musical response.\n\n**Why Other Options Are Incorrect:**\n- **dancing / clapping:** These are physical responses to rhythm.\n- **talking about the music:** This is an analytical/emotional response."
  },
  {
    "id": "q18",
    "questionNumber": 18,
    "questionText": "____ are examples of ornaments used in a Kenyan folk dance.",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Face paintings, hand paintings and jingles", "isCorrect": False},
      {"text": "Necklace, bangles and anklets", "isCorrect": True},
      {"text": "Face paintings, jingles and headgear", "isCorrect": False},
      {"text": "Costumes, jingles and necklaces", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Necklace, bangles and anklets.**\n\n**Analysis of the Correct Answer:**\nOrnaments are decorative items worn on the body to enhance beauty during a performance. Necklaces, bangles, and anklets are all forms of jewelry/ornaments. \n\n**Why Other Options Are Incorrect:**\n- **Face/hand paintings:** These are body art/makeup, not worn ornaments.\n- **Jingles:** While worn, they also serve as rhythmic instruments.\n- **Costumes:** These are clothing/attire, distinct from the smaller decorative ornaments."
  },
  {
    "id": "q19",
    "questionNumber": 19,
    "questionText": "Study the rhythm below:\n\n[Image showing 4 pairs of quavers (eighth notes) = 8 syllables total]\n\nWhich of the sentences below **cannot** be fitted to the rhythm above?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "Twende tukalime shamba", "isCorrect": False},
      {"text": "Tuhifadhi mazingira", "isCorrect": False},
      {"text": "Nahisi njaa sana", "isCorrect": True},
      {"text": "Nina furaha moyoni", "isCorrect": False}
    ],
    "explanation": "The correct answer is **Nahisi njaa sana.**\n\n**Analysis of the Correct Answer:**\nThe rhythm shown consists of 4 pairs of eighth notes (quavers), which totals 8 beats/syllables.\n- *Twe-nde tu-ka-li-me sha-mba* = 8 syllables\n- *Tu-hi-fa-dhi ma-zi-ngi-ra* = 8 syllables\n- *Ni-na fu-ra-ha mo-yo-ni* = 8 syllables\n- *Na-hi-si nja-a sa-na* = 7 syllables (even stretching njaa, it doesn't naturally fit an 8-beat even rhythm without a rest). It naturally reads as 6 or 7 syllables, making it the odd one out.\n\n**Why Other Options Are Incorrect:**\n- The other phrases perfectly match the 8-syllable structure."
  },
  {
    "id": "q20",
    "questionNumber": 20,
    "questionText": "Below are diagrams of two Kenyan indigenous instruments.\n\n(i) [Diagram of a xylophone/marimba with beaters]\n(ii) [Diagram of a one-stringed fiddle (like an orutu) with a bow]\n\nWhich statement is **true** about the instruments above?",
    "questionType": "multiple-choice",
    "options": [
      {"text": "They have a resonator and can play a melody.", "isCorrect": True},
      {"text": "They are tuned the same way and can play a melody.", "isCorrect": False},
      {"text": "They have a resonator and are played the same way.", "isCorrect": False},
      {"text": "They are made of the same material and are made the same way.", "isCorrect": False}
    ],
    "explanation": "The correct answer is **They have a resonator and can play a melody.**\n\n**Analysis of the Correct Answer:**\nInstrument (i) is a melodic idiophone (marimba), which usually has resonators (like gourds or tubes) underneath the wooden slats. Instrument (ii) is a stringed instrument (fiddle), which has a soundbox (resonator) covered with skin. Both instruments are capable of producing different pitches, meaning they can play a melody. \n\n**Why Other Options Are Incorrect:**\n- **Tuned the same way:** A marimba is tuned by carving the wooden slats; a fiddle is tuned by tightening the string.\n- **Played the same way:** One is struck with beaters, the other is bowed.\n- **Same material:** The marimba is primarily wood, while the fiddle involves a tin/gourd, animal skin, and a string."
  }
]

data["sectionA"].extend(q12_to_20)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(f"export const kpseaSstParta2022 = {json.dumps(data, indent=2)};\n")

print("Updated kpsea-sst-parta-2022.js with Q12-Q20 successfully.")
