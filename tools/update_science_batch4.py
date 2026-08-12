import re

new_explanations = {
    "kpsea-science-2022-q31": """The correct answer is **(ii), (i), (iv), (iii)**.

**Analysis of the Correct Answer:**
Safety is the first priority when cleaning a charcoal *jiko*. The correct and safe sequence is:
1. **(ii) Allow it to cool:** Never handle a hot *jiko* to avoid severe burns.
2. **(i) Empty the ashes:** Remove the cold, burnt ash from the ash tray.
3. **(iv) Wipe the metal parts:** Clean the exterior metallic body using a damp cloth.
4. **(iii) Leave it to dry:** Allow any moisture to dry off completely to prevent the metal from rusting.

**Why Other Options Are Incorrect:**
* **(i), (ii), (iv), (iii):** Emptying ashes (i) before allowing the *jiko* to cool (ii) is extremely dangerous as hot ashes can cause severe burns or start a fire.
* **(i), (iii), (ii), (iv):** Again, emptying ashes (i) from a hot *jiko* is dangerous.
* **(ii), (i), (iii), (iv):** Leaving it to dry (iii) before wiping the metal parts (iv) makes no logical sense.

📌 **Key Learning Note:**
Always allow cooking equipment (like a *jiko* or stove) to **cool completely** before attempting to clean or handle them to prevent burn injuries.""",
    
    "kpsea-science-2022-q32": """The correct answer is **To prevent them from staining.**

**Analysis of the Correct Answer:**
Kitchen utensils (like plates, cups, and sufurias) should be cleaned immediately after use while food remnants are still fresh. If dirty utensils are left unwashed for a long time, food particles (especially oils, tea, and colored spices) dry up, harden, and create permanent, stubborn **stains** that are very difficult to remove later.

**Why Other Options Are Incorrect:**
* **To make the utensil last long.:** While proper cleaning maintains hygiene, immediate washing is specifically to prevent staining; durability is more related to the material (e.g. plastic vs steel).
* **To prevent them from cracking.:** Cracking happens due to physical dropping or extreme sudden temperature changes (like pouring cold water on hot glass), not due to delayed washing.
* **To make them shine after washing.:** Shining is achieved by thorough scrubbing and polishing, not necessarily by washing immediately.

📌 **Key Learning Note:**
Wash utensils **immediately after use** to prevent food from hardening and causing permanent **stains**.""",
    
    "kpsea-science-2022-q33": """The correct answer is **prevent further damage to the clothes**.

**Analysis of the Correct Answer:**
Mending (repairing tears, gaping seams, or replacing missing buttons) should always be done **before** washing. The physical action of washing (rubbing, wringing, and agitation in water) puts severe stress on fabric. If a garment with a small tear is washed, the tear will stretch and enlarge, causing **further damage to the clothes**.

**Why Other Options Are Incorrect:**
* **prevent the clothes from getting creased:** Creasing is caused by wringing or folding clothes poorly, and is fixed by ironing, not by mending.
* **make the clothes look new after washing:** Washing and ironing make clothes look neat, but mending itself just repairs damage.
* **retain the original colour of the clothes.:** Color retention is achieved by using mild soap, washing in cold water, and drying in the shade, not by mending.

📌 **Key Learning Note:**
Always **mend** torn clothes *before* washing them because the washing process will enlarge small tears and cause further damage.""",
    
    "kpsea-science-2022-q34": """The correct answer is **Do not bleach.**

**Analysis of the Correct Answer:**
On international laundry care labels, a simple triangle represents the use of bleach. When a symbol has a large cross (X) drawn through it, it indicates a warning or prohibition. Therefore, a triangle with an 'X' crossing it means **"Do not bleach"**.

**Why Other Options Are Incorrect:**
* **Wash by hand.:** The symbol for "hand wash only" is a tub of water with a hand submerged in it.
* **Do not dry clean.:** The symbol for dry cleaning is a circle. A circle with a cross through it means "Do not dry clean."
* **Dry on a clothes line.:** The symbol for line drying is a square with a curved line at the top (like an envelope).

📌 **Key Learning Note:**
- **Triangle:** Bleach allowed.
- **Triangle with X:** Do NOT bleach.
- **Tub of water:** Wash symbol.""",
    
    "kpsea-science-2022-q35": """The correct answer is **Sewing.**

**Analysis of the Correct Answer:**
Knitting, weaving, and crocheting are all primary methods of **creating fabric** or complete garments directly from threads or yarn. **Sewing**, on the other hand, is not a method of creating raw fabric; it is the process of using a needle and thread to **join pre-existing pieces of fabric together**. Therefore, it is the odd one out.

**Why Other Options Are Incorrect:**
* **Knitting.:** Knitting uses two long needles to interlock loops of yarn into a continuous fabric (often used for sweaters and scarves).
* **Weaving.:** Weaving uses a loom to interlace two sets of threads (warp and weft) at right angles to create woven fabric.
* **Crotcheting.:** Crocheting uses a single hooked needle to pull loops of yarn through other loops to create fabric.

📌 **Key Learning Note:**
**Knitting, weaving, and crocheting** create fabric from yarn. **Sewing** joins already-made fabrics together.""",
    
    "kpsea-science-2022-q36": """The correct answer is **Approach, take-off, flight, landing.**

**Analysis of the Correct Answer:**
The long jump is a track and field event divided into four distinct phases that must happen in sequence:
1. **Approach:** The athlete runs along the runway to build maximum speed.
2. **Take-off:** The athlete forcefully jumps upwards and forwards from the wooden take-off board.
3. **Flight:** The athlete moves through the air.
4. **Landing:** The athlete touches down safely in the sandpit.

**Why Other Options Are Incorrect:**
* **Flight, take-off, approach, landing.:** Flight cannot happen before take-off.
* **Take-off, landing, approach, flight.:** You cannot take off before making your approach run.
* **Landing, approach, take-off, flight.:** Landing is the final phase, not the first.

📌 **Key Learning Note:**
The correct sequence for jumps (Long Jump / High Jump): **Approach ➔ Take-off ➔ Flight ➔ Landing**.""",
    
    "kpsea-science-2022-q37": """The correct answer is **The thrower is the only player who is supposed to be in the throwing area.**

**Analysis of the Correct Answer:**
A javelin is a sharp, heavy spear that acts as a dangerous projectile. To prevent fatal accidents during practice or competition, strict safety rules apply. The most critical rule is that the throwing area and the landing sector must be completely clear of all people. **Only the thrower** is permitted in the throwing area when a throw is about to happen.

**Why Other Options Are Incorrect:**
* **Only the thrower and the one to collect...:** No one should be in the landing area waiting to collect it while it is being thrown; they must wait until the javelin lands and stops completely.
* **The javelin may be thrown back to the throwing area...:** A javelin must **never** be thrown back to the starting point. It must be carried back by hand vertically.
* **The thrown javelin should be caught while in the air...:** This is incredibly dangerous and fatal; a flying javelin must never be caught.

📌 **Key Learning Note:**
Javelins are dangerous weapons. **Never** throw a javelin if someone is in the landing area, and **never** throw it back to the starting line.""",
    
    "kpsea-science-2022-q38": """The correct answer is **To reduce swelling.**

**Analysis of the Correct Answer:**
A strain is a stretched or torn muscle/tendon, while a sprain is a stretched or torn ligament. Both injuries cause immediate internal inflammation and swelling. In first aid, applying a firm bandage (compression) around the injured joint limits the accumulation of blood and inflammatory fluids in the tissues, which helps to **reduce swelling** and support the joint.

**Why Other Options Are Incorrect:**
* **To stop bleeding.:** Strains and sprains are internal tissue injuries; they do not involve open cuts or external bleeding.
* **To immobilise the leg.:** While a bandage provides some support, complete immobilization of a fractured leg requires rigid **splints**, not just a bandage.
* **To use the first aid materials.:** First aid materials are used to treat specific injuries, not just for the sake of using them up.

📌 **Key Learning Note:**
The first aid treatment for Sprains and Strains follows the **RICE** method: **R**est, **I**ce, **C**ompression (bandage to reduce swelling), and **E**levation.""",
    
    "kpsea-science-2022-q39": """The correct answer is **Peter drunk water.**

**Analysis of the Correct Answer:**
Athletes need to hydrate properly before engaging in vigorous physical activities like a race to prevent muscle cramps and heat exhaustion. **Water** is the best, most easily absorbed liquid for rapid hydration. Therefore, Peter made the right choice by drinking water.

**Why Other Options Are Incorrect:**
* **James drunk porridge.:** Porridge is heavy, thick, and slow to digest. Drinking it right before a race causes stomach cramps and discomfort.
* **Sophia drunk milk.:** Milk contains fats and proteins that are slow to digest and can cause nausea or an upset stomach during vigorous running.
* **Daisy drunk coffee.:** Coffee contains caffeine, which is a diuretic (it makes you urinate more), leading to faster dehydration during the race.

📌 **Key Learning Note:**
Always drink adequate amounts of plain **water** before and during exercise to stay hydrated. Avoid heavy meals, milk, or coffee right before a race.""",
    
    "kpsea-science-2022-q40": """The correct answer is **Swimming regulary with friends.**

**Analysis of the Correct Answer:**
Physical fitness is defined as the ability of the body systems to work efficiently, which is achieved and maintained through regular, active physical exercise. **Swimming regularly** is an excellent full-body aerobic exercise that builds cardiovascular endurance, muscular strength, and overall physical fitness.

**Why Other Options Are Incorrect:**
* **Sleeping for long hours so as to rest.:** While 8 hours of sleep is necessary for recovery, excessive sleeping leads to physical inactivity and obesity, not fitness.
* **Eating balanced diet at all times.:** A balanced diet provides necessary nutrients for health, but diet alone without physical exercise does not build cardiovascular or muscular fitness.
* **Watching soccer games to learn the skills.:** Watching others play sports is a passive, sedentary activity. Fitness requires *doing* the exercise yourself.

📌 **Key Learning Note:**
**Physical fitness** is achieved through active, regular physical exercises (like running, swimming, skipping rope) combined with a balanced diet."""
}

with open('src/data/kpsea-science-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

for q_id, new_exp in new_explanations.items():
    pattern = r'("id": "' + q_id + r'".*?"explanation": )"(.*?)"'
    def repl(m):
        escaped_exp = new_exp.replace('\n', '\\n').replace('"', '\\"')
        return m.group(1) + '"' + escaped_exp + '"'
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open('src/data/kpsea-science-2022.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Batch 4 completed!")
