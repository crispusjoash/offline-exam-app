import json
import re

file_path = 'src/data/kpsea-science-2025.js'

explanations = {
    "q11": """The correct answer is **Convection.**

**Analysis of the Correct Answer:**
Heat transfer in liquids (like boiling water) and gases (like air) occurs through a process called convection. As the fluid is heated, it expands, becomes less dense, and rises, while cooler, denser fluid sinks to replace it, creating convection currents.

**Why Other Options Are Incorrect:**
* **Conduction:** This is the transfer of heat through solids (like a metal spoon), not liquids.
* **Evaporation:** This is the process of a liquid turning into a gas, not a method of heat transfer.
* **Radiation:** This is the transfer of heat through a vacuum or empty space (like heat from the sun), without needing a medium.

📌 **Key Learning Note:**
Heat travels through solids by conduction, through liquids and gases by convection, and through empty space by radiation.""",

    "q12": """The correct answer is **solid**

**Analysis of the Correct Answer:**
In a string telephone, sound travels as vibrations along the tight string connecting the two cans. A string is a solid material. Sound travels fastest and most efficiently through solids because the particles are tightly packed together.

**Why Other Options Are Incorrect:**
* **gas:** While sound can travel through gases (like air), in this specific setup, it travels primarily through the solid string.
* **liquid:** The string is not a liquid.
* **vacuum:** Sound cannot travel through a vacuum at all because there are no particles to vibrate and transmit the sound waves.

📌 **Key Learning Note:**
Sound requires a material medium (solid, liquid, or gas) to travel. It travels fastest in solids and slowest in gases.""",

    "q13": """The correct answer is **It is upright.**

**Analysis of the Correct Answer:**
When you look at yourself in a plane mirror, the image formed has several specific characteristics: it is upright (erect), it is virtual (cannot be formed on a screen), it is the same size as the object, and it is laterally inverted (left appears as right). 

**Why Other Options Are Incorrect:**
* **It is real:** A real image can be projected onto a screen. A mirror image is virtual.
* **It is formed on a screen:** As mentioned above, plane mirrors form virtual images which cannot be caught on a screen.
* **It is upside down:** Images in a plane mirror are always upright, not inverted vertically.

📌 **Key Learning Note:**
Images formed by a plane mirror are always **upright**, **virtual**, **same size**, and **laterally inverted**.""",

    "q14": """The correct answer is **Radiation.**

**Analysis of the Correct Answer:**
The heat from the sun reaches the earth by traveling through the vacuum of space. The only method of heat transfer that does not require a material medium (solid, liquid, or gas) is radiation. Heat travels as electromagnetic waves.

**Why Other Options Are Incorrect:**
* **Convection:** Requires a fluid medium (liquid or gas) to transfer heat.
* **Conduction:** Requires a solid medium for particles to pass vibrations.
* **Evaporation:** Is a change of state, not a method of heat transfer.

📌 **Key Learning Note:**
Radiation is the only way heat can travel through an empty space (a vacuum), which is how solar energy reaches Earth.""",

    "q15": """The correct answer is **Ambulance siren.**

**Analysis of the Correct Answer:**
An ambulance siren is designed to produce a very loud sound so that it can be heard from a long distance, warning other drivers to clear the road. 

**Why Other Options Are Incorrect:**
* **Baby crying:** While a baby's cry can be loud, it is not as loud or far-reaching as an electronic siren.
* **Leaves rustling:** This produces a very soft, quiet sound.
* **Ringing bell:** A handbell is loud but still significantly quieter than an emergency vehicle's siren.

📌 **Key Learning Note:**
Loud sounds carry more energy and travel further. Sirens are used as warning signals precisely because of their high volume and pitch.""",

    "q16": """The correct answer is **The sun.**

**Analysis of the Correct Answer:**
A source of light is an object that generates its own light. The sun is a natural luminous body that produces its own light through nuclear reactions. 

**Why Other Options Are Incorrect:**
* **A mirror:** A mirror does not produce light; it only reflects light from other sources.
* **The moon:** The moon is a non-luminous body. It only appears bright because it reflects the light from the sun.
* **A glass:** Glass is transparent and transmits light, but it does not generate light.

📌 **Key Learning Note:**
Objects that produce their own light are called **luminous** objects (e.g., the sun, stars, a lit candle). Objects that do not produce light but reflect it are **non-luminous** (e.g., the moon, mirrors).""",

    "q17": """The correct answer is **Turn on and off the light.**

**Analysis of the Correct Answer:**
In a simple electric circuit, a switch is used to control the flow of electricity. By closing the switch, the circuit is completed (turning the light on). By opening it, the circuit is broken (turning the light off).

**Why Other Options Are Incorrect:**
* **Produce electricity:** This is the function of the battery or dry cell.
* **Produce light:** This is the function of the bulb.
* **Connect the bulb:** This is the function of the connecting wires.

📌 **Key Learning Note:**
A switch acts as a bridge in a circuit. When closed, electricity flows. When open, the path is broken and electricity stops.""",

    "q18": """The correct answer is **Aluminium wire.**

**Analysis of the Correct Answer:**
To make a bulb light, the material completing the circuit must be a good conductor of electricity. Metals are excellent conductors. Aluminium is a metal and will allow electric current to pass through it, completing the circuit.

**Why Other Options Are Incorrect:**
* **Dry wood:** Wood is an insulator (non-conductor).
* **Piece of glass:** Glass is an insulator.
* **Plastic ruler:** Plastic is an insulator.

📌 **Key Learning Note:**
Materials that allow electricity to flow through them are called **conductors** (mostly metals). Those that do not are called **insulators** (rubber, wood, glass, plastic).""",

    "q19": """The correct answer is **translucent**

**Analysis of the Correct Answer:**
A clean glass window is transparent, meaning light passes through it clearly and you can see through it. When smeared with petroleum jelly, it scatters the light. It allows some light to pass through, but you can no longer see through it clearly. Such materials are called translucent.

**Why Other Options Are Incorrect:**
* **transparent:** This would mean you can still see through it clearly, which is no longer true after applying jelly.
* **opaque:** This means no light passes through at all (like a brick wall). Light still passes through the jelly.
* **colourless:** The jelly might be colourless, but this doesn't describe the light-transmitting property.

📌 **Key Learning Note:**
* **Transparent:** Light passes clearly (clear glass).
* **Translucent:** Light passes but is scattered (frosted glass, oiled paper).
* **Opaque:** No light passes (wood, metal).""",

    "q20": """The correct answer is **smooth**

**Analysis of the Correct Answer:**
Shoe soles have treads (patterns) to increase friction between the shoe and the ground, preventing slipping. When a sole is worn out, it becomes smooth. A smooth surface reduces friction, making it very slippery and difficult to walk.

**Why Other Options Are Incorrect:**
* **heavy / hard:** The weight or hardness of the shoe does not primarily cause it to be slippery; it is the lack of grip (friction).
* **curved:** Curvature is not the main reason for slipping.

📌 **Key Learning Note:**
Friction is a force that opposes motion. Rough surfaces (like shoe treads or tyre threads) increase friction, while smooth surfaces reduce friction and cause slipping.""",

    "q21": """The correct answer is **K: Vena cava, L: Pulmonary vein, M: Left auricle, N: Aorta**

**Analysis of the Correct Answer:**
In the human circulatory system:
* **K (Vena cava):** The main vein that carries deoxygenated blood from the body back to the right auricle of the heart.
* **L (Pulmonary vein):** Carries oxygenated blood from the lungs to the left auricle of the heart.
* **M (Left auricle):** The upper left chamber that receives oxygenated blood.
* **N (Aorta):** The main artery that pumps oxygenated blood from the left ventricle to the rest of the body.

**Why Other Options Are Incorrect:**
The other options mix up the blood vessels. For instance, the Pulmonary artery carries blood away from the heart to the lungs, not from the lungs to the heart. The Vena cava carries blood from the body, not to the body.

📌 **Key Learning Note:**
Arteries carry blood away from the heart (Aorta, Pulmonary artery), while veins carry blood towards the heart (Vena cava, Pulmonary vein).""",

    "q22": """The correct answer is **N**

**Analysis of the Correct Answer:**
A lever is a simple machine consisting of a rigid bar that turns on a fixed point called a pivot or fulcrum. In this diagram of a hammer pulling a nail, point N is where the hammer rests and turns against the wood. Therefore, N is the pivot.

**Why Other Options Are Incorrect:**
* **M (Effort):** This is where the hand applies force to the hammer.
* **P (Load):** This is the nail being pulled out, which is the resistance or load.
* **Q (Wood):** This is just the surface, not a part of the lever system itself.

📌 **Key Learning Note:**
In any lever, there are three main parts: the **Pivot/Fulcrum** (turning point), the **Effort** (force applied), and the **Load** (object being moved).""",

    "q23": """The correct answer is **wood is a poor conductor of heat.**

**Analysis of the Correct Answer:**
Wood is a non-metal and acts as a thermal insulator. This means it does not allow heat to flow through it easily. Therefore, the heat from the candle flame does not travel along the wooden rod to the learner's hand.

**Why Other Options Are Incorrect:**
* **candle is a poor conductor:** The candle is the source of heat, its conductivity is irrelevant here.
* **heat was transferred upwards:** While heat does rise via convection in the air, conduction along the rod is what would burn the hand.
* **heat from the candle was not enough:** Even a small candle flame is hot enough to burn if conducted through a metal rod.

📌 **Key Learning Note:**
Materials that do not conduct heat well are called **insulators**. Handles of cooking utensils are made of insulators like wood or plastic to prevent burns.""",

    "q24": """The correct answer is **Wearing gloves.**

**Analysis of the Correct Answer:**
Cooking involves handling hot utensils and being near open flames or heat sources. The most appropriate safety measure to prevent burns from hot pots or pans is to wear protective oven gloves or use a thick cloth.

**Why Other Options Are Incorrect:**
* **Using one hand:** This is dangerous and can lead to dropping hot food or losing balance.
* **Using a bigger pan:** While a bigger pan might contain splashes better, it doesn't protect your hands from touching hot handles.
* **Putting hands in cold water:** This is a first-aid step *after* getting burned, not a preventative safety measure.

📌 **Key Learning Note:**
Always use protective gear like oven gloves, mitts, or dry cloths when handling hot kitchenware to prevent contact burns.""",

    "q25": """The correct answer is **(i) and (iv)**

**Analysis of the Correct Answer:**
Fish are a unique class of vertebrates adapted to aquatic life. Their defining characteristics include having **fins** (i) for swimming and breathing using **gills** (iv) to extract oxygen from water. 

**Why Other Options Are Incorrect:**
* **(ii) body covered with scales:** Reptiles (like snakes and lizards) also have scales, so this is not *only* found in fish.
* **(iii) body temperature varies:** Amphibians and reptiles are also cold-blooded (poikilothermic), meaning their temperature varies with the surroundings.

📌 **Key Learning Note:**
While several vertebrates are cold-blooded or have scales, only fish possess both **fins** for locomotion and **gills** for breathing as adults.""",

    "q26": """The correct answer is **conserve water**

**Analysis of the Correct Answer:**
A sunken seedbed is constructed by digging below the normal soil surface level. This creates a basin-like structure. Its main purpose is to collect and retain rainwater or irrigation water, preventing it from running off. This is highly effective in dry areas for conserving moisture.

**Why Other Options Are Incorrect:**
* **control soil erosion:** Terraces and gabions control erosion; sunken beds are primarily for moisture retention.
* **protect the crop from pests:** Fencing or netting is used to protect against pests.
* **control weeds:** Weeding, mulching, or herbicides are used to control weeds.

📌 **Key Learning Note:**
Sunken beds are used in arid and semi-arid regions to harvest and **conserve water**, whereas raised beds are used in wet areas to improve drainage.""",

    "q27": """The correct answer is **Small V-shaped trenches.**

**Analysis of the Correct Answer:**
Rill erosion is a form of water erosion where surface runoff concentrates into small, distinct channels or streamlets. These appear as small V-shaped trenches carved into the soil surface.

**Why Other Options Are Incorrect:**
* **Deep U-shaped trenches:** This describes gulley erosion, which is a more severe and advanced stage of erosion.
* **Small holes left by detached soil:** This describes splash erosion, caused by the impact of raindrops.
* **Stones left after removal of soil:** This describes sheet erosion, where uniform layers of topsoil are washed away.

📌 **Key Learning Note:**
The stages of water erosion are: **Splash erosion** (raindrops), **Sheet erosion** (uniform removal), **Rill erosion** (small V-channels), and **Gulley erosion** (deep U-trenches).""",

    "q28": """The correct answer is **moving water**

**Analysis of the Correct Answer:**
Rill erosion occurs when water flows over the soil surface and gathers into small rivulets. The force of this moving water cuts small channels (rills) into the soil.

**Why Other Options Are Incorrect:**
* **strong wind:** Wind erosion blows away topsoil but does not cut distinct V-shaped trenches.
* **moving animals:** Animal movement causes soil compaction and can trigger erosion, but it does not directly carve rills.
* **road construction:** This is a human activity that can lead to erosion, but the direct agent carving the rills is water.

📌 **Key Learning Note:**
The primary agents of soil erosion are **water** (causes splash, sheet, rill, and gulley erosion) and **wind**.""",

    "q29": """The correct answer is **keep off wild animals**

**Analysis of the Correct Answer:**
Blinking lights, often known as 'lion lights', are an innovative agricultural solution used by farmers and pastoralists. The flashing pattern mimics human movement with flashlights, which scares away nocturnal predators like lions, leopards, and hyenas from attacking livestock.

**Why Other Options Are Incorrect:**
* **attract cattle to the shed:** Cattle do not need blinking lights to find their shed; they are guided by routine or farmers.
* **guide the milkman:** A steady, bright light would be used for illumination, not blinking lights.
* **make the cattle sleep:** Blinking lights would likely keep animals awake or alert rather than inducing sleep.

📌 **Key Learning Note:**
Farmers use innovations like **blinking lights** and **innovative sound devices** to safely deter wild animals without harming them.""",

    "q30": """The correct answer is **Innovative sound.**

**Analysis of the Correct Answer:**
To keep wild animals away from livestock, farmers use deterrents that target the animals' senses. Just as blinking lights target their vision to scare them, innovative sound devices (like alarms, bells, or recorded noises) target their hearing to frighten them away.

**Why Other Options Are Incorrect:**
* **Hole trap:** This is a physical trap used to catch animals, not a deterrent device.
* **Insect catcher:** Used for small pests like flies or mosquitoes, not large wild animals.
* **Rat trap:** Used for rodents, not large predators.

📌 **Key Learning Note:**
Non-lethal deterrents for wildlife include visual deterrents (scarecrows, blinking lights) and auditory deterrents (innovative sounds, sirens)."""
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(export const kpseaScience2025 = )(\{.*\});?\s*$', content, re.DOTALL)
prefix = match.group(1)
data = json.loads(match.group(2))

section_key = "sectionA" if "sectionA" in data else "questions"
for q in data.get(section_key, []):
    q_id = q.get("id")
    if q_id in explanations:
        q["explanation"] = explanations[q_id]

new_content = prefix + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated 11-30")
