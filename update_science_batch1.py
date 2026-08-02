import re

new_explanations = {
    "kpsea-science-2022-q1": """The correct answer is **(i) and (v)**.

**Analysis of the Correct Answer:**
Flowering plants are uniquely characterized by the production of flowers. Flowers often produce sweet nectar (v) to attract insects and birds for pollination. After successful pollination and fertilization, flowers develop into fruits (i) which contain seeds. 

**Why Other Options Are Incorrect:**
* **(i) and (iii):** While they produce fruits (i), all plants (flowering and non-flowering) produce leaves (iii). Leaves are not a unique characteristic of flowering plants only.
* **(ii) and (iv):** Cones (ii) are produced by non-flowering plants like pines and cypress. Spores (iv) are produced by non-flowering plants like ferns and mosses.
* **(iii) and (v):** All plants have leaves (iii), making it an incorrect identifier for distinguishing flowering plants.

📌 **Key Learning Note:**
The main distinguishing features of a flowering plant are the production of **flowers**, **fruits**, and **seeds**.""",
    
    "kpsea-science-2022-q2": """The correct answer is **D**.

**Analysis of the Correct Answer:**
Diagram D represents Penicillium, a type of microscopic fungus. Penicillium is highly valuable in medicine because it is used to extract and produce the antibiotic medicine penicillin, which cures various bacterial infections.

**Why Other Options Are Incorrect:**
* **A:** This represents a toadstool (a type of wild mushroom). Many toadstools are highly poisonous and can be fatal if consumed.
* **B:** This represents yeast, a single-celled fungus used primarily in baking (to make bread rise) and brewing, not for medicine.
* **C:** This represents an edible mushroom, which is consumed as nutritious food by human beings, not used to extract medicine.

📌 **Key Learning Note:**
Different fungi have different uses: **Yeast** (baking), **Edible Mushrooms** (food), and **Penicillium** (making antibiotic medicines).""",
    
    "kpsea-science-2022-q3": """The correct answer is **respond to changes in their environment**.

**Analysis of the Correct Answer:**
When the piece of food fell, the ants detected its presence (a change in their surroundings) using their senses and moved towards it. This behavior demonstrates that living things react or respond to stimuli (changes) in their environment to survive, find food, or escape danger.

**Why Other Options Are Incorrect:**
* **love eating food:** While living things feed, the specific action of detecting something new that dropped and reacting to it highlights responsiveness.
* **hunt for food in their environment:** Hunting is a feeding behavior of predators, but the broader scientific characteristic demonstrated by reacting to a dropped item is responsiveness.
* **hide after feeding.:** The observation was about ants moving *towards* the food, not hiding away.

📌 **Key Learning Note:**
One of the key characteristics of all living things is their ability to **respond to stimuli** (changes in their environment), such as moving towards food or away from heat.""",
    
    "kpsea-science-2022-q4": """The correct answer is **re-using and reducing**.

**Analysis of the Correct Answer:**
Using water that was already meant for washing clothes to clean the house is an example of **re-using** (using something again for another purpose). Turning off the taps when they are not in use minimizes water wastage, which is an example of **reducing** water consumption. Therefore, they are practising re-using and reducing.

**Why Other Options Are Incorrect:**
* **recycling and re-using:** Recycling involves processing waste (like dirty water) through a treatment plant to make it completely clean again, which they are not doing.
* **reducing only:** This ignores the action of washing the house with laundry water, which is re-using.
* **recycling only.:** Neither action involves the industrial or chemical purification process of recycling.

📌 **Key Learning Note:**
- **Reducing:** Using less (e.g., turning off taps).
- **Re-using:** Using the same item again (e.g., using bath water to mop floors).""",
    
    "kpsea-science-2022-q5": """The correct answer is **Sprinkle water on the floor**.

**Analysis of the Correct Answer:**
Sweeping an earthen (mud) floor raises a lot of fine dust into the air, which can irritate the respiratory system and cause sneezing or coughing. By sprinkling water on the floor before sweeping, the water binds the dust particles together, making them heavy so they settle on the ground instead of floating in the air.

**Why Other Options Are Incorrect:**
* **Put on an overcoat.:** An overcoat protects clothing from getting dirty but does not stop dust from being inhaled into the nose and lungs.
* **Wear gloves.:** Gloves protect the hands from dirt and blisters but do not prevent airborne dust from causing sneezing.
* **Change the broom she is using.:** Any dry broom will sweep up and scatter dust on a dry earthen floor; changing the broom will not solve the dust problem.

📌 **Key Learning Note:**
To maintain a healthy respiratory environment, always **sprinkle water** on earthen or dusty floors before sweeping to prevent dust from becoming airborne.""",
    
    "kpsea-science-2022-q6": """The correct answer is **some mushrooms are poisonous.**

**Analysis of the Correct Answer:**
While some mushrooms are edible and nutritious, many species of wild mushrooms (often called toadstools) are highly toxic and poisonous. Eating unidentified wild mushrooms can lead to severe food poisoning, organ failure, or even death. Therefore, it is extremely dangerous to pick and eat mushrooms growing in the forest without expert knowledge.

**Why Other Options Are Incorrect:**
* **mushrooms have no nutrients:** This is false. Edible mushrooms are highly nutritious and contain vitamins, minerals, and proteins.
* **some mushrooms have worms:** While pests may attack wild fungi, the primary life-threatening danger of eating wild mushrooms is their inherent toxicity, not worms.
* **mushrooms are difficult to cook:** Edible mushrooms are very easy and quick to cook; cooking difficulty is not a reason to avoid them.

📌 **Key Learning Note:**
Never pick and eat wild mushrooms from the forest because many varieties are **highly poisonous** and dangerous to human health.""",
    
    "kpsea-science-2022-q7": """The correct answer is **M and P**.

**Analysis of the Correct Answer:**
Part **M** represents the handle of the pan, and Part **P** represents the knob on the lid. Because the pan is used for cooking over fire, the parts that a person touches must be made of **poor conductors of heat (insulators)**, such as plastic or wood, to prevent the user from getting burned.

**Why Other Options Are Incorrect:**
* **L and P:** Part L is the main body of the cooking pan, which must be made of a *good conductor* of heat (like aluminum or steel) to cook the food.
* **L and N:** Part N is the lid covering the food, often made of metal (a good conductor) to trap heat inside.
* **M and N:** Part N is not typically made of an insulator, as it covers the hot pan directly.

📌 **Key Learning Note:**
Cooking utensils are made of **good conductors of heat** (like metals) to cook food, while their handles are made of **poor conductors of heat** (like wood or plastic) to prevent burns.""",
    
    "kpsea-science-2022-q8": """The correct answer is **evaporates easily.**

**Analysis of the Correct Answer:**
Hand sanitisers are primarily composed of alcohol (typically 60-70% ethanol or isopropanol). Alcohol is a highly volatile liquid, meaning it has a low boiling point and **evaporates easily** and rapidly into a gas when exposed to the warmth of the skin and air at room temperature. This is why hands feel dry quickly after rubbing sanitiser.

**Why Other Options Are Incorrect:**
* **freezes quickly:** Freezing means turning into a solid. Alcohol actually has a much lower freezing point than water and does not freeze on hands.
* **is absorbed by the skin:** While a microscopic amount may be absorbed, the vast majority of the liquid physically disappears because it turns into a gas (evaporates), not because the skin drinks it up.
* **condenses easily:** Condensation is the process of a gas turning back into a liquid. Sanitiser goes from liquid to gas, not the reverse.

📌 **Key Learning Note:**
Liquids like alcohol, surgical spirit, and petrol are highly volatile; they **evaporate very quickly** when exposed to air.""",
    
    "kpsea-science-2022-q9": """The correct answer is **K**.

**Analysis of the Correct Answer:**
The gas that supports burning (combustion) is **Oxygen**. In the composition of air, Oxygen makes up approximately **21%** of the atmosphere by volume. In a standard pie chart representing air composition, the largest slice (78%) is Nitrogen, and the second-largest slice (21%) is Oxygen, which corresponds to part **K**.

**Why Other Options Are Incorrect:**
* **M:** This tiny slice represents Carbon dioxide (0.03%), which is used by plants for photosynthesis and actually extinguishes fire.
* **L:** This small slice represents rare/inert gases (0.97%) like argon, which do not support burning.
* **J:** This is the largest slice representing Nitrogen (78%), which is an unreactive gas that does not support burning.

📌 **Key Learning Note:**
- **Oxygen (21%):** Supports burning and breathing.
- **Nitrogen (78%):** Most abundant gas in the air.
- **Carbon Dioxide (0.03%):** Used to put out fires.""",
    
    "kpsea-science-2022-q10": """The correct answer is **the arm was fixed**.

**Analysis of the Correct Answer:**
A beam balance works on the principle of a seesaw; the central beam (arm) must be able to swing freely up and down around a central pivot point to compare the masses on either side. In the diagram, the wooden arm has been **nailed tightly** with two nails at the center, meaning it is fixed and cannot pivot or swing. This structural flaw caused the instrument to fail.

**Why Other Options Are Incorrect:**
* **a wooden arm was used:** Wood is a perfectly suitable material for making a simple beam balance arm; the material is not the issue.
* **wires were used instead of thread:** Wires are strong and can suspend the tins effectively. As long as they hold the tins, they won't prevent the balance from working.
* **similar tins were used.:** Using identical tins is actually the correct procedure for ensuring the balance is fair and equal on both sides.

📌 **Key Learning Note:**
For a locally made beam balance to function properly, the central pivot must be **free-swinging (not fixed)** so the beam can tip towards the heavier mass."""
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

print("Batch 1 completed!")
