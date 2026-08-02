import json
import re

explanations_map = {
    1: """Diagram **D** shows correct overlapping where the object in the foreground partially covers and blocks the view of the object behind it, creating depth and spatial perspective.

* **Why other options are incorrect:**
  * **A:** Objects are drawn side-by-side without any overlapping elements.
  * **B:** Shows floating objects without any spatial overlapping relationship.
  * **C:** Objects touch at edges but do not overlap to show foreground and background depth.

💡 **Key Takeaway:** Overlapping in drawing occurs when one object is placed in front of another, partially concealing it to create depth.""",

    2: """A still life composition is an arrangement of non-moving, inanimate objects (such as **Calabash, gourd, pot**, fruits, or vases) placed together for drawing or painting.

* **Why other options are incorrect:**
  * **People sitting still.:** Refers to human figure drawing or pose models, not inanimate still life objects.
  * **Still trees on a calm day.:** Represents landscape drawing of living outdoor environment.
  * **Buildings and street lights.:** Represents architectural or townscape drawing, not a tabletop still life arrangement.

💡 **Key Takeaway:** Still life art consists of arranged inanimate, non-living objects (calabashes, gourds, pots, fruits).""",

    3: """When changing to a different color of ink in a fountain pen, you must wash it **To avoid mixing ink colours**, which would contaminate the new ink color and alter its purity.

* **Why other options are incorrect:**
  * **To make the pen clean:** Cleaning is a secondary maintenance benefit, but preventing color contamination is the main reason when changing inks.
  * **To make the ink clear:** Ink is meant to be opaque/vibrant, not transparent or clear.
  * **To avoid blocking the pen:** Removing dried ink prevents clogging, but washing specifically when switching colors prevents color bleeding.

💡 **Key Takeaway:** Flushing a fountain pen with clean water when changing ink colors prevents color contamination.""",

    4: """The technique shown in the picture for constructing woven items like baskets or mats using two weaving strands twisted around warps is **Twine** (twinning).

* **Why other options are incorrect:**
  * **Plaiting:** Interlacing three or more strands of flexible material together.
  * **Plain weave:** Passing weft over and under single alternate warp threads in a simple checkerboard pattern.
  * **Coil and stitch:** A basketry method where a central core bundle is wrapped and stitched in a spiral.

💡 **Key Takeaway:** Twining is a weaving technique where pair strands twist around warp threads to form a strong weave.""",

    5: """When building pottery using the coiling technique, joining individual coils securely requires applying **Using slip** (liquid clay mixture) along scored edges to bond the clay coils together.

* **Why other options are incorrect:**
  * **Using pallets:** Pallets are flat boards for mixing paint or supporting pottery, not bonding wet clay.
  * **Using glue:** Synthetic glues burn away or fail on wet clay and cannot replace clay slip in pottery making.
  * **Pressing well:** Pressing helps, but scoring and applying slip is necessary to prevent coils from cracking apart when drying.

💡 **Key Takeaway:** Slip acts as a liquid clay glue used to join clay coils and handles securely.""",

    6: """**Keeping them in the river bank** is an act of environmental littering and pollution, NOT a way of reusing plastic bottles.

* **Why other options are incorrect:**
  * **Making toys:** An effective creative method of upcycling plastic bottles into play items.
  * **Decorating places:** Reusing cut or painted bottles as hanging pots or decorative ornaments.
  * **Using them to water flowers:** Functional reuse of plastic bottles for drip irrigation or plant watering.

💡 **Key Takeaway:** Reusing plastic containers keeps plastic out of riverbanks and ecosystems, preventing environmental pollution.""",

    7: """The picture shows leather wristband decoration made by applying beads onto leather, known as **Beading**.

* **Why other options are incorrect:**
  * **Thonging:** Lacing leather edges together using thin leather strips.
  * **Stitching:** Sewing leather pieces together using thread.
  * **Gluing:** Applying adhesive to stick leather layers without decorative beadwork.

💡 **Key Takeaway:** Beading attaches decorative beads onto leather surfaces to enhance aesthetic appeal.""",

    8: """**Increase size of the theatre** alters the venue architecture, but does NOT give character to a puppet during a dramatic performance.

* **Why other options are incorrect:**
  * **Create a voice:** Modulating voice tone, pitch, and accent gives distinct personality to a puppet character.
  * **Make movements:** Manipulating puppet limbs and gestures expresses actions and emotions.
  * **Use different clothes and jewellery:** Costuming defines the role, status, and appearance of the puppet character.

💡 **Key Takeaway:** Puppeteers bring puppets to life using voice modulation, movement manipulation, and costume design.""",

    9: """Respecting intellectual property rights requires that one should **Seek permission from the artist** (or copyright owner) before using or reproducing their original artwork.

* **Why other options are incorrect:**
  * **Copy and trace the artwork:** Violates copyright laws and constitutes plagiarism.
  * **Edit the artwork and use it:** Modifying another person's art without authorization remains copyright infringement.
  * **Take a photograph when no one is watching:** Unauthorized photo capture for commercial or public use violates artistic copyright.

💡 **Key Takeaway:** Always seek formal permission from original creators to honor copyright and intellectual property rights.""",

    10: """For marketing art sales during an exhibition, **Join the school's art club** is an internal student activity, NOT a direct marketing strategy for selling artwork to customers.

* **Why other options are incorrect:**
  * **Post pictures of artwork on sale on social media:** An effective digital marketing strategy reaching a broad audience.
  * **Announce and invite the community for the exhibition:** A direct promotional strategy raising community awareness.
  * **Create posters to advertise sale of the artwork:** A traditional visual marketing technique attracting visitors.

💡 **Key Takeaway:** Effective marketing relies on advertising, public announcements, and outreach to reach potential buyers.""",

    11: """**Cheering** is an audience reaction or supportive gesture during a performance, NOT a structural component of a traditional folk dance itself.

* **Why other options are incorrect:**
  * **Costumes:** Essential attire reflecting the culture and context of the folk dance.
  * **Body movement:** The core physical dance steps, rhythm, and choreography.
  * **Songs:** The musical accompaniment and lyrics guiding the dance rhythm.

💡 **Key Takeaway:** Core folk dance components include songs, instruments, costumes, body movements, and props; audience cheering is an external reaction.""",

    12: """Folk songs and cultural performances should NEVER be **Performed using sharp props** because sharp objects pose severe physical injury risks to dancers and spectators.

* **Why other options are incorrect:**
  * **Performed observing safety:** A fundamental rule for executing any dance or stage activity safely.
  * **Performed observing good manners:** Essential for cultural respect, decorum, and positive community reception.
  * **Performed with coordinated body movements:** A core characteristic of rhythmic and harmonious group folk dancing.

💡 **Key Takeaway:** Stage safety requires substituting real sharp objects with safe, blunt, improvised props during performances.""",

    13: """**Singing while talking** disrupts vocal tone, breath control, rhythm, and diction, and is NOT a correct singing technique.

* **Why other options are incorrect:**
  * **Singing the tune accurately:** Essential for staying on pitch and producing harmonious music.
  * **Pronouncing the words clearly:** Diction ensures the audience understands the song lyrics.
  * **Using facial expressions:** Expresses emotion and communicates the song's meaning effectively.

💡 **Key Takeaway:** Proper vocal music execution requires clear diction, accurate pitch, breath control, and appropriate facial expression.""",

    14: """To construct a simple wind instrument (like a flute or recorder), learners require a **Hollow tube, knife, nails and ruler** to measure, mark, and craft finger holes accurately.

* **Why other options are incorrect:**
  * **Hollow tube, nails, feathers and knife:** Feathers are not used for structural wind instrument hole crafting or measurement.
  * **Hollow tube, wooden bars, paint and nails:** Wooden bars and paint are for xylophones or decoration, not crafting flute finger holes.
  * **Hollow tube, ruler, nails and feathers:** Missing a cutting tool (knife) needed to bore or shape tone holes.

💡 **Key Takeaway:** Making aerophones (wind instruments) requires measuring tools and cutting/boring tools to create precise tone holes.""",

    15: """After performing with a stringed instrument like a fiddle (wandindi), the player should **Hang it on the wall** (or store it in a dry case) to protect it from floor moisture, dirt, and accidental damage.

* **Why other options are incorrect:**
  * **Wash it with water:** Water warps wooden instrument bodies and ruins skin resonators and strings.
  * **Keep it outside under the sun:** Direct heat and sunlight dry out, crack, and warp wooden instruments.
  * **Put it on the floor:** Leaving instruments on the floor risks them being stepped on or damaged.

💡 **Key Takeaway:** Store wooden musical instruments by hanging them safely in dry, sheltered indoor areas or storing them in padded cases.""",

    16: """Rhythmic pattern **D** correctly matches the syllable counts, accents, and note values of the given text stanza.

* **Why other options are incorrect:**
  * **A:** Contains incorrect measure beat divisions that clash with the poetic meter.
  * **B:** Features mismatched note durations that warp the natural speech rhythm of the words.
  * **C:** Has incorrect rest placements disrupting the metric phrasing.

💡 **Key Takeaway:** Matching text to music requires aligning speech stresses and syllable counts with musical beat rhythms.""",

    17: """A lullaby is a gentle song sung to soothe infants to sleep, and should be sung **Slowly and softly**.

* **Why other options are incorrect:**
  * **Loudly and softly:** Loud vocal surges startle and awaken sleeping babies.
  * **Softly and sadly:** Lullabies are comforting and peaceful, not mournful or sad.
  * **Fast and softly:** Fast tempos excite and stimulate infants rather than calming them.

💡 **Key Takeaway:** Lullabies feature slow tempos, soft dynamics, and soothing melodies to induce peaceful sleep.""",

    18: """The correct sequence of practices when handling and maintaining a musical instrument is **(iii), (iv), (v) and (i)**: inspecting, tuning, playing carefully, and cleaning/storing safely.

* **Why other options are incorrect:**
  * **(vi), (iv), (ii) and (i):** Places storage or improper handling steps before basic tuning and care.
  * **(ii), (iii), (vi) and (i):** Disrupts logical maintenance order, compromising instrument longevity.
  * **(v), (vi), (iv) and (ii):** Starts with post-performance actions prior to setup.

💡 **Key Takeaway:** Proper instrument care follows a systematic routine: pre-check -> tuning -> careful usage -> cleaning and safe storage.""",

    19: """If a string instrument is out of tune or producing distorted pitch, the player **should tune the instrument** by adjusting string tension until correct pitch is achieved.

* **Why other options are incorrect:**
  * **He should clean the instrument:** Cleaning removes dust but does not adjust string pitch frequency.
  * **He should warm the instrument:** Warming applies to membrane drums (to tighten drumheads), not tuning string tension.
  * **He should get another instrument:** Unnecessary and wasteful when simple peg/string tuning resolves off-pitch sound.

💡 **Key Takeaway:** String instruments are tuned by tightening or loosening strings using tuning pegs or bridges.""",

    20: """Diagram (i) shows a string instrument (e.g., nyatiti/litungu) and (ii) shows a single-headed membrane drum. **Instrument (i) is tuned by adjusting knobs while instrument (ii) is tuned by warming** the leather drumhead over heat.

* **Why other options are incorrect:**
  * **Instrument (i) is played by bowing while instrument (ii) is played by hitting:** String instruments like litungu are plucked, not bowed like violins.
  * **Instrument (i) is a percussion instrument while instrument (ii) is a string instrument:** Reverses instrument classifications (i is chordophone, ii is membranophone).
  * **Instrument (i) cannot play a melody while instrument (ii) can play a melody:** String instruments play melodic tunes, while drums provide rhythmic beats.

💡 **Key Takeaway:** String instruments tune via pegs/knobs/bridge adjustments; traditional skin drums tune by warming over mild heat to tighten the membrane.""",

    21: """The standard basic elements of weather include **Wind, temperature, air pressure**, humidity, rainfall, and sunshine.

* **Why other options are incorrect:**
  * **Temperature, snow, rain:** Snow and rain are forms of precipitation (types of weather moisture), not separate primary weather elements.
  * **Sunshine, fog, temperature:** Fog is a condensed moisture condition (like cloud at ground level), not a core fundamental weather element.
  * **Temperature, snow, air pressure:** Includes snow (precipitation form) rather than core elements like wind or humidity.

💡 **Key Takeaway:** Main weather elements measured at meteorological stations include temperature, wind, atmospheric pressure, humidity, sunshine, and rainfall.""",

    22: """Diagram **C** correctly illustrates a major relief feature (such as a valley between mountain ranges or a plateau landform) observed during physical geography field studies.

* **Why other options are incorrect:**
  * **A:** Represents an artificial structure or incorrect landform contour.
  * **B:** Represents drainage or coastal features rather than inland relief terrain.
  * **D:** Shows climate vegetation zones rather than a physical relief landform elevation.

💡 **Key Takeaway:** Relief features in physical geography include mountains, hills, plateaus, plains, and valleys.""",

    23: """Compass direction orientation on standard maps places the top direction as **North**.

* **Why other options are incorrect:**
  * **South:** Located at the bottom of standard maps.
  * **East:** Located to the right side of standard maps.
  * **West:** Located to the left side of standard maps.

💡 **Key Takeaway:** Map convention always places North facing the top of map layouts unless indicated otherwise by a compass rose.""",

    24: """Tropical rainforest vegetation in Eastern Africa is primarily located in areas of high precipitation, such as the **Western region of Kenya** (e.g., Kakamega Forest) and around the Lake Victoria basin.

* **Why other options are incorrect:**
  * **Northern region of Sudan:** Characterized by arid desert and semi-desert conditions with very sparse rainfall.
  * **Northern region of Uganda:** Dominated by dry savanna grassland and acacia scrublands.
  * **Southern region of Tanzania:** Covered predominantly by Miombo woodland savanna.

💡 **Key Takeaway:** Kakamega Forest in Western Kenya is Eastern Africa's primary surviving remnant of the equatorial tropical rainforest belt.""",

    25: """Semi-desert climates (semi-arid zones) are characterized by low, erratic rainfall and **It experiences high temperatures** during daytime.

* **Why other options are incorrect:**
  * **It receives high rainfall:** False; semi-deserts receive low and unpredictable annual rainfall (below 500mm).
  * **It experiences high humidity:** False; semi-arid regions have low relative humidity and high evaporation rates.
  * **It receives rain in the afternoon:** Afternoon convectional rainfall is characteristic of humid equatorial climate zones, not semi-deserts.

💡 **Key Takeaway:** Semi-desert environments feature high daytime temperatures, low humidity, sparse vegetation, and low rainfall.""",

    26: """**Malka Mari** National Park is located in Mandera County in extreme northeastern Kenya along the Daua River.

* **Why other options are incorrect:**
  * **Sibiloi:** Located along the northeastern shores of Lake Turkana in Marsabit/Turkana counties.
  * **Amboseli:** Located at the foot of Mt. Kilimanjaro in Kajiado County.
  * **Kora:** Located in Tana River/Kitui counties along the Tana River basin.

💡 **Key Takeaway:** Malka Mari National Park is situated in Mandera County, known for its unique semi-arid biome and riverine scenery.""",

    27: """The **Maasai and Turkana** communities are both Plains Nilotes who migrated into Kenya from the north.

* **Why other options are incorrect:**
  * **Abagusii and Somali:** Abagusii are Bantus, while Somalis are Cushites.
  * **Luo and Akamba:** Luos are River-Lake Nilotes, while Akamba are Bantus.
  * **Nubians and Pokomo:** Pokomo are Bantus, while Nubians settled from Sudan.

💡 **Key Takeaway:** Nilotic language groups in Kenya comprise River-Lake Nilotes (Luo), Plains Nilotes (Maasai, Turkana, Samburu), and Highland Nilotes (Kalenjin).""",

    28: """Learning a traditional craft by observing an expert master and practicing under their guidance is called **Apprenticeship**.

* **Why other options are incorrect:**
  * **Narration:** Storytelling or verbal presentation of historical tales without practical hands-on craft practice.
  * **Discussion:** Verbal exchange of ideas in a group without physical skill execution.
  * **Riddles:** Word puzzles used to test wits and critical thinking, not practical pottery making.

💡 **Key Takeaway:** Traditional African education relied heavily on apprenticeship—learning practical skills through observation and hands-on practice.""",

    29: """Ensuring teachers report for duty early is an administrative managerial task of the Teachers Service Commission (TSC) and headteacher, **NOT** a function of the student **Children's Government**.

* **Why other options are incorrect:**
  * **It speaks on behalf of the learners to the school administration:** A primary student advocacy role of the Children's Government.
  * **It ensures that the learning environment is friendly:** Helps maintain peer discipline, cleanliness, and child-friendly activities.
  * **It assists teachers to ensure learners follow the school rules:** Promotes peer responsibility, order, and adherence to school codes.

💡 **Key Takeaway:** Children's Student Councils advocate for student welfare and peer discipline, but do not supervise teacher employment duties.""",

    30: """Under the Kenyan Constitution, citizenship acquired by registration can be revoked if it was obtained through **Using false documents**, fraud, or misrepresentation.

* **Why other options are incorrect:**
  * **Voting during the general election:** A fundamental constitutional right granted to all adult Kenyan citizens.
  * **Attending a local harambee meeting:** A normal civic community activity that does not breach citizenship laws.
  * **Joining a political party:** A guaranteed constitutional right of freedom of association.

💡 **Key Takeaway:** Citizenship by registration can be legally revoked if obtained fraudulently through false documentation or deception.""",

    31: """During educational tours inside national parks, visitors use a **Bus** (or tourist van) to observe wildlife safely while adhering to park conservation rules.

* **Why other options are incorrect:**
  * **Train:** Railway lines pass through designated corridors; trains do not transport tourists around internal game view tracks.
  * **Lorry:** Open cargo lorries are unsafe and prohibited for tourist game drives inside national parks.
  * **Motorcycles:** Bicycles and motorcycles are banned inside game parks due to severe predator attack risks.

💡 **Key Takeaway:** Enclosed tour buses and game-viewing vans provide safe transport for observing wildlife in national parks.""",

    32: """**Soils** are naturally occurring Earth materials (natural resources) found in the environment.

* **Why other options are incorrect:**
  * **Bottles:** Synthetic man-made manufactured objects made of glass or plastic.
  * **Tools:** Man-made fabricated implements (hammers, hoes) created from processed materials.
  * **Posters:** Printed paper items produced by humans for visual communication.

💡 **Key Takeaway:** Natural resources exist naturally in the environment (soil, water, minerals, plants, rocks), unlike man-made products.""",

    33: """Subsistence farming differs from small-scale farming because **small scale farmers grow cash crops and food crops while subsistence farmers grow food crops** primarily to feed their households.

* **Why other options are incorrect:**
  * **small scale farmers keep large herds of animals while subsistence farmers grow food crops:** Keeping large herds on vast land describes pastoralism or commercial ranching, not small-scale farming.
  * **subsistence farming is done on small farms while small scale farming is done on large farms.:** Both operate on relatively small land parcels; scale of commercial sale is the key distinction.
  * **subsistence farmers use simple tools while small scale farmers use machinery.:** Both often use hand tools or light equipment, but commercial intent sets them apart.

💡 **Key Takeaway:** Subsistence farming produces food primarily for family consumption, whereas small-scale farming produces both food and cash crops for market sale.""",

    34: """In African traditional society, a respected leader was expected to be a **courageous person** capable of defending the community, making tough decisions, and upholding justice.

* **Why other options are incorrect:**
  * **good dancer:** Entertainment skills like dancing do not define political or community leadership qualities.
  * **prophet:** While religious seers existed, traditional community leaders were evaluated on bravery, wisdom, and justice rather than prophetic roles alone.
  * **storyteller:** Oral performance skill does not replace core leadership attributes like courage and wisdom.

💡 **Key Takeaway:** Traditional African leadership prioritized courage, wisdom, integrity, fairness, and defense of the community.""",

    35: """**Language** (such as Kiswahili) is a national unifying medium, but it is NOT one of the official constitutional **symbols of national unity**. The official national symbols specified in the Constitution are the National Flag, National Anthem, Coat of Arms, and Public Seal.

* **Why other options are incorrect:**
  * **Flag:** The National Flag is an official symbol of national unity prescribed in the Constitution.
  * **National Anthem:** An official constitutional symbol of national identity and unity.
  * **Public seal:** The official seal of the Republic of Kenya, mandated by the Constitution as a national symbol.

💡 **Key Takeaway:** Kenya's constitutional symbols of national unity are: 1. National Flag, 2. National Anthem, 3. Coat of Arms, 4. Public Seal."""
}

file_path = 'src/data/kpsea-sst-parta-2023.js'
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

print("Successfully updated all 35 explanations in Social Studies Part A!")
