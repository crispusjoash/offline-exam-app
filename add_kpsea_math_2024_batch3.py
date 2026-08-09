import re

file_path = 'src/data/kpsea-math-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    21: r'''Let's review the different types of angles based on their sizes.\n\n* An angle that is exactly a right angle is **$90^\circ$**.\n* An angle that forms a straight line is **$180^\circ$**.\n* If an angle is smaller than $90^\circ$, it's called an **acute** angle.\n* But if an angle is greater than $90^\circ$ (a right angle) and less than $180^\circ$ (a straight line), it falls into a special category.\n* This type of angle is called an **obtuse angle**.''',
    22: r'''To find the total amount of garbage collected, we need to add the masses together, handling tonnes and kilograms separately.\n\n* **Tonnes:** Let's add the tonnes first: $2 + 3 + 4 = \textbf{9 tonnes}$.\n* **Kilograms:** Next, let's add the kilograms: $200 + 400 + 350$.\n* $200 + 400 = 600$, and $600 + 350 = \textbf{950 kilograms}$.\n* Since 950 kilograms is less than 1000, we don't need to carry over any extra tonnes.\n* The total garbage collected is **9 tonnes 950 kilograms**.''',
    23: r'''To find the remaining length, we need to subtract the part he cut from the total length: **93 cm 3 mm - 85 cm 6 mm**.\n\n* Let's start with the millimetres: we need to subtract 6 mm from 3 mm. Since we can't do that, we have to borrow.\n* We borrow 1 cm from the 93 cm. Remember, **1 cm = 10 mm**.\n* So, the 93 cm becomes **92 cm**, and the 3 mm becomes $3 + 10 = \textbf{13 mm}$.\n* Now, subtract the millimetres: $13 \text{ mm} - 6 \text{ mm} = \textbf{7 mm}$.\n* Next, subtract the centimetres: $92 \text{ cm} - 85 \text{ cm} = \textbf{7 cm}$.\n* The remaining length of the metal bar is **7 cm 7 mm**.''',
    24: r'''Let's break down the information to form a simple algebraic equation.\n\n* We are told to let Beatrice's amount be **$x$**.\n* Loise fetched 4 more than Beatrice, which means Loise fetched **$x + 4$** jerrycans.\n* Together, they fetched a total of 16 jerrycans.\n* This means: (Beatrice's amount) + (Loise's amount) = 16.\n* Replacing the words with our expressions gives: **$x + (x + 4) = 16$**.\n* This can simply be written as **$x + x + 4 = 16$**.''',
    25: r'''Let's think about the shape of this milk packet.\n\n* It is a pyramid with exactly **4 faces** in total.\n* A pyramid with 4 faces must have a triangular base (1 face) and three triangular sides meeting at the top (3 faces). This shape is called a **tetrahedron**.\n* To count the edges (the straight lines where the faces meet), we look at the base and the sides.\n* The triangular base has **3 edges**.\n* There are also **3 edges** sloping up to the top point (apex).\n* Total edges = $3 + 3 = \textbf{6}$.\n* The packet has **6 edges**.''',
    26: r'''Let's recall the special properties of different types of triangles.\n\n* An **equilateral triangle** has all three sides and all three angles equal.\n* A **scalene triangle** has no equal sides and no equal angles.\n* An **isosceles triangle**, which Abdul drew, is special because it has exactly **two sides of equal length**.\n* Because it has two equal sides, the two angles opposite those sides are also exactly equal.\n* Therefore, the correct property is that **two angles were equal**.''',
    27: r'''We can write this situation using a simple inequality.\n\n* The company used **2** buses.\n* The number of vans is represented by **$x$**.\n* The total number of vehicles is the buses plus the vans, which is **$2 + x$**.\n* The problem clearly states this total number was **less than 8**.\n* The symbol for "less than" is **$<$**.\n* Putting it all together, we get the inequality: **$2 + x < 8$**.''',
    28: r'''To find perpendicular pairs of wood, we need to look for pieces that meet at a perfect right angle ($90^\circ$).\n\n* In the design of the door, there are horizontal planks and vertical planks.\n* The horizontal planks are marked **m, p, and q**.\n* The vertical planks are marked **o and s**.\n* Any horizontal plank meeting a vertical plank forms a right angle (they are perpendicular).\n* Looking at our options, plank **m** (horizontal) and plank **o** (vertical) meet exactly at a right angle.\n* Therefore, pieces **m and o** are perpendicular.''',
    29: r'''To find the difference between the highest and lowest numbers, we need to carefully read the bar graph.\n\n* First, let's find the **highest** bar. It is on Thursday, reaching the line for **20** children.\n* Next, let's find the **lowest** bar. It happens on both Monday and Wednesday, resting at the line for **5** children.\n* The difference means we need to subtract the lowest from the highest: $20 - 5$.\n* $20 - 5 = \textbf{15}$.\n* The difference between the highest and lowest number is **15** children.''',
    30: r'''To find the least popular mode of transport, we need to count the tally marks for each and find the lowest total.\n\n* **Motor bike:** Two full groups of 5 and 4 single marks ($5 + 5 + 4 = 14$).\n* **Bicycle:** Two full groups of 5 and 3 single marks ($5 + 5 + 3 = 13$).\n* **Matatu:** Two full groups of 5 and 1 single mark ($5 + 5 + 1 = 11$).\n* **School bus:** Three full groups of 5 ($5 + 5 + 5 = 15$).\n* Comparing these numbers (14, 13, 11, and 15), the lowest is **11**.\n* The least popular mode of transport is the **Matatu**.'''
}

for q_num, new_exp in replacements.items():
    pattern = r'("questionNumber": ' + str(q_num) + r',.*?"explanation": )"(.*?)"'
    
    def repl(m):
        import json
        return m.group(1) + json.dumps(new_exp)
        
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Batch 3 completed successfully.")
