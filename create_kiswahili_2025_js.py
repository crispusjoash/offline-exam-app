import json

data = {
  "id": "kpsea-kiswahili-2025",
  "title": "KPSEA 2025 Kiswahili",
  "subject": "Kiswahili",
  "year": "2025",
  "durationMinutes": 60,
  "timeAllowed": 60,
  "sharedContexts": {
    "ctx-kis-2025-q1-5": {
      "title": "Swali la 1 hadi la 5\nSoma mazungumzo yafuatayo kisha ujibu maswali.",
      "type": "text",
      "text": "(Ni jioni, shuleni. Maria ameketi kwenye fomu akisoma hadithi. Sara, rafikiye, anamjia kwa kunyatia.)\n\n**Sara:** (Baada ya kumwamkua.) Maria, ni hadithi gani hiyo ambayo imeyateka nyara mawazo yako mpaka huoni mvua ikija?\n\n**Maria:** (Akitabasamu.) Hata si hadithi. Ni yaliyomo katika hadithi yenyewe. Yanakuvuta tu bila kutaka.\n\n**Sara:** (Akimakinika zaidi.) Kwani inahusu nini?\n\n**Maria:** Inahusu jinsi urafiki wa Kuku na Mwewe ulivyofikia kikomo. (Akicheka.) Ni hali ya kusisimua na hapo hapo kuhuzunisha.\n\n**Sara:** (Akikubaliana naye.) Ahaa! Sasa naelewa sababu ya kuzama huko hadithini. Hata mimi ningependa kuisoma ila naona mvua ya masika inatishia kuanguka. Ni muhimu tuondoke.\n\n**Maria:** Kumbe! Sikuwa nimeona dalili ya mvua. Kweli, tunaweza kuondoka."
    },
    "ctx-kis-2025-q6-9": {
      "title": "Swali la 6 hadi la 9\nSoma kifungu kifuatacho kisha ujibu maswali.",
      "type": "text",
      "text": "Daudi alipenda sana kucheza kandanda. Kila alipouona mchezo huo ukichezwa karibu naye alifululiza hadi pahali hapo na kuomba kushirikishwa. Wakati mwingine alijitengenezea mpira kwa vitambaa vikuukuu na kuwaita wenzake wacheze pamoja.\n\nSiku moja, Daudi alitumwa dukani kununua mkate na pakiti ya maziwa. Alipokuwa akirudi nyumbani, aliona marafiki wake wakicheza kandanda karibu na nyumbani kwao. Ghafla, kiu yake ya kandanda iliamka, akasahau mfuko wa bidhaa aliokuwa amebeba na kujitoma katika mchezo. Yeye na wenzake walizama katika kusakata gozi. Hakuna aliyemwona paka akinyemelea mfuko ambao Daudi alikuwa ameuweka karibu na lango.\n\nDaudi hakujua vipi, lakini baada ya muda, moyo ulimwambia autazame ule mfuko. Lo! Alimwona paka mkubwa ameining'iniza pakiti ya maziwa mdomoni. Daudi **alitoka shoti** kumfuata paka. Hata alipomfikia, pakiti ilikuwa tupu! Paka alikuwa amekamilisha kazi yake."
    },
    "ctx-kis-2025-q10-12": {
      "title": "Swali la 10 hadi la 12\nSoma kifungu kifuatacho kisha ujibu maswali.",
      "type": "image",
      "imagePath": "/assets/kiswahili_2025_table_10_12.svg",
      "text": "Yusuf, Ali, Amina na Pendo **huzingatia** lishe bora. Pamoja na kula vyakula vyenye wanga na protini, wao hula mboga na matunda ili kupata vitamini. Jedwali lifuatalo linaonyesha matunda ambayo kila mmoja anakula kwa siku nne zilizoonyeshwa."
    },
    "ctx-kis-2025-q13-15": {
      "title": "Swali la 13 hadi la 15\nSoma kifungu kifuatacho kisha ujibu maswali.",
      "type": "text",
      "text": "Baharini na maziwani mnaishi aina za samaki na wanyama wengine wengi. Wanyama hao wa majini wana umuhimu mkubwa kwa maisha ya binadamu kwa jumla. Kuna wale wanaotumiwa kama chakula, wanaosawazisha mazingira na hata wanaopamba dunia tu. Kuna aina kadha za wanyama wa majini kama vile papa, nyangumi, dagaa na kambare. Bila kuwepo kwao binadamu atanyimwa sio tu chakula chenye madini bali pia burudani inayotokana na mienendo ya wanyama hao wawapo majini.\n\nBaadhi ya wanyama wa majini ni wa ajabu. Mmoja wao ni papa. Papa anasemekana kwamba ndiye samaki mkubwa zaidi ulimwenguni. Ana ngozi ngumu, meno makubwa na hula watu! Wasemao husema ukistaajabu ya Musa utayaona ya Firauni. Ikiwa umeshangazwa na ya papa kuwala watu, sikiliza ya nyangumi. Nyangumi ni mwenye kimo kikubwa. **Utafiti** unaonyesha kwamba anaweza kuwa na urefu wa futi tisini na uzani wa kilo elfu mia moja na hamsini. Nyangumi hunyonyesha vikembe vyake. Mataifa yanafaa, kuhakikisha kwamba uhai wa baharini unatunzwa kabla mambo yaende segemnege."
    },
    "ctx-kis-2025-q16-20": {
      "title": "Swali la 16 hadi la 20\nSoma kifungu kifuatacho. Kina nafasi 16 hadi 20. Umepewa majibu manne. Chagua jibu lifaalo zaidi kati ya yale uliyopewa.",
      "type": "text",
      "text": "Nyumbani kwetu ----16---- miti ya kila aina. Kuna ----17---- inayotupatia kivuli. Mingine ----18---- mazingira ----19---- mingine inatufaa kwa dawa za magonjwa mbalimbali. Ni vyema sote ----20---- ili kuhifadhi miti."
    },
    "ctx-kis-2025-q21-30": {
      "title": "Swali la 21 hadi la 30\nKutoka swali la 21 hadi la 30, chagua jibu sahihi.",
      "type": "text",
      "text": ""
    }
  },
  "sectionA": [
    {
      "id": "q1",
      "questionNumber": 1,
      "questionText": "Kauli, **'Baada ya kumwamkua'** imetumiwa katika mazungumzo. Unadhani Sara alitumia neno lipi kumwamkua Maria?",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q1-5",
      "options": [
        { "text": "Chewa", "isCorrect": False },
        { "text": "Shikamoo", "isCorrect": False },
        { "text": "Masalheri", "isCorrect": True },
        { "text": "Hamjambo", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Masalheri**.\n\n**Uchambuzi wa Jibu Sahihi:**\nMazungumzo haya yanafanyika *jioni*. Maamkuzi maalum ya jioni katika Kiswahili ni \"Masalheri\" (au \"Masaalkheri\"). Kwa kuwa wao ni marafiki wanaosoma pamoja, haya ni maamkuzi mwafaka.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Shikamoo:** Haya ni maamkuzi ya kumpa heshima mtu mzima au mzee, sio rafiki wa rika lako.\n- **Hamjambo:** Haya ni maamkuzi ya kuuliza watu wengi (wingi), lakini Sara alikuwa anamsalimia Maria peke yake (Hujambo).\n- **Chewa:** Hili si neno la maamkuzi sanifu ya jioni katika muktadha huu.\n\n📌 **Kidokezo cha Kujifunza:**\nMaamkuzi ya jioni ni **Masalheri** na hujibiwa **Masalheri** (au akheraheri), ilhali ya asubuhi ni **Sabalkheri**."
    },
    {
      "id": "q2",
      "questionNumber": 2,
      "questionText": "Sara anakubaliana na Maria kwa kusema, \"Ahaa!\" Sara alitumia ishara gani kuonyesha hali hii?",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q1-5",
      "options": [
        { "text": "Alitikisa kichwa.", "isCorrect": True },
        { "text": "Alimpungia mkono.", "isCorrect": False },
        { "text": "Alimkazia macho.", "isCorrect": False },
        { "text": "Alimpigia makofi.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Alitikisa kichwa**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKatika mawasiliano ya ishara, kutikisa au kutingisha kichwa (hasa kuelekeza chini na juu) ni ishara ya kukubaliana na jambo au kuonyesha kwamba umeelewa (kama kusema \"ndiyo\"). Hii inalingana na mshangao wa kuelewa \"Ahaa!\".\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Alimpungia mkono:** Hii ni ishara ya kuaga (kwaheri) au kuita.\n- **Alimkazia macho:** Hii ni ishara ya mshangao mkubwa, hasira, au kutaka kumtisha mtu.\n- **Alimpigia makofi:** Hii ni ishara ya kupongeza au kushangilia, sio tu kuonyesha kuelewa na kukubaliana.\n\n📌 **Kidokezo cha Kujifunza:**\nKutikisa au kutingisha kichwa ni ishara ya **kukubali** au **kuelewa** kile kinachosemwa."
    },
    {
      "id": "q3",
      "questionNumber": 3,
      "questionText": "Mwishoni mwa mazungumzo, Maria na Sara wanaondoka. Sara angetumia neno lipi kumuaga Maria?",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q1-5",
      "options": [
        { "text": "Alamsiki", "isCorrect": False },
        { "text": "Mchana mwema", "isCorrect": False },
        { "text": "Baki salama", "isCorrect": False },
        { "text": "Kwaheri", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **Kwaheri**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNeno la kawaida na mwafaka la kuagana wakati wowote ni \"Kwaheri\". Wanafunzi hawa wanaondoka kurudi nyumbani.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Alamsiki:** Hili hutumika wakati wa kuagana *usiku* mtu akienda kulala (linamaanisha Mungu akulaze salama).\n- **Mchana mwema:** Mazungumzo haya yanafanyika jioni, siyo mchana.\n- **Baki salama:** Hili huambiwa mtu anayebaki mahali wakati wewe unaondoka, lakini hapa *wote wawili* wanaondoka pamoja.\n\n📌 **Kidokezo cha Kujifunza:**\n**Kwaheri** ni neno la kuaga linalotumika wakati wowote. **Alamsiki** linatumika usiku tu."
    },
    {
      "id": "q4",
      "questionNumber": 4,
      "questionText": "'Ni muhimu tuondoke.' Sara angetumia maneno mengine yepi yenye adabu?",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q1-5",
      "options": [
        { "text": "Utasimama twende?", "isCorrect": False },
        { "text": "Hebu simama.", "isCorrect": False },
        { "text": "Bado umeketi?", "isCorrect": False },
        { "text": "Inafaa twende.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **Inafaa twende**.\n\n**Uchambuzi wa Jibu Sahihi:**\n\"Inafaa twende\" ni kauli yenye adabu inayoonyesha pendekezo nzuri kwamba ni wakati wa wao kuondoka, sawa na kusema \"Ni muhimu tuondoke\".\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Utasimama twende? / Bado umeketi?:** Kauli hizi zinasikika kama maswali ya dharau au lawama.\n- **Hebu simama:** Hii ni amri (command) inayokosa adabu kwa rafiki.\n\n📌 **Kidokezo cha Kujifunza:**\nKutumia maneno kama **inafaa** au **ni vyema** hufanya sentensi iwe na adabu na heshima kuliko kutoa amri."
    },
    {
      "id": "q5",
      "questionNumber": 5,
      "questionText": "Sara anamtahadharisha Maria kwamba mvua inakaribia kunyesha. Maria anastahili kumwambia nini Sara?",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q1-5",
      "options": [
        { "text": "Kunradhi", "isCorrect": False },
        { "text": "Asante", "isCorrect": True },
        { "text": "Tafadhali", "isCorrect": False },
        { "text": "Simile", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Asante**.\n\n**Uchambuzi wa Jibu Sahihi:**\nSara amemfanyia Maria jambo zuri kwa kumtahadharisha (kumkumbusha) kuhusu mvua ambayo Maria hakuiona. Neno sahihi la kuonyesha shukrani kwa onyo au msaada wowote ni \"Asante\".\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Kunradhi:** Hutumika kuomba msamaha (samahani) unapotatiza au kukosea.\n- **Tafadhali:** Hutumika unapoanza kuomba usaidizi.\n- **Simile:** Hutumika kumuomba mtu akupishe njia ili upite.\n\n📌 **Kidokezo cha Kujifunza:**\nMtu anapokupa tahadhari nzuri ili ukwepe shida (kama mvua), unapaswa kumshukuru kwa kusema **Asante**."
    },
    {
      "id": "q6",
      "questionNumber": 6,
      "questionText": "Kulingana na aya ya kwanza, Daudi",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q6-9",
      "options": [
        { "text": "alipenda kuchezea mpira karibu na kwao.", "isCorrect": False },
        { "text": "alifurahia kutazama mechi ya kandanda ikiendelea.", "isCorrect": False },
        { "text": "aliwauliza wengine wamshirikishe katika kandanda.", "isCorrect": True },
        { "text": "aliwashauri wenzake watumie mpira wa vitambaa vikuukuu.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **aliwauliza wengine wamshirikishe katika kandanda.**\n\n**Uchambuzi wa Jibu Sahihi:**\nAya ya kwanza inasema: \"Kila alipouona mchezo huo... alifululiza hadi pahali hapo na kuomba kushirikishwa.\" Kuomba kushirikishwa maana yake ni kuwauliza wengine wamruhusu acheze pamoja nao.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Kutazama mechi:** Yeye hakutaka kutazama tu, alitaka *kucheza* na kushirikishwa.\n- **Kuwashauri wenzake:** Hakuna mahali aya inasema aliwashauri wengine jinsi ya kutengeneza mpira; yeye mwenyewe ndiye aliyekuwa akijitengenezea mpira wake.\n\n📌 **Kidokezo cha Kujifunza:**\nKushirikishwa inamaanisha kukubaliwa kujiunga na kundi kufanya jambo pamoja."
    },
    {
      "id": "q7",
      "questionNumber": 7,
      "questionText": "Daudi ni mbunifu kwa kuwa",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q6-9",
      "options": [
        { "text": "anang'amua kwamba alikuwa na mfuko.", "isCorrect": False },
        { "text": "anacheza kandanda na wenzake nyumbani.", "isCorrect": False },
        { "text": "anamfuata paka kuokoa maziwa.", "isCorrect": False },
        { "text": "anajiundia vifaa vya kuchezea.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **anajiundia vifaa vya kuchezea.**\n\n**Uchambuzi wa Jibu Sahihi:**\nMtu mbunifu ni mtu mwenye uwezo wa kutumia akili kubuni au kutengeneza kitu kipya. Aya ya kwanza inasema, \"alijitengenezea mpira kwa vitambaa vikuukuu\". Huku kujitengenezea mpira wake ndiko kunakomfanya awe mbunifu.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Kucheza kandanda, kukumbuka mfuko, au kumkimbiza paka ni matendo ya kawaida na hayahitaji ubunifu (creativity).\n\n📌 **Kidokezo cha Kujifunza:**\n**Ubunifu** ni kutumia akili na ujuzi kuunda au kutengeneza vitu kutokana na yale uliyo nayo."
    },
    {
      "id": "q8",
      "questionNumber": 8,
      "questionText": "Daudi alifika nyumbani bila pakiti ya maziwa. Huenda alifanya mambo yafuatayo, isipokuwa:",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q6-9",
      "options": [
        { "text": "alisimulia kuhusu mchezo wa kandanda.", "isCorrect": True },
        { "text": "aliomba msamaha kwa kosa alilofanya.", "isCorrect": False },
        { "text": "alilia kwa kujutia aliyofanya.", "isCorrect": False },
        { "text": "aliahidi kuwa makini zaidi.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **alisimulia kuhusu mchezo wa kandanda.**\n\n**Uchambuzi wa Jibu Sahihi:**\nSwali linauliza ni jambo gani Daudi *hangefanya* (isipokuwa). Daudi amepoteza maziwa aliyotumwa kununua. Kwa hivyo, atakapofika nyumbani atakuwa na hofu na hatia. Hangeanza kusimulia kwa furaha jinsi mchezo wa kandanda ulivyokuwa.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Mtu anapokosa (kama kupoteza maziwa kwa uzembe wake), anatarajiwa kuomba msamaha, kulia kwa majuto, na kuahidi kuwa makini (angalifu) zaidi. Haya ndiyo mambo ambayo angeyafanya.\n\n📌 **Kidokezo cha Kujifunza:**\nNeno **isipokuwa** linamaanisha unatafuta jambo ambalo **siyo** la kawaida au **halikutokea** katika hali hiyo."
    },
    {
      "id": "q9",
      "questionNumber": 9,
      "questionText": "Maana ya **'alitoka shoti'** ni",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q6-9",
      "options": [
        { "text": "aliweka mpira chini.", "isCorrect": False },
        { "text": "aliwaaga wenzake.", "isCorrect": False },
        { "text": "aliondoka haraka.", "isCorrect": True },
        { "text": "aliuchukua mfuko wake.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **aliondoka haraka**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNahau \"kutoka shoti\" inamaanisha kukimbia kwa kasi sana au kuondoka kwa haraka (kama farasi anayepiga shoti). Daudi alimkimbiza paka kwa haraka sana ili kuokoa maziwa yake.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Nahau hii haihusiani na kuweka mpira chini, kuaga, au kubeba mfuko. Inaangazia *mwendo wa kasi* (kasi ya kukimbia).\n\n📌 **Kidokezo cha Kujifunza:**\n**Kutoka shoti** au **kupiga shoti** ni maneno yanayotumiwa kueleza mtu anayekimbia haraka sana."
    },
    {
      "id": "q10",
      "questionNumber": 10,
      "questionText": "Ni matunda gani ambayo yanaliwa siku mbili tu?",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q10-12",
      "options": [
        { "text": "papai, zabibu", "isCorrect": False },
        { "text": "papai, embe", "isCorrect": True },
        { "text": "tufaha, papai", "isCorrect": False },
        { "text": "tikitimaji, pera", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **papai, embe**.\n\n**Uchambuzi wa Jibu Sahihi:**\nTukiangalia jedwali kujua ni *siku ngapi* kila tunda lililiwa (bila kujali ni nani alikula):\n- **Papai** lililiwa siku mbili: Jumatatu na Jumanne.\n- **Embe** lililiwa siku mbili: Jumatatu na Alhamisi.\nKwa hivyo, matunda yaliyoliwa siku mbili tu ni papai na embe.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Zabibu, pera, tikitimaji:** Matunda haya yaliliwa kwa siku tatu tofauti (Jumatatu, Jumatano, Alhamisi n.k.).\n- **Tufaha:** Lililiwa siku moja tu (Jumanne).\n\n📌 **Kidokezo cha Kujifunza:**\nChunguza kila tunda kwenye jedwali kuanzia Jumatatu hadi Alhamisi na uhesabu ni siku ngapi jina lake limeonekana."
    },
    {
      "id": "q11",
      "questionNumber": 11,
      "questionText": "Baadhi ya matunda yanaliwa mara nyingi kuliko mengine. Unadhani kwa nini hali ikawa hivyo?",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q10-12",
      "options": [
        { "text": "yanapatikana kwa wingi, yana bei nafuu.", "isCorrect": True },
        { "text": "yana rangi ya kuvutia, yanaiva haraka.", "isCorrect": False },
        { "text": "yanapendwa na wengi, ni makubwa.", "isCorrect": False },
        { "text": "yanastahimili kiangazi, ni matamu.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **yanapatikana kwa wingi, yana bei nafuu.**\n\n**Uchambuzi wa Jibu Sahihi:**\nKwa kawaida, vyakula (kama matunda) vinavyoliwa mara nyingi na watu mbalimbali huwa ni vile vinavyopatikana kwa urahisi (wingi) sokoni na vinauzwa kwa bei inayomudu kila mtu (bei nafuu).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Rangi kuvutia, ukubwa, au kustahimili kiangazi ni sifa za matunda, lakini siyo sababu kuu inayofanya watu wayanunue na kuyala *kila mara*. Upatikanaji na gharama (bei) ndio huathiri matumizi ya kila siku.\n\n📌 **Kidokezo cha Kujifunza:**\nVitu vinavyotumiwa sana katika jamii mara nyingi huwa ni rahisi kupatikana na vina bei inayowezekana (nafuu)."
    },
    {
      "id": "q12",
      "questionNumber": 12,
      "questionText": "Maana ya **huzingatia** ni",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q10-12",
      "options": [
        { "text": "hutofautisha vyema.", "isCorrect": False },
        { "text": "hufurahi kuona.", "isCorrect": False },
        { "text": "hueleza waziwazi.", "isCorrect": False },
        { "text": "hutilia maanani.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **hutilia maanani**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKuzingatia maana yake ni kuweka nia, kutilia maanani, au kujali sana jambo fulani. Wanaposema \"Wanafunzi huzingatia lishe bora\", inamaanisha wanatilia maanani (make a conscious effort) kula chakula chenye afya.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Hutofautisha vyema:** Hii inamaanisha kupambanua (differentiate).\n- **Hueleza waziwazi:** Hii inamaanisha kufafanua (explain clearly).\n\n📌 **Kidokezo cha Kujifunza:**\nManeno **kuzingatia** na **kutilia maanani** yana maana sawa ya kulipa jambo umuhimu au uangalifu."
    },
    {
      "id": "q13",
      "questionNumber": 13,
      "questionText": "Kulingana na aya ya kwanza, wanyama wana umuhimu ufuatao isipokuwa",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q13-15",
      "options": [
        { "text": "kuwa lishe kwa binadamu.", "isCorrect": False },
        { "text": "kufanya dunia ipendeze.", "isCorrect": False },
        { "text": "kufanya mazingira iwe sawa.", "isCorrect": False },
        { "text": "kuwala wanyama wengine.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **kuwala wanyama wengine**.\n\n**Uchambuzi wa Jibu Sahihi:**\nAya ya kwanza inaeleza umuhimu huu: kutumiwa kama chakula (lishe), kusawazisha mazingira (kufanya mazingira yawe sawa), na kupamba dunia (kufanya dunia ipendeze). Kuwala wanyama wengine hakutajwi kama \"umuhimu kwa maisha ya binadamu\" katika aya ya kwanza.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Majibu haya yote yametajwa katika aya kama faida za wanyama wa majini, kwa hivyo siyo jibu sahihi unapotafuta lile lililo *isipokuwa*.\n\n📌 **Kidokezo cha Kujifunza:**\nSwali lenye neno **isipokuwa** linakutaka uchague jambo ambalo **halipo** katika orodha iliyotolewa kwenye kifungu."
    },
    {
      "id": "q14",
      "questionNumber": 14,
      "questionText": "Ni kauli ipi katika kifungu inayoonyesha kwamba baadhi ya tabia za nyangumi ni sawa na za mwanadamu?",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q13-15",
      "options": [
        { "text": "Nyangumi ni mwenye kimo kikubwa.", "isCorrect": False },
        { "text": "Nyangumi hunyonyesha vikembe vyake.", "isCorrect": True },
        { "text": "Anaweza kuwa na urefu wa futi tisini.", "isCorrect": False },
        { "text": "Ana uzani wa kilo elfu mia moja na hamsini.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Nyangumi hunyonyesha vikembe vyake**.\n\n**Uchambuzi wa Jibu Sahihi:**\nBinadamu ni katika kundi la mamalia (wanyama wanaonyonyesha watoto wao). Nyangumi pia hunyonyesha vikembe (watoto) vyake kama mwanadamu.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Kimo kikubwa, urefu wa futi tisini, na uzani wa kilo elfu mia moja na hamsini ni sifa za kipekee za nyangumi ambazo ni tofauti kabisa na za binadamu.\n\n📌 **Kidokezo cha Kujifunza:**\nNyangumi (whale) si samaki, ni **mamalia wa majini** (marine mammal) na anazaa na kunyonyesha sawa na binadamu."
    },
    {
      "id": "q15",
      "questionNumber": 15,
      "questionText": "Kulingana na kifungu, neno lingine lenye maana sawa na **utafiti** ni",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q13-15",
      "options": [
        { "text": "uvumbuzi.", "isCorrect": False },
        { "text": "utatuzi.", "isCorrect": False },
        { "text": "uchunguzi.", "isCorrect": True },
        { "text": "ugunduzi.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **uchunguzi**.\n\n**Uchambuzi wa Jibu Sahihi:**\nUtafiti ni kitendo cha kusaka habari kwa kina au kuchunguza jambo ili kupata ukweli. Kwa hivyo, uchunguzi una maana sawa na utafiti.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Uvumbuzi:** Ni kutengeneza au kubuni kitu kipya ambacho hakikuwepo.\n- **Ugunduzi:** Ni kupata kitu ambacho kilikuwepo lakini kilikuwa hakijulikani.\n- **Utatuzi:** Ni kupata majibu au njia ya kumaliza tatizo (solving a problem).\n\n📌 **Kidokezo cha Kujifunza:**\nManeno **utafiti** (research) na **uchunguzi** (investigation) huambatana kwani yote yanahusisha kutafuta maarifa zaidi."
    },
    {
      "id": "q16",
      "questionNumber": 16,
      "questionText": "Nyumbani kwetu ----16---- miti ya kila aina.",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q16-20",
      "options": [
        { "text": "tungepanda", "isCorrect": False },
        { "text": "tutapanda", "isCorrect": False },
        { "text": "tukipanda", "isCorrect": False },
        { "text": "tumepanda", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **tumepanda**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKifungu kinasimulia mambo ambayo tayari yapo na yanaendelea kuonekana nyumbani (Kuna miti, mingine inatupatia...). Hali hii inaonyesha kwamba kitendo cha kupanda kilishafanyika na matokeo yake yapo. Kwa hivyo, \"tumepanda\" (wakati uliopo mkamilifu) ndio sahihi: \"Nyumbani kwetu tumepanda miti...\"\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **tungepanda:** Hali ya masharti ambayo haikutimia.\n- **tutapanda:** Wakati ujao (lakini miti tayari ipo).\n- **tukipanda:** Hali ya masharti ya wakati huu (if we plant).\n\n📌 **Kidokezo cha Kujifunza:**\nKiambishi **-me-** huonyesha tendo ambalo limeshafanyika lakini matokeo yake bado yanaonekana."
    },
    {
      "id": "q17",
      "questionNumber": 17,
      "questionText": "Kuna ----17---- inayotupatia kivuli.",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q16-20",
      "options": [
        { "text": "ile", "isCorrect": True },
        { "text": "yale", "isCorrect": False },
        { "text": "zile", "isCorrect": False },
        { "text": "pale", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **ile**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNeno linalokosekana linarejelea nomino \"miti\". Neno mti lipo katika ngeli ya U-I. Katika wingi, miti inachukua viashiria vya ngeli ya 'I' (miti *hii*, miti *ile*). Sentensi inapaswa kuwa: \"Kuna **ile** inayotupatia kivuli.\"\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **yale:** Ni kwa ngeli ya LI-YA (k.m. matunda yale).\n- **zile:** Ni kwa ngeli ya I-ZI (k.m. nyumba zile).\n- **pale:** Ni kiashiria cha mahali (PA-KU-MU).\n\n📌 **Kidokezo cha Kujifunza:**\nKumbuka viashiria vya ngeli ya U-I: mti huu/ule, miti hii/ile."
    },
    {
      "id": "q18",
      "questionNumber": 18,
      "questionText": "Mingine ----18---- mazingira...",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q16-20",
      "options": [
        { "text": "hupambwa", "isCorrect": False },
        { "text": "hupamba", "isCorrect": True },
        { "text": "hupambika", "isCorrect": False },
        { "text": "hupambiana", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **hupamba**.\n\n**Uchambuzi wa Jibu Sahihi:**\nMiti yenyewe ndiyo inafanya kitendo cha kufanya mazingira yapendeze. Kwa hivyo, miti \"hupamba\" (decorate) mazingira.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **hupambwa:** Ni kauli ya kutendewa (miti is decorated).\n- **hupambika:** Ni kauli ya kutendeka (inaweza kupambwa).\n- **hupambiana:** Ni kauli ya kutendeana (miti inajipamba yenyewe kwa yenyewe).\n\n📌 **Kidokezo cha Kujifunza:**\nMiti ikiwekwa mahali inafanya pale pawe pazuri, kwa hivyo **inapamba** mazingira hayo."
    },
    {
      "id": "q19",
      "questionNumber": 19,
      "questionText": "...mazingira ----19---- mingine inatufaa kwa dawa za magonjwa mbalimbali.",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q16-20",
      "options": [
        { "text": "angaa", "isCorrect": False },
        { "text": "lau", "isCorrect": False },
        { "text": "ilhali", "isCorrect": True },
        { "text": "iwapo", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **ilhali**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKiunganishi \"ilhali\" hutumika kuonyesha tofauti mbili zinazoendelea kwa wakati mmoja (whereas / while). \"Mingine hupamba mazingira **ilhali** (wakati huo huo) mingine inatufaa kwa dawa.\"\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **angaa:** Inamaanisha angalau (at least).\n- **lau:** Inamaanisha kama / endapo (if / supposing).\n- **iwapo:** Inamaanisha ikiwa (if / in case).\n\n📌 **Kidokezo cha Kujifunza:**\nKiunganishi **ilhali** hutumika kuunganisha mambo mawili tofauti yanayotendeka au kuwepo kwa wakati mmoja (k.m. Yeye anacheka ilhali mimi ninalia)."
    },
    {
      "id": "q20",
      "questionNumber": 20,
      "questionText": "Ni vyema sote ----20---- ili kuhifadhi miti.",
      "questionType": "multiple-choice",
      "contextRef": "ctx-kis-2025-q16-20",
      "options": [
        { "text": "tutie fora", "isCorrect": False },
        { "text": "tupige chuku", "isCorrect": False },
        { "text": "tujitanue kifua", "isCorrect": False },
        { "text": "tujifunge nira", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **tujifunge nira**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNahau \"kujifunga nira\" inamaanisha kujitolea au kufanya bidii kwa pamoja ili kutimiza lengo fulani (kama wanyama wanaofungwa nira pamoja kuvuta jembe). Hapa inahamasisha watu kufanya bidii na kushirikiana kuhifadhi miti.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **kutia fora:** Kufanya vizuri sana kushinda wengine.\n- **kupiga chuku:** Kutia chumvi / kuzidisha mambo unaposimulia.\n- **kujitanua kifua:** Kujivuna au kuringa.\n\n📌 **Kidokezo cha Kujifunza:**\n**Kujifunga nira** au **kujifunga kibwebwe** ni nahau zinazohimiza watu kutia bidii katika kazi fulani."
    },
    {
      "id": "q21",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 21,
      "questionText": "Wanafunzi wana nidhamu, _________ huheshimu walimu.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "wao", "isCorrect": True },
        { "text": "wewe", "isCorrect": False },
        { "text": "yeye", "isCorrect": False },
        { "text": "nyinyi", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **wao**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNeno \"Wanafunzi\" lipo katika nafsi ya tatu wingi. Kivumishi / kiwakilishi chake sahihi ni \"wao\" (they). \"Wanafunzi wana nidhamu, **wao** huheshimu walimu.\"\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **wewe:** Nafsi ya pili umoja (you).\n- **yeye:** Nafsi ya tatu umoja (he/she), kwa mwanafunzi mmoja.\n- **nyinyi:** Nafsi ya pili wingi (you all).\n\n📌 **Kidokezo cha Kujifunza:**\nTunapotaja kundi la watu ambao hawapo mbele yetu, tunatumia kiwakilishi **wao**."
    },
    {
      "id": "q22",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 22,
      "questionText": "Chagua neno ambalo limeambatanishwa na kinyume kisichofaa.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "hakika - wasiwasi", "isCorrect": False },
        { "text": "panda - shuka", "isCorrect": False },
        { "text": "upole - moto", "isCorrect": True },
        { "text": "tia - toa", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **upole - moto**.\n\n**Uchambuzi wa Jibu Sahihi:**\nSwali linataka kinyume ambacho **siyo** sahihi (kisichofaa). Kinyume cha upole ni **ukali**. Moto ni kinyume cha baridi. Kwa hivyo huu ni mwambatano usiofaa.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Hakika kinyume chake ni wasiwasi.\n- Panda kinyume chake ni shuka.\n- Tia kinyume chake ni toa. \nHivi vyote ni vinyume sahihi.\n\n📌 **Kidokezo cha Kujifunza:**\nKinyume cha mtu mpole ni mtu mkali (**ukali**)."
    },
    {
      "id": "q23",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 23,
      "questionText": "Chagua ukanusho sahihi wa sentensi ifuatayo:\n\nAfisa wa kilimo aliwashauri wanakijiji kuhusu mbinu bora za kilimo.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Afisa wa kilimo hajawashauri wanakijiji kuhusu mbinu bora za kilimo.", "isCorrect": False },
        { "text": "Afisa wa kilimo hangewashauri wanakijiji kuhusu mbinu bora za kilimo.", "isCorrect": False },
        { "text": "Afisa wa kilimo hakuwashauri wanakijiji kuhusu mbinu bora za kilimo.", "isCorrect": True },
        { "text": "Afisa wa kilimo hatawashauri wanakijiji kuhusu mbinu bora za kilimo.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Afisa wa kilimo hakuwashauri...**\n\n**Uchambuzi wa Jibu Sahihi:**\nSentensi ipo katika wakati uliopita kwa sababu ya kiambishi \"-li-\" (aliwashauri). Wakati uliopita hukanushwa kwa kutumia kiambishi \"-ku-\". Kwa hivyo, a-li-washauri inabadilika kuwa ha-ku-washauri.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **hajawashauri:** Huu ni ukanusho wa wakati uliopo mkamilifu (amewashauri -> hajawashauri).\n- **hangewashauri:** Huu ni ukanusho wa hali ya nge (angewashauri -> hangewashauri).\n- **hatawashauri:** Huu ni ukanusho wa wakati ujao (atawashauri -> hatawashauri).\n\n📌 **Kidokezo cha Kujifunza:**\nKitendo cha wakati uliopita **-li-** (k.m. nilikula) hukanushwa kwa kutumia **-ku-** (síkula)."
    },
    {
      "id": "q24",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 24,
      "questionText": "Chagua ukubwa wa sentensi ifuatayo:\n\nMlango wa nyumba yake unapendeza.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Lango la jumba lake linapendeza.", "isCorrect": True },
        { "text": "Mlango wa jumba lake linapendeza.", "isCorrect": False },
        { "text": "Lango la nyumba yake linapendeza.", "isCorrect": False },
        { "text": "Mlango wa nyumba yake linapendeza.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Lango la jumba lake linapendeza.**\n\n**Uchambuzi wa Jibu Sahihi:**\nUkubwa wa nomino \"mlango\" ni \"lango\". Ukubwa wa \"nyumba\" ni \"jumba\". \nInapobadilika kwenda hali ya ukubwa (ngeli ya LI-YA), vivumishi pia vinabadilika: \"wa\" inakuwa \"la\", \"yake\" inakuwa \"lake\", na \"unapendeza\" inakuwa \"linapendeza\".\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Sentensi zingine zinachanganya maneno ya ukubwa (k.m. kuacha mlango/nyumba) au zinatumia viambishi vya ngeli isivyo sahihi.\n\n📌 **Kidokezo cha Kujifunza:**\nKatika hali ya ukubwa (ngeli ya LI-YA), maneno yote katika sentensi lazima yapate viambishi vya LI (umoja) au YA (wingi)."
    },
    {
      "id": "q25",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 25,
      "questionText": "Chagua jibu lenye wingi wa sentensi ifuatayo:\n\nNdege amejenga kiota kwenye mti huu.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Ndege amejenga viota kwenye mti huu.", "isCorrect": False },
        { "text": "Ndege amejenga kiota kwenye miti hii.", "isCorrect": False },
        { "text": "Ndege wamejenga kiota kwenye mti huu.", "isCorrect": False },
        { "text": "Ndege wamejenga viota kwenye miti hii.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **Ndege wamejenga viota kwenye miti hii.**\n\n**Uchambuzi wa Jibu Sahihi:**\nTunabadilisha kila neno katika sentensi kwenda katika wingi:\n- Ndege -> Ndege (haibadiliki jina, lakini kiambishi chake cha kitenzi hubadilika).\n- amejenga -> wamejenga.\n- kiota -> viota.\n- mti huu -> miti hii.\n\n📌 **Kidokezo cha Kujifunza:**\nHakikisha umebadilisha viashiria na vitenzi vyote ipasavyo kulingana na ngeli za maneno husika katika wingi."
    },
    {
      "id": "q26",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 26,
      "questionText": "Ni jibu lipi linaloonyesha maana ya sentensi zifuatazo?\n\nMikaili hakufuata maagizo ya tabibu.\nMikaili aliathirika.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Mikaili angalifuata maagizo ya tabibu asingaliathirika.", "isCorrect": True },
        { "text": "Mikaili akifuata maagizo ya tabibu hataathirika.", "isCorrect": False },
        { "text": "Mikaili asingalifuata maagizo ya tabibu asingaliathirika.", "isCorrect": False },
        { "text": "Mikaili asipofuata maagizo ya tabibu hataathirika.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Mikaili angalifuata maagizo ya tabibu asingaliathirika.**\n\n**Uchambuzi wa Jibu Sahihi:**\nSentensi hizi zinaonyesha jambo ambalo tayari limeshatokea kwa njia mbaya. Njia pekee ya kueleza matokeo mbadala ambayo hayakutokea ni kwa kutumia hali ya \"-ngali-\" (masharti yaliyopita). Kama *angalifuata* (lakini hakufuata), *asingaliathirika* (lakini sasa ameathirika).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Hali ya \"-ki-\" au \"-sipo-\" hutumika kwa matukio ya wakati ujao ambayo yanaweza kuzuiwa, wakati hapa madhara tayari yameshatokea (aliathirika).\n\n📌 **Kidokezo cha Kujifunza:**\nHali ya **-ngali-** inatumika kueleza majuto au mambo ambayo yangewezekana kama hali fulani ingezingatiwa hapo zamani."
    },
    {
      "id": "q27",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 27,
      "questionText": "Chagua jibu sahihi kujaza nafasi.\n\nHazina ameshinda nishani ya dhahabu ____________.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "daima", "isCorrect": False },
        { "text": "kabisa", "isCorrect": False },
        { "text": "tena", "isCorrect": True },
        { "text": "nadra", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **tena**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKushinda nishani (medali) ni kitendo ambacho kinaweza kurudiwa. Kwa hivyo, inawezekana kusema mtu ameshinda nishani ya dhahabu \"tena\" (again). \n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **kabisa:** Hutumika kusisitiza hali ya kukamilika (k.m. amepona kabisa), lakini huwezi kushinda nishani 'kabisa'.\n- **daima:** Inamaanisha kila wakati/siku zote (always). Sentensi ingekuwa \"Hazina hushinda... daima\".\n- **nadra:** Inamaanisha mara chache sana (rarely).\n\n📌 **Kidokezo cha Kujifunza:**\nNeno **tena** linaonyesha kurudiwa kwa kitendo ambacho kilishafanyika hapo awali."
    },
    {
      "id": "q28",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 28,
      "questionText": "Ni kiunganishi kipi ambacho kinaunganisha sentensi zifuatazo kwa usahihi?\n\nJibril aliweza kutengeneza gari. Ataweza pia kutengeneza baiskeli hii.\nJibril ametengeneza gari, ____________ baiskeli hii?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "sembuse", "isCorrect": True },
        { "text": "kama", "isCorrect": False },
        { "text": "maadamu", "isCorrect": False },
        { "text": "bali", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **sembuse**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKiunganishi \"sembuse\" hutumika kulinganisha jambo kubwa/gumu ambalo mtu ameliweza, na kuonyesha kuwa jambo dogo/rahisi litakuwa jepesi sana kwake. Kama Jibril aliweza kutengeneza gari (gumu), vipi ashindwe baiskeli (rahisi)?\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **kama:** Inamaanisha 'if' au 'like'.\n- **maadamu:** Inamaanisha mradi (as long as).\n- **bali:** Inamaanisha 'but rather' au 'instead'.\n\n📌 **Kidokezo cha Kujifunza:**\nNeno **sembuse** ni sawa na kusema \"acha hilo kubwa, sembuse hili dogo!\""
    },
    {
      "id": "q29",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 29,
      "questionText": "Ni sentensi ipi inayoonyesha huruma?",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Simile! Mpishe bwana mdogo.", "isCorrect": False },
        { "text": "Oyee! Wamefunga bao la kwanza.", "isCorrect": False },
        { "text": "Maskini! Mbuzi wangu ameumia.", "isCorrect": True },
        { "text": "Jamani! Tumsikize mwalimu wetu.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Maskini! Mbuzi wangu ameumia.**\n\n**Uchambuzi wa Jibu Sahihi:**\nNeno \"Maskini\" likitumiwa kama kihisishi (interjection) huonyesha kusikitika, majonzi au huruma kwa tatizo lililompata mtu au mnyama.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Simile:** Inaonyesha onyo au kuomba njia upite.\n- **Oyee:** Inaonyesha furaha au kushangilia.\n- **Jamani:** Hapa imetumika kuomba watu wasikilize kwa makini.\n\n📌 **Kidokezo cha Kujifunza:**\nKihisishi **Maskini!** hutumika kueleza hisia za **huruma** au huzuni."
    },
    {
      "id": "q30",
      "contextRef": "ctx-kis-2025-q21-30",
      "questionNumber": 30,
      "questionText": "Zubeda ni msanii hodari. Chagua methali utakayotumia kumhimiza kuendelea kukikuza kipawa chake ili afaidike.",
      "questionType": "multiple-choice",
      "options": [
        { "text": "Chanda chema huvikwa pete.", "isCorrect": True },
        { "text": "Haba na haba hujaza kibaba.", "isCorrect": False },
        { "text": "Samaki mkunje angali mbichi.", "isCorrect": False },
        { "text": "Ukiona vyaelea vimeundwa.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Chanda chema huvikwa pete.**\n\n**Uchambuzi wa Jibu Sahihi:**\nMethali hii inamaanisha kwamba mtu mwema, mwenye tabia nzuri, au mwenye bidii na kipawa (chanda chema/kidole kizuri) ndiye anayestahili kutuzwa au kupongezwa (kuvikwa pete). Inatumika kumtia moyo Zubeda aendeleze usanii wake kwani atakuja kufaidika (kutuzwa).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Haba na haba hujaza kibaba:** Hufundisha kuhusu kuweka akiba au kufanya mambo polepole.\n- **Samaki mkunje angali mbichi:** Hufundisha kuhusu kuonya na kufunza mtoto akiwa bado mdogo.\n- **Ukiona vyaelea vimeundwa:** Hufundisha kuwa mafanikio yanayokuvutia yaligharimu kazi ngumu kuyafikia.\n\n📌 **Kidokezo cha Kujifunza:**\nMethali **Chanda chema huvikwa pete** hutumiwa kuhimiza na kusifia watu wafanyao vizuri ili wapate thawabu."
    }
  ]
}

js_content = "export const kpseaKiswahili2025 = " + json.dumps(data, indent=2) + ";\n"

with open('src/data/kpsea-kiswahili-2025.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Created kpsea-kiswahili-2025.js successfully!")
