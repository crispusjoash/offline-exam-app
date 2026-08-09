import re

file_path = 'src/data/kpsea-math-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    1: r'''When you look at a large number like **76,859**, the easiest way to read it is by breaking it into groups based on place value.\n\n* First, the '76' is in the thousands section, so we say 'Seventy-six thousand'.\n* Next, the '8' is in the hundreds place, giving us 'eight hundred'.\n* Finally, the last two digits form '59'.\n* Putting it all together, we read the number smoothly as **Seventy-six thousand eight hundred and fifty-nine**.''',
    2: r'''To find the value of a specific digit in the number **4,297,653**, we just need to identify its position starting from the right.\n\n* Counting from the right end, we pass the ones (3), tens (5), and hundreds (6), which lands the digit **7** squarely in the **thousands** place.\n* Since it represents seven thousands, we apply its place value ($7 \times 1000$).\n* The total value of the digit is **7000**.''',
    3: r'''Let's break down the pattern formed by the square root numbers on the chalkboard.\n\n* First, let's find the actual value of each square root: $\sqrt{121} = 11$, $\sqrt{144} = 12$, $\sqrt{169} = 13$, and $\sqrt{196} = 14$.\n* We can clearly see a pattern of consecutive numbers: **11, 12, 13, 14**.\n* The next number in this sequence must be **15**.\n* To write it back in the square root format, we square it: $15 \times 15 = 225$.\n* Therefore, the next square root number in the pattern is **$\sqrt{225}$**.''',
    4: r'''Rounding off to the nearest thousand means we need to look closely at the digit in the **hundreds** place.\n\n* The number is **8501**.\n* The digit in the thousands place is 8, and the digit right next to it in the hundreds place is **5**.\n* The rule for rounding is: if the next digit is 5 or more, we round **up**.\n* Since our hundreds digit is exactly 5, we round up the thousands digit from 8 to 9.\n* Therefore, 8501 rounded off to the nearest thousands is **9000**.''',
    5: r'''To find the total number of learners in the school, we need to multiply the number of classrooms by the number of learners in each one.\n\n* We have **52** classrooms in total.\n* Each classroom has exactly **36** learners.\n* So, we set up our multiplication: $52 \times 36$.\n* When we multiply these two numbers, we get **1872**.\n* There are a total of **1872** learners in the school.''',
    6: r'''To find the total area of the combined pieces of leather, we can calculate the area of each shape separately and then add them together.\n\n* **Part 1: The Rectangle**\n  The area of a rectangle is $\text{length} \times \text{width}$.\n  Here, it's $40 \times 20 = \textbf{800 \text{ cm}^2}$.\n* **Part 2: The Right-angled Triangle**\n  The area of a triangle is $\frac{1}{2} \times \text{base} \times \text{height}$.\n  Here, it's $\frac{1}{2} \times 12 \times 16 = \textbf{96 \text{ cm}^2}$.\n* **Putting it together:**\n  Total area = $800 + 96 = \textbf{896 \text{ cm}^2}$.''',
    7: r'''To arrange the decimal numbers in **descending order**, we need to list them from the largest to the smallest.\n\n* All three times start with **9.5**, so we need to look at the next digits (the hundredths and thousandths places).\n* The numbers are: 9.5**87**, 9.5**78**, and 9.5**58**.\n* Comparing these ends: 87 is the largest, 78 is in the middle, and 58 is the smallest.\n* Therefore, the correct descending order is **9.587, 9.578, 9.558**.''',
    8: r'''This is a division problem where we are looking for the **remainder** after sharing the goats equally.\n\n* The total number of goats is **1055**, and they are being shared among **24** members.\n* We need to divide: $1055 \div 24$.\n* We can do this step-by-step: $24 \times 40 = 960$. Subtracting this leaves us with 95.\n* Next, $24 \times 3 = 72$. Subtracting 72 from 95 leaves us with **23**.\n* Each member gets 43 goats, and there is a remainder of **23**.\n* Thus, **23** goats remained after sharing.''',
    9: r'''To solve this, it's best to first convert the total length of the cloth into a single unit, centimetres.\n\n* We know that **$1 \text{ m} = 100 \text{ cm}$**.\n* So, $17 \text{ m}$ is $17 \times 100 = 1700 \text{ cm}$.\n* The total length is $1700 \text{ cm} + 50 \text{ cm} = \textbf{1750 \text{ cm}}$.\n* The tailor cuts this into 5 equal pieces, so we divide: $1750 \div 5$.\n* $1750 \div 5 = \textbf{350 \text{ cm}}$.\n* The length of each piece was **350** centimetres.''',
    10: r'''To find out what fraction of the bread remained, we first need to calculate the total fraction that was eaten.\n\n* Ali ate **$\frac{2}{5}$** and Baraza ate **$\frac{1}{4}$**.\n* To add them, we find a common denominator, which is 20: $\frac{2}{5} = \frac{8}{20}$ and $\frac{1}{4} = \frac{5}{20}$.\n* Total eaten = $\frac{8}{20} + \frac{5}{20} = \textbf{\frac{13}{20}}$.\n* A whole loaf of bread represents $1$, or **$\frac{20}{20}$**.\n* To find what remains, we subtract the eaten part from the whole: $\frac{20}{20} - \frac{13}{20} = \textbf{\frac{7}{20}}$.\n* The fraction of the bread that remained is **$\frac{7}{20}$**.'''
}

for q_num, new_exp in replacements.items():
    # Replace the explanation field for the given question number
    # Use regex to find the block for the specific question number and replace its explanation
    pattern = r'("questionNumber": ' + str(q_num) + r',.*?"explanation": )"(.*?)"'
    
    def repl(m):
        # Escape newlines correctly for JSON
        escaped_exp = new_exp.replace('\n', '\\n').replace('\\', '\\\\')
        # Wait, using raw string already escapes backslashes. Let's just dump it as JSON string to be safe.
        import json
        return m.group(1) + json.dumps(new_exp)
        
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Batch 1 completed successfully.")
