import re

file_path = 'src/data/kpsea-math-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    11: r'''To convert any decimal number into a percentage, the rule is to multiply it by 100.\n\n* We have the decimal **0.3**.\n* When we multiply by 100, we move the decimal point two places to the right: $0.3 \times 100 = 30$.\n* This gives us **30%**.\n* So, the answer as a percentage is **30**.''',
    12: r'''To find the total fraction of the journey travelled by rail and matatu, we simply need to add their fractions together.\n\n* The fraction for the rail is **$\frac{2}{5}$**.\n* The fraction for the matatu is **$\frac{1}{3}$**.\n* Before adding, we need a common denominator. For 5 and 3, it's **15**.\n* Let's convert them: $\frac{2}{5} = \frac{6}{15}$ and $\frac{1}{3} = \frac{5}{15}$.\n* Now, we add the numerators: $\frac{6}{15} + \frac{5}{15} = \textbf{\frac{11}{15}}$.\n* The fraction of the journey travelled by rail and matatu is **$\frac{11}{15}$**.''',
    13: r'''This question requires us to convert a measurement from millimetres (mm) to centimetres (cm).\n\n* We know the basic conversion rule: **1 centimetre is equal to 10 millimetres**.\n* The jeweller measured the ring's diameter as **20 mm**.\n* To convert to centimetres, we divide by 10: $20 \div 10 = 2$.\n* So, the diameter of the ring is **2** centimetres.''',
    14: r'''First, let's find the volume of the cuboid in cubic centimetres.\n\n* The formula for the volume of a cuboid is $\text{length} \times \text{width} \times \text{height}$.\n* We multiply the given dimensions: $30 \times 15 \times 40 = \textbf{18,000 \text{ cm}^3}$.\n* Now, we need to convert this volume into litres. Remember that **$1000 \text{ cm}^3$ equals $1 \text{ Litre}$**.\n* To find the litres, we divide our volume by 1000: $18,000 \div 1000 = \textbf{18}$.\n* The container holds **18** litres of detergent.''',
    15: r'''To find out how many bags were packed, we need all our measurements to be in the same unit, kilograms.\n\n* We know that **1 tonne is equal to 1000 kilograms**.\n* The factory has 8 tonnes, which is $8 \times 1000 = \textbf{8000 \text{ kg}}$.\n* The cement is packed into bags of 50 kg each.\n* To find the number of bags, we divide the total mass by the mass of one bag: $8000 \div 50$.\n* $8000 \div 50 = \textbf{160}$.\n* The factory packed **160** bags of cement.''',
    16: r'''Let's figure out how much change Rukia should receive first.\n\n* She gave the cashier **sh 1000** and the dress cost **sh 700**.\n* Her balance is $1000 - 700 = \textbf{sh 300}$.\n* The cashier gave her this balance entirely in **sh 50** notes.\n* To find how many notes she got, we divide her total balance by 50: $300 \div 50$.\n* $300 \div 50 = \textbf{6}$.\n* Rukia received **6** sh 50 notes.''',
    17: r'''To make the subtraction easy, let's convert both amounts entirely into kilograms.\n\n* Remember, **1 tonne equals 1000 kg**.\n* The imported fertilizer is 4 tonnes 500 kg, which is $4000 + 500 = \textbf{4500 \text{ kg}}$.\n* The distributed fertilizer is 2 tonnes 900 kg, which is $2000 + 900 = \textbf{2900 \text{ kg}}$.\n* To find what remained, we subtract the distributed amount from the imported amount: $4500 - 2900$.\n* $4500 - 2900 = \textbf{1600}$.\n* The society had **1600** kilograms of fertilizer remaining.''',
    18: r'''To find the profit, we need to subtract the amount they spent (the cost price) from the amount they earned (the selling price).\n\n* They spent **sh 6,450** to cultivate the cabbages.\n* They sold all of them for **sh 9,380**.\n* The formula for profit is: $\text{Selling Price} - \text{Cost Price}$.\n* So, we calculate: $9380 - 6450$.\n* $9380 - 6450 = \textbf{2930}$.\n* The learners made a profit of **sh 2,930**.''',
    19: r'''Let's calculate the duration of the journey by breaking it down into smaller steps.\n\n* The bus departs Mtito Andei at **2.45 p.m.** and arrives in Nairobi at **6.30 p.m.**\n* First, from 2.45 p.m. to the next full hour (3.00 p.m.) is exactly **15 minutes**.\n* Next, from 3.00 p.m. to 6.00 p.m. is a solid block of **3 hours**.\n* Finally, from 6.00 p.m. to the arrival time of 6.30 p.m. is another **30 minutes**.\n* Adding these times together: $3 \text{ hours} + 15 \text{ minutes} + 30 \text{ minutes} = \textbf{3 hours 45 minutes}$.\n* The journey takes **3 hours 45 minutes**.''',
    20: r'''Let's read the clock and convert it to the 24-hour system.\n\n* The clock face shows the time is **1:30**.\n* Since the question tells us it's daytime (afternoon), this is **1:30 p.m.**\n* To convert a p.m. time into the 24-hour format, we simply add 12 hours to it.\n* So, $1 + 12 = 13$.\n* The time becomes **13:30**.\n* In the 24-hour system, this is written without the colon as **1330 h**.'''
}

for q_num, new_exp in replacements.items():
    pattern = r'("questionNumber": ' + str(q_num) + r',.*?"explanation": )"(.*?)"'
    
    def repl(m):
        import json
        return m.group(1) + json.dumps(new_exp)
        
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Batch 2 completed successfully.")
