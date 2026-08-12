"""
Rewrite explanations into conversational paragraphs separated by \\n.
ALL STRINGS MUST BE RAW STRINGS (r"...") to prevent Python from parsing \t and \d!
"""
import re, sys

EXPS = {
    "q1":  (r"When you look at a large number like **84,072**, the easiest way to read it is by breaking it into groups based on place value." + "\n"
            r"First, the '84' is in the thousands section, so we say 'Eighty four thousand'." + "\n"
            r"Next, notice there is a '0' in the hundreds place, meaning there are no hundreds at all. We just skip over it!" + "\n"
            r"Finally, the last two digits form '72'. Putting it all together, we read the number smoothly as **Eighty four thousand and seventy two**."),
    
    "q2":  (r"To find the value of a specific digit in the number **436,587**, we just need to identify its position starting from the right." + "\n"
            r"Counting from the right end, we pass the ones (7), tens (8), and hundreds (5), which lands the digit **6** squarely in the **thousands** place." + "\n"
            r"Since it represents six thousands, we apply its place value ($6 \times 1000$). The total value of the digit is **6000**."),
    
    "q3":  (r"This is a straightforward subtraction problem! We start with the total number of seedlings the farmer had, which is **368,593**." + "\n"
            r"Then, we subtract the seedlings that were bought by customers (**27,364**)." + "\n"
            r"When you carefully calculate $368{,}593 - 27{,}364$, you'll find that the farmer remained with exactly **341,229** seedlings."),
    
    "q4":  (r"When rounding **19,468** to the nearest thousand, the crucial digit to look at is the one immediately to its right, which is the hundreds digit." + "\n"
            r"Here, the hundreds digit is **4**. The rule is simple: if this digit is 5 or more, we round up. Since $4 < 5$, we round down." + "\n"
            r"Rounding down means we keep the thousands part exactly as it is (19) and turn everything after it into zeros. This gives us our final rounded figure of **19,000**."),
    
    "q5":  (r"Let's figure out the hidden rule in this number sequence: $8,\ 24,\ 72,\ 216,\ ?$." + "\n"
            r"If you check the ratio of each number to the one before it, a clear pattern emerges: $24 \div 8 = 3$, and $72 \div 24 = 3$. The rule is a constant multiplier of **$\times 3$** to get the next one!" + "\n"
            r"To find the missing number, just take the last number and apply the rule: $216 \times 3$. That gives us our answer: **648**."),
    
    "q6":  (r"To solve $24 \div 3 + 9 \times 6 - 4$, we have to follow the **BODMAS** rule so we do the operations in the right order." + "\n"
            r"First, we evaluate the $\div$ and $\times$ operations: $24 \div 3$ gives us 8, and $9 \times 6$ gives us 54. This simplifies our expression nicely down to $8 + 54 - 4$." + "\n"
            r"Now it's just basic addition and subtraction from left to right. Adding 8 and 54 gives 62, and taking away 4 leaves us with a final answer of **58**."),
    
    "q7":  (r"We're dealing with two fractions here: $\dfrac{2}{5}$ for food and $\dfrac{1}{4}$ for rent. To add them together, they need to speak the same language—meaning they need a common denominator." + "\n"
            r"The lowest common multiple for 5 and 4 is **20**. Let's convert both fractions: the food fraction becomes $\dfrac{8}{20}$ and the rent fraction becomes $\dfrac{5}{20}$." + "\n"
            r"Now that the denominators match, we just calculate $8 + 5$ for the top numbers. The total fraction of the salary spent is **$\dfrac{13}{20}$**."),
    
    "q8":  (r"We want to calculate $9\dfrac{5}{6} - 1\dfrac{1}{3}$. Just like addition, subtraction requires common denominators. For 6 and 3, the common denominator is **6**." + "\n"
            r"Let's change $1\dfrac{1}{3}$ so its denominator is 6. It becomes $1\dfrac{2}{6}$. Now our math is much easier: we calculate the whole numbers ($9 - 1 = 8$) and then the fractions ($\dfrac{5}{6} - \dfrac{2}{6} = \dfrac{3}{6}$)." + "\n"
            r"Putting it together gives $8\dfrac{3}{6}$. But wait! We can simplify the fraction $\dfrac{3}{6}$ down to $\dfrac{1}{2}$, making our final answer **$8\dfrac{1}{2}$**."),
    
    "q9":  (r"Think of the entire collection of beads as being exactly **100%**." + "\n"
            r"The problem tells us that the red beads make up 25% of the total. That leaves the rest of the percentage entirely for the green beads, which is exactly 75% ($100\% - 25\%$)." + "\n"
            r"The question asks for this as a decimal. To turn a percentage into a decimal, we calculate using $\div 100$. So, $75 \div 100$ gives us **0.75**."),
    
    "q10": (r"This question gives you extra information to test your focus! It asks specifically for the total fabric used on the **shirt and the dress** combined." + "\n"
            r"We only need to look at two numbers: **0.287** (for the shirt) and **0.45** (for the dress). We can completely ignore the fabric used for the shorts!" + "\n"
            r"When you carefully align the decimal points and calculate $0.287 + 0.450$, you get the total fabric used, which is **0.737**."),
    
    "q11": (r"The tree's height increased by a total of **5 cm**." + "\n"
            r"To convert this measurement into millimetres, you need to remember the basic conversion rule: $1 \text{ cm} = 10 \text{ mm}$." + "\n"
            r"So, we simply calculate $5 \times 10$. The increase in height is **50 mm**."),
    
    "q12": (r"The perimeter of any 2-D shape is simply the total distance around its outside edge. Imagine walking like an ant all the way around the shape!" + "\n"
            r"If we look at the diagram and identify all the outer side lengths, we have: 15 cm, 15 cm, 10 cm, 10 cm, and 8 cm." + "\n"
            r"All we have to do is calculate their sum: $15 + 15 + 10 + 10 + 8$, which gives us a total perimeter of **58 cm**."),
    
    "q13": (r"We start with a ribbon that is **31 cm 6 mm** long, and a piece measuring **5 cm 3 mm** is cut off from it. " + "\n"
            r"The easiest way to calculate this is to handle the smaller units first. Taking away 3 mm from 6 mm leaves us with 3 mm." + "\n"
            r"Next, we handle the centimetres: taking 5 cm away from 31 cm leaves us with 26 cm. Bringing both parts together, the remaining ribbon is **26 cm 3 mm** long."),
    
    "q14": (r"The wall shape in the diagram is what we call a compound shape. It's actually a combination of two simpler shapes joined together: a large **rectangle** and a smaller **triangle**." + "\n"
            r"First, let's find the area of the rectangle. Calculating $\text{length} \times \text{width}$ ($65 \times 74$) gives us $4{,}810 \text{ cm}^2$." + "\n"
            r"Next, the area of the triangle is $\frac{1}{2} \times \text{base} \times \text{height}$ ($\frac{1}{2} \times 65 \times 24$), which gives us $780 \text{ cm}^2$." + "\n"
            r"To find the total area of the wall, we simply add these two areas together. The total combined area is **$5{,}590 \text{ cm}^2$**."),
    
    "q15": (r"Kimeto's daily water intake is given as **3.7 litres**." + "\n"
            r"The question asks for the answer in millilitres. You need to recall the standard volume conversion: there are exactly $1000 \text{ ml}$ in every $1 \text{ litre}$." + "\n"
            r"To convert, we calculate $3.7 \times 1000$. This gives us exactly **$3{,}700 \text{ ml}$**."),
    
    "q16": (r"A lorry is carrying two materials: sand and small stones. The sand weighs **18 tonnes 481 kg** and the small stones weigh **12 tonnes 394 kg**." + "\n"
            r"Just like with other measurements, it's easiest to add the smaller units first. When we calculate $481 + 394$, we get 875 kg." + "\n"
            r"Then, we add the larger units: 18 tonnes plus 12 tonnes equals 30 tonnes. The total mass carried by the lorry is therefore **30 tonnes 875 kilograms**."),
    
    "q17": (r"There are 4 lorries, and each one is carrying a mass of **24 tonnes 235 kg**. To find the total mass, we calculate using $\times 4$." + "\n"
            r"Let's tackle the kilograms first: $235 \text{ kg} \times 4$ gives us exactly 940 kg." + "\n"
            r"Next, we calculate the tonnes: $24 \text{ tonnes} \times 4$ equals 96 tonnes. Combining these, the total mass distributed across all lorries is **96 tonnes 940 kilograms**."),
    
    "q18": (r"A massive amount of flowers were exported—**4,850,000 kg** to be exact!" + "\n"
            r"Such large numbers are much easier to understand when converted to tonnes. The conversion factor you need to remember is that $1 \text{ tonne}$ is equal to $1000 \text{ kg}$." + "\n"
            r"To perform the conversion, we calculate $4{,}850{,}000 \div 1000$. This chops off three zeros, leaving us with a much friendlier number: **4,850 tonnes**."),
    
    "q19": (r"To read an analogue clock, always start by checking the shorter hand, which points to the hour. Here, it sits between the 2 and the 3, which means the hour is **2**." + "\n"
            r"Next, look at the longer minute hand. It points directly at the 7. Since each number represents a 5-minute interval, calculating $7 \times 5$ tells us it is 35 minutes past the hour. So the time reads 2:35." + "\n"
            r"Finally, the question tells us the performance happened 'in the afternoon', so we use 'p.m.'. The correct time is **2.35 p.m.**"),
    
    "q20": (r"This is a travel time problem! The train left Manga station at **6.15 a.m.** and finally pulled into Pate station at **11.54 a.m.**" + "\n"
            r"To find out exactly how long the journey took, we just need to calculate the difference between the arrival and departure times." + "\n"
            r"Subtracting the hours gives us $11 - 6 = 5 \text{ hours}$. Subtracting the minutes gives us $54 - 15 = 39 \text{ minutes}$. The whole journey took exactly **5 hours 39 minutes**."),
    
    "q21": (r"In business, your profit is the extra money you make after selling an item for more than you bought it. We are told the dress sold for **sh 1,675**, generating a profit of **sh 390**." + "\n"
            r"We can find out how much the dress originally cost to buy by reversing this logic using the formula: $\text{Buying Price} = \text{Selling Price} - \text{Profit}$." + "\n"
            r"When we calculate $1{,}675 - 390$, we find that the original Buying Price was **sh 1,285**."),
    
    "q22": (r"We know the total area of the rectangular paper is $72 \text{ cm}^2$ and its length is **9 cm**." + "\n"
            r"Since the formula is $\text{Area} = \text{Length} \times \text{Width}$, we can work backward to find the Width by calculating $\text{Area} \div \text{Length}$. Thus, $72 \div 9$ gives us a width of exactly $8 \text{ cm}$." + "\n"
            r"But watch out! The options are in millimetres. To convert from cm to mm, we apply $\times 10$. So the width is **$80 \text{ mm}$**."),
    
    "q23": (r"Using a protractor correctly is all about careful alignment! First, locate the vertex of the angle—that's point **M**—and place the center mark (or crosshair) of your protractor exactly on it." + "\n"
            r"Next, rotate the protractor so that its flat baseline (the 0 degrees line) lies perfectly flat along the line segment **LM**." + "\n"
            r"Now, trace the other line segment, **MN**, up to the curved edge of the protractor. Read the scale that started at 0 on your baseline. The line crosses the mark at **40 degrees**!"),
    
    "q24": (r"The 3-D shape shown in the diagram is a rectangular prism, commonly known as a **cuboid**." + "\n"
            r"Notice those **dotted lines** at the top? In geometry drawings, this indicates that the box is actually 'open'—it doesn't have a lid, meaning it only has 5 faces instead of the usual 6." + "\n"
            r"However, the question specifically asks for the number of **edges**, which form the frame of the shape. Even without a lid, the top opening still has 4 structural edges. Combined with the 4 base edges and 4 vertical edges, the cuboid still has **12 edges**!"),
    
    "q25": (r"**Parallel lines** are lines that run side-by-side in exactly the same direction and will never cross each other, no matter how far you stretch them." + "\n"
            r"If you look at the window frame, piece **n** forms the top edge and piece **q** forms the bottom edge. Because they are opposite horizontal sides of a rectangle, they are perfectly parallel." + "\n"
            r"Piece **r**, however, is a diagonal strut that slants across the frame and intersects the others. Therefore, the only pieces listed that are parallel to each other are **n and q**."),
    
    "q26": (r"Reading bar graphs requires you to trace lines carefully. First, locate **Wednesday** along the bottom horizontal axis." + "\n"
            r"Follow the top of Wednesday's bar straight across to the left until you hit the vertical axis, which shows the amount of money." + "\n"
            r"The top of the bar stops exactly halfway between the 1500 and 2000 marks. Halfway between those numbers is a difference of 250, making the total amount **sh 1,750**."),
    
    "q27": (r"Let's evaluate each shape's properties! A cylinder has curved sides and circular ends. A cube is made entirely of perfect squares. A cuboid is made of rectangles." + "\n"
            r"A **pyramid**, however, is unique. It always has a polygon at its base, and all of its side faces are **triangles** that slant upwards to meet at a single sharp point at the top (the apex)." + "\n"
            r"Because of this, the statement 'A pyramid has a triangular face' is the only mathematically correct description!"),
    
    "q28": (r"To find the total number of patients, we need to read and add up all the tally marks in the table." + "\n"
            r"Malaria and HIV/AIDS are easy because the numbers are given directly as **12** and **8**." + "\n"
            r"For Diabetes, we count 4 vertical strokes, which means 4 patients. For Tuberculosis, there is one completed bundle (four strokes crossed by a diagonal line) representing 5, plus one extra stroke, making it 6 patients." + "\n"
            r"Calculating the total ($12 + 4 + 6 + 8$) gives us **30 patients** treated at the dispensary."),
    
    "q29": (r"Let's turn this story into math! We can use the letter $p$ to represent the unknown number of oranges Ngei started with." + "\n"
            r"We're told he gave out 4 oranges to a friend. Giving away means subtraction, so we write this part as $p - 4$." + "\n"
            r"After giving them away, he was left with 'more than 6' oranges. In mathematics, 'more than' is shown using the greater than symbol ($>$). When we put it all together, the correct inequality is **$p - 4 > 6$**."),
    
    "q30": (r"We are dealing with an unknown total amount of money, which we will call $x$." + "\n"
            r"This money was shared equally among 50 women. In math, sharing equally means division ($\div$), so we can write this as a fraction: $\dfrac{x}{50}$." + "\n"
            r"The problem tells us that after the division, each woman received exactly sh 8,500. So, we set our fraction equal to that amount. The equation that perfectly represents this information is **$\dfrac{x}{50} = 8500$**."),
}

def to_js_string(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    return s

with open("src/data/pastPapers.js", "r", encoding="utf-8") as f:
    content = f.read()

for q_id, explanation in EXPS.items():
    js_safe = to_js_string(explanation)
    pattern = r'(id:\s*"' + re.escape(q_id) + r'"(?:(?!id:\s*").)*?explanation:\s*)"(?:[^"\\]|\\.|\n|\r)*?"'
    
    def repl(m, text=js_safe):
        return m.group(1) + '"' + text + '"'
        
    new_content = re.sub(pattern, repl, content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
    else:
        print(f"WARNING: Missed {q_id}")

with open("src/data/pastPapers.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Rewritten and applied ALL RAW STRINGS successfully.")
