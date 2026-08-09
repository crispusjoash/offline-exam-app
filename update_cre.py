import json
import re

file_path = 'src/data/kpsea-sst-cre-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'export const \w+ = (\{.*\});?\s*$', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

explanations = {
    41: """The correct answer is **D**.

**Analysis of the Correct Answer:**
According to the Biblical creation story in Genesis, the defining characteristic that separates humans from all other animals and plants is that they were uniquely created in the **image and likeness of God** (Imago Dei). This grants humans special dignity, intelligence, and a spiritual connection to the Creator.

**Why Other Options Are Incorrect:**
* **A:** While God created humans male and female, He also created animals as male and female to reproduce.
* **B & C:** Providing food and placing them in a specific location (Eden) were acts of God's provision, not the fundamental reason they are considered biologically and spiritually special.

📌 **Key Learning Note:**
Being created in the image of God is the foundation of Christian teaching on human dignity and the sacredness of human life.""",

    42: """The correct answer is **B**.

**Analysis of the Correct Answer:**
A **civil marriage** is a marriage that is performed, recorded, and recognized by a government official (such as a registrar of marriages). It takes place in a government office rather than a religious institution.

**Why Other Options Are Incorrect:**
* **A:** Customary marriage is conducted according to the traditional practices and customs of a specific community.
* **C:** Polygamous marriage involves having more than one wife, which can be customary or Islamic, but civil marriages in Kenya are strictly monogamous.
* **D:** Christian (or religious) marriages are officiated by a licensed clergy member (like a pastor or priest) in a church.

📌 **Key Learning Note:**
The three main types of legally recognized marriages in Kenya are Civil (by the government), Religious (Christian, Islamic, Hindu), and Customary (traditional).""",

    43: """The correct answer is **C**.

**Analysis of the Correct Answer:**
The primary mission of Bible translation societies is evangelism. Translating the Bible into local, indigenous languages ensures that people can clearly understand the Word of God, making it much easier to **spread the good news (the Gospel) to many people** across diverse linguistic groups.

**Why Other Options Are Incorrect:**
* **A:** While translation requires translators and creates some jobs, employment is not the core religious purpose.
* **B:** Promoting local languages is a positive cultural side-effect, but not the primary spiritual motivation.
* **D:** Selling books is a logistical distribution method, not the ultimate goal of the translation effort.

📌 **Key Learning Note:**
Bible translation breaks down language barriers, allowing individuals to engage with scripture intimately in their mother tongue.""",

    44: """The correct answer is **A**.

**Analysis of the Correct Answer:**
When faced with two women claiming the same baby, King Solomon prayed for and utilized divine **wisdom** to reveal the true mother (by threatening to cut the baby in half). Christians learn that difficult conflicts require discernment, fairness, and God-given wisdom to resolve justly.

**Why Other Options Are Incorrect:**
* **B:** Avoiding sharing a room is a trivial, literal takeaway that misses the spiritual and moral lesson of the narrative.
* **C & D:** While seeking counsel is good, the central theme of this specific biblical story is Solomon's legendary wisdom, not the act of escalating cases to leaders or relatives.

📌 **Key Learning Note:**
Wisdom is a gift from the Holy Spirit that enables believers to make just, fair, and righteous decisions in complex situations.""",

    45: """The correct answer is **D**.

**Analysis of the Correct Answer:**
According to the Gospels, immediately after Jesus was baptized by John the Baptist in the Jordan River, the heavens opened, the Holy Spirit descended on Him like a dove, and a **voice was heard from heaven** saying, "This is my Son, whom I love; with him I am well pleased."

**Why Other Options Are Incorrect:**
* **A:** An earthquake occurred during the crucifixion and resurrection of Jesus, not His baptism.
* **B:** Jesus' appearance was changed (transfigured) during the Transfiguration on the mountain, not at His baptism.
* **C:** The disciples had not yet been formally called and gathered at the time of His baptism.

📌 **Key Learning Note:**
The baptism of Jesus is a crucial event because it marks the beginning of His public ministry and visibly demonstrates the Holy Trinity (Father speaking, Son baptized, Spirit descending).""",

    46: """The correct answer is **C**.

**Analysis of the Correct Answer:**
The parables of the Lost Coin, the Lost Sheep, and the Lost Son (Prodigal Son) all share a common theme: something valuable was lost, a great effort was made to find it, and immense rejoicing occurred when it was recovered. Jesus told these parables to teach that God rejoices over one sinner who repents, encouraging believers to seek out and **bring sinners to God**.

**Why Other Options Are Incorrect:**
* **A & B:** These are practical life lessons (stewardship and diligence) but completely miss the spiritual metaphor of the parables.
* **D:** Telling others what God has done is testimony (evangelism), but the specific core focus of these three parables is God's grace, forgiveness, and the active pursuit of the "lost" (sinners).

📌 **Key Learning Note:**
In biblical parables, being "lost" represents spiritual separation from God through sin, and being "found" represents repentance and salvation.""",

    47: """The correct answer is **B**.

**Analysis of the Correct Answer:**
The woman with the issue of blood believed that if she could just touch the hem of Jesus' garment, she would be healed. When she did, Jesus told her, "Daughter, your faith has healed you." The central lesson is that believers must **always have unwavering faith in God's power** to overcome seemingly impossible situations.

**Why Other Options Are Incorrect:**
* **A:** Hiding sickness is a result of stigma (which the woman suffered from), not a positive lesson to emulate.
* **C:** Building hospitals is a good act of Christian charity, but it is not the direct spiritual lesson of this specific miracle.
* **D:** Touching pastors' clothes is superstitious; the healing came from her faith in Jesus (God), not the physical cloth itself.

📌 **Key Learning Note:**
Miracles in the New Testament are almost always directly linked to the active faith of the individual seeking help.""",

    48: """The correct answer is **C**.

**Analysis of the Correct Answer:**
Forgiving someone who has caused physical pain or injury requires a great deal of forbearance and the ability to endure wrongs without immediate retaliation. This endurance and willingness to forgive is a primary demonstration of **patience** (longsuffering), which is a fruit of the Holy Spirit.

**Why Other Options Are Incorrect:**
* **A:** Self-control involves restraining one's own impulses or anger. While related to not fighting back, the act of *forgiving* the injury leans heavily into patience and love.
* **B:** Faithfulness is loyalty and trustworthiness to God and others.
* **D:** Joy is a deep spiritual gladness regardless of circumstances.

📌 **Key Learning Note:**
The fruits of the Holy Spirit (Galatians 5:22-23) are love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, and self-control. Forbearance (patience) is essential for true forgiveness.""",

    49: """The correct answer is **C**.

**Analysis of the Correct Answer:**
Mob justice, which results in the killing of a suspect, directly violates the sixth commandment given to Moses: "You shall not **commit murder**." Taking a human life, regardless of the person's alleged crime, without lawful authority is considered murder in the eyes of God.

**Why Other Options Are Incorrect:**
* **A:** Accusing falsely (bearing false witness) is a sin, but the ultimate act committed by the crowd was the physical killing.
* **B:** The *thief* broke the commandment not to steal, but the *crowd* broke the commandment not to murder.
* **D:** Desiring someone's property (coveting) is an internal sin that leads to theft, unrelated to the crowd's violent action.

📌 **Key Learning Note:**
The Ten Commandments teach the absolute sanctity of human life. Vengeance and mob justice are condemned; justice belongs to God and lawful authorities.""",

    50: """The correct answer is **D**.

**Analysis of the Correct Answer:**
To search the internet for information, a learner requires a computing device with a web browser and internet connectivity. A **tablet** is a smart digital device capable of connecting to Wi-Fi and running search engines, making it the correct choice.

**Why Other Options Are Incorrect:**
* **A:** A camera captures photos and videos; it is not designed for web browsing.
* **B:** A radio receives audio broadcasts; it has no screen or internet capability.
* **C:** A projector displays images from a computer onto a wall; it cannot independently search the internet.

📌 **Key Learning Note:**
Modern Christian education often integrates digital technology (like tablets, smartphones, and computers) to access religious resources, digital Bibles, and historical information online."""
}

for q in data["sectionA"]:
    num = q["questionNumber"]
    if num in explanations:
        q["explanation"] = explanations[num]

new_content = "export const kpseaSstCre2024 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 1 completed successfully.")
