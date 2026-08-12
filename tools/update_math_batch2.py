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
    "q11": "To solve this problem, we must first round off both numbers to the nearest tens.\n\n* The number **696** ends in 6 (which is 5 or more), so we round it up to **700**.\n* The number **12** ends in 2 (which is less than 5), so we round it down to **10**.\n* Next, we share the rounded number of bags equally among the rounded number of farmers: $700 \\div 10 = 70$.\n* Each farmer will get **70** bags.",
    
    "q12": "To find the total length of the two ropes, we add their lengths together, combining the units carefully.\n\n* First, align the measurements: \n   $123$ cm $7$ mm\n$+ \\ \\ 39$ cm $2$ mm\n* Add the millimetres: $7 + 2 = 9$ mm.\n* Add the centimetres: $123 + 39 = 162$ cm.\n* Since the millimetres (9 mm) are less than 10 mm (which would make 1 cm), no carrying over is needed.\n* The total length is **162 cm 9 mm**.",
    
    "q13": "To convert the total length into millimetres, we need to know the relationship between centimetres and millimetres.\n\n* We know that **1 centimetre = 10 millimetres**.\n* Abdi's line is 6 centimetres and 5 millimetres.\n* First, convert the 6 cm to millimetres: $6 \\times 10 = 60$ mm.\n* Next, add the remaining 5 mm: $60 + 5 = 65$ mm.\n* The total length of the line is **65** millimetres.",
    
    "q14": "To determine how many more chicks the farmer needs, we must first figure out the remainder when the chicks are divided.\n\n* The farmer has 2,156 chicks to share among 15 families: $2156 \\div 15$.\n* Performing the division gives a quotient of **143** and a remainder of **11**.\n* This means after giving each family 143 chicks, there are 11 chicks left over.\n* For all 15 families to get one more chick, the farmer needs 15 chicks in total for the next round.\n* Subtract the remainder from the divisor: $15 - 11 = 4$.\n* The farmer needs to add **4** more chicks.",
    
    "q15": "To find the capacity in millilitres, we need to convert the capacity from litres.\n\n* The standard conversion is **1 litre = 1,000 millilitres (ml)**.\n* The jerrycan has a capacity of 20 litres.\n* Multiply the capacity by 1,000: $20 \\times 1000 = 20,000$.\n* The capacity of the container is **20,000** millilitres.",
    
    "q16": "To convert the mass from kilograms to tonnes, we use the standard unit conversion.\n\n* We know that **1 tonne = 1,000 kilograms (kg)**.\n* The lorry is carrying 4,500 kg of sand.\n* Divide the mass in kg by 1,000 to convert to tonnes: $4500 \\div 1000 = 4.5$.\n* The mass of the sand is **4.5** tonnes.",
    
    "q17": "To find the fraction of the material that was not used, we must first find how much material was left.\n\n* Anne started with 6.25 m and used 1.5 m.\n* The material left is: $6.25 - 1.50 = 4.75$ m.\n* The fraction not used is the material left divided by the total material: $4.75 \\div 6.25$.\n* To make the division easier, multiply both numbers by 100 to remove the decimals: $475 \\div 625$.\n* Simplifying the fraction $\\frac{475}{625}$ (by dividing by 25) gives $\\frac{19}{25}$.\n* Converting $\\frac{19}{25}$ to a decimal (by multiplying numerator and denominator by 4) gives $\\frac{76}{100} = 0.76$.\n* The fraction of the material not used is **0.76**.",
    
    "q18": "To find out how much sawdust each member gets, we divide the total mass by the number of members.\n\n* Total mass is 65 kg 460 g, and there are 5 members.\n* First, divide the kilograms: $65 \\div 5 = 13$ kg.\n* Next, divide the grams: $460 \\div 5 = 92$ g.\n* Since there's no remainder from the kg division to carry over to grams, we just combine the results.\n* Each member receives **13 kg 92 g** of sawdust.",
    
    "q19": "To write the time in the 12-hour system, we must interpret the meaning of \"a quarter past\".\n\n* A \"quarter\" of an hour is 15 minutes.\n* \"Past seven\" means the time is 15 minutes after 7 o'clock.\n* Because it is in the morning, we use the **a.m.** indicator (ante meridiem).\n* Therefore, the time is written as **7.15 a.m.**",
    
    "q20": "To find the total profit Ahmed made, we need to calculate the profit per dress and then multiply it by the number of dresses.\n\n* Profit is the selling price minus the buying price.\n* For one dress, the profit is: $1150 - 900 = 250$ shillings.\n* Since he bought and sold 2 dresses, we multiply the profit by 2: $250 \\times 2 = 500$.\n* His total profit altogether is **sh 500**."
}

for q in data["sectionA"]:
    if q["id"] in updates:
        q["explanation"] = updates[q["id"]]

new_content = "export const kpseaMath2025 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 2 completed!")
