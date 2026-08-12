import json
import re

file_path = 'src/data/kpsea-math-2025.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

updates = {
    "q21": "To find out how much balance Peter received, we must first calculate the total cost of the items he bought.\n\n* Add the prices of the items together: $250 + 45 + 25$.\n* $250 + 45 = 295$.\n* $295 + 25 = 320$.\n* The total cost of the items is **sh 320**.\n* Peter paid with a 1,000 shilling note.\n* Subtract the total cost from the amount paid to find the balance: $1000 - 320 = 680$.\n* Peter received a balance of **sh 680**.",
    
    "q22": "To determine the size of angle *r*, we can analyze the drawing and use visual estimation strategies.\n\n* First, we observe that angle *r* is an **acute angle**, which means it is less than $90^{\\circ}$. This eliminates the $120^{\\circ}$ option immediately.\n* Next, we can compare it to familiar angles. A $45^{\\circ}$ angle would cut exactly halfway through a $90^{\\circ}$ corner. \n* Looking at the drawing, angle *r* is visibly larger than half of a right angle (larger than $45^{\\circ}$).\n* At the same time, it is not almost a right angle, which eliminates $80^{\\circ}$.\n* Based on this, the most accurate measurement for angle *r* is **$60^{\\circ}$**.",
    
    "q23": "To answer this, we need to know the properties of a cuboid and consider the special condition of the garbage box.\n\n* A standard closed cuboid has **8 vertices** (corners), **12 edges**, and **6 faces**.\n* The question states that this object is an **open** cuboid box with **no top face**.\n* Removing the top face does not remove any corners, so it still has **8 vertices**.\n* However, because the top face is missing, we subtract 1 from the original 6 faces: $6 - 1 = 5$.\n* The open box has **8 vertices** and **5 faces**.",
    
    "q24": "To find which pieces of timber are parallel, we must understand what parallel lines are.\n\n* **Parallel lines** are lines that run side by side, always keeping the same distance apart, and never meet or touch.\n* Looking at the diagram of the rabbit hutch, timbers **h** and **i** form the left and right vertical posts.\n* Because they are both perfectly vertical and stand straight up from the base, they will never intersect.\n* Therefore, timbers **h** and **i** are parallel to each other.",
    
    "q25": "To find the total number of learners who chose netball and volleyball, we need to read their values from the bar graph.\n\n* First, locate the bar for **Netball**. Follow the top of the bar across to the vertical axis, which reads **100**.\n* Next, locate the bar for **Volleyball**. Follow the top of this bar across to the vertical axis, which reads **60**.\n* Finally, add these two values together to get the total number: $100 + 60 = 160$.\n* Altogether, **160** learners chose netball and volleyball.",
    
    "q26": "To find the number of patients received on Wednesday, we need to use the total given and the values from the other days.\n\n* The total number of patients received from Tuesday to Friday is **101**.\n* From the table, we know the patients for Tuesday (23), Thursday (18), and Friday (26).\n* Let's add these known numbers together: $23 + 18 + 26 = 67$.\n* To find the missing number for Wednesday, subtract the known total from the overall total: $101 - 67 = 34$.\n* The hospital received **34** patients on Wednesday.",
    
    "q27": "To identify the 2-D shape seen on the face of the stone, we must recall the properties of a cube.\n\n* A **cube** is a special 3-dimensional object.\n* One of its defining characteristics is that all of its dimensions (length, width, and height) are exactly equal.\n* Because of this, every single flat surface (or face) on a cube is a perfectly regular quadrilateral where all sides are equal and all angles are right angles.\n* Such a 2-D shape is called a **Square**.",
    
    "q28": "To find how long Fatuma's journey took, we calculate the time elapsed from 11.20 a.m. to 2.30 p.m.\n\n* Let's break the time down into manageable parts.\n* First, calculate the time from 11.20 a.m. to 12.00 noon: This is **40 minutes**.\n* Next, calculate the time from 12.00 noon to 2.30 p.m.: This is exactly **2 hours and 30 minutes**.\n* Finally, add these two durations together: 2 hours 30 minutes + 40 minutes.\n* Adding the minutes gives 70 minutes. Since 60 minutes make 1 hour, 70 minutes is 1 hour and 10 minutes.\n* Add this 1 hour to the 2 hours: $2 + 1 = 3$ hours.\n* The total journey took **3 hours 10 minutes**.",
    
    "q29": "To translate this word problem into an inequality, we simply replace the words with mathematical symbols.\n\n* The number of pineapples is **6**.\n* The number of oranges is represented by **x**.\n* \"The total number of pineapples and oranges\" means we add them together: **$6 + x$**.\n* The phrase \"were less than 25\" translates to the symbol **$<$** followed by 25: **$< 25$**.\n* Putting the two parts together gives the correct inequality: **$6 + x < 25$**.",
    
    "q30": "To represent this information in an equation, we need to show that the sum of the two parts equals the total.\n\n* The total number of uniforms bought is **56**.\n* The handball team received **18** pairs.\n* The netball team's pairs are represented by the letter **y**.\n* The sum of the netball pairs and handball pairs must equal the total pairs: **$y + 18$**.\n* Setting this equal to the total gives us the correct equation: **$y + 18 = 56$**."
}

for q in data["sectionA"]:
    if q["id"] in updates:
        q["explanation"] = updates[q["id"]]

new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 3 completed!")
