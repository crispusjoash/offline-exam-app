export const kpseaMath2023 = {
  "id": "kpsea-math-2023",
  "title": "KPSEA 2023 Mathematics",
  "subject": "Mathematics",
  "year": "2023",
  "durationMinutes": 80,
  "sharedContexts": {
    "ctx-q12": {
      "title": "Shape on board",
      "type": "image",
      "imagePath": "/assets/q12.svg",
      "caption": "A teacher drew the following shape on the board."
    },
    "ctx-q14": {
      "title": "Rabbit hutch wall",
      "type": "image",
      "imagePath": "/assets/q14.svg",
      "caption": "A wall of a rabbit hutch is in the shape of a rectangle and a triangle as shown."
    },
    "ctx-q19": {
      "title": "Clock Face",
      "type": "image",
      "imagePath": "/assets/q19_clock.png",
      "caption": "Wambua began his performance in the afternoon at the time shown on the clock face."
    },
    "ctx-q20": {
      "title": "Travel Timetable",
      "type": "image",
      "imagePath": "/assets/q20_table.png",
      "caption": "The table shows a travel timetable for a train from Manga station to Pate through Nanga."
    },
    "ctx-q23": {
      "title": "Triangle LMN",
      "type": "image",
      "imagePath": "/assets/q23_triangle.png",
      "caption": "Omondi drew accurately the triangle shown on a piece of paper."
    },
    "ctx-q24": {
      "title": "3-D Object",
      "type": "image",
      "imagePath": "/assets/q24_cuboid.svg",
      "caption": "Munya picked the following 3-D object."
    },
    "ctx-q25": {
      "title": "Window Frame",
      "type": "image",
      "imagePath": "/assets/q25_frame.svg",
      "caption": "A carpenter joined five pieces of timber to make a window frame as shown."
    },
    "ctx-q26": {
      "title": "Bar Graph",
      "type": "image",
      "imagePath": "/assets/q26_graph.png",
      "caption": "The bar graph shows the amount of money received from Monday to Friday after selling the tomatoes."
    },
    "ctx-q28": {
      "title": "Tally Table",
      "type": "image",
      "imagePath": "/assets/q28_table.png",
      "caption": "The table shows the number of patients who were treated for various diseases in a dispensary. Some information is missing in the table."
    }
  },
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "Lorries delivered 84072 bags of maize to a refugee camp. What is the number of bags of maize in words?",
      "questionType": "mcq",
      "options": [
        {
          "text": "Eighty thousand four hundred and seventy two",
          "isCorrect": false
        },
        {
          "text": "Eighty four thousand seven hundred and two",
          "isCorrect": false
        },
        {
          "text": "Eighty four thousand and seventy two",
          "isCorrect": true
        },
        {
          "text": "Eighty four thousand seven hundred and twenty",
          "isCorrect": false
        }
      ],
      "explanation": "When you look at a large number like **84,072**, the easiest way to read it is by breaking it into groups based on place value.\n\n* First, the '84' is in the thousands section, so we say 'Eighty four thousand'.\n* Next, notice there is a '0' in the hundreds place, meaning there are no hundreds at all.\n* We just skip over it!\n* Finally, the last two digits form '72'.\n* Putting it all together, we read the number smoothly as **Eighty four thousand and seventy two**."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "In a hospital, 436587 children were vaccinated against polio in a certain year. What is the total value of digit 6 in the number?",
      "questionType": "mcq",
      "options": [
        {
          "text": "600",
          "isCorrect": false
        },
        {
          "text": "6000",
          "isCorrect": true
        },
        {
          "text": "60000",
          "isCorrect": false
        },
        {
          "text": "600000",
          "isCorrect": false
        }
      ],
      "explanation": "To find the value of a specific digit in the number **436,587**, we just need to identify its position starting from the right.\n\n* Counting from the right end, we pass the ones (7), tens (8), and hundreds (5), which lands the digit **6** squarely in the **thousands** place.\n* Since it represents six thousands, we apply its place value ($6 \\times 1000$).\n* The total value of the digit is **6000**."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "A tree nursery had 368593 seedlings. Customers bought 27364 tree seedlings in a day. How many tree seedlings remained?",
      "questionType": "mcq",
      "options": [
        {
          "text": "395957",
          "isCorrect": false
        },
        {
          "text": "341239",
          "isCorrect": false
        },
        {
          "text": "341229",
          "isCorrect": true
        },
        {
          "text": "94953",
          "isCorrect": false
        }
      ],
      "explanation": "This is a straightforward subtraction problem!\n\n* We start with the total number of seedlings the farmer had, which is **368,593**.\n* Then, we subtract the seedlings that were bought by customers (**27,364**).\n* When you carefully calculate $368{,}593 - 27{,}364$, you'll find that the farmer remained with exactly **341,229** seedlings."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "A milk processing factory produced 19468 packets of milk. How many packets of milk to the nearest thousands were produced?",
      "questionType": "mcq",
      "options": [
        {
          "text": "20000",
          "isCorrect": false
        },
        {
          "text": "19500",
          "isCorrect": false
        },
        {
          "text": "19470",
          "isCorrect": false
        },
        {
          "text": "19000",
          "isCorrect": true
        }
      ],
      "explanation": "When rounding **19,468** to the nearest thousand, the crucial digit to look at is the one immediately to its right, which is the hundreds digit.\n\n* Here, the hundreds digit is **4**.\n* The rule is simple: if this digit is 5 or more, we round up.\n* Since $4 < 5$, we round down.\n* Rounding down means we keep the thousands part exactly as it is (19) and turn everything after it into zeros.\n* This gives us our final rounded figure of **19,000**."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "What is the next number in the pattern? $8, 24, 72, 216,$ ------",
      "questionType": "mcq",
      "options": [
        {
          "text": "232",
          "isCorrect": false
        },
        {
          "text": "264",
          "isCorrect": false
        },
        {
          "text": "360",
          "isCorrect": false
        },
        {
          "text": "648",
          "isCorrect": true
        }
      ],
      "explanation": "Let's figure out the hidden rule in this number sequence: $8, 24, 72, 216, ?$.\n\n* If you check the ratio of each number to the one before it, a clear pattern emerges: $24\\div 8 = 3$, and $72\\div 24 = 3$.\n* The rule is a constant multiplier of **$\\times 3$** to get the next one!\n* To find the missing number, just take the last number and apply the rule: $216 \\times 3$.\n* That gives us our answer: **648**."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "Work out $24\\div 3 + 9 \\times 6 - 4$",
      "questionType": "mcq",
      "options": [
        {
          "text": "8",
          "isCorrect": false
        },
        {
          "text": "26",
          "isCorrect": false
        },
        {
          "text": "58",
          "isCorrect": true
        },
        {
          "text": "98",
          "isCorrect": false
        }
      ],
      "explanation": "To solve $24 \\div 3 + 9 \\times 6 - 4$, we have to follow the **BODMAS** rule so we do the operations in the right order.\n\n* First, we evaluate the $\\div$ and $\\times$ operations: $24 \\div 3$ gives us 8, and $9 \\times 6$ gives us 54.\n* This simplifies our expression nicely down to $8 + 54 - 4$.\n* Now it's just basic addition and subtraction from left to right.\n* Adding 8 and 54 gives 62, and taking away 4 leaves us with a final answer of **58**."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "Musa spent $\\dfrac{2}{5}$ of his salary on food. He also spent $\\dfrac{1}{4}$ of the salary on rent. What is the total fraction of the salary that Musa spent on food and rent?",
      "questionType": "mcq",
      "options": [
        {
          "text": "$\\dfrac{13}{20}$",
          "isCorrect": true
        },
        {
          "text": "$\\dfrac{9}{20}$",
          "isCorrect": false
        },
        {
          "text": "$\\dfrac{7}{20}$",
          "isCorrect": false
        },
        {
          "text": "$\\dfrac{3}{20}$",
          "isCorrect": false
        }
      ],
      "explanation": "We're dealing with two fractions here: $\\dfrac{2}{5}$ for food and $\\dfrac{1}{4}$ for rent.\n\n* To add them together, they need to speak the same language—meaning they need a common denominator.\n* The lowest common multiple for 5 and 4 is **20**.\n* Let's convert both fractions: the food fraction becomes $\\dfrac{8}{20}$ and the rent fraction becomes $\\dfrac{5}{20}$.\n* Now that the denominators match, we just calculate $8 + 5$ for the top numbers.\n* The total fraction of the salary spent is **$\\dfrac{13}{20}$**."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "What is the value of $9 \\dfrac{5}{6} - 1 \\dfrac{1}{3}$?",
      "questionType": "mcq",
      "options": [
        {
          "text": "$11 \\dfrac{1}{6}$",
          "isCorrect": false
        },
        {
          "text": "$9 \\dfrac{1}{6}$",
          "isCorrect": false
        },
        {
          "text": "$8 \\dfrac{2}{3}$",
          "isCorrect": false
        },
        {
          "text": "$8 \\dfrac{1}{2}$",
          "isCorrect": true
        }
      ],
      "explanation": "We want to calculate $9\\dfrac{5}{6} - 1\\dfrac{1}{3}$.\n\n* Just like addition, subtraction requires common denominators.\n* For 6 and 3, the common denominator is **6**.\n* Let's change $1\\dfrac{1}{3}$ so its denominator is 6.\n* It becomes $1\\dfrac{2}{6}$.\n* Now our math is much easier: we calculate the whole numbers ($9 - 1 = 8$) and then the fractions ($\\dfrac{5}{6} - \\dfrac{2}{6} = \\dfrac{3}{6}$).\n* Putting it together gives $8\\dfrac{3}{6}$.\n* But wait!\n* We can simplify the fraction $\\dfrac{3}{6}$ down to $\\dfrac{1}{2}$, making our final answer **$8\\dfrac{1}{2}$**."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "Wangeci made a necklace using red and green beads. The red beads used were $25\\%$ while the rest were green. Which of the following decimals represent the green beads?",
      "questionType": "mcq",
      "options": [
        {
          "text": "7.5",
          "isCorrect": false
        },
        {
          "text": "0.75",
          "isCorrect": true
        },
        {
          "text": "0.075",
          "isCorrect": false
        },
        {
          "text": "0.0075",
          "isCorrect": false
        }
      ],
      "explanation": "Think of the entire collection of beads as being exactly **100%**.\n\n* The problem tells us that the red beads make up 25% of the total.\n* That leaves the rest of the percentage entirely for the green beads, which is exactly 75% ($100\\% - 25\\%$).\n* The question asks for this as a decimal.\n* To turn a percentage into a decimal, we calculate using $\\div 100$.\n* So, $75 \\div 100$ gives us **0.75**."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "A tailor bought a fabric material. He used 0.263 of the fabric to make a pair of shorts, 0.287 to make a shirt and 0.45 to make a dress. How much of the fabric was used to make both the dress and the shirt?",
      "questionType": "mcq",
      "options": [
        {
          "text": "0.332",
          "isCorrect": false
        },
        {
          "text": "0.637",
          "isCorrect": false
        },
        {
          "text": "0.713",
          "isCorrect": false
        },
        {
          "text": "0.737",
          "isCorrect": true
        }
      ],
      "explanation": "This question gives you extra information to test your focus!\n\n* It asks specifically for the total fabric used on the **shirt and the dress** combined.\n* We only need to look at two numbers: **0.287** (for the shirt) and **0.45** (for the dress).\n* We can completely ignore the fabric used for the shorts!\n* When you carefully align the decimal points and calculate $0.287 + 0.450$, you get the total fabric used, which is **0.737**."
    },
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "The height of water in a dam increased by 5 cm after it rained. What is the increase in the height of water in millimetres?",
      "questionType": "mcq",
      "options": [
        {
          "text": "50",
          "isCorrect": true
        },
        {
          "text": "500",
          "isCorrect": false
        },
        {
          "text": "5000",
          "isCorrect": false
        },
        {
          "text": "50000",
          "isCorrect": false
        }
      ],
      "explanation": "The tree's height increased by a total of **5 cm**.\n\n* To convert this measurement into millimetres, you need to remember the basic conversion rule: $1 \\text{ cm} = 10 \\text{ mm}$.\n* So, we simply calculate $5 \\times 10$.\n* The increase in height is **50 mm**."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "What is the perimeter of the shape?",
      "questionType": "mcq",
      "contextRef": "ctx-q12",
      "options": [
        {
          "text": "43 cm",
          "isCorrect": false
        },
        {
          "text": "48 cm",
          "isCorrect": false
        },
        {
          "text": "50 cm",
          "isCorrect": false
        },
        {
          "text": "58 cm",
          "isCorrect": true
        }
      ],
      "explanation": "The perimeter of any 2-D shape is simply the total distance around its outside edge.\n\n* Imagine walking like an ant all the way around the shape!\n* If we look at the diagram and identify all the outer side lengths, we have: 15 cm, 15 cm, 10 cm, 10 cm, and 8 cm.\n* All we have to do is calculate their sum: $15 + 15 + 10 + 10 + 8$, which gives us a total perimeter of **58 cm**."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "A ribbon is 31 cm 6 mm long. Rehema cut 5 cm 3 mm of the ribbon to make a flower. What length of the ribbon remained?",
      "questionType": "mcq",
      "options": [
        {
          "text": "26 cm 3 mm",
          "isCorrect": true
        },
        {
          "text": "34 cm 3 mm",
          "isCorrect": false
        },
        {
          "text": "36 cm 9 mm",
          "isCorrect": false
        },
        {
          "text": "36 cm 3 mm",
          "isCorrect": false
        }
      ],
      "explanation": "We start with a ribbon that is **31 cm 6 mm** long, and a piece measuring **5 cm 3 mm** is cut off from it.\n\n* The easiest way to calculate this is to handle the smaller units first.\n* Taking away 3 mm from 6 mm leaves us with 3 mm.\n* Next, we handle the centimetres: taking 5 cm away from 31 cm leaves us with 26 cm.\n* Bringing both parts together, the remaining ribbon is **26 cm 3 mm** long."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "What is the area of the wall?",
      "questionType": "mcq",
      "contextRef": "ctx-q14",
      "options": [
        {
          "text": "$6370 \\text{ cm}^2$",
          "isCorrect": false
        },
        {
          "text": "$5590 \\text{ cm}^2$",
          "isCorrect": true
        },
        {
          "text": "$4810 \\text{ cm}^2$",
          "isCorrect": false
        },
        {
          "text": "$3185 \\text{ cm}^2$",
          "isCorrect": false
        }
      ],
      "explanation": "The wall shape in the diagram is what we call a compound shape.\n\n* It's actually a combination of two simpler shapes joined together: a large **rectangle** and a smaller **triangle**.\n* First, let's find the area of the rectangle.\n* Calculating $\\text{length} \\times \\text{width}$ ($65 \\times 74$) gives us $4{,}810 \\text{ cm}^2$.\n* Next, the area of the triangle is $\\frac{1}{2} \\times \\text{base} \\times \\text{height}$ ($\\frac{1}{2} \\times 65 \\times 24$), which gives us $780 \\text{ cm}^2$.\n* To find the total area of the wall, we simply add these two areas together.\n* The total combined area is **$5{,}590 \\text{ cm}^2$**."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "Kimeto drinks 3.7 litres of water everyday. How many millilitres of water does he drink?",
      "questionType": "mcq",
      "options": [
        {
          "text": "37",
          "isCorrect": false
        },
        {
          "text": "370",
          "isCorrect": false
        },
        {
          "text": "3700",
          "isCorrect": true
        },
        {
          "text": "37000",
          "isCorrect": false
        }
      ],
      "explanation": "Kimeto's daily water intake is given as **3.7 litres**.\n\n* The question asks for the answer in millilitres.\n* You need to recall the standard volume conversion: there are exactly $1000 \\text{ ml}$ in every $1 \\text{ litre}$.\n* To convert, we calculate $3.7 \\times 1000$.\n* This gives us exactly **$3{,}700 \\text{ ml}$**."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "A road construction company mixed sand and small stones. The mass of sand was 18 tonnes 481 kilograms. The mass of small stones was 12 tonnes 394 kilograms. What is the total mass of the mixture?",
      "questionType": "mcq",
      "options": [
        {
          "text": "30 tonnes 875 kilograms",
          "isCorrect": true
        },
        {
          "text": "30 tonnes 775 kilograms",
          "isCorrect": false
        },
        {
          "text": "20 tonnes 875 kilograms",
          "isCorrect": false
        },
        {
          "text": "6 tonnes 87 kilograms",
          "isCorrect": false
        }
      ],
      "explanation": "A lorry is carrying two materials: sand and small stones.\n\n* The sand weighs **18 tonnes 481 kg** and the small stones weigh **12 tonnes 394 kg**.\n* Just like with other measurements, it's easiest to add the smaller units first.\n* When we calculate $481 + 394$, we get 875 kg.\n* Then, we add the larger units: 18 tonnes plus 12 tonnes equals 30 tonnes.\n* The total mass carried by the lorry is therefore **30 tonnes 875 kilograms**."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "A tea processing factory distributed fertilizer to farmers using 4 lorries. Each lorry carried 24 tonnes 235 kilograms of fertilizer. What was the total mass of the fertilizer distributed?",
      "questionType": "mcq",
      "options": [
        {
          "text": "96 tonnes 940 kilograms",
          "isCorrect": true
        },
        {
          "text": "96 tonnes 920 kilograms",
          "isCorrect": false
        },
        {
          "text": "96 tonnes 840 kilograms",
          "isCorrect": false
        },
        {
          "text": "86 tonnes 940 kilograms",
          "isCorrect": false
        }
      ],
      "explanation": "There are 4 lorries, and each one is carrying a mass of **24 tonnes 235 kg**.\n\n* To find the total mass, we calculate using $\\times 4$.\n* Let's tackle the kilograms first: $235 \\text{ kg} \\times 4$ gives us exactly 940 kg.\n* Next, we calculate the tonnes: $24 \\text{ tonnes} \\times 4$ equals 96 tonnes.\n* Combining these, the total mass distributed across all lorries is **96 tonnes 940 kilograms**."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "A flower company exported 4850000 kilograms of fresh flowers. How many tonnes of fresh flowers did the company export?",
      "questionType": "mcq",
      "options": [
        {
          "text": "485000",
          "isCorrect": false
        },
        {
          "text": "48500",
          "isCorrect": false
        },
        {
          "text": "4850",
          "isCorrect": true
        },
        {
          "text": "485",
          "isCorrect": false
        }
      ],
      "explanation": "A massive amount of flowers were exported—**4,850,000 kg** to be exact!\n\n* Such large numbers are much easier to understand when converted to tonnes.\n* The conversion factor you need to remember is that $1 \\text{ tonne}$ is equal to $1000 \\text{ kg}$.\n* To perform the conversion, we calculate $4{,}850{,}000\\div 1000$.\n* This chops off three zeros, leaving us with a much friendlier number: **4,850 tonnes**."
    },
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "Wambua represented his school in a music festival. He began his performance in the afternoon at the time shown on the clock face. At what time did Wambua begin his performance?",
      "questionType": "mcq",
      "contextRef": "ctx-q19",
      "options": [
        {
          "text": "2.07 p.m.",
          "isCorrect": false
        },
        {
          "text": "2.35 a.m.",
          "isCorrect": false
        },
        {
          "text": "2.35 p.m.",
          "isCorrect": true
        },
        {
          "text": "3.35 p.m.",
          "isCorrect": false
        }
      ],
      "explanation": "To read an analogue clock, always start by checking the shorter hand, which points to the hour.\n\n* Here, it sits between the 2 and the 3, which means the hour is **2**.\n* Next, look at the longer minute hand.\n* It points directly at the 7.\n* Since each number represents a 5-minute interval, calculating $7 \\times 5$ tells us it is 35 minutes past the hour.\n* So the time reads 2:35.\n* Finally, the question tells us the performance happened 'in the afternoon', so we use 'p.m.'.\n* The correct time is **2.35 p.m.**"
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "A tourist travelled from Manga station to Pate using the train. How long did the journey take?",
      "questionType": "mcq",
      "contextRef": "ctx-q20",
      "options": [
        {
          "text": "5 hours 39 minutes",
          "isCorrect": true
        },
        {
          "text": "3 hours 24 minutes",
          "isCorrect": false
        },
        {
          "text": "3 hours 14 minutes",
          "isCorrect": false
        },
        {
          "text": "2 hours 15 minutes",
          "isCorrect": false
        }
      ],
      "explanation": "This is a travel time problem!\n\n* The train left Manga station at **6.15 a.m.** and finally pulled into Pate station at **11.54 a.m.** To find out exactly how long the journey took, we just need to calculate the difference between the arrival and departure times.\n* Subtracting the hours gives us $11 - 6 = 5 \\text{ hours}$.\n* Subtracting the minutes gives us $54 - 15 = 39 \\text{ minutes}$.\n* The whole journey took exactly **5 hours 39 minutes**."
    },
    {
      "id": "q21",
      "questionNumber": 21,
      "questionText": "Ndemo assists his father to sell clothes in their shop. He sold a dress for sh 1 675. He made a profit of sh 390 after selling the dress. What was the buying price of the dress?",
      "questionType": "mcq",
      "options": [
        {
          "text": "sh 2 065",
          "isCorrect": false
        },
        {
          "text": "sh 1 385",
          "isCorrect": false
        },
        {
          "text": "sh 1 325",
          "isCorrect": false
        },
        {
          "text": "sh 1 285",
          "isCorrect": true
        }
      ],
      "explanation": "In business, your profit is the extra money you make after selling an item for more than you bought it.\n\n* We are told the dress sold for **sh 1,675**, generating a profit of **sh 390**.\n* We can find out how much the dress originally cost to buy by reversing this logic using the formula: $\\text{Buying Price} = \\text{Selling Price} - \\text{Profit}$.\n* When we calculate $1{,}675 - 390$, we find that the original Buying Price was **sh 1,285**."
    },
    {
      "id": "q22",
      "questionNumber": 22,
      "questionText": "The area of a rectangular piece of paper is $72 \\text{ cm}^2$. The length of the paper is 9 cm. What is the width of the paper in millimetres?",
      "questionType": "mcq",
      "options": [
        {
          "text": "0.8",
          "isCorrect": false
        },
        {
          "text": "8",
          "isCorrect": false
        },
        {
          "text": "80",
          "isCorrect": true
        },
        {
          "text": "800",
          "isCorrect": false
        }
      ],
      "explanation": "We know the total area of the rectangular paper is $72 \\text{ cm}^2$ and its length is **9 cm**.\n\n* Since the formula is $\\text{Area} = \\text{Length} \\times \\text{Width}$, we can work backward to find the Width by calculating $\\text{Area}\\div \\text{Length}$.\n* Thus, $72\\div 9$ gives us a width of exactly $8 \\text{ cm}$.\n* But watch out!\n* The options are in millimetres.\n* To convert from cm to mm, we apply $\\times 10$.\n* So the width is **$80 \\text{ mm}$**."
    },
    {
      "id": "q23",
      "questionNumber": 23,
      "questionText": "Measure angle LMN using a protractor. What is the size of angle LMN?",
      "questionType": "mcq",
      "contextRef": "ctx-q23",
      "options": [
        {
          "text": "$100^{\\circ}$",
          "isCorrect": false
        },
        {
          "text": "$80^{\\circ}$",
          "isCorrect": false
        },
        {
          "text": "$60^{\\circ}$",
          "isCorrect": false
        },
        {
          "text": "$40^{\\circ}$",
          "isCorrect": true
        }
      ],
      "explanation": "Using a protractor correctly is all about careful alignment!\n\n* First, locate the vertex of the angle—that's point **M**—and place the center mark (or crosshair) of your protractor exactly on it.\n* Next, rotate the protractor so that its flat baseline (the 0 degrees line) lies perfectly flat along the line segment **LM**.\n* Now, trace the other line segment, **MN**, up to the curved edge of the protractor.\n* Read the scale that started at 0 on your baseline.\n* The line crosses the mark at **40 degrees**!"
    },
    {
      "id": "q24",
      "questionNumber": 24,
      "questionText": "How many edges does the object have?",
      "questionType": "mcq",
      "contextRef": "ctx-q24",
      "options": [
        {
          "text": "6",
          "isCorrect": false
        },
        {
          "text": "8",
          "isCorrect": false
        },
        {
          "text": "9",
          "isCorrect": false
        },
        {
          "text": "12",
          "isCorrect": true
        }
      ],
      "explanation": "The 3-D shape shown in the diagram is a rectangular prism, commonly known as a **cuboid**.\n\n* The question specifically asks for the number of **edges**, which form the frame of the shape.\n* A cuboid has 4 edges at the rectangular base, 4 vertical edges, and 4 edges at the top.\n* Combined together, a cuboid always has **12 edges**!"
    },
    {
      "id": "q25",
      "questionNumber": 25,
      "questionText": "Which of the following pieces of timber are parallel?",
      "questionType": "mcq",
      "contextRef": "ctx-q25",
      "options": [
        {
          "text": "r and p",
          "isCorrect": false
        },
        {
          "text": "m and n",
          "isCorrect": false
        },
        {
          "text": "n and q",
          "isCorrect": true
        },
        {
          "text": "r and q",
          "isCorrect": false
        }
      ],
      "explanation": "**Parallel lines** are lines that run side-by-side in exactly the same direction and will never cross each other, no matter how far you stretch them.\n\n* If you look at the window frame, piece **n** forms the top edge and piece **q** forms the bottom edge.\n* Because they are opposite horizontal sides of a rectangle, they are perfectly parallel.\n* Piece **r**, however, is a diagonal strut that slants across the frame and intersects the others.\n* Therefore, the only pieces listed that are parallel to each other are **n and q**."
    },
    {
      "id": "q26",
      "questionNumber": 26,
      "questionText": "How much money did the learners receive on Wednesday?",
      "questionType": "mcq",
      "contextRef": "ctx-q26",
      "options": [
        {
          "text": "sh 2 250",
          "isCorrect": false
        },
        {
          "text": "sh 2 000",
          "isCorrect": false
        },
        {
          "text": "sh 1 750",
          "isCorrect": true
        },
        {
          "text": "sh 1 500",
          "isCorrect": false
        }
      ],
      "explanation": "Reading bar graphs requires you to trace lines carefully.\n\n* First, locate **Wednesday** along the bottom horizontal axis.\n* Follow the top of Wednesday's bar straight across to the left until you hit the vertical axis, which shows the amount of money.\n* The top of the bar stops exactly halfway between the 1500 and 2000 marks.\n* Halfway between those numbers is a difference of 250, making the total amount **sh 1,750**."
    },
    {
      "id": "q27",
      "questionNumber": 27,
      "questionText": "During a geometry lesson, learners were asked to describe the faces of a cylinder, pyramid, cube and cuboid. Which of the following descriptions was correct?",
      "questionType": "mcq",
      "options": [
        {
          "text": "A cylinder has a square face",
          "isCorrect": false
        },
        {
          "text": "A pyramid has a triangular face",
          "isCorrect": true
        },
        {
          "text": "A cube has a rectangular face",
          "isCorrect": false
        },
        {
          "text": "A cuboid has a circular face",
          "isCorrect": false
        }
      ],
      "explanation": "Let's evaluate each shape's properties!\n\n* A cylinder has curved sides and circular ends.\n* A cube is made entirely of perfect squares.\n* A cuboid is made of rectangles.\n* A **pyramid**, however, is unique.\n* It always has a polygon at its base, and all of its side faces are **triangles** that slant upwards to meet at a single sharp point at the top (the apex).\n* Because of this, the statement 'A pyramid has a triangular face' is the only mathematically correct description!"
    },
    {
      "id": "q28",
      "questionNumber": 28,
      "questionText": "How many patients were treated altogether?",
      "questionType": "mcq",
      "contextRef": "ctx-q28",
      "options": [
        {
          "text": "30",
          "isCorrect": true
        },
        {
          "text": "20",
          "isCorrect": false
        },
        {
          "text": "29",
          "isCorrect": false
        },
        {
          "text": "10",
          "isCorrect": false
        }
      ],
      "explanation": "To find the total number of patients, we need to read and add up all the tally marks in the table.\n\n* Malaria and HIV/AIDS are easy because the numbers are given directly as **12** and **8**.\n* For Diabetes, we count 4 vertical strokes, which means 4 patients.\n* For Tuberculosis, there is one completed bundle (four strokes crossed by a diagonal line) representing 5, plus one extra stroke, making it 6 patients.\n* Calculating the total ($12 + 4 + 6 + 8$) gives us **30 patients** treated at the dispensary."
    },
    {
      "id": "q29",
      "questionNumber": 29,
      "questionText": "Ngei had some oranges. He gave out 4 oranges to his friend. He remained with more than 6 oranges. Use letter $p$ to represent the number of oranges that Ngei originally had. Which of the following inequalities correctly represents this information?",
      "questionType": "mcq",
      "options": [
        {
          "text": "$p - 4 < 6$",
          "isCorrect": false
        },
        {
          "text": "$6 - p > 4$",
          "isCorrect": false
        },
        {
          "text": "$p - 4 > 6$",
          "isCorrect": true
        },
        {
          "text": "$p - 6 < 4$",
          "isCorrect": false
        }
      ],
      "explanation": "Let's turn this story into math!\n\n* We can use the letter $p$ to represent the unknown number of oranges Ngei started with.\n* We're told he gave out 4 oranges to a friend.\n* Giving away means subtraction, so we write this part as $p - 4$.\n* After giving them away, he was left with 'more than 6' oranges.\n* In mathematics, 'more than' is shown using the greater than symbol ($>$).\n* When we put it all together, the correct inequality is **$p - 4 > 6$**."
    },
    {
      "id": "q30",
      "questionNumber": 30,
      "questionText": "A self-help group shared some money among 50 women. Each woman in the group got sh 8 500. Use letter $x$ to represent the amount of money shared. Which of the following equations correctly represents this information?",
      "questionType": "mcq",
      "options": [
        {
          "text": "$50x = 8 500$",
          "isCorrect": false
        },
        {
          "text": "$\\frac{50}{x} = 8 500$",
          "isCorrect": false
        },
        {
          "text": "$x + 50 = 8 500$",
          "isCorrect": false
        },
        {
          "text": "$\\frac{x}{50} = 8 500$",
          "isCorrect": true
        }
      ],
      "explanation": "We are dealing with an unknown total amount of money, which we will call $x$.\n\n* This money was shared equally among 50 women.\n* In math, sharing equally means division ($\\div$), so we can write this as a fraction: $\\dfrac{x}{50}$.\n* The problem tells us that after the division, each woman received exactly sh 8,500.\n* So, we set our fraction equal to that amount.\n* The equation that perfectly represents this information is **$\\dfrac{x}{50} = 8500$**."
    }
  ],
  "sectionB": [],
  "timeAllowed": 80
};