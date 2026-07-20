import json

# Define the exact text replacements using literal '\\n'
replacements = {
    # 1. Dialogue (Leni/Kibo)
    r'"text": "(Ni jioni. Leni na Kibo wamekutana mtoni. Ni msimu wa kiangazi.)\nLeni: (Akitabasamu.) Bingwa, hujambo? Ha! Ha! Ha! Umejitwika mtungi kichwani kutafuta maji!\nKibo: (Akionyesha kukasirika.) Sijambo, lakini mimi si bingwa. Ubingwa gani na hata tone la maji sina?\nLeni: Samahani kaka. Sikudhani unaweza kukosa maji. Ajabu! Matangi yako makubwa yamekauka?\nKibo: Bila shaka. Unavyoona kiangazi kimetuathiri sisi sote. Hali ya anga isipobadilika tutaangamia.\nLeni: (Akionyesha kuhuzunika.) Ni kweli unavyosema mwenzangu. Lakini hiyo anga itabadilikaje ilhali miti inakatwa ovyo?\nKibo: Ipo haja ya sisi kushirikiana ili kutunza na kuhifadhi mazingira yetu. Kumbuka tusipoziba ufa...\nLeni: (Akikubaliana naye.) Tutajenga ukuta. Nasikitika hali hii ikiendelea tutakosa chakula. Wanyama na ndege nao watakosa makao.\nKibo: Mwandani wangu, hakika utunzi wa mazingira ni wajibu wetu.\nLeni: Kweli kabisa. (Wanaagana na kuondoka)"': 
    r'"text": "(Ni jioni. Leni na Kibo wamekutana mtoni. Ni msimu wa kiangazi.)\n\n**Leni:** (Akitabasamu.) Bingwa, hujambo? Ha! Ha! Ha! Umejitwika mtungi kichwani kutafuta maji!\n\n**Kibo:** (Akionyesha kukasirika.) Sijambo, lakini mimi si bingwa. Ubingwa gani na hata tone la maji sina?\n\n**Leni:** Samahani kaka. Sikudhani unaweza kukosa maji. Ajabu! Matangi yako makubwa yamekauka?\n\n**Kibo:** Bila shaka. Unavyoona kiangazi kimetuathiri sisi sote. Hali ya anga isipobadilika tutaangamia.\n\n**Leni:** (Akionyesha kuhuzunika.) Ni kweli unavyosema mwenzangu. Lakini hiyo anga itabadilikaje ilhali miti inakatwa ovyo?\n\n**Kibo:** Ipo haja ya sisi kushirikiana ili kutunza na kuhifadhi mazingira yetu. Kumbuka tusipoziba ufa...\n\n**Leni:** (Akikubaliana naye.) Tutajenga ukuta. Nasikitika hali hii ikiendelea tutakosa chakula. Wanyama na ndege nao watakosa makao.\n\n**Kibo:** Mwandani wangu, hakika utunzi wa mazingira ni wajibu wetu.\n\n**Leni:** Kweli kabisa. (Wanaagana na kuondoka)"',

    # 2. Ushuru passage
    r'"text": "Ushuru ni malipo yanayotozwa na serikali kama ada ya kuingiza bidhaa ndani ya nchi au kuziuza nje ya nchi. Pia, ni ada inayotozwa raia kwa kuuza au kununua huduma mbalimbali. Nchi yetu hutegemea ushuru ambao wananchi hutozwa ili kuendesha shughuli zake.\nShirika lenye jukumu la kukusanya ushuru nchini Kenya ni Halmashauri ya Ukusanyaji Ushuru almaarufu KRA. Shirika hili limepewa mamlaka ya kikatiba kukusanya aina zote za ushuru: ushuru wa mapato, ushuru wa forodhani, ushuru kutokana na shughuli za kitalii na nyinginezo.\nSerikali huandaa bajeti kila mwaka ili kuhakikisha matumizi yafaayo ya fedha. Bajeti huwa na makadirio ya mapato na mgao wa fedha kwa matumizi mbalimbali. Makadirio hayo husomwa bungeni na Waziri wa Hazina ya Kitaifa kisha kuidhinishwa.\nNi wajibu wa kila mwananchi kulipa ushuru ili taifa letu liweze kujitegemea. Tukifanya hivyo, tutaweza kupiga hatua kimaendeleo. Tutakuwa na miundomsingi bora, huduma nzuri za kimsingi kama vile afya na elimu na hata nafasi zaidi za ajira."':
    r'"text": "Ushuru ni malipo yanayotozwa na serikali kama ada ya kuingiza bidhaa ndani ya nchi au kuziuza nje ya nchi. Pia, ni ada inayotozwa raia kwa kuuza au kununua huduma mbalimbali. Nchi yetu hutegemea ushuru ambao wananchi hutozwa ili kuendesha shughuli zake.\n\nShirika lenye jukumu la kukusanya ushuru nchini Kenya ni Halmashauri ya Ukusanyaji Ushuru almaarufu KRA. Shirika hili limepewa mamlaka ya kikatiba kukusanya aina zote za ushuru: ushuru wa mapato, ushuru wa forodhani, ushuru kutokana na shughuli za kitalii na nyinginezo.\n\nSerikali huandaa bajeti kila mwaka ili kuhakikisha matumizi yafaayo ya fedha. Bajeti huwa na makadirio ya mapato na mgao wa fedha kwa matumizi mbalimbali. Makadirio hayo husomwa bungeni na Waziri wa Hazina ya Kitaifa kisha **kuidhinishwa**.\n\nNi wajibu wa kila mwananchi kulipa ushuru ili taifa letu liweze kujitegemea. Tukifanya hivyo, tutaweza kupiga hatua kimaendeleo. Tutakuwa na miundomsingi bora, huduma nzuri za kimsingi kama vile afya na elimu na hata nafasi zaidi za ajira."',

    # 3. Mifugo passage
    r'"text": "Likizo iliyopita nilitumia muda wangu wa mapumziko kumsaidia mlezi wangu kuwatunza mifugo wetu. Jambo hilo lilimfurahisha sana mlezi wangu akanizawidi ndama wa kike. Nilimpa ndama wangu jina, Simati.\nNilijitolea kwa hali na mali kumtunza Simati. Anapendeza kwa rangi yake nyeupe na madoa meusi. Matarajio yangu ni kwamba siku za usoni atapata ndama wake. Wakati huo utakapofika, nitamkama maziwa.\nMaziwa nitakayoyapata nitayagawa kwa matumizi ya nyumbani na mengine nitayauza kwa usaidizi wa mlezi wangu. Hela nitakazopata kutokana na mauzo ya maziwa hayo, nitaziweka kama akiba kwani akiba haiozi."':
    r'"text": "Likizo iliyopita nilitumia muda wangu wa mapumziko kumsaidia mlezi wangu **kuwatunza** mifugo wetu. Jambo hilo lilimfurahisha sana mlezi wangu akanizawidi ndama wa kike. Nilimpa ndama wangu jina, Simati.\n\nNilijitolea kwa hali na mali kumtunza Simati. Anapendeza kwa rangi yake nyeupe na madoa meusi. Matarajio yangu ni kwamba siku za usoni atapata ndama wake. Wakati huo utakapofika, nitamkama maziwa.\n\nMaziwa nitakayoyapata nitayagawa kwa matumizi ya nyumbani na mengine nitayauza kwa usaidizi wa mlezi wangu. Hela nitakazopata kutokana na mauzo ya maziwa hayo, nitaziweka kama akiba kwani akiba haiozi."'
}

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

changes_made = 0
for old, new in replacements.items():
    # Convert literal '\n' in the old string to literal '\\n' which is what is in the file
    old_escaped = old.replace('\n', '\\n')
    new_escaped = new.replace('\n', '\\n')
    
    if old_escaped in content:
        content = content.replace(old_escaped, new_escaped)
        changes_made += 1
    else:
        print(f"Could not find block starting with: {old_escaped[:50]}...")

if changes_made > 0:
    with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Applied {changes_made} formatting replacements using escaped backslashes.")
else:
    print("No changes were made. Check if the strings match exactly.")
