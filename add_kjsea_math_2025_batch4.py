import json

new_questions = [
    {
      "id": "q31",
      "questionNumber": 31,
      "questionText": "Juma placed a metal rod against a wall. The foot of the rod was 3.6 m away from the wall. The top of the rod was 4.8 m above the ground.\n(a) Calculate the length of the rod.\n(b) If the rod has a volume of 600 cm\u00b3 and a mass of 2.4 kg, calculate the density of the rod.",
      "maxScore": 4,
      "modelAnswer": "(a) The rod, wall, and ground form a right-angled triangle. By Pythagoras' theorem:\nLength\u00b2 = Base\u00b2 + Height\u00b2\nLength\u00b2 = 3.6\u00b2 + 4.8\u00b2\nLength\u00b2 = 12.96 + 23.04 = 36.00\nLength = \u221a36 = 6.0 m.\n\n(b) Density = Mass / Volume\nMass = 2.4 kg = 2400 g\nVolume = 600 cm\u00b3\nDensity = 2400 g / 600 cm\u00b3 = 4 g/cm\u00b3.\n(Alternatively in SI units: Density = 2.4 kg / 0.0006 m\u00b3 = 4000 kg/m\u00b3)",
      "rubric": "Award 4 marks:\n(a) 1 mark for Pythagoras equation, 1 mark for correct length (6.0 m).\n(b) 1 mark for conversion and formula, 1 mark for correct density (4 g/cm\u00b3 or 4000 kg/m\u00b3).",
      "questionType": "structured"
    },
    {
      "id": "q32",
      "questionNumber": 32,
      "questionText": "A town P lies on the longitude 50\u00b0W. A town Q lies on the longitude 40\u00b0E. The local time at town Q is 4.00 p.m. Determine the local time at town P.",
      "maxScore": 4,
      "modelAnswer": "Longitude difference between P (50\u00b0W) and Q (40\u00b0E) = 50\u00b0 + 40\u00b0 = 90\u00b0.\nTime difference = 90\u00b0 \u00d7 4 minutes/degree = 360 minutes = 6 hours.\nSince town P is to the West of town Q, it is behind in time.\nLocal time at P = 4:00 p.m. - 6 hours = 10:00 a.m.",
      "rubric": "Award 4 marks:\n- 1 mark for finding longitude difference (90\u00b0).\n- 1 mark for converting to time difference (360 mins or 6 hrs).\n- 1 mark for recognizing P is behind Q (subtracting time).\n- 1 mark for correct local time at P (10:00 a.m.).",
      "questionType": "structured"
    },
    {
      "id": "q33",
      "questionNumber": 33,
      "questionText": "Festus imported a printing machine with a customs value of Ksh 1 200 000. He was charged an import duty at the rate of 20%, excise duty at the rate of 18% and Value Added Tax (VAT) at the rate of 16%. Determine the amount of money Festus paid as:\n(a) import duty;\n(b) excise duty;\n(c) Value Added Tax.",
      "maxScore": 5,
      "modelAnswer": "(a) Import duty = 20% of 1,200,000 = (20/100) \u00d7 1,200,000 = Ksh 240,000.\n\n(b) Excise duty is charged on the customs value plus import duty.\nValue for excise duty = 1,200,000 + 240,000 = Ksh 1,440,000.\nExcise duty = 18% of 1,440,000 = (18/100) \u00d7 1,440,000 = Ksh 259,200.\n\n(c) VAT is charged on the total value inclusive of import and excise duties.\nTotal value for VAT = 1,440,000 + 259,200 = Ksh 1,699,200.\nVAT = 16% of 1,699,200 = (16/100) \u00d7 1,699,200 = Ksh 271,872.",
      "rubric": "Award 5 marks:\n(a) 1 mark for correct method, 1 mark for Ksh 240,000.\n(b) 1 mark for finding the new base (1,440,000), 1 mark for Ksh 259,200.\n(c) 1 mark for Ksh 271,872.",
      "questionType": "structured"
    },
    {
      "id": "q34",
      "questionNumber": 34,
      "questionText": "A table top is in the shape of a parallelogram. The table top is represented by a drawing ABCD such that AB = 6 cm, AD = 4 cm and angle DAB = 45\u00b0. Using a ruler and a pair of compasses only, construct:\n(a) parallelogram ABCD;\n(b) perpendicular line from D to meet AB at E. Measure DE.",
      "maxScore": 5,
      "modelAnswer": "(a) Construction steps:\n1. Draw a line segment AB = 6 cm.\n2. At A, construct an angle of 45\u00b0 (by bisecting a 90\u00b0 angle).\n3. Along the 45\u00b0 line, mark point D such that AD = 4 cm.\n4. With D as centre and radius 6 cm, draw an arc. \n5. With B as centre and radius 4 cm, draw an arc to intersect the previous arc at C.\n6. Join CD and BC to complete the parallelogram.\n\n(b) Construction of perpendicular:\n1. Place the compass at D and draw an arc intersecting line AB at two points.\n2. From these points, draw two intersecting arcs below AB.\n3. Draw a line from D through the intersection to meet AB at E.\nMeasure DE. Using trigonometry to verify: DE = AD \u00d7 sin(45\u00b0) = 4 \u00d7 0.7071 \u2248 2.8 cm. Measurement should be approximately 2.8 cm.",
      "rubric": "Award 5 marks:\n(a) 1 mark for line AB, 1 mark for 45\u00b0 angle construction, 1 mark for completing the parallelogram.\n(b) 1 mark for constructing the perpendicular line, 1 mark for accurate measurement of DE (\u2248 2.8 cm \u00b1 0.1 cm).",
      "questionType": "structured"
    },
    {
      "id": "q35",
      "questionNumber": 35,
      "questionText": "The amount of money (y) that a farmer gets from selling milk is given by the equation y = 50x where x is the amount of milk in litres.\n(a) Use the equation to complete the following table.\nx | 0 | 0.5 | 1  | 1.5 | 2\ny | 0 |     | 50 | 75  | \n(b) On the grid provided, draw the graph of y = 50x.",
      "maxScore": 3,
      "modelAnswer": "(a) For x = 0.5, y = 50 \u00d7 0.5 = 25.\nFor x = 2, y = 50 \u00d7 2 = 100.\nThe completed values are 25 and 100.\n\n(b) To draw the graph:\n1. Plot the coordinates: (0, 0), (0.5, 25), (1, 50), (1.5, 75), and (2, 100) on the grid.\n2. Join the plotted points with a straight line using a ruler.",
      "rubric": "Award 3 marks:\n(a) 1 mark for correct table values (25 and 100).\n(b) 1 mark for plotting points correctly, 1 mark for drawing a straight line passing through the points.",
      "questionType": "structured"
    },
    {
      "id": "q36",
      "questionNumber": 36,
      "questionText": "Daudi was standing on a balcony. He observed a ball on the ground, 47 m from the foot of the building. The angle of depression of the ball from Daudi's position was 35\u00b0. Calculate the height from the ground to where Daudi was.",
      "maxScore": 2,
      "modelAnswer": "Let the height of Daudi from the ground be h.\nThe angle of depression (35\u00b0) is equal to the angle of elevation from the ball to the balcony due to alternate interior angles.\nUsing trigonometry (SOH CAH TOA):\ntan(35\u00b0) = Opposite / Adjacent\ntan(35\u00b0) = h / 47\nh = 47 \u00d7 tan(35\u00b0)\nh = 47 \u00d7 0.7002\nh \u2248 32.91 m.\nThe height is approximately 32.91 m.",
      "rubric": "Award 2 marks:\n- 1 mark for setting up the correct trigonometric equation (h = 47 \u00d7 tan 35\u00b0).\n- 1 mark for the correct answer (\u2248 32.91 m).",
      "questionType": "structured"
    },
    {
      "id": "q37",
      "questionNumber": 37,
      "questionText": "A learner marked three points A, B and C on a playing field. From point A she walked 50 m on a bearing of 120\u00b0 to reach point B. From point B she walked 70 m on a bearing of 210\u00b0 to reach point C.\n(a) Using a scale of 1 cm to represent 10 m, show the relative positions of points A, B and C.\n(b) Use the diagram to determine:\n(i) the distance from A to C;\n(ii) the bearing of C from A.",
      "maxScore": 5,
      "modelAnswer": "(a) Drawing the scale diagram:\nScale: 1 cm = 10 m.\nLength AB = 50 m / 10 = 5 cm. Bearing from North = 120\u00b0.\nLength BC = 70 m / 10 = 7 cm. Bearing from North = 210\u00b0.\nDraw North line at A, measure 120\u00b0 and draw 5 cm line to B. At B, draw North line, measure 210\u00b0 and draw 7 cm line to C.\n\n(b)(i) Distance AC:\nBy measuring the length AC on the scale diagram, it should be approximately 8.6 cm. \nActual distance = 8.6 cm \u00d7 10 m/cm = 86 m. (Can be verified by calculation: The angle inside the triangle at B is 90\u00b0. AC\u00b2 = 50\u00b2 + 70\u00b2 = 2500 + 4900 = 7400. AC = \u221a7400 \u2248 86 m).\n\n(b)(ii) Bearing of C from A:\nMeasure the angle clockwise from the North line at A to the line AC. It should be approximately 174.5\u00b0. (By calculation, interior angle A = arctan(70/50) = 54.5\u00b0. Total bearing = 120 + 54.5 = 174.5\u00b0).",
      "rubric": "Award 5 marks:\n(a) 3 marks: 1 for correct scale lines, 1 for angle at A, 1 for angle at B.\n(b)(i) 1 mark for correct distance (\u2248 86 m \u00b1 1 m).\n(b)(ii) 1 mark for correct bearing (\u2248 174\u00b0 - 175\u00b0).",
      "questionType": "structured"
    },
    {
      "id": "q38",
      "questionNumber": 38,
      "questionText": "Karen modelled a cuboid of dimensions 3 cm by 5 cm by 2 cm as shown.\n(a) Draw the net of the cuboid.\n(b) Calculate the total surface area of the cuboid from the net.",
      "maxScore": 5,
      "modelAnswer": "(a) The net of the cuboid is drawn by sketching 6 connected rectangles:\n- A central rectangle of 5 cm \u00d7 3 cm (base).\n- Attached to its 5 cm sides are two 5 cm \u00d7 2 cm rectangles (front and back faces).\n- Attached to its 3 cm sides are two 3 cm \u00d7 2 cm rectangles (side faces).\n- Attached to one of the 5 cm \u00d7 2 cm faces is another 5 cm \u00d7 3 cm rectangle (top face).\n\n(b) Total surface area is the sum of the areas of the 6 rectangles in the net.\nArea = 2(lw) + 2(lh) + 2(wh)\nArea = 2(5 \u00d7 3) + 2(5 \u00d7 2) + 2(3 \u00d7 2)\nArea = 2(15) + 2(10) + 2(6)\nArea = 30 + 20 + 12 = 62 cm\u00b2.",
      "rubric": "Award 5 marks:\n(a) 2 marks for a correctly drawn net with 6 appropriate rectangles.\n(b) 3 marks: 1 for correct formula/method, 1 for substitution, 1 for final correct answer (62 cm\u00b2).",
      "questionType": "structured"
    }
]

file_path = 'src/data/kjsea-math-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of sectionB array (the last bracket before the closing brace)
# Look for the last ']' in the file
insert_pos = content.rfind(']')

# Generate JSON for the new questions
new_json = json.dumps(new_questions, indent=2)
# Remove the outer brackets of the JSON list to inject the objects
new_json = new_json[new_json.find('{'):new_json.rfind('}')+1]

# Inject the new objects
prefix = content[:insert_pos].strip()
suffix = content[insert_pos:]

new_content = prefix + ',\n  ' + new_json + '\n' + suffix

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 4 (Q31-Q38) for KJSEA Math 2025 appended!")
