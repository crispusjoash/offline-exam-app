import json
import shutil

filepath = 'public/data/kjsea-pretech-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    d = json.load(f)

exp_updates = {
    '1': '''The correct answer is **mechanic**.

**Analysis of the Correct Answer:**
A mechanic is a skilled professional whose primary occupation is the maintenance, repair, and troubleshooting of motor vehicles (cars, trucks, motorcycles) and machinery.

**Why Other Options Are Incorrect:**
* **repairer:** This is a generic term that could apply to repairing anything (shoes, electronics, clothes) and is not the specific vocational term for vehicle repair.
* **engineer:** An engineer focuses on the scientific design, development, and building of engines, systems, or structures, rather than performing day-to-day manual repairs in a garage.
* **designer:** A designer creates the aesthetic or functional blueprints and plans for a vehicle prior to its manufacturing, rather than fixing it.''',

    '2': '''The correct answer is **avoid occurrence of accidents**.

**Analysis of the Correct Answer:**
The primary and most critical reason for observing safety measures (like wearing PPE, following machine guidelines, and ensuring proper lighting) in a technical learning environment is to prevent injuries, harm, and the occurrence of workplace accidents.

**Why Other Options Are Incorrect:**
* **improve their understanding:** While a safe environment is conducive to learning, safety measures themselves do not directly improve cognitive understanding of a topic.
* **maintain clean workshop areas:** Cleanliness (housekeeping) is a *part* of safety, but the ultimate goal of safety measures goes far beyond just keeping the area clean.
* **keep the learners healthy:** Safety prevents acute injuries (accidents), whereas health generally relates to long-term well-being and disease prevention (though occupational health is related, avoiding accidents is the direct goal of workshop safety rules).''',

    '3': '''The correct answer is **Technical**.

**Analysis of the Correct Answer:**
The image displays an isometric projection of a rectangular block. This is a form of **technical drawing**, which uses specific standardized rules, scales, and geometric principles to accurately represent 3D objects on a 2D surface for engineering and manufacturing purposes.

**Why Other Options Are Incorrect:**
* **Artistic:** Artistic drawings focus on aesthetics, emotion, and free expression, without strict adherence to standardized geometric dimensions.
* **Freehand sketch:** While a sketch is a type of technical drawing, the sharp, perfectly straight lines and precise angles shown typically indicate a formal instrument-drawn technical drawing, not a rough freehand sketch.
* **Rectangular block:** This describes the *object* being drawn, not the *type* (category) of drawing communication.''',

    '4': '''The correct answer is **Plastic**.

**Analysis of the Correct Answer:**
Plastic (e.g., from an old jerrycan or large container) is the ideal material to improvise a basin because it is completely waterproof, lightweight, durable, and can easily be cut into a basin shape to hold water without leaking.

**Why Other Options Are Incorrect:**
* **Rubber:** While rubber is waterproof, standard rubber materials (like old inner tubes) are usually too flexible and floppy to form a rigid, freestanding basin structure without a frame.
* **Timber:** Untreated wood is porous, absorbs water, and eventually leaks or rots. It is very difficult to quickly improvise a watertight basin from timber.
* **Leather:** Leather is porous, absorbs moisture, and degrades quickly when subjected to standing water. It cannot function as a water basin.''',

    '5': '''The correct answer is **Vernier calliper**.

**Analysis of the Correct Answer:**
A Vernier calliper is a highly precise measurement instrument equipped with external lower jaws. These jaws are specifically designed to accurately grip and measure the external diameter of cylindrical or spherical objects, such as pipes, to a high degree of accuracy (e.g., 0.02 mm).

**Why Other Options Are Incorrect:**
* **Tape measure:** A flexible tape measure is used for measuring long linear distances (like room dimensions) and is not accurate enough for small pipe diameters.
* **Steel tape:** Similar to a tape measure, it is meant for linear measurements and cannot properly wrap around or grip a small pipe to find the exact diameter.
* **Ruler:** A ruler can only approximate the diameter by holding it across the end of the pipe, which leads to parallax errors and lacks the precision of a calliper's gripping jaws.''',

    '6': '''The correct answer is **Starving**.

**Analysis of the Correct Answer:**
The "Fire Triangle" consists of three elements: Heat, Oxygen, and Fuel. **Starving** a fire specifically means physically removing the fuel source (in this case, taking the unburnt pieces of firewood away from the fire). Without fuel, the fire eventually dies out.

**Why Other Options Are Incorrect:**
* **Cooling:** This method involves removing the *heat* element, almost always by applying water to lower the temperature.
* **Smothering:** This method involves cutting off the *oxygen* supply, such as covering the fire with a fire blanket, sand, or foam.
* **Interrupting:** This refers to breaking the chemical chain reaction (using specific dry chemical extinguishers), not the physical removal of firewood.''',

    '7': '''The correct answer is **margin**.

**Analysis of the Correct Answer:**
In technical drawing and drafting, the continuous border drawn at a specified distance from the edges of the drawing paper is known as the **margin**. It frames the drawing area, ensuring that if the edges of the paper get frayed or torn, the actual drawing remains intact and readable.

**Why Other Options Are Incorrect:**
* **draft:** A draft refers to a preliminary version of a drawing or document, or the taper on a molded part.
* **drift:** In engineering, drift refers to a gradual deviation from a set course or standard, or a tool used for aligning holes.
* **outline:** The outline refers to the visible outer boundary lines of the *object* being drawn, not the border of the drawing paper.''',

    '8': '''The correct answer is **title block**.

**Analysis of the Correct Answer:**
The rectangular box (marked Q) located at the bottom right corner of standard technical drawing layouts is the **title block**. It contains crucial metadata about the drawing, including the title of the project, the draftsman's name, the scale, date, drawing number, and projection symbol.

**Why Other Options Are Incorrect:**
* **title margin:** There is no standard drafting term called "title margin". The margin surrounds the paper.
* **title layout:** The layout refers to the overall arrangement of the entire sheet (including borders, margins, and orthographic views), not just the specific box containing the text details.
* **name block:** While it contains the draftsman's name, the universally accepted standard technical term is "title block".''',

    '9': '''The correct answer is **C**.

**Analysis of the Correct Answer:**
In engineering drawing standards (such as BS 8888 or ISO), when dimensioning a very small circle (like 10 mm), there is not enough space inside the circle for the arrows and text. Therefore, the leader line is drawn originating from the *outside*, with the arrowhead pointing inwards towards the center, touching the outer circumference. Option C illustrates this correct convention.

**Why Other Options Are Incorrect:**
* **A:** This option incorrectly places the dimension text and arrows entirely inside, which is cluttered and against standards for circles that are too small (like 10 mm).
* **B:** The dimension line does not pass through or point to the center properly, or the arrowheads are pointing outwards from inside, which is incorrect for small circles.
* **D:** The leader line format or arrowhead placement violates standard dimensioning conventions for small circular features.''',

    '10': '''The correct answer is **Size of the drawing in relation to the actual object.**

**Analysis of the Correct Answer:**
A scale in technical drawing is defined as the mathematical ratio or proportion between the linear dimensions drawn on the paper and the actual, real-life dimensions of the physical object. For example, a scale of 1:10 means 1 unit on the drawing represents 10 units on the actual object.

**Why Other Options Are Incorrect:**
* **Type of the required drawing:** The type of drawing refers to the projection method (isometric, orthographic, oblique), not the scale.
* **Ratio of the dimensions of a drawing:** This is incomplete. It must be the ratio of the drawing's dimensions *relative to the actual object's* dimensions, not just the ratio of dimensions within the drawing itself.
* **Angle of the drawing in relation to the actual object:** Angles in technical drawings remain true and do not change regardless of the scale used. Scale affects size, not angles.'''
}

for q in d['sectionA']:
    qn = str(q.get('questionNumber'))
    if qn in exp_updates:
        q['explanation'] = exp_updates[qn]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-pretech-2025.json')
print('Batch 1 (Q1-Q10) explanations updated successfully.')
