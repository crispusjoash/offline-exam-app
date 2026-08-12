import json

explanations_map = {
    36: """📘 **Study Note & Concept Overview:**
In Christian Religious Education, taking care of the environment is a direct assignment from God given to human beings in Genesis 2:15 (stewardship of creation). Planting trees is a key practical way to care for God's creation, prevent soil erosion, clean the air, and conserve the environment.

✅ **Correct Answer Breakdown:**
**conserve the school environment** is the correct answer because planting trees helps protect the soil, provide shade, keep the air fresh, and preserve nature as God commanded human stewards to do.

❌ **Why Other Options Are Incorrect:**
* **avoid living in a dusty compound:** While trees reduce dust, avoiding dust is only a minor physical side effect, not the primary CRE reason for environmental stewardship.
* **ensure learners are busy:** Tree planting is a purposeful act of environmental care, not just a random chore to keep students occupied.
* **utilize the water in the school:** Tree planting uses water to grow, but utilizing excess water is not the purpose of caring for creation.

💡 **Key Takeaway for Revision:** Planting trees fulfills God's biblical command of creation stewardship by conserving the environment.""",

    37: """📘 **Study Note & Concept Overview:**
Christianity teaches that leisure time should be spent doing wholesome, constructive, and healthy activities that build the body, mind, and spirit. 1 Corinthians 6:19 reminds Christians that the body is the temple of the Holy Spirit, so we should keep it fit and healthy.

✅ **Correct Answer Breakdown:**
**Doing physical exercises** is the correct choice because physical exercise keeps the body healthy and strong, promotes positive character, and makes productive use of free time.

❌ **Why Other Options Are Incorrect:**
* **Sitting by the roadside:** Sitting idle along roads leads to wasted time and increases exposure to negative peer pressure or unsafe habits.
* **Attending disco parties:** Exposes young learners to noisy, unsafe environments and morally harmful behaviors.
* **Participating in betting games:** Gambling and betting promote greed, financial dishonesty, and addiction, which contradict Christian teachings.

💡 **Key Takeaway for Revision:** Christian leisure time should be spent constructively in health-building activities like sports and exercises.""",

    38: """📘 **Study Note & Concept Overview:**
A strong Christian family is built on love, mutual support, cooperation, and humility. Sharing responsibilities at home ensures that no single family member is overworked and promotes unity and peace within the home.

✅ **Correct Answer Breakdown:**
**sharing duties among themselves** is correct because when family members divide household work fairly, they demonstrate teamwork, love, and respect for one another.

❌ **Why Other Options Are Incorrect:**
* **reporting those who do not work:** Complaining and tattling creates hostility, resentment, and arguments rather than encouraging peaceful cooperation.
* **inviting their friends to help them to do the work:** Expecting outside friends to do your household chores avoids personal responsibility.
* **giving gifts to those who work hard:** Using gifts as a condition for doing work creates favoritism or bribery, whereas family duties should be shared out of love.

💡 **Key Takeaway for Revision:** Sharing household chores fosters family harmony, teamwork, and Christian love.""",

    39: """📘 **Study Note & Concept Overview:**
In Exodus 2:1-10, when Pharaoh had ordered all newborn Hebrew boys to be thrown into the Nile, Moses' mother placed him in a basket among the reeds. Pharaoh's daughter found the crying baby and showed mercy and compassion by adopting him.

✅ **Correct Answer Breakdown:**
**Kindness** is correct because Pharaoh's daughter felt deep sympathy and compassion for the helpless infant and chose to save his life and care for him despite his Hebrew origins.

❌ **Why Other Options Are Incorrect:**
* **Holiness:** Refers to moral purity and devotion to God, which is not the primary emotion shown when saving the baby.
* **Peace:** Means harmony and absence of conflict; her specific action was driven by tender compassion and kindness.
* **Loyalty:** Means faithfulness to one's king or nation; in fact, she defied her father Pharaoh's cruel decree to show kindness to the baby.

💡 **Key Takeaway for Revision:** Rescuing baby Moses was an act of kindness and mercy that saved the leader who would later free Israel.""",

    40: """📘 **Study Note & Concept Overview:**
The Bible contains 66 books in total, divided into two main sections: the Old Testament (39 books written before Jesus) and the New Testament (27 books covering the life of Jesus and the early Christian Church).

✅ **Correct Answer Breakdown:**
**Box A** is correct because it contains books exclusively from the New Testament (such as Matthew, Mark, Luke, John, Acts, Romans, Corinthians, Galatians, Ephesians, Philippians, Colossians, Thessalonians, Timothy, Titus, Philemon, Hebrews, James, Peter, John, Jude, and Revelation).

❌ **Why Other Options Are Incorrect:**
* **Box B:** Contains a mix of Old Testament books (like Genesis or Exodus) alongside New Testament books.
* **Box C:** Contains Old Testament books of wisdom and poetry (such as Psalms or Proverbs).
* **Box D:** Contains Old Testament major and minor prophetic books (such as Isaiah, Jeremiah, or Daniel).

💡 **Key Takeaway for Revision:** The New Testament has 27 books starting from the Gospel of Matthew through to Revelation.""",

    41: """📘 **Study Note & Concept Overview:**
God gave Moses the Ten Commandments on Mount Sinai (Exodus 20). The Tenth Commandment specifically states: "You shall not covet your neighbor's house, wife, servants, animals, or anything that belongs to your neighbor."

✅ **Correct Answer Breakdown:**
**Do not desire another man's property** is correct because coveting means secretly wishing to take or own what rightfully belongs to someone else. The commandment teaches contentment and gratitude for what you have.

❌ **Why Other Options Are Incorrect:**
* **Do not worship any other God:** This is the First Commandment, which teaches monotheism and devotion to the one true God.
* **Do not commit adultery:** This is the Seventh Commandment, which protects the sanctity of marriage.
* **Do not accuse anyone falsely:** This is the Ninth Commandment, which forbids lying and false testimony against others.

💡 **Key Takeaway for Revision:** The 10th Commandment warns against envy and covetousness, teaching us to be content with our own blessings.""",

    42: """📘 **Study Note & Concept Overview:**
In Luke 8:43-48, a woman who had suffered from a bleeding disorder for 12 long years came up behind Jesus in a large crowd. She believed with all her heart that simply touching the hem of His garment would heal her.

✅ **Correct Answer Breakdown:**
**She had faith that she would be healed** is correct because Jesus explicitly told her, "Daughter, your faith has healed you; go in peace." It was her strong faith in Jesus' power that drove her action.

❌ **Why Other Options Are Incorrect:**
* **She loved the garment of Jesus:** It was not admiration for His clothing, but faith in His divine healing power that healed her.
* **She touched it by mistake:** Her action was intentional, reaching out specifically to touch the fringe of His cloak.
* **She was told by the disciple to do so:** No disciple directed her; she acted on her own personal faith.

💡 **Key Takeaway for Revision:** Faith in God's power brings healing and restoration, as demonstrated by the woman who touched Jesus' cloak.""",

    43: """📘 **Study Note & Concept Overview:**
In Luke 11:5-8, Jesus taught the Parable of the Friend at Midnight, where a man goes to his neighbor late at night asking for bread. Even though the friend hesitates initially, he grants the request because of the man's persistence.

✅ **Correct Answer Breakdown:**
**be persistent in prayer** is correct because the parable teaches Christians to pray continuously and boldly without giving up.

❌ **Why Other Options Are Incorrect:**
* **provide help to our friends:** While helping friends is good, the main spiritual lesson of this specific parable is persistent prayer.
* **welcome visitors in our homes:** Hospitality is important, but Jesus used this scenario to illustrate unceasing prayer.
* **lock our doors at night:** Physical security is practical, but locking doors is merely part of the story's setting, not its spiritual lesson.

💡 **Key Takeaway for Revision:** The Parable of the Friend at Midnight teaches unceasing, persistent prayer.""",

    44: """📘 **Study Note & Concept Overview:**
In Luke 17:11-19, Jesus healed ten men suffering from leprosy as they walked away to show themselves to the priests, demonstrating His divine authority over disease.

✅ **Correct Answer Breakdown:**
**healing the Ten Lepers** is correct because this miracle demonstrated Jesus' mercy and power to heal incurable skin diseases.

❌ **Why Other Options Are Incorrect:**
* **healing the Roman Officer's servant:** Demonstrated great faith of a Gentile officer (Luke 7:1-10).
* **turning water into wine:** Jesus' first miracle performed at the wedding in Cana of Galilee (John 2:1-11).
* **calming the storm:** Demonstrated Jesus' power over physical nature and elements (Mark 4:35-41).

💡 **Key Takeaway for Revision:** Jesus healed the ten lepers, reminding Christians to show gratitude to God when healed or blessed.""",

    45: """📘 **Study Note & Concept Overview:**
Christianity teaches that material resources and personal talents should be shared unselfishly to assist those in need, following Jesus' example of charity.

✅ **Correct Answer Breakdown:**
**buying food for poor people** is correct because using pocket money or resources to feed the hungry is a direct fulfillment of Christian charity (Matthew 25:35).

❌ **Why Other Options Are Incorrect:**
* **organising parties for friends:** Focuses on personal recreation rather than serving the needy.
* **buying clothes for themselves:** Reflects self-centered spending rather than helping marginalized people.
* **travelling to different places:** Leisure travel serves personal enjoyment rather than charitable service.

💡 **Key Takeaway for Revision:** Christian charity involves serving the needy, such as providing food and shelter for the poor.""",

    46: """📘 **Study Note & Concept Overview:**
During the Last Supper (Luke 22:19), Jesus broke bread and gave it to His disciples, establishing the Holy Communion sacrament for His followers.

✅ **Correct Answer Breakdown:**
**Do this in memory of me.** is correct because Jesus commanded His disciples to celebrate Holy Communion as a perpetual remembrance of His sacrificial death on the cross.

❌ **Why Other Options Are Incorrect:**
* **Go and heal the sick:** The commission given when sending out the twelve disciples (Matthew 10:8), not the words of Holy Communion.
* **Do not take a purse for yourself:** An instruction for missionary travel simplicity (Luke 10:4).
* **Bless those who curse you:** A moral instruction from the Sermon on the Plain/Mount (Luke 6:28).

💡 **Key Takeaway for Revision:** Jesus commanded "Do this in memory of me" when instituting the Holy Communion sacrament.""",

    47: """📘 **Study Note & Concept Overview:**
In Acts 5:1-11, Ananias and his wife Sapphira sold a piece of property. They secretly kept back part of the money while claiming to give the full amount to the apostles. Because they lied to God and the Holy Spirit, they both fell down dead.

✅ **Correct Answer Breakdown:**
**Honesty** is correct because the story serves as a serious warning against dishonesty, hypocrisy, and lying in financial and spiritual matters.

❌ **Why Other Options Are Incorrect:**
* **Tolerance:** Refers to accepting others; Ananias and Sapphira were judged for deceit, not intolerance.
* **Mercy:** Refers to showing forgiveness; the narrative highlights God's strict judgment against deceit in the early church.
* **Perseverance:** Refers to continuing through hardship; the core lesson is about truthfulness and integrity.

💡 **Key Takeaway for Revision:** The story of Ananias and Sapphira teaches Christians to practice absolute honesty in all dealings.""",

    48: """📘 **Study Note & Concept Overview:**
Child safety and personal protection are essential life skills. Strangers may attempt to lure children into vehicles under false pretenses, which poses severe safety risks including abduction or harm.

✅ **Correct Answer Breakdown:**
**Refuse and continue walking to school** is correct because staying on the public path, declining offers from unknown people, and proceeding safely to school keeps the child protected.

❌ **Why Other Options Are Incorrect:**
* **Accept the lift and get into the car:** Extremely dangerous; entering a stranger's car exposes children to kidnapping, assault, or harm.
* **Refuse and go back home:** Walking back home alone leaves the student unsupervised and causes them to miss school when they could walk safely along the school route.
* **Hide in the bush until the vehicle goes away:** Hiding in bushes isolates the child, increases panic, and exposes them to hidden outdoor dangers like snakes or insects.

💡 **Key Takeaway for Revision:** Always say NO to lifts or gifts from strangers and stay on safe, public routes to school.""",

    49: """📘 **Study Note & Concept Overview:**
School prefects are student leaders appointed to assist teachers in maintaining order and discipline. Romans 13:1 teaches that all authority comes from God and should be respected so that harmony is preserved.

✅ **Correct Answer Breakdown:**
**promote respect for authority** is correct because obeying prefects and school regulations builds a disciplined environment and teaches respect for leadership.

❌ **Why Other Options Are Incorrect:**
* **To avoid being punished:** True obedience comes from respect and moral duty, not merely fear of punishment.
* **To obtain good things from the prefect:** Cooperating to gain personal favors or bribes is corrupt and dishonest.
* **To be recognized by the teachers:** Doing what is right simply to get praise or attention from teachers lacks genuine moral integrity.

💡 **Key Takeaway for Revision:** Cooperating with prefects promotes respect for authority and maintains a peaceful school environment.""",

    50: """📘 **Study Note & Concept Overview:**
Social media and digital technology are powerful tools. When used responsibly by learners, social media can enhance education, enable academic research, and facilitate learning group discussions.

✅ **Correct Answer Breakdown:**
**Exchanging messages in their learning areas** is correct because using digital platforms for homework assistance, educational discussion, and revision is safe, productive, and valuable.

❌ **Why Other Options Are Incorrect:**
* **Chatting with friends all the time:** Continuous non-stop chatting causes digital addiction and wastes valuable study time.
* **Taking and posting their pictures:** Posting personal photos publicly poses serious privacy risks and exposes young learners to online safety hazards.
* **Watching all kinds of videos:** Unrestricted video viewing exposes children to inappropriate, violent, or unverified online content.

💡 **Key Takeaway for Revision:** Social media should be used by students safely and productively for educational and learning purposes."""
}

file_path = 'src/data/kpsea-sst-cre-2023.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for q_num, exp_text in explanations_map.items():
    q_str = f'"questionNumber": {q_num},'
    q_pos = content.find(q_str)
    if q_pos != -1:
        exp_pos = content.find('"explanation":', q_pos)
        if exp_pos != -1:
            quote_start = content.find('"', exp_pos + 14)
            curr = quote_start + 1
            while curr < len(content):
                if content[curr] == '"' and content[curr-1] != '\\':
                    rest = content[curr+1:curr+30].lstrip()
                    if rest.startswith('}') or rest.startswith(','):
                        quote_end = curr
                        break
                curr += 1
            
            new_json_exp = json.dumps(exp_text)
            content = content[:exp_pos] + '"explanation": ' + new_json_exp + content[quote_end+1:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated CRE explanations successfully!")
