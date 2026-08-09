import json
import os

new_questions = [
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "Which one of the following sets of tools is more suitable for carving a wooden toy?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Sandpaper, razor blade, knife.", "isCorrect": False },
        { "text": "Mallet, adze, broken glass.", "isCorrect": False },
        { "text": "Mallet, chisel, sandpaper.", "isCorrect": True },
        { "text": "Knife, broken glass, mallet.", "isCorrect": False }
      ],
      "explanation": "A mallet and chisel are the standard and most effective tools for carving wood. Sandpaper is then used for smoothing the finished toy."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "Which of the following is not an aspect of etiquette in a group folk song performance?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Dressing appropriately.", "isCorrect": False },
        { "text": "Incorporating decent movements.", "isCorrect": False },
        { "text": "Keeping to one's role in the performance.", "isCorrect": False },
        { "text": "Using accompaniment.", "isCorrect": True }
      ],
      "explanation": "Etiquette refers to proper behavior and presentation, such as dressing appropriately, using decent movements, and sticking to your role. Using musical accompaniment is a performance choice, not a matter of etiquette."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "During a gymnastics display, your school's team was awarded for being the best in the three-action gymnastic sequences. The three-action sequence in gymnastics means a performance of",
      "questionType": "multiple-choice",
      "options": [
        { "text": "any three gymnastics skills that are easy to perform.", "isCorrect": False },
        { "text": "three gymnastics skills that flow into each other.", "isCorrect": True },
        { "text": "any three rolling skills that flow into each other.", "isCorrect": False },
        { "text": "any routine that consists of any three gymnastics skills.", "isCorrect": False }
      ],
      "explanation": "A sequence in gymnastics involves performing multiple skills consecutively in a way that they flow smoothly from one to the next without awkward pauses."
    },
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "Which one of the following materials is not used in preparing papier m\u00e2ch\u00e9?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Water.", "isCorrect": False },
        { "text": "Newspaper.", "isCorrect": False },
        { "text": "Starch.", "isCorrect": False },
        { "text": "Fibre.", "isCorrect": True }
      ],
      "explanation": "Papier-m\u00e2ch\u00e9 is typically made from torn or mashed paper (like newspaper), water, and a binder (like starch or glue). Fibre is not a standard ingredient."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "Which of the following statements is true about a folksong and a folkdance?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "A folksong emphasizes on costuming while a folkdance emphasizes on instrumentation.", "isCorrect": False },
        { "text": "A folksong focuses on singing while a folkdance focuses on dancing.", "isCorrect": True },
        { "text": "A folksong is led by singers while a folkdance is led by dancers.", "isCorrect": False },
        { "text": "A folksong has instrumentation while a folkdance has no instrumentation.", "isCorrect": False }
      ],
      "explanation": "The primary distinction is their focus: a folksong is primarily a vocal musical performance (singing), whereas a folkdance is primarily a physical performance (dancing), though they often accompany each other."
    },
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "Learners were asked to perform side roll in gymnastics. Which one of the following is a safety measure that they should observe?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Performing the skills under a shade and avoiding direct sunlight.", "isCorrect": False },
        { "text": "Performing on a flat ground free from objects and holes.", "isCorrect": True },
        { "text": "Performing after running around the field several times.", "isCorrect": False },
        { "text": "Performing very early in the morning before getting tired.", "isCorrect": False }
      ],
      "explanation": "In physical activities like rolling, ensuring the area is flat and free of hazards (objects, holes) is a critical safety measure to prevent injuries."
    },
    {
      "id": "q22",
      "questionNumber": 22,
      "questionText": "Temi needs to use one of the following techniques to decorate a dry clay pot. Which one is suitable?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Piercing.", "isCorrect": False },
        { "text": "Painting.", "isCorrect": True },
        { "text": "Texturing.", "isCorrect": False },
        { "text": "Embedding.", "isCorrect": False }
      ],
      "explanation": "Piercing, texturing, and embedding must be done while the clay is still wet or leather-hard. Once a clay pot is dry (or fired), painting is the suitable technique for decoration."
    },
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "The following are roles played by a fiddle in a folksong performance except",
      "questionType": "multiple-choice",
      "options": [
        { "text": "accompanying the singing", "isCorrect": False },
        { "text": "pitching the singing", "isCorrect": False },
        { "text": "playing a percussive role", "isCorrect": True },
        { "text": "playing interludes.", "isCorrect": False }
      ],
      "explanation": "A fiddle is a string instrument that plays melodies, accompanies singers, sets the pitch, and plays interludes. Percussive roles are played by drums or shakers."
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "A physical and health education teacher displayed a variety of balls used in playing different games. The shape of the ball that is used to play football is",
      "questionType": "multiple-choice",
      "options": [
        { "text": "oval", "isCorrect": False },
        { "text": "cuboid", "isCorrect": False },
        { "text": "spherical", "isCorrect": True },
        { "text": "cylindrical.", "isCorrect": False }
      ],
      "explanation": "A standard football (soccer ball) is spherical (perfectly round) in shape. An oval ball is used in rugby."
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "Which one of the following surfaces can be improvised to mount drawings?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Manilla paper.", "isCorrect": False },
        { "text": "Hard board.", "isCorrect": False },
        { "text": "Sugar paper.", "isCorrect": False },
        { "text": "Old carton boxes.", "isCorrect": True }
      ],
      "explanation": "While hardboard is a standard mounting surface, old carton boxes provide a sturdy, accessible, and cheap material that can be effectively improvised for mounting artwork."
    },
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "Which of the following is not a way of caring for and maintaining a string instrument?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Hanging it on the wall.", "isCorrect": False },
        { "text": "Washing it with water.", "isCorrect": True },
        { "text": "Putting it in a storage box.", "isCorrect": False },
        { "text": "Putting it against the wall.", "isCorrect": False }
      ],
      "explanation": "String instruments are usually made of wood, and washing them with water can warp the wood and damage the instrument."
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "During a game of rounders, learners were asked to observe safety measures to avoid injuries. Which one of the following is the suitable safety measure they should observe?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "The batsman to throw the ball slowly.", "isCorrect": False },
        { "text": "Batting team to wear correct hand gloves.", "isCorrect": False },
        { "text": "Batter to closely stand behind the bowler.", "isCorrect": False },
        { "text": "Fielders to avoid obstructing runners.", "isCorrect": True }
      ],
      "explanation": "In games involving running between bases (like rounders), fielders must not obstruct runners to prevent dangerous physical collisions."
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "Which one of the following is the correct order of mounting a painting using the matt technique?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Cut, measure, paste and centre it.", "isCorrect": False },
        { "text": "Paste, measure, centre and cut it.", "isCorrect": False },
        { "text": "Cut, paste, centre and measure it.", "isCorrect": False },
        { "text": "Measure, cut, centre and paste it.", "isCorrect": True }
      ],
      "explanation": "The logical sequence for matting is to first measure the dimensions, cut the window out of the mount, centre the artwork behind the window, and finally paste it securely."
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "Grade 6 learners visited a cultural centre and were required to record folk-dance performances. The learners used the following devices except",
      "questionType": "multiple-choice",
      "options": [
        { "text": "camera", "isCorrect": False },
        { "text": "flash disk", "isCorrect": True },
        { "text": "smart phone", "isCorrect": False },
        { "text": "tablet.", "isCorrect": False }
      ],
      "explanation": "Cameras, smartphones, and tablets have built-in lenses and microphones to record performances. A flash disk is only a storage device and cannot record directly."
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "The following picture shows a learner playing the ball in a game of volleyball.\n\n[Image: A learner with bent knees and arms held straight together in front, ready to hit the ball from below.]\n\nThe skill that the learner is using to play the ball is known as",
      "questionType": "multiple-choice",
      "options": [
        { "text": "blocking", "isCorrect": False },
        { "text": "digging", "isCorrect": True },
        { "text": "spiking", "isCorrect": False },
        { "text": "serving.", "isCorrect": False }
      ],
      "explanation": "The posture depicted, with hands joined together and extended forward to receive a low ball, is the digging (or forearm pass) skill in volleyball."
    }
]

file_path = 'src/data/kpsea-sst-parta-2024.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content.replace('export const kpseaSstParta2024 = ', '').rstrip(';\n')
data = json.loads(json_str)

data['sectionA'].extend(new_questions)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstParta2024 = ' + json.dumps(data, indent=2) + ';\n')

print("Batch 2 questions inserted successfully!")
