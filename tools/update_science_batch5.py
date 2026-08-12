import re

new_explanations = {
    "kpsea-science-2022-q41": """The correct answer is **6**.

**Analysis of the Correct Answer:**
In a standard competitive game of volleyball, each team is allowed to have exactly **6 players** on the court at any one time. The players rotate positions on the court in a clockwise direction after winning the serve.

**Why Other Options Are Incorrect:**
* **12:** 12 represents the total number of players in a full squad (6 starting players + 6 substitutes on the bench), but only 6 are on the court at once.
* **11:** 11 is the number of players on a field in soccer (football) or field hockey, not volleyball.
* **7:** 7 is the number of players on a court in a standard game of netball or handball.

📌 **Key Learning Note:**
- **Volleyball:** 6 players per team.
- **Netball:** 7 players per team.
- **Football/Soccer:** 11 players per team.""",
    
    "kpsea-science-2022-q42": """The correct answer is **Astride Vault to Forward roll.**

**Analysis of the Correct Answer:**
In gymnastics, a two-action sequence involves performing one skill immediately followed by another in a smooth, continuous motion. An **astride vault** involves jumping over a piece of apparatus (like a buck or box) with the legs spread wide apart. As the gymnast lands on the mat, their forward momentum naturally and safely allows them to tuck their head and perform a **forward roll** as the second action.

**Why Other Options Are Incorrect:**
* **Side vault to Backward roll.:** A side vault does not naturally provide the correct backward momentum or body position needed to smoothly transition into a backward roll upon landing.
* **Backward roll to fence vault.:** A backward roll ends on the floor, making it impossible to immediately transition into a fence vault (which requires a running start and an apparatus).
* **Cartwheel to Headstand.:** While possible for advanced gymnasts, a cartwheel ends in a standing lunge, making a sudden transition into a static headstand awkward and not a standard smooth continuous sequence for beginners.

📌 **Key Learning Note:**
A good gymnastic sequence connects movements smoothly using the body's natural momentum, such as transitioning from an **Astride Vault** directly into a **Forward Roll**.""",
    
    "kpsea-science-2022-q43": """The correct answer is **Sit and reach box.**

**Analysis of the Correct Answer:**
The **"sit and reach" box** is a standardized piece of physical fitness equipment specifically designed to measure the flexibility of the lower back and the hamstring muscles (back of the thighs). The individual sits with their legs flat against the box and reaches forward as far as possible along a measuring scale.

**Why Other Options Are Incorrect:**
* **Tape measure.:** While a tape measure is used to measure height or long jump distance, it is not a specialized box used to measure sitting flexibility.
* **Weighing scale.:** A weighing scale is used to measure a person's body mass (weight), which is a measure of body composition, not flexibility.
* **Measuring string.:** A string can measure distances (like the perimeter of a field), but it is not a standardized test equipment for measuring body flexibility.

📌 **Key Learning Note:**
The **Sit and Reach test** is the most common way to measure the **flexibility** of the lower back and hamstrings.""",
    
    "kpsea-science-2022-q44": """The correct answer is **Endurance.**

**Analysis of the Correct Answer:**
A marathon is a long-distance running event (usually 42.195 km). To successfully complete a marathon, an athlete requires excellent cardiovascular and muscular **endurance (stamina)**. Endurance is the ability of the heart, lungs, and muscles to sustain prolonged physical activity over a long period without getting overly tired.

**Why Other Options Are Incorrect:**
* **Power.:** Power is the ability to exert maximum force quickly (e.g., in weightlifting or shot put). Marathon running requires sustained effort, not short bursts of maximum power.
* **Speed.:** While speed is crucial for 100m sprints, a marathon runner paces themselves; endurance is far more important than raw sprinting speed for long distances.
* **Coordination.:** Coordination is the ability to use different parts of the body together smoothly (important in gymnastics or dribbling), but endurance is the primary limiting factor in a marathon.

📌 **Key Learning Note:**
- **Endurance:** Needed for long-distance running (Marathons).
- **Speed:** Needed for short-distance sprints (100m dash).
- **Power:** Needed for throwing events (Shot put, Javelin).""",
    
    "kpsea-science-2022-q45": """The correct answer is **To stay long before spoiling.**

**Analysis of the Correct Answer:**
Food preservation involves treating and handling food (such as drying, salting, canning, or smoking) to stop or severely slow down the growth of microorganisms (like bacteria and fungi) that cause rotting. The primary purpose of doing this is to extend the shelf life of the food so it can **stay a long time before spoiling** and be consumed during dry seasons.

**Why Other Options Are Incorrect:**
* **To add taste before eating.:** While some methods like smoking or salting do add flavor, the primary scientific goal of preservation is to stop rotting, not just to season the food.
* **To keep warm and dry.:** Drying removes moisture, but preservation methods like freezing make food extremely cold, not warm. The goal is longevity, not temperature control.
* **For ease of carrying.:** Drying makes food lighter and easier to transport, but this is a secondary benefit. The main goal is always to prevent spoilage.

📌 **Key Learning Note:**
The main purpose of **food preservation** is to prevent the growth of bacteria and fungi, allowing food to be stored for a long time without spoiling.""",
    
    "kpsea-science-2022-q46": """The correct answer is **Airways Breathing and Circulation.**

**Analysis of the Correct Answer:**
In first aid, the primary survey is a quick way to assess a casualty for life-threatening conditions. It follows the acronym **ABC**:
- **A (Airways):** Check if the throat/windpipe is clear of obstructions so air can pass.
- **B (Breathing):** Look, listen, and feel to check if the casualty is actually breathing in and out.
- **C (Circulation):** Check for a pulse or severe bleeding to ensure blood is circulating in the body.

**Why Other Options Are Incorrect:**
* **Awake Breathing and Circulation.:** 'A' does not stand for Awake; a casualty can be unconscious but still have a clear airway.
* **Assess Breathing and Circulation.:** While you do assess them, 'A' stands specifically for Airways.
* **Airways Bleeding and Circulation.:** 'B' stands for Breathing. Bleeding is handled under 'C' (Circulation).

📌 **Key Learning Note:**
The most critical First Aid check for an unconscious casualty is the **ABC** rule: **Airway**, **Breathing**, and **Circulation**.""",
    
    "kpsea-science-2022-q47": """The correct answer is **Pull the sting out immediately.**

**Analysis of the Correct Answer:**
When a honeybee stings, it dies and leaves its barbed stinger attached to a venom sac embedded in the victim's skin. The sac continues to pump venom into the body for several minutes. The most critical and immediate first aid step is to **pull or scrape the sting out immediately** to stop more venom from entering the body, which reduces pain and swelling.

**Why Other Options Are Incorrect:**
* **Immediately go home and sleep.:** Sleeping does not stop the venom from being pumped in. The sting must be removed first.
* **Place hot water in the stung area.:** Hot water will increase blood circulation in the area, causing the venom to spread faster and increasing the pain and swelling. A cold compress (ice) should be used instead.
* **Kill the bees and continue.:** The bee that stung is already dying. Attacking other bees might provoke a swarm attack, making the situation much worse.

📌 **Key Learning Note:**
In the event of a bee sting, immediately **scrape or pull out the stinger** to stop the venom, then apply a cold compress to reduce swelling.""",
    
    "kpsea-science-2022-q48": """The correct answer is **D**.

**Analysis of the Correct Answer:**
Image **D** illustrates a player executing an **overarm serve** in volleyball. In this technique, the player tosses the ball high into the air and strikes it powerfully with an open hand using an overarm swinging motion (above the shoulder) to send it over the net. 

**Why Other Options Are Incorrect:**
* **A:** Image A shows a player diving or rolling on the floor to save a low ball, not serving.
* **B:** Image B shows a player executing a **dig** or underarm pass, used to receive a serve or spike.
* **C:** Image C shows a player performing a **volley** (or set) using the fingertips above the head to pass the ball to a spiker.

📌 **Key Learning Note:**
- **Overarm Serve:** Hitting the ball forcefully over the net from above the shoulder.
- **Volley:** Passing the ball using fingertips above the head.
- **Dig:** Receiving a low ball using the forearms.""",
    
    "kpsea-science-2022-q49": """The correct answer is **Soccer  Goal**.

**Analysis of the Correct Answer:**
Different sports have different terminology for scoring. In **Soccer (Football)**, when the ball successfully crosses the goal line between the goalposts, it is correctly referred to as scoring a **"Goal"**.

**Why Other Options Are Incorrect:**
* **Tag rugby  Shot:** In Tag Rugby (and standard rugby), scoring by placing the ball down in the opponent's goal area is called a **"Try"**, not a shot.
* **Volleyball  Try:** In Volleyball, scoring is referred to as winning a **"Point"**, and games are won by winning "Sets," not tries.
* **Handball  Gun:** In Handball, scoring is called a **"Goal"**. "Gun" is not a scoring term in any of these sports; it is an unrelated word.

📌 **Key Learning Note:**
- **Soccer & Handball:** Score is a **Goal**.
- **Rugby:** Score is a **Try**.
- **Volleyball & Tennis:** Score is a **Point**.""",
    
    "kpsea-science-2022-q50": """The correct answer is **Team mate was far.**

**Analysis of the Correct Answer:**
The **shoulder pass** in netball is a powerful, one-handed pass executed from shoulder height. It is specifically used to throw the ball very quickly over **long distances** down the court to a teammate who is **far** away. 

**Why Other Options Are Incorrect:**
* **Team mate was close.:** If a teammate is close, a short, quick **chest pass** or a gentle **bounce pass** is much safer and more accurate than a powerful shoulder pass.
* **Team mate was running.:** A teammate can be running close by or far away. The defining reason for choosing a shoulder pass over a chest pass is the distance, not just the movement.
* **Team mate was marked.:** If a teammate is heavily marked by a defender, a high **lob pass** over the defender's head is often used, rather than a direct, flat shoulder pass which might be intercepted.

📌 **Key Learning Note:**
- **Shoulder Pass:** Used for passing the ball over **long distances**.
- **Chest Pass:** Used for quick, accurate passes over **short distances**."""
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

print("Batch 5 completed!")
