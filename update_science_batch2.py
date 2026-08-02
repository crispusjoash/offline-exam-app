import re

new_explanations = {
    "kpsea-science-2022-q11": """The correct answer is **(i) and (iii)**.

**Analysis of the Correct Answer:**
Gravity is the force of attraction that pulls all objects downwards towards the centre of the Earth. It causes water to flow downhill in rivers (i) and makes ripe fruits fall downwards from trees (iii) to the ground.

**Why Other Options Are Incorrect:**
* **(ii) and (iii):** While (iii) involves gravity, (ii) swimming in a pool primarily involves buoyancy (upthrust pushing up) and muscular force to overcome water resistance, not gravity.
* **(i) and (iv):** While (i) involves gravity, (iv) writing on a chalkboard relies on the force of friction between the chalk and the rough board to leave a mark.
* **(ii) and (iv):** Neither swimming nor writing on a chalkboard are direct demonstrations of the downward pull of gravity.

📌 **Key Learning Note:**
The **Force of Gravity** always pulls objects downwards towards the centre of the Earth.""",
    
    "kpsea-science-2022-q12": """The correct answer is **Hot air carried leaves upwards**.

**Analysis of the Correct Answer:**
When air is heated by a fire, its particles gain energy, expand, and become lighter (less dense) than the surrounding cold air. This creates a convection current where the hot air rises. As the hot air moves forcefully upwards, it carries light objects like dry leaves and ash into the sky along with it.

**Why Other Options Are Incorrect:**
* **Leaves are light.:** While dry leaves are indeed light, they would simply fall to the ground due to gravity if there was no upward force carrying them.
* **Leaves expand.:** Leaves do not expand significantly when heated in a fire; they burn and shrivel up. The expansion happens to the air, not the leaves.
* **Wind carried leaves upwards.:** Wind generally blows horizontally across the land. The specific upward movement directly above a fire is caused by localized rising hot air, not general wind.

📌 **Key Learning Note:**
**Hot air is lighter than cold air.** When heated, air expands and rises, creating upward convection currents.""",
    
    "kpsea-science-2022-q13": """The correct answer is **Gloves and overcoats**.

**Analysis of the Correct Answer:**
When handling plants in a forest or farm, protective clothing is essential. **Gloves** protect the hands from being pricked by thorns, stung by nettles, or exposed to toxic plant sap. **Overcoats (or overalls)** cover the torso and arms, protecting the body and personal clothing from scratches, insect bites, and sticky saps.

**Why Other Options Are Incorrect:**
* **Gloves and goggles.:** While gloves are correct, goggles protect the eyes (useful for spraying chemicals or cutting wood), but an overcoat provides the necessary full-body protection from scratches when handling plants.
* **Tongs and overcoats.:** Tongs are tools for picking up dangerous objects (like hot coals or snakes) but are not practical or necessary for general plant handling.
* **Goggles and tongs.:** Neither of these provides the basic skin protection needed against thorns and scratches when handling plants.

📌 **Key Learning Note:**
Always wear **protective clothing** (like gloves, overcoats, and gumboots) when working in a forest or farm to prevent physical injuries and allergic reactions.""",
    
    "kpsea-science-2022-q14": """The correct answer is **Cholera**.

**Analysis of the Correct Answer:**
Cholera is an acute, highly contagious waterborne bacterial disease. Its classic, identifying symptoms include sudden onset of **severe watery diarrhoea** (often described as "rice-water stools") and **severe vomiting**. These lead to rapid fluid loss, resulting in extreme dehydration and intense thirst.

**Why Other Options Are Incorrect:**
* **Bilharzia.:** Bilharzia (Schistosomiasis) is caused by parasitic worms found in freshwater snails. Symptoms include blood in urine/stool and abdominal pain, not sudden severe watery diarrhoea.
* **Typhoid.:** Typhoid is a waterborne disease characterized by a prolonged high fever, headache, stomach pain, and sometimes a rash. While diarrhoea can occur, severe vomiting and rapid dehydration are hallmarks of cholera.
* **Dysentry.:** Dysentery is an intestinal infection that causes severe diarrhoea specifically containing **blood and mucus**, accompanied by painful stomach cramps, unlike the watery diarrhoea of cholera.

📌 **Key Learning Note:**
- **Cholera:** Severe watery diarrhoea and vomiting leading to rapid dehydration.
- **Dysentery:** Diarrhoea with blood and mucus.""",
    
    "kpsea-science-2022-q15": """The correct answer is **rainy weather**.

**Analysis of the Correct Answer:**
Nimbus clouds (such as nimbostratus or cumulonimbus) are typically low-level, very thick, and dark-grey or black in color. They are heavy with water droplets and block out sunlight. The appearance of dark nimbus clouds is a direct indication that heavy precipitation or **rainy weather** is imminent.

**Why Other Options Are Incorrect:**
* **windy weather:** Windy weather is often associated with the rapid movement of various cloud types, but dark nimbus clouds specifically signal rain, not just wind.
* **foggy weather:** Fog is essentially a stratus cloud that forms at ground level, reducing visibility, not dark nimbus clouds high in the sky.
* **sunny weather.:** Sunny and fair weather is indicated by high, wispy cirrus clouds or small, fluffy white cumulus clouds, not dark nimbus clouds.

📌 **Key Learning Note:**
**Nimbus clouds** are dark, heavy, and low-lying; they are the primary clouds that bring **rain**.""",
    
    "kpsea-science-2022-q16": """The correct answer is **Passion**.

**Analysis of the Correct Answer:**
Passion fruit is a climbing plant (a vine) that produces long, weak, non-woody stems. Because it cannot stand upright on its own, it relies on specialized structures called **tendrils** to coil around fences, trellises, or other trees for physical support as it grows toward the sunlight.

**Why Other Options Are Incorrect:**
* **Orange.:** An orange tree has a strong, thick, woody trunk that supports itself; it does not climb or use tendrils.
* **Mango.:** A mango tree is a large, sturdy woody plant with a thick trunk that stands upright on its own.
* **Apple.:** An apple tree also develops a strong, woody trunk and branches to support its own weight without climbing.

📌 **Key Learning Note:**
Climbing plants (like passion fruit, grapes, and pumpkins) have weak stems and use structures like **tendrils** or twining stems to cling to supports.""",
    
    "kpsea-science-2022-q17": """The correct answer is **Trapping the animals**.

**Analysis of the Correct Answer:**
To protect crops from destruction by wild animals and pests (like rodents, squirrels, or monkeys), physical barriers and control methods are used. **Trapping** is a direct method used by farmers to capture and remove problematic wild animals that invade the farm and eat or destroy the crops.

**Why Other Options Are Incorrect:**
* **Staking the plants.:** Staking is providing a wooden pole for weak-stemmed plants (like tomatoes) to climb; it does not stop wild animals from eating them.
* **Constructing a shade.:** A shade is built over a nursery bed to protect young delicate seedlings from the scorching sun and heavy rain drops, not from wild animals.
* **Applying a mulch.:** Mulching involves covering the soil with dry grass or leaves to conserve moisture and suppress weeds; it has no effect on large wild animals.

📌 **Key Learning Note:**
Farmers protect crops from wild animals by **trapping**, using **scarecrows**, building **fences/bomas**, and making loud noises.""",
    
    "kpsea-science-2022-q18": """The correct answer is **Training**.

**Analysis of the Correct Answer:**
**Training** is an agricultural practice used on climbing plants or vines (such as tomatoes, passion fruits, or climbing beans). It involves tying, directing, or guiding the growing plant onto a support structure (like a stake or trellis) to keep it upright, clean, and exposed to adequate sunlight.

**Why Other Options Are Incorrect:**
* **Hardening.:** Hardening off is the process of gradually exposing nursery seedlings to harsh outdoor conditions (sun and wind) before transplanting them to the main field.
* **Pruning.:** Pruning is the removal of extra, dead, or diseased branches and leaves from a plant to encourage better fruit yields.
* **Mulching.:** Mulching involves placing a layer of dry organic material on the soil surface to retain moisture and prevent weed growth.

📌 **Key Learning Note:**
- **Training:** Directing climbing plants to grow on a support structure.
- **Staking:** Providing a stick/pole for the plant to climb on.""",
    
    "kpsea-science-2022-q19": """The correct answer is **Water melon**.

**Analysis of the Correct Answer:**
A **watermelon** is a sweet, fleshy crop that is typically harvested, sliced, and eaten raw as a refreshing dessert or snack. Therefore, it is classified as a fresh fruit crop.

**Why Other Options Are Incorrect:**
* **Pumpkin.:** While botanically a fruit, pumpkins are treated culinarily as vegetables; they are hard and must be cooked (boiled or roasted) before eating.
* **Cucumber.:** Cucumbers are eaten raw, but they are generally considered culinary vegetables and are used in salads rather than consumed as a sweet dessert fruit.
* **Calabash.:** Calabashes (bottle gourds) are often cooked as vegetables when young, or dried and hollowed out when mature to be used as containers; they are not eaten as sweet fresh fruits.

📌 **Key Learning Note:**
Fruits like **watermelons**, **mangoes**, and **oranges** are sweet and eaten raw, whereas gourds like pumpkins are usually cooked as vegetables.""",
    
    "kpsea-science-2022-q20": """The correct answer is **Vitamins**.

**Analysis of the Correct Answer:**
Fruits like mangoes, oranges, and pineapples are primarily known for being incredibly rich natural sources of **vitamins** (especially Vitamin C and Vitamin A). Vitamins are protective nutrients required in small amounts by the body to boost the immune system and protect against diseases like scurvy and night blindness.

**Why Other Options Are Incorrect:**
* **Proteins.:** Proteins are body-building foods essential for growth and tissue repair, mostly found in meat, beans, milk, and eggs, not fruits.
* **Fibre.:** While fruits do contain dietary fiber (roughage) which aids digestion, their primary nutritional classification and value lies in their high vitamin content.
* **Carbohydrates.:** Carbohydrates are energy-giving foods found primarily in cereals, tubers (potatoes, cassava), and bread, not primarily in fleshy fruits.

📌 **Key Learning Note:**
- **Vitamins:** Protective foods (Fruits and Vegetables).
- **Proteins:** Body-building foods (Meat, Beans, Milk).
- **Carbohydrates:** Energy-giving foods (Maize, Bread, Potatoes)."""
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

print("Batch 2 completed!")
