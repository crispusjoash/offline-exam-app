import json

filepath = 'src/data/kpsea-sst-parta-2023.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const kpseaSstParta2023 = '
clean_text = text.replace(prefix, '').strip()
if clean_text.endswith(';'):
    clean_text = clean_text[:-1]

data = json.loads(clean_text)

sst_explanations = {
    1: """The correct answer is **A**.

**Detailed Analysis of the Correct Answer:**
In visual arts and drawing, **overlapping** is a technique used to create the illusion of 3D depth and spatial distance on a flat 2D surface. Diagram **A** illustrates correct overlapping where an object in the foreground partially covers or conceals part of an object situated behind it, clearly establishing which object is closer to the viewer.

**Why Other Options Are Incorrect:**
* **B:** Shows objects floating separately in space without any overlapping relationship to show depth.
* **C:** Shows objects drawn side-by-side touching at the edges rather than overlapping.
* **D:** Displays isolated objects without any overlapping elements.

📌 **Key Learning Note:**
Overlapping occurs when an object in front partially hides an object behind it, creating visual depth and perspective.""",

    2: """The correct answer is **Calabash, gourd, pot.**.

**Detailed Analysis of the Correct Answer:**
A **still life composition** is an artistic arrangement of non-moving, inanimate (non-living) man-made or natural objects placed together on a surface for drawing or painting. A group consisting of a **calabash, gourd, and clay pot** is a classic example of a traditional still life arrangement.

**Why Other Options Are Incorrect:**
* **People sitting still.:** Refers to human figure drawing or pose modeling, not still life art.
* **Still trees on a calm day.:** Represents landscape drawing of outdoor natural living environments.
* **Buildings and street lights.:** Represents architectural or townscape drawing, not a tabletop still life arrangement.

📌 **Key Learning Note:**
Still life art consists of arranged non-living (inanimate) objects such as pots, gourds, fruits, vases, or books.""",

    3: """The correct answer is **To avoid mixing ink colours.**.

**Detailed Analysis of the Correct Answer:**
When switching to a new ink color in a fountain pen or calligraphic pen, it is essential to flush the nib and reservoir with clean water **to avoid mixing ink colours**. If residual old ink remains inside, it will mix with the new ink, contaminating its color purity and producing muddy, unexpected shades.

**Why Other Options Are Incorrect:**
* **To make the pen clean.:** While cleaning removes dust, preventing color contamination is the primary functional reason when changing ink colors.
* **To make the ink clear.:** Ink is intended to be vibrant and opaque, not transparent or clear.
* **To avoid blocking the pen.:** Removing dried ink prevents clogging, but flushing specifically when changing inks prevents color bleeding.

📌 **Key Learning Note:**
Flushing a fountain pen with clean water when changing ink cartridges prevents color contamination.""",

    4: """The correct answer is **Twine**.

**Detailed Analysis of the Correct Answer:**
The weaving technique illustrated is **twining** (twine weave). Twining is a basketry and weaving method where a pair of flexible horizontal weft strands are twisted around each vertical warp strand as weaving progresses, creating a strong, tight, and durable woven structure.

**Why Other Options Are Incorrect:**
* **Plaiting:** Involves braiding three or more flexible strands over each other without fixed warp threads.
* **Plain weave:** Involves passing a single weft thread alternately over and under single warp threads in a simple checkerboard pattern.
* **Coil and stitch:** A basketry method where a central core bundle is coiled spirally and stitched together using thread or raffia.

📌 **Key Learning Note:**
**Twining** is a weaving technique where two weft strands twist around warp threads to construct durable baskets and mats.""",

    5: """The correct answer is **Using slip.**.

**Detailed Analysis of the Correct Answer:**
In pottery and clay work using the coiling technique, individual clay coils must be joined securely to form a solid vessel. The best way to join coils is by scoring (scratching) the joining edges and applying **slip** (a liquid cream-like mixture of clay and water). Slip acts as a natural **clay glue**, fusing the coils together seamlessly when pressed and smoothed.

**Why Other Options Are Incorrect:**
* **Using pallets:** Pallets are flat wooden boards used for holding or mixing materials, not bonding clay.
* **Using glue:** Synthetic chemical glues fail on wet clay and burn away during kiln firing; only clay slip creates a permanent bond.
* **Pressing well:** Simply pressing dry or firm coils without slip leaves weak seams that crack open as the pot dries.

📌 **Key Learning Note:**
**Clay slip** (clay mixed with water) is used as a natural adhesive to join clay coils, handles, and slabs in pottery.""",

    6: """The correct answer is **Keeping them in the river bank.**.

**Detailed Analysis of the Correct Answer:**
**Keeping plastic bottles on a river bank** is an act of environmental littering and pollution. When rain falls or river levels rise, these discarded plastic bottles are washed into the water, causing severe aquatic pollution and endangering marine life. It is **not** a method of reusing plastic.

**Why Other Options Are Incorrect:**
* **Making toys:** An excellent creative upcycling method of reusing plastic bottles into play items.
* **Decorating places:** Reusing cut or painted bottles as hanging flower pots or decorative ornaments.
* **Using them to water flowers:** A functional reuse of plastic bottles for drip irrigation or plant watering.

📌 **Key Learning Note:**
Reusing plastic containers prevents environmental pollution and keeps plastic waste out of water bodies and ecosystems.""",

    7: """The correct answer is **Beading.**.

**Detailed Analysis of the Correct Answer:**
The leather wristband shown is decorated using **beading**. Beading is a traditional craft technique where colorful beads are sewn, woven, or attached onto leather surfaces to create decorative patterns and cultural motifs.

**Why Other Options Are Incorrect:**
* **Thonging:** Lacing leather edges together using thin leather strips or thongs.
* **Stitching:** Sewing leather pieces together structurally using thread.
* **Gluing:** Applying adhesive to stick leather layers together without decorative beadwork.

📌 **Key Learning Note:**
**Beading** is the art of attaching decorative beads to fabric or leather to enhance aesthetic appeal.""",

    8: """The correct answer is **Increase size of the theatre.**.

**Detailed Analysis of the Correct Answer:**
**Increasing the size of the theatre** alters the venue architecture, but does **not** contribute to giving personality or character to a puppet during a performance. Characterization depends on the puppeteer's performance and the puppet's design.

**Why Other Options Are Incorrect:**
* **Create a voice:** Modulating voice pitch, tone, and speech rhythm gives a distinct personality and emotion to the puppet.
* **Make movements:** Manipulating puppet limbs, head gestures, and body language brings the character to life physically.
* **Use different clothes and jewellery:** Costuming defines the age, social status, and role of the puppet character.

📌 **Key Learning Note:**
Puppet characterization is achieved through **voice modulation, expressive movement manipulation, and costume design**.""",

    9: """The correct answer is **Seek permission from the artist.**.

**Detailed Analysis of the Correct Answer:**
Respecting intellectual property and copyright laws requires that anyone wishing to use, display, or reproduce another person's artwork must first **seek permission from the artist** (the copyright holder). Obtaining consent honors the creator's legal and moral rights.

**Why Other Options Are Incorrect:**
* **Copy and trace the artwork:** Copying or tracing another person's work without permission constitutes plagiarism and copyright infringement.
* **Edit the artwork and use it:** Altering someone else's original creation without authorization still violates intellectual property rights.
* **Take a photograph when no one is watching:** Secretly photographing artwork for unauthorized reproduction or commercial use is unethical and illegal.

📌 **Key Learning Note:**
Always **seek permission from original artists** before reproducing or using their creative work to respect copyright laws.""",

    10: """The correct answer is **Join the school's art club.**.

**Detailed Analysis of the Correct Answer:**
Joining the school's art club is an internal extracurricular student activity for learning art, **not** a direct marketing or promotional strategy for selling artwork to customers during an exhibition.

**Why Other Options Are Incorrect:**
* **Post pictures of artwork on sale on social media:** An effective digital marketing strategy reaching a broad online target audience.
* **Announce and invite the community for the exhibition:** A direct public relations strategy raising community awareness and attendance.
* **Create posters to advertise sale of the artwork:** A proven visual advertising technique attracting visitors to the sale.

📌 **Key Learning Note:**
Effective marketing strategies include **advertising posters, social media promotion, and public invitations** to attract buyers.""",

    11: """The correct answer is **Cheering.**.

**Detailed Analysis of the Correct Answer:**
**Cheering** is an external reaction or supportive response from the audience watching a performance. It is **not** a structural component of the folk dance performance itself.

**Why Other Options Are Incorrect:**
* **Costumes:** Essential cultural attire reflecting the origin, theme, and context of the folk dance.
* **Body movement:** The core physical dance steps, body gestures, and rhythm executed by dancers.
* **Songs:** The musical vocal accompaniment and lyrics that guide the tempo and story of the dance.

📌 **Key Learning Note:**
Core components of a folk dance include **music/songs, dance movements, costumes, musical instruments, and props**.""",

    12: """The correct answer is **Performed using sharp props.**.

**Detailed Analysis of the Correct Answer:**
Folk songs and cultural dances should **never be performed using sharp props** (such as real spears, sharp knives, or panga blades) because sharp objects pose extreme physical injury risks to performers and audience members. Safe, blunt improvised props should always be substituted.

**Why Other Options Are Incorrect:**
* **Performed observing safety:** A fundamental rule for executing any stage dance or performance safely.
* **Performed observing good manners:** Essential for cultural respect, decorum, and positive community reception.
* **Performed with coordinated body movements:** A core requirement for rhythmic and harmonious group performance.

📌 **Key Learning Note:**
Stage safety requires substituting real sharp objects with **safe, blunt, improvised props** during cultural performances.""",

    13: """The correct answer is **Singing while talking.**.

**Detailed Analysis of the Correct Answer:**
**Singing while talking** disrupts vocal tone, breath control, pitch accuracy, and musical rhythm. Talking during singing prevents proper vocal execution and is **not** a correct singing technique.

**Why Other Options Are Incorrect:**
* **Singing the tune accurately:** Essential for producing correct musical pitch and harmonious melody.
* **Pronouncing the words clearly:** Diction ensures the audience understands the lyrics and message of the song.
* **Using facial expressions:** Conveys the mood, emotion, and story of the song effectively.

📌 **Key Learning Note:**
Proper singing requires **clear diction (pronunciation), accurate pitch/tune, proper breath control, and expressive facial communication**.""",

    14: """The correct answer is **Hollow tube, knife, nails and ruler.**.

**Detailed Analysis of the Correct Answer:**
To construct a simple wind instrument (aerophone) like a flute or recorder, learners need:
1. A **hollow tube** (bamboo or PVC pipe) for the instrument body.
2. A **ruler** to measure precise hole spacings.
3. A **knife** or hot **nails** to bore the mouth piece and finger tone holes cleanly.

**Why Other Options Are Incorrect:**
* **Hollow tube, nails, feathers and knife:** Feathers are decorative items and serve no structural purpose in wind instrument craft.
* **Hollow tube, wooden bars, paint and nails:** Wooden bars are used for marimbas/xylophones, not for boring tone holes in a flute.
* **Hollow tube, ruler, nails and feathers:** Lacks a cutting tool (knife) needed to shape and smooth the mouthpiece and tone holes.

📌 **Key Learning Note:**
Crafting wind instruments (aerophones) requires **measuring tools (ruler) and cutting/boring tools (knife/nails)** to make accurate tone holes.""",

    15: """The correct answer is **Hang it on the wall.**.

**Detailed Analysis of the Correct Answer:**
After performing with a traditional string instrument (like a *Wandindi* or fiddle), the player should **hang it on the wall** (or store it in a dry protective case). Hanging keeps the wooden body and skin resonator off the ground, protecting it from moisture, dust, pests, and accidental damage.

**Why Other Options Are Incorrect:**
* **Wash it with water:** Washing wooden instruments with water warps the wood, damages skin resonators, and ruins strings.
* **Keep it outside under the sun:** Direct heat and sunlight dry out, crack, and warp wooden instrument bodies.
* **Put it on the floor:** Leaving instruments on the floor exposes them to dirt, moisture, and risk of being stepped on.

📌 **Key Learning Note:**
Store musical instruments safely by **hanging them in dry indoor areas or storing them in padded cases**.""",

    16: """The correct answer is **D**.

**Detailed Analysis of the Correct Answer:**
Rhythmic pattern **D** correctly matches the syllable counts, speech accents, and note values of the Kiswahili text stanza **"Njoo twende uwanjani"** (5 syllables: Njoo - twen - de - u - wan - ja - ni).

**Why Other Options Are Incorrect:**
* **A:** Features incorrect measure beat divisions that clash with the poetic meter of the sentence.
* **B:** Features mismatched note durations that distort the natural speech rhythm of the words.
* **C:** Contains incorrect rest placements that disrupt metric phrasing.

📌 **Key Learning Note:**
Matching text to music requires aligning natural speech stresses and syllable counts with musical rhythms.""",

    17: """The correct answer is **Slowly and softly.**.

**Detailed Analysis of the Correct Answer:**
A **lullaby** is a quiet, soothing song sung to calm infants and induce sleep. It should always be sung **slowly and softly** to create a peaceful, relaxing environment for a child.

**Why Other Options Are Incorrect:**
* **Loudly and softly:** Loud vocal surges startle and wake sleeping infants.
* **Softly and sadly:** Lullabies are comforting and warm, not sad or mournful.
* **Fast and softly:** Fast tempos excite and stimulate babies rather than lulling them to sleep.

📌 **Key Learning Note:**
**Lullabies** feature **slow tempos, soft dynamics, and gentle melodies** designed to soothe babies to sleep.""",

    18: """The correct answer is **(iii), (iv), (v) and (i).**.

**Detailed Analysis of the Correct Answer:**
Hygiene and maintenance measures after playing a descant recorder follow a logical order:
1. **(iii) Wipe moisture from the instrument after use:** Removes saliva from inside the tube.
2. **(iv) Wash the mouthpiece with warm soapy water:** Disinfects the head joint where mouth contact occurred.
3. **(v) Clean the instrument with warm soapy water / damp cloth:** Removes fingerprints and grime.
4. **(i) Return the instrument in its case after use:** Protects it from dust and damage.

Thus, set **(iii), (iv), (v) and (i)** is correct.

**Why Other Options Are Incorrect:**
* **(vi), (iv), (ii) and (i):** Places assembly step (ii) after performance care, which is out of order.
* **(ii), (iii), (vi) and (i):** Includes setup step (ii) instead of post-playing hygiene disinfection.
* **(v), (vi), (iv) and (ii):** Ends with assembly (ii) rather than safe case storage (i).

📌 **Key Learning Note:**
Descan recorder care: **Wipe internal moisture ➔ Wash mouthpiece with warm soapy water ➔ Store safely in case**.""",

    19: """The correct answer is **He should tune the instrument.**.

**Detailed Analysis of the Correct Answer:**
If a string instrument (like a guitar, fiddle, or litungu) produces incorrect or off-pitch sound, the player **should tune the instrument**. Tuning involves adjusting the tension of the strings using tuning pegs or bridges until each string produces its correct musical pitch.

**Why Other Options Are Incorrect:**
* **He should clean the instrument:** Cleaning removes dust but does not change string tension or musical pitch.
* **He should warm the instrument:** Warming over heat is used to tighten membrane drumheads, not stringed instruments.
* **He should get another instrument:** Unnecessary and wasteful when simple peg tuning resolves the issue.

📌 **Key Learning Note:**
String instruments are tuned by **adjusting string tension** using tuning pegs or tuning bridges.""",

    20: """The correct answer is **Instrument (i) is tuned by adjusting knobs while instrument (ii) is tuned by warming.**.

**Detailed Analysis of the Correct Answer:**
Instrument (i) is a traditional **string instrument** (chordophone like a *Nyatiti* or *Litungu*), which is tuned by **adjusting tuning knobs/pegs** to change string tension. Instrument (ii) is a traditional **membrane drum** (membranophone), which is tuned by **warming the leather drumhead over mild heat** to tighten the skin membrane.

**Why Other Options Are Incorrect:**
* **Instrument (i) is played by bowing while instrument (ii) is played by hitting:** String instruments like litungu are plucked with fingers, not bowed like violins.
* **Instrument (i) is a percussion instrument while instrument (ii) is a string instrument:** Reverses instrument classifications (i is chordophone, ii is membranophone).
* **Instrument (i) cannot play a melody while instrument (ii) can play a melody:** String instruments play melodic tunes, while drums provide rhythmic beats.

📌 **Key Learning Note:**
- **String Instruments:** Tuned by adjusting tuning pegs/knobs.
- **Membrane Drums:** Tuned by warming over heat or tightening laces.""",

    21: """The correct answer is **Wind, temperature, air pressure.**.

**Detailed Analysis of the Correct Answer:**
The primary **elements of weather** measured at weather stations include **wind, temperature, air pressure (atmospheric pressure)**, humidity, rainfall, and sunshine.

**Why Other Options Are Incorrect:**
* **Temperature, snow, rain:** Snow and rain are specific forms of precipitation, not separate fundamental weather elements.
* **Sunshine, fog, temperature:** Fog is a ground-level condensation condition, not a primary weather element.
* **Temperature, snow, air pressure:** Includes snow (a precipitation type) rather than core elements like wind or humidity.

📌 **Key Learning Note:**
Main **Elements of Weather**: Temperature, Wind, Air Pressure, Humidity, Rainfall, and Sunshine.""",

    22: """The correct answer is **C**.

**Detailed Analysis of the Correct Answer:**
In physical geography, **relief features** refer to the physical landforms and variations in elevation on the Earth's surface. Diagram **C** illustrates a major physical relief feature such as a valley or mountain landscape.

**Why Other Options Are Incorrect:**
* **A:** Represents an artificial man-made structure rather than a natural landform.
* **B:** Represents drainage/water bodies rather than land relief elevation.
* **D:** Shows vegetation cover rather than physical landform relief.

📌 **Key Learning Note:**
**Relief Features** include physical landforms such as mountains, hills, plateaus, valleys, and plains.""",

    23: """The correct answer is **North.**.

**Detailed Analysis of the Correct Answer:**
In standard map reading and cartography, the **top direction of a map** represents **North**. Therefore, locating an object towards the top of a map relative to a starting point gives the direction as **North**.

**Why Other Options Are Incorrect:**
* **South:** Located towards the bottom of standard maps.
* **East:** Located towards the right side of standard maps.
* **West:** Located towards the left side of standard maps.

📌 **Key Learning Note:**
Unless otherwise indicated, the top of a map always points to **North**.""",

    24: """The correct answer is **Western region of Kenya.**.

**Detailed Analysis of the Correct Answer:**
In Eastern Africa, **tropical rainforest vegetation** thrives in areas experiencing high, well-distributed rainfall throughout the year. The primary example in Kenya is the **Western region of Kenya** (specifically Kakamega Forest), which is the easternmost remnant of the equatorial Guinea-Congolian tropical rainforest.

**Why Other Options Are Incorrect:**
* **Northern region of Sudan:** Arid and semi-arid desert environment receiving extremely low rainfall.
* **Northern region of Uganda:** Dominated by dry savanna grassland and acacia woodlands.
* **Southern region of Tanzania:** Covered mainly by Miombo savanna woodlands.

📌 **Key Learning Note:**
**Kakamega Forest in Western Kenya** is the main tropical rainforest region in Kenya.""",

    25: """The correct answer is **It experiences high temperatures.**.

**Detailed Analysis of the Correct Answer:**
**Semi-desert (semi-arid) climate zones** are characterized by **high daytime temperatures**, clear skies, low relative humidity, high evaporation rates, and low, unreliable rainfall (below 500mm annually).

**Why Other Options Are Incorrect:**
* **It receives high rainfall:** False; semi-deserts receive very low and erratic annual rainfall.
* **It experiences high humidity:** False; semi-deserts have dry air with very low humidity.
* **It receives rain in the afternoon:** Afternoon convectional rainfall is typical of hot, humid equatorial regions, not dry semi-deserts.

📌 **Key Learning Note:**
Characteristics of **Semi-Desert Climate**: High daytime temperatures, low rainfall, dry air, and high evaporation.""",

    26: """The correct answer is **Malka Mari.**.

**Detailed Analysis of the Correct Answer:**
**Malka Mari National Park** is located in **Mandera County** in extreme northeastern Kenya along the border with Ethiopia, along the Daua River.

**Why Other Options Are Incorrect:**
* **Sibiloi:** Located along the northeastern shores of Lake Turkana in Marsabit County.
* **Amboseli:** Located in Kajiado County at the foot of Mt. Kilimanjaro.
* **Kora:** Located in Tana River and Kitui counties along the Tana River basin.

📌 **Key Learning Note:**
**Malka Mari National Park** is situated in Mandera County in northeastern Kenya.""",

    27: """The correct answer is **Maasai and Turkana.**.

**Detailed Analysis of the Correct Answer:**
The **Maasai and Turkana** are both **Plains Nilotic** ethnic groups in Kenya who migrated from the Nile valley region into the rift valley and northern plains of Kenya.

**Why Other Options Are Incorrect:**
* **Abagusii and Somali:** Abagusii are Bantus, while Somalis are Cushites.
* **Luo and Akamba:** Luos are River-Lake Nilotes, while Akamba are Bantus.
* **Nubians and Pokomo:** Pokomo are Bantus, while Nubians settled from Sudan.

📌 **Key Learning Note:**
Nilotic Groups in Kenya:
- **Plains Nilotes:** Maasai, Turkana, Samburu, Njemps.
- **River-Lake Nilotes:** Luo.
- **Highland Nilotes:** Kalenjin (Kipsigis, Nandi, Tugen, etc.).""",

    28: """The correct answer is **Apprenticeship**.

**Detailed Analysis of the Correct Answer:**
**Apprenticeship** is a traditional system of learning where a learner acquires practical skills and craft knowledge by **observing, imitating, and practicing under the guidance of an experienced master** (such as a grandmother teaching pottery).

**Why Other Options Are Incorrect:**
* **Narration:** Storytelling or verbal presentation of historical tales without practical hands-on craft practice.
* **Discussion:** Verbal exchange of ideas without physical skill execution.
* **Riddles:** Word puzzles used to test wits and memory, not practical craft skills.

📌 **Key Learning Note:**
**Apprenticeship** is learning practical skills through observation and hands-on guidance from an expert.""",

    29: """The correct answer is **It ensures teachers report for duty early.**.

**Detailed Analysis of the Correct Answer:**
Supervising teacher attendance and ensuring teachers report for duty early is an administrative duty of the **Headteacher and Teachers Service Commission (TSC)**, **NOT** a function of the student **Children's Government**.

**Why Other Options Are Incorrect:**
* **It speaks on behalf of the learners to the school administration:** A primary representation role of the Children's Government.
* **It ensures that the learning environment is friendly:** Promotes peer discipline, cleanliness, and child-friendly activities.
* **It assists teachers to ensure learners follow the school rules:** Helps maintain order and peer compliance with school regulations.

📌 **Key Learning Note:**
The **Children's Government** represents student interests and peer discipline, but does not manage teacher employment duties.""",

    30: """The correct answer is **Using false documents.**.

**Detailed Analysis of the Correct Answer:**
According to the Constitution of Kenya, citizenship acquired by registration can be legally revoked or cancelled if it was obtained through **fraud, false representation, or forged documents**.

**Why Other Options Are Incorrect:**
* **Voting during the general election:** A fundamental constitutional right granted to all adult Kenyan citizens.
* **Attending a local harambee meeting:** A lawful community participation activity.
* **Joining a political party:** A guaranteed constitutional right of freedom of association.

📌 **Key Learning Note:**
Citizenship by registration can be revoked if obtained **fraudulently using false documents**.""",

    31: """The correct answer is **Bus.**.

**Detailed Analysis of the Correct Answer:**
During educational tours inside national parks, visitors travel in an enclosed **tour bus** (or game-viewing van) to safely observe wildlife while adhering to park conservation regulations.

**Why Other Options Are Incorrect:**
* **Train:** Railway tracks pass through fixed corridors and do not transport tourists around internal game-viewing tracks.
* **Lorry:** Open cargo lorries are unsafe and unsuitable for tourist game drives.
* **Motorcycles:** Bicycles and motorcycles are strictly prohibited inside national parks due to extreme predator attack risks.

📌 **Key Learning Note:**
Enclosed **tour buses and vans** provide safe transportation for viewing wildlife in national parks.""",

    32: """The correct answer is **Soils.**.

**Detailed Analysis of the Correct Answer:**
**Soils** are naturally occurring materials formed by the weathering of rocks and organic decomposition. Soil is a vital **natural resource** found directly in the Earth's environment.

**Why Other Options Are Incorrect:**
* **Bottles:** Man-made manufactured synthetic objects made of glass or plastic.
* **Tools:** Man-made fabricated implements (hoes, hammers) made from processed metals/wood.
* **Posters:** Man-made printed paper items.

📌 **Key Learning Note:**
**Natural Resources** occur naturally in the environment (e.g. soil, water, air, minerals, plants, rocks).""",

    33: """The correct answer is **small scale farmers grow cash crops and food crops while subsistence farmers grow food crops**.

**Detailed Analysis of the Correct Answer:**
The fundamental difference is that **subsistence farming** focuses exclusively on growing food crops to feed the farmer's immediate family, whereas **small-scale farming** produces both food crops and **cash crops** for sale in local markets to generate income.

**Why Other Options Are Incorrect:**
* **small scale farmers keep large herds of animals while subsistence farmers grow food crops:** Keeping large herds on vast land describes commercial ranching or pastoralism.
* **subsistence farming is done on small farms while small scale farming is done on large farms.:** Both operate on relatively small land parcels; market intent is the main difference.
* **subsistence farmers use simple tools while small scale farmers use machinery.:** Both often use hand tools, but commercial sale sets small-scale farming apart.

📌 **Key Learning Note:**
- **Subsistence Farming:** Growing food primarily for **family consumption**.
- **Small-Scale Farming:** Growing food and cash crops for **market sale**.""",

    34: """The correct answer is **courageous person.**.

**Detailed Analysis of the Correct Answer:**
In African traditional society, a great leader was expected to be a **courageous person** who demonstrated bravery in defending the community, making difficult decisions, and maintaining justice and peace.

**Why Other Options Are Incorrect:**
* **good dancer:** Entertainment skills like dancing do not define political or community leadership qualities.
* **prophet:** While religious seers existed, traditional leaders were evaluated on courage, wisdom, and justice.
* **storyteller:** Oral performance skill does not replace core leadership attributes like courage and wisdom.

📌 **Key Learning Note:**
Traditional African leaders were valued for **courage, wisdom, integrity, and defense of the community**.""",

    35: """The correct answer is **Language.**.

**Detailed Analysis of the Correct Answer:**
While language (such as Kiswahili) is a national unifying medium, it is **not** one of the official constitutional **symbols of national unity**. The official national symbols explicitly defined in the Constitution of Kenya are:
1. The National Flag
2. The National Anthem
3. The Coat of Arms
4. The Public Seal

**Why Other Options Are Incorrect:**
* **Flag:** The National Flag is an official symbol of national unity prescribed in the Constitution.
* **National Anthem:** An official constitutional symbol of national identity and unity.
* **Public seal:** The official seal of the Republic of Kenya, mandated by the Constitution as a national symbol.

📌 **Key Learning Note:**
Kenya's 4 Official Symbols of National Unity:
1. **National Flag**
2. **National Anthem**
3. **Coat of Arms**
4. **Public Seal**"""
}

for q in data['sectionA']:
    qn = q['questionNumber']
    if qn in sst_explanations:
        q['explanation'] = sst_explanations[qn]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')

print("All 35 questions updated successfully in kpsea-sst-parta-2023.js!")
