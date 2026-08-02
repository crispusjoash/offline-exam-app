import json

filepath = 'src/data/kpsea-sst-cre-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const kpseaSstCre2023 = '
clean_text = text.replace(prefix, '').strip()
if clean_text.endswith(';'):
    clean_text = clean_text[:-1]

data = json.loads(clean_text)

cre_explanations = {
    36: """The correct answer is **conserve the school environment**.

**Detailed Analysis of the Correct Answer:**
In Christian Religious Education, taking care of the environment is a direct responsibility given to human beings by God in **Genesis 2:15** (stewardship of creation). Planting trees is a practical and vital way to protect soil from erosion, provide shade, keep the air clean, and **conserve the school environment**.

**Why Other Options Are Incorrect:**
* **avoid living in a dusty compound:** Reducing dust is a minor physical benefit, not the main biblical reason for environmental stewardship.
* **ensure learners are busy:** Tree planting is a purposeful act of environmental care, not a chore just to keep students occupied.
* **utilize the water in the school.:** Trees require water to grow, but utilizing excess water is not the primary purpose of tree planting.

📌 **Key Learning Note:**
Planting trees fulfills God's biblical command of **creation stewardship** by conserving and caring for the environment.""",

    37: """The correct answer is **Doing physical exercises.**.

**Detailed Analysis of the Correct Answer:**
Christianity teaches that leisure time should be spent engaging in wholesome, constructive, and health-building activities. **Doing physical exercises** keeps the body strong, promotes discipline, and respects our bodies as temples of the Holy Spirit (**1 Corinthians 6:19**).

**Why Other Options Are Incorrect:**
* **Sitting by the roadside.:** Sitting idle along roads wastes time and increases exposure to negative peer pressure and dangerous habits.
* **Attending disco parties.:** Exposes young learners to noisy, unsafe environments and morally harmful behaviors.
* **Participating in betting games.:** Gambling and betting promote greed, financial dishonesty, and addiction, which contradict Christian values.

📌 **Key Learning Note:**
Christian leisure time should be spent constructively in health-building activities such as sports, exercise, and helping others.""",

    38: """The correct answer is **sharing duties among themselves**.

**Detailed Analysis of the Correct Answer:**
A Christian family thrives on love, cooperation, and mutual support. **Sharing duties among themselves** ensures that household work is divided fairly, preventing any single member from becoming overworked and promoting unity, peace, and teamwork in the home.

**Why Other Options Are Incorrect:**
* **reporting those who do not work:** Complaining and tattling creates hostility, resentment, and arguments rather than encouraging peaceful cooperation.
* **inviting their friends to help them to do the work:** Expecting outside friends to do family household chores avoids personal family responsibility.
* **giving gifts to those who work hard.:** Using gifts creates bribery or favoritism, whereas family duties should be shared out of mutual love.

📌 **Key Learning Note:**
**Sharing household chores** promotes family unity, teamwork, and Christian love.""",

    39: """The correct answer is **Kindness.**.

**Detailed Analysis of the Correct Answer:**
In **Exodus 2:1-10**, when Pharaoh had ordered all newborn Hebrew boys to be killed, Pharaoh's daughter found baby Moses crying in a basket along the river. She demonstrated **kindness** and compassion by feeling deep sympathy for the baby and choosing to save his life and raise him.

**Why Other Options Are Incorrect:**
* **Holiness.:** Refers to moral purity and devotion to God, which is not the specific emotion shown when saving the infant.
* **Peace.:** Refers to harmony; her specific action was driven by tender compassion and mercy.
* **Loyalty.:** Means faithfulness to a ruler; in fact, she defied her father Pharaoh's cruel decree to show kindness to the helpless baby.

📌 **Key Learning Note:**
Rescuing baby Moses was a great act of **kindness and mercy** that preserved the future leader of Israel.""",

    40: """The correct answer is **A**.

**Detailed Analysis of the Correct Answer:**
The Bible contains 66 books divided into two testaments: the Old Testament (39 books) and the New Testament (27 books). **Box A** is correct because it lists books exclusively from the **New Testament** (such as Matthew, Mark, Luke, John, Acts, Romans, Corinthians, Galatians, and Revelation).

**Why Other Options Are Incorrect:**
* **B:** Contains a mixture of Old Testament books (like Genesis or Exodus) alongside New Testament books.
* **C:** Contains Old Testament books of poetry and wisdom (such as Psalms and Proverbs).
* **D:** Contains Old Testament prophetic books (such as Isaiah, Jeremiah, or Daniel).

📌 **Key Learning Note:**
The **New Testament** consists of **27 books**, beginning with the Gospel of Matthew and ending with Revelation.""",

    41: """The correct answer is **Do not desire another man's property.**.

**Detailed Analysis of the Correct Answer:**
The Tenth Commandment (**Exodus 20:17**) states: *"You shall not covet your neighbor's house, wife, or anything that belongs to your neighbor."* This commandment specifically teaches Christians to **be content with what they have** and avoid secret envy or greed for other people's possessions.

**Why Other Options Are Incorrect:**
* **Do not worship any other God.:** The First Commandment, which teaches monotheism and single devotion to God.
* **Do not commit adultery.:** The Seventh Commandment, which protects the sanctity of marriage.
* **Do not accuse anyone falsely.:** The Ninth Commandment, which forbids lying and bearing false witness.

📌 **Key Learning Note:**
The **Tenth Commandment** warns against envy and covetousness, teaching us to be content with our own blessings.""",

    42: """The correct answer is **She had faith that she would be healed.**.

**Detailed Analysis of the Correct Answer:**
In **Luke 8:43-48**, the woman who had suffered from a bleeding disorder for 12 years touched the hem of Jesus' cloak because **she had strong faith that she would be healed**. Jesus confirmed this by telling her, *"Daughter, your faith has healed you; go in peace."*

**Why Other Options Are Incorrect:**
* **She loved the garment of Jesus.:** It was not admiration for clothing, but her faith in Jesus' divine healing power that healed her.
* **She touched it by mistake.:** Her action was intentional, reaching out specifically to touch the fringe of His cloak.
* **She was told by the disciple to do so.:** No disciple directed her; she acted independently on her personal faith.

📌 **Key Learning Note:**
Strong **faith in God's power** brings spiritual and physical healing, as shown by the woman who touched Jesus' cloak.""",

    43: """The correct answer is **be persistent in prayer**.

**Detailed Analysis of the Correct Answer:**
In **Luke 11:5-8**, Jesus taught the Parable of the Friend at Midnight, where a man repeatedly knocks on his neighbor's door at night for bread until the neighbor gets up and gives it to him. The main lesson of this parable is that Christians should **be persistent and unceasing in prayer**.

**Why Other Options Are Incorrect:**
* **provide help to our friends:** While helping friends is good, the main spiritual lesson of this specific parable is persistent prayer.
* **welcome visitors in our homes:** Hospitality is important, but Jesus used this illustration to teach unceasing prayer.
* **lock our doors at night.:** Practical home security is part of the story's setting, not its spiritual lesson.

📌 **Key Learning Note:**
The Parable of the Friend at Midnight teaches Christians to **pray persistently** without giving up.""",

    44: """The correct answer is **healing the Ten Lepers**.

**Detailed Analysis of the Correct Answer:**
In **Luke 17:11-19**, Jesus healed ten men suffering from leprosy. However, only one of them (a Samaritan) returned to fall at Jesus' feet and thank Him. Jesus praised him, making this miracle a lesson that **encourages Christians to always be thankful to God** for His blessings and healing.

**Why Other Options Are Incorrect:**
* **healing the Roman Officer's servant:** Highlights the great faith of the Gentile centurion (Luke 7:1-10).
* **turning water into wine:** Jesus' first miracle at Cana demonstrating His glory (John 2:1-11).
* **calming the storm.:** Demonstrates Jesus' divine power over physical nature and elements (Mark 4:35-41).

📌 **Key Learning Note:**
The miracle of **healing the ten lepers** teaches Christians to express gratitude and thanksgiving to God for His blessings.""",

    45: """The correct answer is **buying food for poor people**.

**Detailed Analysis of the Correct Answer:**
In the story of the Rich Man and Lazarus (**Luke 16:19-31**), the rich man was condemned because he lived in luxury while completely ignoring the starving poor beggar Lazarus at his gate. This story teaches Christians to **use their money unselfishly to care for the poor and needy**.

**Why Other Options Are Incorrect:**
* **organising parties for friends:** Focuses on selfish pleasure rather than helping those in poverty.
* **buying clothes for themselves:** Reflects self-centered spending without concern for the less fortunate.
* **travelling to different places.:** Personal leisure travel does not fulfill the duty of caring for the poor.

📌 **Key Learning Note:**
Christians should use their wealth and resources to **help the poor, hungry, and needy**.""",

    46: """The correct answer is **Do this in memory of me.**.

**Detailed Analysis of the Correct Answer:**
During the Last Supper (**Luke 22:19**), Jesus broke bread, gave it to His disciples, and said, *"This is my body given for you; **do this in memory of me**."* This established the sacrament of Holy Communion (Eucharist) for believers.

**Why Other Options Are Incorrect:**
* **Go and heal the sick.:** Given when commissioning the twelve disciples for missionary work (Matthew 10:8).
* **Do not take a purse for yourself.:** Instruction for traveling light during evangelism (Luke 10:4).
* **Bless those who curse you.:** Teaching from the Sermon on the Mount regarding loving enemies (Luke 6:28).

📌 **Key Learning Note:**
Jesus instituted Holy Communion with the command: **"Do this in memory of me."**""",

    47: """The correct answer is **Honesty.**.

**Detailed Analysis of the Correct Answer:**
In **Acts 5:1-11**, Ananias and Sapphira sold land and secretly kept back part of the money while lying to Peter and the Holy Spirit that they were donating the full amount. Their immediate judgment teaches Christians the vital importance of **honesty and integrity**.

**Why Other Options Are Incorrect:**
* **Tolerance.:** Refers to accepting others; their sin was deceit and lying, not intolerance.
* **Mercy.:** Refers to forgiveness; the narrative highlights God's judgment against deceit.
* **Perseverance.:** Refers to enduring hardship; the core lesson is about truthfulness.

📌 **Key Learning Note:**
The story of Ananias and Sapphira teaches Christians to practice **absolute honesty and truthfulness**.""",

    48: """The correct answer is **Refuse and continue walking to school.**.

**Detailed Analysis of the Correct Answer:**
Child personal safety rules dictate that learners should **never accept rides or gifts from strangers**. If a stranger offers a lift, the safest action is to **refuse politely but firmly and continue walking to school** along well-traveled, public routes.

**Why Other Options Are Incorrect:**
* **Accept the lift and get into the car.:** Extremely dangerous; getting into a stranger's vehicle exposes children to abduction or severe harm.
* **Refuse and go back home.:** Walking back alone leaves the child unsupervised and causes them to miss school needlessly.
* **Hide in the bush until the vehicle goes away.:** Hiding in bushes isolates the child and exposes them to environmental hazards like snakes or criminals.

📌 **Key Learning Note:**
Always **refuse lifts from strangers** and proceed safely to school along public routes.""",

    49: """The correct answer is **To promote respect for authority.**.

**Detailed Analysis of the Correct Answer:**
School prefects are student leaders appointed to assist in maintaining order and discipline. Cooperating with prefects teaches students **to promote respect for authority** and divine leadership principles (**Romans 13:1**).

**Why Other Options Are Incorrect:**
* **To avoid being punished.:** True obedience should stem from respect and moral duty, not just fear of punishment.
* **To obtain good things from the prefect.:** Cooperating to gain personal favors or bribes is corrupt.
* **To be recognized by the teachers.:** Doing right simply for teacher praise lacks genuine moral integrity.

📌 **Key Learning Note:**
Cooperating with school prefects promotes **respect for authority** and maintains school harmony.""",

    50: """The correct answer is **Exchanging messages in their learning areas.**.

**Detailed Analysis of the Correct Answer:**
Social media and digital devices should be used responsibly by learners. **Exchanging messages in their learning areas** (such as sharing revision notes, homework help, and academic discussions) is a safe, productive, and beneficial use of technology.

**Why Other Options Are Incorrect:**
* **Chatting with friends all the time.:** Continuous non-stop chatting leads to digital addiction and wastes study time.
* **Taking and posting their pictures.:** Posting personal photos publicly poses serious privacy and online safety risks for minors.
* **Watching all kinds of videos.:** Unrestricted video viewing exposes children to inappropriate or harmful content.

📌 **Key Learning Note:**
Learners should use social media **productively for educational purposes and learning group revision**."""
}

for q in data['sectionA']:
    qn = q['questionNumber']
    if qn in cre_explanations:
        q['explanation'] = cre_explanations[qn]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')

print("All 15 CRE questions updated successfully in kpsea-sst-cre-2023.js!")
