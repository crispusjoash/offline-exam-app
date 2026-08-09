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
    "q1": "To read a large number like **346,920** in words, we group the digits by their place value periods (thousands and ones).\n\n* First, we read the numbers in the thousands period: '346' is read as **Three hundred forty-six thousand**.\n* Next, we read the numbers in the ones period: '920' is read as **nine hundred and twenty**.\n* Combining both parts together, the price of the land is **Three hundred forty-six thousand nine hundred and twenty shillings**.",
    
    "q2": "To find the place value of the digit **9** in the number **49,361**, we identify the position of each digit starting from the right.\n\n* The digit 1 is in the ones place.\n* The digit 6 is in the tens place.\n* The digit 3 is in the hundreds place.\n* The digit 9 is in the **thousands** place.\n* Therefore, the place value of digit 9 is **Thousands**.",
    
    "q3": "Arranging numbers in **descending order** means placing them from the largest to the smallest.\n\n* Let's look at the numbers: 46,455, 62,326, 200,152, and 59,441.\n* The largest number is **200,152** because it has a digit in the hundreds of thousands place.\n* Comparing the remaining five-digit numbers, the largest is **62,326**, followed by **59,441**, and finally **46,455**.\n* So, the correct descending order is: **200,152, 62,326, 59,441, 46,455**.",
    
    "q4": "To find the total number of seedlings, we need to multiply the number of rows by the number of seedlings in each row.\n\n* There are **91** rows, and each row has **807** seedlings.\n* We calculate the total by multiplying: $91 \\times 807$.\n* Breaking it down: $90 \\times 807 = 72,630$ and $1 \\times 807 = 807$.\n* Adding them together: $72,630 + 807 = 73,437$.\n* Therefore, there are **73,437** seedlings altogether.",
    
    "q5": "To find the area of the part decorated with flowers, we must identify the shape of that part.\n\n* The decorated section forms a **right-angled triangle**.\n* The base of this triangle is **20 cm**, and the height is **18 cm**.\n* The formula for the area of a triangle is: $\\frac{1}{2} \\times \\text{base} \\times \\text{height}$.\n* Applying the formula: $\\frac{1}{2} \\times 20 \\times 18 = 10 \\times 18 = 180$.\n* The area of the decorated part is **180 cm\u00b2**.",
    
    "q6": "Let's analyze the pattern in the distance run by the athlete each day.\n\n* Monday: 400 m\n* Tuesday: 800 m (which is $400 \\times 2$)\n* Wednesday: 1,600 m (which is $800 \\times 2$)\n* Thursday: 3,200 m (which is $1600 \\times 2$)\n* The pattern reveals that the distance **doubles** every consecutive day.\n* To find the distance for Friday, we multiply Thursday's distance by 2: $3200 \\times 2 = 6400$.\n* The athlete ran **6,400** metres on Friday.",
    
    "q7": "To find the total fraction of the land given away, we need to add the two fractions: $\\frac{5}{8}$ and $\\frac{1}{4}$.\n\n* Before adding, the fractions must have a **common denominator**.\n* The lowest common multiple of 8 and 4 is **8**.\n* Convert $\\frac{1}{4}$ to have a denominator of 8: $\\frac{1 \\times 2}{4 \\times 2} = \\frac{2}{8}$.\n* Now, add the fractions: $\\frac{5}{8} + \\frac{2}{8} = \\frac{7}{8}$.\n* Wanjala gave away **$\\frac{7}{8}$** of the land altogether.",
    
    "q8": "To find the fraction of the population that was vaccinated, we must convert the percentage into a simplified fraction.\n\n* Percentages are essentially fractions with a denominator of 100, so 62% can be written as **$\\frac{62}{100}$**.\n* Next, we simplify the fraction by dividing both the numerator and the denominator by their greatest common divisor, which is 2.\n* Numerator: $62 \\div 2 = 31$.\n* Denominator: $100 \\div 2 = 50$.\n* The simplified fraction is **$\\frac{31}{50}$**.",
    
    "q9": "To convert the fraction $\\frac{7}{20}$ into a decimal, we can make the denominator 100.\n\n* A fraction with a denominator of 10 or 100 is very easy to convert to a decimal.\n* Multiply both the numerator and the denominator by 5 to get a denominator of 100: $\\frac{7 \\times 5}{20 \\times 5} = \\frac{35}{100}$.\n* Now, we can easily write $\\frac{35}{100}$ as a decimal.\n* Since 35 is divided by 100, we move the decimal point two places to the left, giving us **0.35**.",
    
    "q10": "To solve this subtraction problem, we must align the numbers properly according to their decimal points.\n\n* Write the numbers vertically:\n   $0.345$\n$-$ $0.236$\n* Start subtracting from the rightmost digit (thousandths place): We cannot subtract 6 from 5, so we borrow 1 from the hundredths place (making it 3) and change 5 to 15. $15 - 6 = 9$.\n* In the hundredths place: $3 - 3 = 0$.\n* In the tenths place: $3 - 2 = 1$.\n* In the ones place: $0 - 0 = 0$.\n* The correct answer is **0.109**."
}

for q in data["sectionA"]:
    if q["id"] in updates:
        q["explanation"] = updates[q["id"]]

new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 1 completed!")
