import json
import re

explanations_map = {
    36: """In Christian Religious Education, planting trees stewardship fulfills God's command to care for Creation (Genesis 2:15) and serves to **conserve the school environment**.

* **Why other options are incorrect:**
  * **avoid living in a dusty compound:** Reducing dust is a minor physical benefit, but environmental conservation and stewardship is the primary CRE goal.
  * **ensure learners are busy:** Tree planting is purposeful environmental stewardship, not a distraction activity to keep learners busy.
  * **utilize the water in the school:** Tree planting utilizes water, but water usage is not the primary purpose of environmental conservation.

💡 **Key Takeaway:** Planting trees is an act of environmental stewardship, taking care of God's creation.""",

    37: """Engaging in **Doing physical exercises** during leisure time promotes health, physical stewardship of the body as the temple of the Holy Spirit (1 Corinthians 6:19), and positive character building.

* **Why other options are incorrect:**
  * **Sitting by the roadside:** Idleness leads to wasted time and vulnerability to negative peer pressure or bad habits.
  * **Attending disco parties:** Exposes young learners to inappropriate environments, loud music, alcohol, or immoral behavior.
  * **Participating in betting games:** Gambling promotes greed, financial ruin, and dishonesty, contradicting Christian values.

💡 **Key Takeaway:** Christian leisure time should be spent constructively in activities that glorify God and build bodily and moral health.""",

    38: """Family members promote Christian love, harmony, and mutual support by **sharing duties among themselves**, demonstrating teamwork and humility.

* **Why other options are incorrect:**
  * **reporting those who do not work:** Causes conflict, resentment, and division rather than encouraging unity.
  * **inviting their friends to help them to do the work:** Avoids personal household responsibility and shirks family duties onto outsiders.
  * **giving gifts to those who work hard:** Creates favoritism or bribery, whereas family work should be done out of love and duty.

💡 **Key Takeaway:** Sharing household responsibilities builds family unity, cooperation, and mutual respect.""",

    39: """Pharaoh's daughter demonstrated **Kindness** and compassion when she rescued baby Moses from the basket in the River Nile and raised him despite his Hebrew origin (Exodus 2:5-10).

* **Why other options are incorrect:**
  * **Holiness:** Moral purity and set-apartness for God, whereas rescuing the baby was an act of mercy and compassion.
  * **Peace:** Harmony between people; while peaceful, her specific motive was compassion for a crying babe.
  * **Loyalty:** Faithfulness to a person or nation; Pharaoh's daughter actually defied her father's decree out of human kindness.

💡 **Key Takeaway:** Acts of compassion and kindness to the helpless reflect God's love and mercy.""",

    40: """Box **A** contains only books belonging to the New Testament (e.g., Matthew, Mark, Luke, John, Acts, Romans, Revelation).

* **Why other options are incorrect:**
  * **B:** Includes Old Testament books like Genesis or Exodus mixed with New Testament books.
  * **C:** Includes Old Testament books of history or wisdom (like Psalms or Proverbs).
  * **D:** Contains Old Testament prophetic books (like Isaiah or Jeremiah).

💡 **Key Takeaway:** The Bible consists of 66 books: 39 in the Old Testament and 27 in the New Testament.""",

    41: """The Tenth Commandment ("You shall not covet your neighbor's house, wife, or property" - Exodus 20:17) teaches us **Do not desire another man's property**, encouraging contentment with what God has provided.

* **Why other options are incorrect:**
  * **Do not worship any other God:** The First Commandment, teaching monotheism and loyalty to God.
  * **Do not commit adultery:** The Seventh Commandment, teaching marital fidelity and moral purity.
  * **Do not accuse anyone falsely:** The Ninth Commandment, teaching truthfulness and honesty in speech.

💡 **Key Takeaway:** Contentment involves being thankful for what you have and avoiding envy or desiring others' possessions.""",

    42: """The woman suffering from a hemorrhage for 12 years touched the hem of Jesus' cloak because **She had faith that she would be healed** (Luke 8:43-48).

* **Why other options are incorrect:**
  * **She loved the garment of Jesus:** She was seeking divine healing, not admiring clothing material.
  * **She touched it by mistake:** It was an intentional, deliberate act driven by deep faith amidst a crowding press.
  * **She was told by the disciple to do so:** Disciples actually tried to keep people back; she acted on her personal faith.

💡 **Key Takeaway:** Faith in Jesus Christ brings spiritual and physical healing and restoration.""",

    43: """The parable of the friend at midnight (Luke 11:5-13) teaches Christians that we should **be persistent in prayer**, trusting that God hears and answers persistent requests.

* **Why other options are incorrect:**
  * **provide help to our friends:** While helping friends is good, the specific spiritual lesson of this parable is about prayer persistence.
  * **welcome visitors in our homes:** Hospitality is a Christian duty, but not the primary allegorical lesson of this parable.
  * **lock our doors at night:** A practical security measure, not the spiritual teaching of Jesus' parable.

💡 **Key Takeaway:** Persistence in prayer demonstrates faith and trust in God's provision.""",

    44: """The miracle of **healing the Ten Lepers** (Luke 17:11-19) encourages thankfulness because only one leper (a Samaritan) returned to give glory and thanks to Jesus for his healing.

* **Why other options are incorrect:**
  * **healing the Roman Officer's servant:** Highlights great faith in Jesus' authority to command healing from a distance.
  * **turning water into wine:** Demonstrates Jesus' divine power over nature and glory at the wedding in Cana.
  * **calming the storm:** Shows Jesus' divine power over natural elements and wind/waves.

💡 **Key Takeaway:** Always express gratitude and thankfulness to God for His blessings and miracles.""",

    45: """The parable of the Rich Man and Lazarus (Luke 16:19-31) teaches Christians to share their wealth by **buying food for poor people** and showing charity to the needy.

* **Why other options are incorrect:**
  * **organising parties for friends:** The rich man spent his money selfishly on extravagant feasting while ignoring Lazarus.
  * **buying clothes for themselves:** Selfish luxury without helping the poor leads to spiritual judgment.
  * **travelling to different places:** Using money solely for personal pleasure fails to fulfill God's command to love your neighbor.

💡 **Key Takeaway:** Use material wealth generously to help the needy and poor in society.""",

    46: """During the Last Supper, when instituting the Holy Communion (Eucharist), Jesus instructed His disciples: "**Do this in memory of me**" (Luke 22:19).

* **Why other options are incorrect:**
  * **Go and heal the sick:** A commission given when sending out the 12 or 72 disciples during missionary outreach.
  * **Do not take a purse for yourself:** An instruction regarding travel light provisions during missionary journeys.
  * **Bless those who curse you:** Teaching from the Sermon on the Mount regarding love for enemies.

💡 **Key Takeaway:** The Holy Communion is celebrated in remembrance of Jesus' sacrifice on the cross.""",

    47: """The story of Ananias and Sapphira (Acts 5:1-11), who lied about the sale price of their land and died, teaches Christians the vital value of **Honesty** and truthfulness before God and the church.

* **Why other options are incorrect:**
  * **Tolerance:** Enduring differences; Ananias and Sapphira were punished specifically for dishonesty and deception.
  * **Mercy:** Compassion; the judgment demonstrated God's intolerance of hypocrisy and lies in the early church.
  * **Perseverance:** Steadfastness; the key moral lesson of this narrative centers on financial honesty.

💡 **Key Takeaway:** Honesty and integrity are essential Christian virtues; lying to God and leaders brings destruction.""",

    48: """If a stranger offers you a lift in their vehicle, the safest personal protective action is to **Refuse and continue walking to school**, staying in public view.

* **Why other options are incorrect:**
  * **Accept the lift and get into the car:** Extremely dangerous; exposes child to kidnapping, abuse, or harm from strangers.
  * **Refuse and go back home:** Misses school unnecessarily when continuing safely along the public school route is proper.
  * **Hide in the bush until the vehicle goes away:** Hiding in bushes exposes children to hidden hazards, wild animals, or suspicious isolation.

💡 **Key Takeaway:** Never accept rides or gifts from strangers; politely refuse and walk safely along public paths to school.""",

    49: """Cooperating with student school prefects is important to **promote respect for authority**, which reflects the biblical principle of obeying legitimate leaders (Romans 13:1).

* **Why other options are incorrect:**
  * **To avoid being punished:** Obedience should be motivated by respect and moral duty, not just fear of punishment.
  * **To obtain good things from the prefect:** Seeking personal favors or bribery contradicts Christian integrity.
  * **To be recognized by the teachers:** Performing duties for eye-service or praise lacks genuine obedience.

💡 **Key Takeaway:** Respecting student leaders and authority maintains order, discipline, and peaceful learning environments.""",

    50: """The best and safest use of social media for Grade 6 learners is **Exchanging messages in their learning areas** (educational discussions, study groups, revision).

* **Why other options are incorrect:**
  * **Chatting with friends all the time:** Wastes valuable study time and creates digital addiction.
  * **Taking and posting their pictures:** Poses child online privacy and safety risks if posted indiscriminately.
  * **Watching all kinds of videos:** Exposes learners to unvetted, inappropriate, or harmful internet content.

💡 **Key Takeaway:** Use digital devices and social media responsibly for educational learning, academic research, and safe communication."""
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

print("Successfully updated all 15 explanations in CRE (kpsea-sst-cre-2023.js)!")
