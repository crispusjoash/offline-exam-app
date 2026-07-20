import re
import json

new_exps = {
    "q1": "• Identify the given number: 84,072.\\n• Break it down by place value.\\n• 84 stands for Eighty four thousand.\\n• 0 in the hundreds place means zero hundreds.\\n• 72 stands for seventy two.\\n• Combine them to get: Eighty four thousand and seventy two.",
    "q2": "• Identify the given number: 436,587.\\n• Locate the digit 6.\\n• Observe its place value: It is in the thousands place.\\n• Multiply the digit by its place value: 6 \\times 1000.\\n• The total value is 6000.",
    "q3": "• Identify the total number of seedlings: 368,593.\\n• Identify the number of seedlings bought: 27,364.\\n• Subtract the bought seedlings from the total: 368,593 - 27,364.\\n• The remaining number of seedlings is 341,229.",
    "q4": "• Identify the number to be rounded: 19,468.\\n• Check the digit in the hundreds place, which is 4.\\n• Since 4 is less than 5, round down.\\n• Keep the thousands digit (9) the same and replace the rest with zeros.\\n• The rounded number is 19,000.",
    "q5": "• Observe the given pattern: 8, 24, 72, 216.\\n• Determine the rule by dividing consecutive terms: 24 \\div 8 = 3, 72 \\div 24 = 3.\\n• The rule is to multiply the previous number by 3.\\n• Multiply the last term by 3: 216 \\times 3.\\n• The next number is 648.",
    "q6": "• Apply the BODMAS rule (Brackets, Orders, Division, Multiplication, Addition, Subtraction).\\n• Step 1: Perform Division: 24 \\div 3 = 8.\\n• Step 2: Perform Multiplication: 9 \\times 6 = 54.\\n• Step 3: Rewrite the equation: 8 + 54 - 4.\\n• Step 4: Add and Subtract from left to right: 62 - 4 = 58.",
    "q7": "• Identify the fraction spent on food: 2/5.\\n• Identify the fraction spent on rent: 1/4.\\n• Find the Lowest Common Multiple (LCM) of the denominators 5 and 4, which is 20.\\n• Convert both fractions: 2/5 = 8/20 and 1/4 = 5/20.\\n• Add the fractions: 8/20 + 5/20 = 13/20.",
    "q8": "• Identify the mixed numbers: 9 5/6 and 1 1/3.\\n• Find the LCM for the denominators 6 and 3, which is 6.\\n• Convert 1 1/3 to have a denominator of 6: 1 2/6.\\n• Subtract the whole numbers: 9 - 1 = 8.\\n• Subtract the fractions: 5/6 - 2/6 = 3/6.\\n• Simplify the fraction: 3/6 = 1/2.\\n• Combine to get the final answer: 8 1/2.",
    "q9": "• Note that the total percentage of beads is 100%.\\n• Identify the percentage of red beads: 25%.\\n• Calculate the percentage of green beads: 100% - 25% = 75%.\\n• Convert the percentage to a decimal by dividing by 100.\\n• 75 \\div 100 = 0.75.",
    "q10": "• Identify the fabric used for the shirt: 0.287.\\n• Identify the fabric used for the dress: 0.45.\\n• Align the decimals and add the two values: 0.287 + 0.450.\\n• The total fabric used is 0.737.",
    "q11": "• Identify the given increase in height: 5 cm.\\n• Recall the conversion factor: 1 centimetre (cm) = 10 millimetres (mm).\\n• Multiply the value in cm by 10.\\n• 5 \\times 10 = 50 mm.",
    "q12": "• Recall that perimeter is the total distance around the outside of a shape.\\n• Identify all the outer side lengths from the diagram: 15 cm, 15 cm, 10 cm, 10 cm, and 8 cm.\\n• Add all the outer lengths together: 15 + 15 + 10 + 10 + 8.\\n• The total perimeter is 58 cm.",
    "q13": "• Identify the total length of the ribbon: 31 cm 6 mm.\\n• Identify the length cut off: 5 cm 3 mm.\\n• Subtract the millimetres separately: 6 mm - 3 mm = 3 mm.\\n• Subtract the centimetres separately: 31 cm - 5 cm = 26 cm.\\n• Combine the results: 26 cm 3 mm.",
    "q14": "• Identify the two shapes making up the wall: a rectangle and a triangle.\\n• Calculate the Area of the rectangle: length \\times width = 65 cm \\times 74 cm = 4810 cm².\\n• Calculate the Area of the triangle: 1/2 \\times base \\times height = 1/2 \\times 65 cm \\times 24 cm = 780 cm².\\n• Add the two areas together: 4810 + 780 = 5590 cm².",
    "q15": "• Identify the amount of water Kimeto drinks: 3.7 litres.\\n• Recall the conversion factor: 1 litre (L) = 1000 millilitres (ml).\\n• Multiply the value in litres by 1000.\\n• 3.7 \\times 1000 = 3700 ml.",
    "q16": "• Identify the mass of sand: 18 tonnes 481 kg.\\n• Identify the mass of small stones: 12 tonnes 394 kg.\\n• Add the kilograms together: 481 + 394 = 875 kg.\\n• Add the tonnes together: 18 + 12 = 30 tonnes.\\n• Combine the results: 30 tonnes 875 kilograms.",
    "q17": "• Identify the number of lorries: 4.\\n• Identify the mass carried by each lorry: 24 tonnes 235 kg.\\n• Multiply the kilograms by 4: 235 \\times 4 = 940 kg.\\n• Multiply the tonnes by 4: 24 \\times 4 = 96 tonnes.\\n• Combine the results: 96 tonnes 940 kilograms.",
    "q18": "• Identify the mass of exported flowers: 4,850,000 kg.\\n• Recall the conversion factor: 1 tonne = 1000 kilograms.\\n• Divide the mass in kilograms by 1000 to convert to tonnes.\\n• 4,850,000 \\div 1000 = 4850 tonnes.",
    "q19": "• Observe the short hand (hour hand) on the clock: It is between 2 and 3, indicating the hour is 2.\\n• Observe the long hand (minute hand): It is pointing at 7, which represents 35 minutes (7 \\times 5).\\n• Combine them to read the time: 2:35.\\n• Note the time of day given: 'in the afternoon'.\\n• Therefore, the time is 2.35 p.m.",
    "q20": "• Identify the departure time from Manga station: 6.15 a.m.\\n• Identify the arrival time at Pate station: 11.54 a.m.\\n• Subtract the departure minutes from the arrival minutes: 54 - 15 = 39 minutes.\\n• Subtract the departure hours from the arrival hours: 11 - 6 = 5 hours.\\n• The total journey duration is 5 hours 39 minutes.",
    "q21": "• Identify the Selling Price of the dress: sh 1675.\\n• Identify the Profit made: sh 390.\\n• Recall the formula: Buying Price = Selling Price - Profit.\\n• Substitute the values: 1675 - 390.\\n• The Buying Price is sh 1285.",
    "q22": "• Identify the Area of the paper: 72 cm².\\n• Identify the Length of the paper: 9 cm.\\n• Recall the area formula: Area = Length \\times Width.\\n• Calculate Width in cm: 72 \\div 9 = 8 cm.\\n• Convert cm to mm by multiplying by 10 (1 cm = 10 mm): 8 \\times 10 = 80 mm.",
    "q23": "• Place the center mark of the protractor exactly on vertex M of the triangle.\\n• Align the base line (0° mark) of the protractor perfectly with the line segment LM.\\n• Trace the line segment MN upwards and see where it crosses the curved edge of the protractor.\\n• Ensure you read the correct inner or outer scale that starts with 0° on line LM.\\n• The line crosses at the 40° mark, so angle LMN is 40°.",
    "q24": "• Identify the given 3-D object: It is a rectangular prism (also known as a cuboid).\\n• Recall the geometric properties of a cuboid.\\n• A cuboid has 6 rectangular flat faces.\\n• A cuboid has 8 vertices (the sharp corners).\\n• A cuboid has 12 edges (the straight lines where two faces meet).",
    "q25": "• Observe the orientation of the timber pieces in the window frame.\\n• Pieces 'n' (top) and 'q' (bottom) are straight horizontal lines.\\n• Horizontal lines on opposite ends of a rectangle are parallel because they never intersect.\\n• Pieces 'm' and 'p' are vertical and also parallel, but not listed together as an option.\\n• Piece 'r' is a diagonal line that intersects the frame.\\n• Therefore, 'n' and 'q' are the parallel pieces.",
    "q26": "• Locate 'Wednesday' on the horizontal (x-axis) of the bar graph.\\n• Follow the top of the bar for Wednesday straight across to the vertical (y-axis).\\n• Observe that the top of the bar lies exactly halfway between the 1500 and 2000 marks.\\n• Calculate the halfway point: 1500 + 250 = 1750.\\n• The amount received is sh 1750.",
    "q27": "• Review the defining properties of the given 3-D geometric shapes.\\n• A cylinder has circular flat faces and a curved surface, not square faces.\\n• A cube has square faces, not just 'rectangular' (though squares are special rectangles, 'square' is the strict definition).\\n• A cuboid has rectangular faces, not circular.\\n• A pyramid always has a polygonal base and triangular side faces that meet at an apex. This description is accurate.",
    "q28": "• Count the tally marks for each disease to find the number of patients.\\n• Malaria: Given directly as 12.\\n• Diabetes: The tally shows 4 individual vertical strokes (////), so it is 4.\\n• Tuberculosis: The tally shows one completed bundle of 5 (four vertical strokes crossed by a diagonal) and 1 individual stroke, making it 5 + 1 = 6.\\n• HIV/AIDS: Given directly as 8.\\n• Add them all together: 12 + 4 + 6 + 8 = 30 patients.",
    "q29": "• Let $p$ represent the original number of oranges.\\n• Ngei gave out 4 oranges, which is represented mathematically by subtraction: $p - 4$.\\n• The problem states he remained with 'more than' 6 oranges.\\n• In mathematics, 'more than' is represented by the greater than symbol (>).\\n• Combine these to form the correct inequality: $p - 4 > 6$.",
    "q30": "• Let $x$ represent the total amount of money shared.\\n• The money was shared equally among 50 women, meaning we divide the total by 50: $\\\\frac{x}{50}$.\\n• The problem states that each woman received sh 8 500.\\n• Set the divided amount equal to what each woman received.\\n• The correct equation is $\\\\frac{x}{50} = 8 500$."
}

with open("c:/Users/JOASH/Desktop/CBC/offline-exam-app/src/data/pastPapers.js", "r", encoding="utf-8") as f:
    content = f.read()

for q_id, explanation in new_exps.items():
    pattern = r'(id:\s*"' + q_id + r'",.*?explanation:\s*)"(.*?)"'
    def replacer(match):
        return f'{match.group(1)}"{explanation}"'
        
    content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open("c:/Users/JOASH/Desktop/CBC/offline-exam-app/src/data/pastPapers.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Explanations updated successfully.")
