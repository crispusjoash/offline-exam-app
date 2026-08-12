import json
import re

file_path = 'src/data/kpsea-sst-parta-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

explanations = {
    21: """The correct answer is **B**.

**Analysis of the Correct Answer:**
A side roll involves the entire body rolling laterally across the floor. Performing on a **flat ground free from objects and holes** is a critical safety measure because any uneven surface, stones, or depressions can cause severe bruises, sprains, or spinal injuries during the roll.

**Why Other Options Are Incorrect:**
* **A & D:** While avoiding extreme heat or fatigue is a good general practice for physical activity, it is not a direct safety measure specific to executing a rolling skill.
* **C:** Running around is a warm-up activity, not a safety precaution for the surface on which you roll.

📌 **Key Learning Note:**
In gymnastics, the environment (the physical surface and surrounding space) must be checked and cleared of all hazards before any tumbling or rolling begins.""",

    22: """The correct answer is **B**.

**Analysis of the Correct Answer:**
Once a clay pot has completely dried (or has been fired in a kiln), its surface is hard and brittle. **Painting** is the most suitable decoration technique because it applies color to the surface without requiring the clay to be soft or pliable.

**Why Other Options Are Incorrect:**
* **A:** Piercing involves cutting holes through the walls, which must be done when the clay is leather-hard (partially dried but still soft).
* **C:** Texturing (scratching or stamping patterns) requires the clay to be wet or leather-hard.
* **D:** Embedding (pressing objects like beads or shells into the surface) must also be done when the clay is soft enough to yield.

📌 **Key Learning Note:**
Decoration techniques in pottery are strictly dictated by the moisture content of the clay. Subtractive or additive physical alterations must happen before drying, while surface coloring (painting) happens after.""",

    23: """The correct answer is **C**.

**Analysis of the Correct Answer:**
A fiddle is a stringed instrument played with a bow. Because it is melodic, it does **not play a percussive role**. Percussive roles (providing the beat and rhythm) are played by membranophones (drums) or idiophones (shakers, bells).

**Why Other Options Are Incorrect:**
* **A:** A fiddle often plays alongside the voices, providing harmonic accompaniment.
* **B:** The sharp, clear tone of a fiddle is frequently used to set the pitch for singers before they enter.
* **D:** Fiddles commonly play instrumental solos or interludes between vocal verses.

📌 **Key Learning Note:**
Instruments are classified by how they produce sound. Melodic stringed instruments (chordophones) handle pitch and interludes, while drums and shakers handle percussion.""",

    24: """The correct answer is **C**.

**Analysis of the Correct Answer:**
A standard football (soccer ball) is perfectly round in all directions, a 3D geometric shape known as **spherical**. This shape allows it to roll smoothly and predictably across a flat field.

**Why Other Options Are Incorrect:**
* **A:** An oval ball is used in sports like rugby and American football, designed for carrying and unpredictable bouncing.
* **B:** A cuboid is box-shaped and cannot roll.
* **D:** A cylindrical shape (like a can) only rolls in one direction, making it unsuitable for multidirectional field games.

📌 **Key Learning Note:**
The spherical shape of a soccer ball is engineered specifically for aerodynamics, rolling efficiency, and equal bounce from any angle.""",

    25: """The correct answer is **D**.

**Analysis of the Correct Answer:**
To "improvise" means to create or use something from whatever is available when the standard materials are not present. **Old carton boxes** provide a stiff, accessible, and cheap material that can effectively replace expensive commercial mounting boards.

**Why Other Options Are Incorrect:**
* **A & C:** Manilla and sugar paper are generally too thin and flimsy to act as a sturdy backing mount for other drawings.
* **B:** Hardboard is a standard, commercial mounting surface, not an *improvised* (recycled or locally sourced alternative) material.

📌 **Key Learning Note:**
Improvisation in art promotes environmental conservation through recycling and makes art creation accessible regardless of financial resources.""",

    26: """The correct answer is **B**.

**Analysis of the Correct Answer:**
Traditional string instruments (like the Nyatiti, Orutu, or fiddle) are typically constructed from wood and animal skin. **Washing it with water** is highly destructive; it will warp and rot the wood, and ruin the tension and integrity of the skin resonator. 

**Why Other Options Are Incorrect:**
* **A & C:** Hanging the instrument or keeping it in a dedicated storage box are excellent ways to protect it from physical damage and pests.
* **D:** While not as secure as a box, carefully resting it against a wall in a safe place is a standard way of setting it down.

📌 **Key Learning Note:**
Wooden and skin-based musical instruments should be cleaned by wiping with a dry or very slightly damp cloth, never by soaking or washing.""",

    27: """The correct answer is **D**.

**Analysis of the Correct Answer:**
In rounders, the batting team scores points by running quickly between bases. A critical safety measure is that **fielders must avoid obstructing (blocking) runners**. If a fielder stands in the running path, it can lead to severe, high-speed collisions.

**Why Other Options Are Incorrect:**
* **A:** In rounders, the *bowler* throws the ball, not the batsman. Furthermore, throwing slowly is a tactical choice, not a strict safety rule.
* **B:** Rounders does not traditionally require the batting team to wear heavy gloves (unlike baseball).
* **C:** The batter stands at the batting square facing the bowler, not behind them.

📌 **Key Learning Note:**
Obstruction in base-running games is both a foul and a major safety hazard; the running track must always be kept clear.""",

    28: """The correct answer is **D**.

**Analysis of the Correct Answer:**
Matting (creating a window mount) requires a precise, logical sequence. First, you must **measure** the artwork to determine the window size. Next, you **cut** the window out of the mounting board. Then, you **centre** the artwork precisely behind the window. Finally, you **paste** (tape or adhere) it in place.

**Why Other Options Are Incorrect:**
* **A, B & C:** Any sequence that involves cutting before measuring will result in inaccurate sizes and ruined materials. Pasting before centering guarantees a crooked display.

📌 **Key Learning Note:**
In all design and fabrication processes, measurement is always the first step: "Measure twice, cut once." """,

    29: """The correct answer is **B**.

**Analysis of the Correct Answer:**
To record a live performance, a device must possess an input sensor (a lens for video and a microphone for audio). A **flash disk** (USB drive) is merely a digital storage medium; it has no lenses or microphones and cannot record anything on its own.

**Why Other Options Are Incorrect:**
* **A, C & D:** Cameras, smartphones, and tablets are all equipped with built-in cameras and microphones capable of capturing both the visual and auditory elements of a folk dance.

📌 **Key Learning Note:**
Recording devices actively capture input from the physical world, whereas storage devices only passively hold digital data.""",

    30: """The correct answer is **B**.

**Analysis of the Correct Answer:**
When a volleyball player joins their hands together and extends their forearms forward to receive a low-flying ball (usually a serve or a spike), they are executing a skill known as **digging** (or the forearm pass).

**Why Other Options Are Incorrect:**
* **A:** Blocking involves jumping at the net with raised hands to stop a spike from crossing over.
* **C:** Spiking is aggressively hitting the ball downwards over the net into the opponent's court.
* **D:** Serving is the action used to initiate play from behind the baseline.

📌 **Key Learning Note:**
The dig is the primary defensive skill in volleyball, essential for keeping the ball in the air when the opponent makes a hard offensive attack."""
}

for q in data["sectionA"]:
    num = q["questionNumber"]
    if num in explanations:
        q["explanation"] = explanations[num]

new_content = "export const kpseaSstParta2024 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 3 completed successfully.")
