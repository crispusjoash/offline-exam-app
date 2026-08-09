import json
import re

file_path = 'src/data/kpsea-sst-parta-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract JSON part
json_str = re.sub(r'^export const [a-zA-Z0-9_]+ = ', '', content)
json_str = re.sub(r';\s*$', '', json_str)
paper_structure = json.loads(json_str)

new_questions = [
    {
      'id': 'q16',
      'questionNumber': 16,
      'questionText': 'Which one of the following sets of tools is more suitable for carving a wooden toy?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Sandpaper, razor blade, knife.', 'isCorrect': False },
        { 'text': 'Mallet, adze, broken glass.', 'isCorrect': False },
        { 'text': 'Mallet, chisel, sandpaper.', 'isCorrect': True },
        { 'text': 'Knife, broken glass, mallet.', 'isCorrect': False }
      ],
      'explanation': 'Mallet and chisel are the primary tools used for carving wood, while sandpaper is used for finishing and smoothing the toy.'
    },
    {
      'id': 'q17',
      'questionNumber': 17,
      'questionText': 'Which of the following is not an aspect of etiquette in a group folk song performance?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Dressing appropriately.', 'isCorrect': False },
        { 'text': 'Incorporating decent movements.', 'isCorrect': False },
        { 'text': 'Keeping to one\'s role in the performance.', 'isCorrect': False },
        { 'text': 'Using accompaniment.', 'isCorrect': True }
      ],
      'explanation': 'Using accompaniment is a musical arrangement choice, not a rule of etiquette or conduct for the performers.'
    },
    {
      'id': 'q18',
      'questionNumber': 18,
      'questionText': 'During a gymnastics display, your school\'s team was awarded for being the best in the three-action gymnastic sequences. The three-action sequence in gymnastics means a performance of ________',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'any three gymnastics skills that are easy to perform.', 'isCorrect': False },
        { 'text': 'three gymnastics skills that flow into each other.', 'isCorrect': True },
        { 'text': 'any three rolling skills that flow into each other.', 'isCorrect': False },
        { 'text': 'any routine that consists of any three gymnastics skills.', 'isCorrect': False }
      ],
      'explanation': 'A sequence in gymnastics involves linking skills together so they flow smoothly into one another without interruption.'
    },
    {
      'id': 'q19',
      'questionNumber': 19,
      'questionText': 'Which one of the following materials is not used in preparing papier mâché?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Water.', 'isCorrect': False },
        { 'text': 'Newspaper.', 'isCorrect': False },
        { 'text': 'Starch.', 'isCorrect': False },
        { 'text': 'Fibre.', 'isCorrect': True }
      ],
      'explanation': 'Papier-mâché is typically made from torn paper (like newspaper), water, and a binder (like starch or glue). Fibre is not a standard ingredient.'
    },
    {
      'id': 'q20',
      'questionNumber': 20,
      'questionText': 'Which of the following statements is true about a folksong and a folkdance?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'A folksong emphasizes on costuming while a folkdance emphasizes on instrumentation.', 'isCorrect': False },
        { 'text': 'A folksong focuses on singing while a folkdance focuses on dancing.', 'isCorrect': True },
        { 'text': 'A folksong is led by singers while a folkdance is led by dancers.', 'isCorrect': False },
        { 'text': 'A folksong has instrumentation while a folkdance has no instrumentation.', 'isCorrect': False }
      ],
      'explanation': 'The primary distinction is that a folksong is a vocal performance (singing), whereas a folkdance is primarily a physical performance (dancing).'
    },
    {
      'id': 'q21',
      'questionNumber': 21,
      'questionText': 'Learners were asked to perform side roll in gymnastics. Which one of the following is a safety measure that they should observe?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Performing the skills under a shade and avoiding direct sunlight.', 'isCorrect': False },
        { 'text': 'Performing on a flat ground free from objects and holes.', 'isCorrect': True },
        { 'text': 'Performing after running around the field several times.', 'isCorrect': False },
        { 'text': 'Performing very early in the morning before getting tired.', 'isCorrect': False }
      ],
      'explanation': 'Ensuring the performance area is flat and free of hazards like objects and holes is a critical physical safety measure to prevent injuries.'
    },
    {
      'id': 'q22',
      'questionNumber': 22,
      'questionText': 'Temi needs to use one of the following techniques to decorate a dry clay pot. Which one is suitable?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Piercing.', 'isCorrect': False },
        { 'text': 'Painting.', 'isCorrect': True },
        { 'text': 'Texturing.', 'isCorrect': False },
        { 'text': 'Embedding.', 'isCorrect': False }
      ],
      'explanation': 'Painting is suitable for a dry (or fired) clay pot. Techniques like piercing, texturing, and embedding must be done while the clay is still wet or leather-hard.'
    },
    {
      'id': 'q23',
      'questionNumber': 23,
      'questionText': 'The following are roles played by a fiddle in a folksong performance except',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'accompanying the singing', 'isCorrect': False },
        { 'text': 'pitching the singing', 'isCorrect': False },
        { 'text': 'playing a percussive role', 'isCorrect': True },
        { 'text': 'playing interludes.', 'isCorrect': False }
      ],
      'explanation': 'A fiddle is a string instrument played with a bow (melodic/harmonic), whereas a percussive role is played by instruments like drums or shakers.'
    },
    {
      'id': 'q24',
      'questionNumber': 24,
      'questionText': 'A physical and health education teacher displayed a variety of balls used in playing different games. The shape of the ball that is used to play football is',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'oval', 'isCorrect': False },
        { 'text': 'cuboid', 'isCorrect': False },
        { 'text': 'spherical', 'isCorrect': True },
        { 'text': 'cylindrical.', 'isCorrect': False }
      ],
      'explanation': 'A standard association football (soccer ball) is spherical in shape.'
    },
    {
      'id': 'q25',
      'questionNumber': 25,
      'questionText': 'Which one of the following surfaces can be improvised to mount drawings?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Manilla paper.', 'isCorrect': False },
        { 'text': 'Hard board.', 'isCorrect': False },
        { 'text': 'Sugar paper.', 'isCorrect': False },
        { 'text': 'Old carton boxes.', 'isCorrect': True }
      ],
      'explanation': 'Old carton boxes are sturdy and readily available, making them a great improvised material for mounting drawings.'
    },
    {
      'id': 'q26',
      'questionNumber': 26,
      'questionText': 'Which of the following is not a way of caring for and maintaining a string instrument?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Hanging it on the wall.', 'isCorrect': False },
        { 'text': 'Washing it with water.', 'isCorrect': True },
        { 'text': 'Putting it in a storage box.', 'isCorrect': False },
        { 'text': 'Putting it against the wall.', 'isCorrect': False }
      ],
      'explanation': 'Washing a string instrument (usually made of wood) with water will damage the wood and the strings.'
    },
    {
      'id': 'q27',
      'questionNumber': 27,
      'questionText': 'During a game of rounders, learners were asked to observe safety measures to avoid injuries. Which one of the following is the suitable safety measure they should observe?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'The batsman to throw the ball slowly.', 'isCorrect': False },
        { 'text': 'Batting team to wear correct hand gloves.', 'isCorrect': False },
        { 'text': 'Batter to closely stand behind the bowler.', 'isCorrect': False },
        { 'text': 'Fielders to avoid obstructing runners.', 'isCorrect': True }
      ],
      'explanation': 'Fielders obstructing runners can cause severe collisions and injuries. Avoiding obstruction is a key safety rule.'
    },
    {
      'id': 'q28',
      'questionNumber': 28,
      'questionText': 'Which one of the following is the correct order of mounting a painting using the matt technique?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Cut, measure, paste and centre it.', 'isCorrect': False },
        { 'text': 'Paste, measure, centre and cut it.', 'isCorrect': False },
        { 'text': 'Cut, paste, centre and measure it.', 'isCorrect': False },
        { 'text': 'Measure, cut, centre and paste it.', 'isCorrect': True }
      ],
      'explanation': 'You must first measure the dimensions, then cut the matt board, centre the artwork within the window, and finally paste/secure it.'
    },
    {
      'id': 'q29',
      'questionNumber': 29,
      'questionText': 'Grade 6 learners visited a cultural centre and were required to record folk-dance performances. The learners used the following devices except',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'camera', 'isCorrect': False },
        { 'text': 'flash disk', 'isCorrect': True },
        { 'text': 'smart phone', 'isCorrect': False },
        { 'text': 'tablet.', 'isCorrect': False }
      ],
      'explanation': 'A flash disk is a storage device, not a recording device. Cameras, smartphones, and tablets have lenses to record videos.'
    },
    {
      'id': 'q30',
      'questionNumber': 30,
      'questionText': 'The following picture shows a learner playing the ball in a game of volleyball.\n\n[Image: A learner with bent knees, arms together and extended downwards, playing the ball].\n\nThe skill that the learner is using to play the ball is known as',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'blocking', 'isCorrect': False },
        { 'text': 'digging', 'isCorrect': True },
        { 'text': 'spiking', 'isCorrect': False },
        { 'text': 'serving.', 'isCorrect': False }
      ],
      'explanation': 'The posture shown (bent knees, arms joined and extended to hit the ball underhand) is characteristic of a dig or forearm pass.'
    },
    {
      'id': 'q31',
      'questionNumber': 31,
      'questionText': 'Study the following map of Eastern Africa and use it to answer questions 31 and 32.\n\n[Map of Eastern Africa. Region F is the northern part near the Red Sea. Arrow G points to Lake Victoria from the west].\n\nThe climatic region marked F is',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'modified equatorial', 'isCorrect': False },
        { 'text': 'modified tropical', 'isCorrect': False },
        { 'text': 'desert', 'isCorrect': True },
        { 'text': 'mountain.', 'isCorrect': False }
      ],
      'explanation': 'Region F covers the northern parts of Eastern Africa (Sudan/Eritrea/Djibouti area), which experiences an arid/desert climate.'
    },
    {
      'id': 'q32',
      'questionNumber': 32,
      'questionText': 'Which language group migrated into Eastern Africa using the route marked G?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Nilotes.', 'isCorrect': False },
        { 'text': 'Bantus.', 'isCorrect': True },
        { 'text': 'Semites.', 'isCorrect': False },
        { 'text': 'Cushites.', 'isCorrect': False }
      ],
      'explanation': 'Route G shows movement from the Congo Basin towards the Lake Victoria region, which represents the migration route of the Bantus.'
    },
    {
      'id': 'q33',
      'questionNumber': 33,
      'questionText': 'Grade 6 learners are planning to harvest the beans they had planted. Which weather season is suitable for the activity?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Dry.', 'isCorrect': True },
        { 'text': 'Cold.', 'isCorrect': False },
        { 'text': 'Windy.', 'isCorrect': False },
        { 'text': 'Rainy.', 'isCorrect': False }
      ],
      'explanation': 'Harvesting beans is best done during the dry season so the beans can dry properly and avoid rotting.'
    },
    {
      'id': 'q34',
      'questionNumber': 34,
      'questionText': 'Grade 4 learners created a corner in their class to showcase cultural items during a school cultural day. Which one of the following consists of cultural items only?',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'Baskets, beads, sufurias.', 'isCorrect': False },
        { 'text': 'Calabash, arrows, carvings.', 'isCorrect': True },
        { 'text': 'Gourds, drums, plates.', 'isCorrect': False },
        { 'text': 'Stove, bows, pots.', 'isCorrect': False }
      ],
      'explanation': 'Calabashes, arrows, and carvings are traditional cultural items. Sufurias, plates, and stoves are modern/utilitarian items.'
    },
    {
      'id': 'q35',
      'questionNumber': 35,
      'questionText': 'Soil is one of the natural resources found in Hema school. The best way of taking care of this resource is by',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'ploughing the soil repeatedly', 'isCorrect': False },
        { 'text': 'starting a nature corner', 'isCorrect': False },
        { 'text': 'treating the soil with chemicals', 'isCorrect': False },
        { 'text': 'planting cover crops.', 'isCorrect': True }
      ],
      'explanation': 'Planting cover crops helps prevent soil erosion, conserves moisture, and maintains soil structure.'
    },
    {
      'id': 'q36',
      'questionNumber': 36,
      'questionText': 'During a radio lesson on \'beef farming in Kenya\', a learner noted that imported beef products affect local beef farming. This is because it may lead to',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'increased prices of beef products', 'isCorrect': False },
        { 'text': 'reduced market for local beef products', 'isCorrect': True },
        { 'text': 'increased foreign exchange earnings', 'isCorrect': False },
        { 'text': 'reduced import trade.', 'isCorrect': False }
      ],
      'explanation': 'Importing beef creates competition for local farmers, leading to a reduced market share for locally produced beef products.'
    },
    {
      'id': 'q37',
      'questionNumber': 37,
      'questionText': 'Learners at Masomo school watched a video clip on the effects of mining on the environment. Which of the following is an effect they are likely to have observed? It',
      'questionType': 'multiple-choice',
      'options': [
        { 'text': 'creates many sceneries', 'isCorrect': False },
        { 'text': 'creates land for farming', 'isCorrect': False },
        { 'text': 'leads to ugly landscape', 'isCorrect': True },
        { 'text': 'leads to growth of dense vegetation.', 'isCorrect': False }
      ],
      'explanation': 'Mining often involves digging deep pits and removing vegetation, resulting in land degradation and an ugly landscape.'
    }
]

paper_structure['sectionA'].extend(new_questions)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('export const kpseaSstParta2024 = ' + json.dumps(paper_structure, indent=2) + ';\n')

print('Questions 16 to 37 successfully appended!')
