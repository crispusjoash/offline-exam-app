import json

kiswahili_paper = {
    "id": "kpsea-kiswahili-2023",
    "title": "KPSEA 2023 Kiswahili",
    "subject": "Kiswahili",
    "year": "2023",
    "durationMinutes": 60,
    "sharedContexts": {
        "ctx-swa-q1-5": {
            "title": "Swali la 1 hadi la 5\\nSoma kifungu kifuatacho kisha ujibu maswali.",
            "type": "text",
            "text": "(Ni jioni. Leni na Kibo wamekutana mtoni. Ni msimu wa kiangazi.)\\nLeni: (Akitabasamu.) Bingwa, hujambo? Ha! Ha! Ha! Umejitwika mtungi kichwani kutafuta maji!\\nKibo: (Akionyesha kukasirika.) Sijambo, lakini mimi si bingwa. Ubingwa gani na hata tone la maji sina?\\nLeni: Samahani kaka. Sikudhani unaweza kukosa maji. Ajabu! Matangi yako makubwa yamekauka?\\nKibo: Bila shaka. Unavyoona kiangazi kimetuathiri sisi sote. Hali ya anga isipobadilika tutaangamia.\\nLeni: (Akionyesha kuhuzunika.) Ni kweli unavyosema mwenzangu. Lakini hiyo anga itabadilikaje ilhali miti inakatwa ovyo?\\nKibo: Ipo haja ya sisi kushirikiana ili kutunza na kuhifadhi mazingira yetu. Kumbuka tusipoziba ufa...\\nLeni: (Akikubaliana naye.) Tutajenga ukuta. Nasikitika hali hii ikiendelea tutakosa chakula. Wanyama na ndege nao watakosa makao.\\nKibo: Mwandani wangu, hakika utunzi wa mazingira ni wajibu wetu.\\nLeni: Kweli kabisa. (Wanaagana na kuondoka)"
        },
        "ctx-swa-q6-9": {
            "title": "Swali la 6 hadi la 9\\nSoma kifungu kifuatacho kisha ujibu maswali.",
            "type": "text",
            "text": "Ushuru ni malipo yanayotozwa na serikali kama ada ya kuingiza bidhaa ndani ya nchi au kuziuza nje ya nchi. Pia, ni ada inayotozwa raia kwa kuuza au kununua huduma mbalimbali. Nchi yetu hutegemea ushuru ambao wananchi hutozwa ili kuendesha shughuli zake.\\n\\nShirika lenye jukumu la kukusanya ushuru nchini Kenya ni Halmashauri ya Ukusanyaji Ushuru almaarufu KRA. Shirika hili limepewa mamlaka ya kikatiba kukusanya aina zote za ushuru: ushuru wa mapato, ushuru wa forodhani, ushuru kutokana na shughuli za kitalii na nyinginezo.\\n\\nSerikali huandaa bajeti kila mwaka ili kuhakikisha matumizi yafaayo ya fedha. Bajeti huwa na makadirio ya mapato na mgao wa fedha kwa matumizi mbalimbali. Makadirio hayo husomwa bungeni na Waziri wa Hazina ya Kitaifa kisha kuidhinishwa.\\n\\nNi wajibu wa kila mwananchi kulipa ushuru ili taifa letu liweze kujitegemea. Tukifanya hivyo, tutaweza kupiga hatua kimaendeleo. Tutakuwa na miundomsingi bora, huduma nzuri za kimsingi kama vile afya na elimu na hata nafasi zaidi za ajira."
        },
        "ctx-swa-q10-12": {
            "title": "Swali la 10 hadi la 12\\nSoma kifungu kifuatacho kisha ujibu maswali.",
            "type": "text",
            "text": "Likizo iliyopita nilitumia muda wangu wa mapumziko kumsaidia mlezi wangu kuwatunza mifugo wetu. Jambo hilo lilimfurahisha sana mlezi wangu akanizawidi ndama wa kike. Nilimpa ndama wangu jina, Simati.\\n\\nNilijitolea kwa hali na mali kumtunza Simati. Anapendeza kwa rangi yake nyeupe na madoa meusi. Matarajio yangu ni kwamba siku za usoni atapata ndama wake. Wakati huo utakapofika, nitamkama maziwa.\\n\\nMaziwa nitakayoyapata nitayagawa kwa matumizi ya nyumbani na mengine nitayauza kwa usaidizi wa mlezi wangu. Hela nitakazopata kutokana na mauzo ya maziwa hayo, nitaziweka kama akiba kwani akiba haiozi."
        },
        "ctx-swa-q13-15": {
            "title": "Swali la 13 hadi la 15\\nSoma kifungu kifuatacho kisha ujibu maswali.",
            "type": "text",
            "text": "Kesho ni Ijumaa. Itakuwa sikukuu ya Mashujaa nchini. Kutakuwa na sherehe ya kuadhimisha siku hiyo. Jena na Joana watakariri shairi kuhusu mashujaa. Tangu juzi, wamekuwa wakifanya mazoezi ili kujiandaa. Mtondogoo watarejea shuleni. Watawasimulia wenzao kuhusu matukio ya siku hiyo."
        },
        "ctx-swa-q16-20": {
            "title": "Swali la 16 hadi la 20\\nSoma kifungu kifuatacho. Kina nafasi 16 hadi 20. Umepewa majibu manne hapo. Chagua jibu lifaalo zaidi kati ya yale uliyopewa.",
            "type": "text",
            "text": "Kuwa na afya yaani ____16____ bora ni jambo muhimu kwa binadamu. Mlezi wangu husema kuwa lishe bora na mazoezi ya viungo vya mwili ni njia ____17____ ya kutupatia afya njema. Yeye huhakikisha kwamba ____18____ matunda, mboga, mihogo na maharagwe ____19____ wingi. Tukiwa na afya njema, tutaweza kufanya kazi kwa bidii kama ____20____."
        }
    },
    "sectionA": [
        {
            "id": "sq1",
            "questionNumber": 1,
            "questionText": "1. Leni alimwamkua Kibo, hujambo? Ni salamu gani nyingine ambayo Leni angetumia kumwamkua Kibo?",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q1-5",
            "options": [
                { "text": "Chewa?", "isCorrect": False },
                { "text": "Masalkheri?", "isCorrect": True },
                { "text": "Sabalkheri?", "isCorrect": False },
                { "text": "Shikamoo?", "isCorrect": False }
            ],
            "explanation": "Kulingana na maelezo ya mwanzo, wamekutana 'jioni'. Salamu mwafaka ya wakati wa jioni katika Kiswahili ni 'Masalkheri'."
        },
        {
            "id": "sq2",
            "questionNumber": 2,
            "questionText": "2. Leni alitumia lugha ya adabu alipokuwa akizungumza na Kibo. Chagua kauli aliyoitumia inayoonyesha adabu.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q1-5",
            "options": [
                { "text": "Umejitwika mtungi kichwani kutafuta maji!", "isCorrect": False },
                { "text": "Wanyama na ndege nao watakosa makao.", "isCorrect": False },
                { "text": "Matangi yako makubwa yamekauka?", "isCorrect": False },
                { "text": "Ni kweli unavyosema mwenzangu.", "isCorrect": True }
            ],
            "explanation": "Kuonyesha kukubaliana na mtu na kumwita 'mwenzangu' (kama katika 'Ni kweli unavyosema mwenzangu') ni dhihirisho la heshima, adabu, na unyenyekevu katika mazungumzo."
        },
        {
            "id": "sq3",
            "questionNumber": 3,
            "questionText": "3. Katika mazungumzo, msikilizaji anaweza kukamilisha kauli ya anayezungumza. Chagua kauli iliyotumiwa kukamilisha nyingine katika mazungumzo haya.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q1-5",
            "options": [
                { "text": "Bila shaka.", "isCorrect": False },
                { "text": "Tutajenga ukuta.", "isCorrect": True },
                { "text": "Kweli kabisa.", "isCorrect": False },
                { "text": "Samahani kaka.", "isCorrect": False }
            ],
            "explanation": "Kibo alianza methali akisema 'Kumbuka tusipoziba ufa...', naye Leni akadakia na kuikamilisha akisema 'Tutajenga ukuta.'"
        },
        {
            "id": "sq4",
            "questionNumber": 4,
            "questionText": "4. Leni alimweleza Kibo athari za kutotunza mazingira. Ungekuwa Kibo, ungetaja athari gani nyingine?",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q1-5",
            "options": [
                { "text": "Kiwango cha joto kuongezeka.", "isCorrect": True },
                { "text": "Wanafunzi kuacha shule.", "isCorrect": False },
                { "text": "Mahusiano baina ya watu yataharibika.", "isCorrect": False },
                { "text": "Vyombo vya usafiri wa umma vitapungua.", "isCorrect": False }
            ],
            "explanation": "Kutotunza mazingira, kama vile kukata miti, husababisha mabadiliko ya tabianchi ikiwemo kuongezeka kwa kiwango cha joto. Chaguo hili linaambatana na mada ya kimazingira."
        },
        {
            "id": "sq5",
            "questionNumber": 5,
            "questionText": "5. Neno mwandani limetumika katika mazungumzo. Chagua neno lenye maana sawa na mwandani.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q1-5",
            "options": [
                { "text": "Ndugu.", "isCorrect": False },
                { "text": "Jirani.", "isCorrect": False },
                { "text": "Sahibu.", "isCorrect": True },
                { "text": "Mwenza.", "isCorrect": False }
            ],
            "explanation": "Mwandani ni mtu ambaye una uhusiano wa karibu sana naye; rafiki wa kufa kupona. Kisawe (neno lenye maana sawa) cha mwandani ni 'Sahibu'."
        },
        {
            "id": "sq6",
            "questionNumber": 6,
            "questionText": "6. Kulingana na kifungu, maendeleo ya taifa hutegemea:",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q6-9",
            "options": [
                { "text": "bidhaa zinazouzwa.", "isCorrect": False },
                { "text": "bajeti ya taifa.", "isCorrect": False },
                { "text": "huduma za kimsingi.", "isCorrect": False },
                { "text": "ushuru unaotozwa.", "isCorrect": True }
            ],
            "explanation": "Kifungu kinasema 'Nchi yetu hutegemea ushuru ambao wananchi hutozwa ili kuendesha shughuli zake.' Hivyo, maendeleo ya taifa hutegemea ushuru unaotozwa."
        },
        {
            "id": "sq7",
            "questionNumber": 7,
            "questionText": "7. Kifungu kimeonyesha kuwa ni haki ya KRA kukusanya ushuru kwa sababu:",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q6-9",
            "options": [
                { "text": "bajeti huandaliwa kila mwaka.", "isCorrect": False },
                { "text": "imepewa mamlaka kikatiba.", "isCorrect": True },
                { "text": "ni muhimu kuhakikisha matumizi yafaayo ya fedha.", "isCorrect": False },
                { "text": "bidhaa nyingi huuzwa ndani na nje ya nchi.", "isCorrect": False }
            ],
            "explanation": "Mwandishi anasema waziwazi kuwa KRA ni shirika ambalo 'limepewa mamlaka ya kikatiba kukusanya aina zote za ushuru'."
        },
        {
            "id": "sq8",
            "questionNumber": 8,
            "questionText": "8. Miundomsingi ikiimarika:",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q6-9",
            "options": [
                { "text": "viwanda vya uzalishaji bidhaa vitaimarika.", "isCorrect": True },
                { "text": "wakulima watapata mazao mengi.", "isCorrect": False },
                { "text": "idadi ya watu itaongezeka.", "isCorrect": False },
                { "text": "uharibifu wa mazingira utapungua.", "isCorrect": False }
            ],
            "explanation": "Kulingana na muktadha wa kiuchumi (kama unavyotolewa na ushuru), miundomsingi bora (k.m. barabara, umeme) inaimarisha moja kwa moja utendakazi wa viwanda na kuchochea ajira na uzalishaji."
        },
        {
            "id": "sq9",
            "questionNumber": 9,
            "questionText": "9. Chagua maana ya neno kuidhinishwa kama lilivyotumiwa katika kifungu.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q6-9",
            "options": [
                { "text": "kuwasilishwa.", "isCorrect": False },
                { "text": "kuchunguzwa.", "isCorrect": False },
                { "text": "kukubaliwa.", "isCorrect": True },
                { "text": "kukamilika.", "isCorrect": False }
            ],
            "explanation": "Bajeti inaposomwa bungeni na 'kuidhinishwa', ina maana kuwa imepitishwa au 'kukubaliwa' rasmi kutumika."
        },
        {
            "id": "sq10",
            "questionNumber": 10,
            "questionText": "10. Kulingana na kifungu, msimulizi alipewa zawadi kwa sababu:",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q10-12",
            "options": [
                { "text": "alifika nyumbani kwa likizo.", "isCorrect": False },
                { "text": "alimsaidia mlezi wake.", "isCorrect": True },
                { "text": "alimpa ndama jina Simati.", "isCorrect": False },
                { "text": "alitamani kuuza maziwa.", "isCorrect": False }
            ],
            "explanation": "Msimulizi anasema, 'nilitumia muda wangu wa mapumziko kumsaidia mlezi wangu... Jambo hilo lilimfurahisha sana mlezi wangu akanizawidi ndama wa kike.' Kwa hivyo, kitendo cha kumsaidia mlezi ndicho kilichomletea zawadi."
        },
        {
            "id": "sq11",
            "questionNumber": 11,
            "questionText": "11. Chagua jibu linaloonyesha kuwa msimulizi anafahamu uwekezaji.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q10-12",
            "options": [
                { "text": "Anatumia likizo yake vizuri.", "isCorrect": False },
                { "text": "Anatarajia Simati atapata ndama.", "isCorrect": False },
                { "text": "Anafurahisha sana mlezi wake.", "isCorrect": False },
                { "text": "Anapanga kuuza maziwa ili apate pesa.", "isCorrect": True }
            ],
            "explanation": "Uwekezaji (investment) ni mpango wa kuzalisha faida za kifedha. Mpango wake wa kuuza maziwa na kuweka pesa akiba ('akiba haiozi') ni thibitisho la fikra za kiuwekezaji."
        },
        {
            "id": "sq12",
            "questionNumber": 12,
            "questionText": "12. Msimulizi alimsaidia mlezi wake kuwatunza mifugo wao. Kuwatunza ni:",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q10-12",
            "options": [
                { "text": "kuwalinda.", "isCorrect": True },
                { "text": "kuwatayarisha.", "isCorrect": False },
                { "text": "kuwapenda.", "isCorrect": False },
                { "text": "kuwafurahisha.", "isCorrect": False }
            ],
            "explanation": "Kuwatunza mifugo inamaanisha kuwapa uangalizi kamili ikiwemo chakula na 'kuwalinda' dhidi ya magonjwa au wanyama wakali."
        },
        {
            "id": "sq13",
            "questionNumber": 13,
            "questionText": "13. Jena na Joana watarejea shuleni mtondogoo. Mtondogoo itakuwa siku gani?",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q13-15",
            "options": [
                { "text": "Jumamosi.", "isCorrect": False },
                { "text": "Jumapili.", "isCorrect": False },
                { "text": "Jumatatu.", "isCorrect": True },
                { "text": "Jumanne.", "isCorrect": False }
            ],
            "explanation": "Ikiwa kesho ni Ijumaa, basi leo ni Alhamisi. Mtiririko wa siku zifuatazo ni: Kesho (Ijumaa), Keshokutwa (Jumamosi), Mtondo (Jumapili), Mtondogoo (Jumatatu). Kwa hivyo, Mtondogoo ni Jumatatu."
        },
        {
            "id": "sq14",
            "questionNumber": 14,
            "questionText": "14. Chagua vitendo vinavyoonyesha kuwa Jena na Joana wanapenda nchi yao.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q13-15",
            "options": [
                { "text": "Kuhudhuria sherehe, kukariri shairi.", "isCorrect": True },
                { "text": "Kurejea shuleni, kukariri shairi.", "isCorrect": False },
                { "text": "Kusimulia matukio, kuhudhuria sherehe.", "isCorrect": False },
                { "text": "Kusimulia matukio, kurejea shuleni.", "isCorrect": False }
            ],
            "explanation": "Kupenda nchi hudhihirishwa na uzalendo, ambao unaonyeshwa na vitendo vya kushiriki katika sikukuu ya kitaifa (kuhudhuria sherehe za Mashujaa) na kusifu mashujaa (kukariri shairi)."
        },
        {
            "id": "sq15",
            "questionNumber": 15,
            "questionText": "15. Maana ya kujiandaa kulingana na kifungu ni:",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q13-15",
            "options": [
                { "text": "kujitambulisha.", "isCorrect": False },
                { "text": "kujitayarisha.", "isCorrect": True },
                { "text": "kujinufaisha.", "isCorrect": False },
                { "text": "kujiburudisha.", "isCorrect": False }
            ],
            "explanation": "Kujiandaa inamaanisha kujiweka tayari kwa jambo litakalotendeka; yaani 'kujitayarisha'."
        },
        {
            "id": "sq16",
            "questionNumber": 16,
            "questionText": "16. Kuwa na afya yaani ____16____ bora ni jambo muhimu kwa binadamu.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q16-20",
            "options": [
                { "text": "uhai", "isCorrect": False },
                { "text": "nguvu", "isCorrect": False },
                { "text": "kimo", "isCorrect": False },
                { "text": "siha", "isCorrect": True }
            ],
            "explanation": "Neno 'siha' ni kisawe (neno lenye maana sawa) cha 'afya'. Kwa hivyo, kuwa na afya ni kuwa na siha bora."
        },
        {
            "id": "sq17",
            "questionNumber": 17,
            "questionText": "17. Mlezi wangu husema kuwa lishe bora na mazoezi ya viungo vya mwili ni njia ____17____ ya kutupatia afya njema.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q16-20",
            "options": [
                { "text": "kuzuri", "isCorrect": False },
                { "text": "nzuri", "isCorrect": True },
                { "text": "mzuri", "isCorrect": False },
                { "text": "vizuri", "isCorrect": False }
            ],
            "explanation": "Neno 'njia' lipo katika ngeli ya I-ZI. Kivumishi kikubaliano chake lazima kianze na herufi 'n' iwapo ni kimoja (njia nzuri) au nyingi (njia nzuri)."
        },
        {
            "id": "sq18",
            "questionNumber": 18,
            "questionText": "18. Yeye huhakikisha kwamba ____18____ matunda, mboga, mihogo na maharagwe...",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q16-20",
            "options": [
                { "text": "tunakula", "isCorrect": True },
                { "text": "tungekula", "isCorrect": False },
                { "text": "tukila", "isCorrect": False },
                { "text": "tulikula", "isCorrect": False }
            ],
            "explanation": "Kifungu kinazungumzia tabia ya kawaida na ya mara kwa mara (present tense), hivyo kitenzi mwafaka ni 'tunakula' ambacho huonyesha kitendo cha wakati uliopo."
        },
        {
            "id": "sq19",
            "questionNumber": 19,
            "questionText": "19. ...matunda, mboga, mihogo na maharagwe ____19____ wingi.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q16-20",
            "options": [
                { "text": "ya", "isCorrect": False },
                { "text": "kwa", "isCorrect": True },
                { "text": "ni", "isCorrect": False },
                { "text": "vya", "isCorrect": False }
            ],
            "explanation": "Nahau inayotumika kuonyesha kiwango kikubwa au kitu kingi katika Kiswahili ni 'kwa wingi'."
        },
        {
            "id": "sq20",
            "questionNumber": 20,
            "questionText": "20. Tukiwa na afya njema, tutaweza kufanya kazi kwa bidii kama ____20____.",
            "questionType": "mcq",
            "contextRef": "ctx-swa-q16-20",
            "options": [
                { "text": "kiwavi", "isCorrect": False },
                { "text": "mchwa", "isCorrect": True },
                { "text": "tausi", "isCorrect": False },
                { "text": "njiwa", "isCorrect": False }
            ],
            "explanation": "Hii ni tashbihi (simile) maarufu katika Kiswahili inayosifu uchapakazi. Mchwa hujulikana sana kwa kujenga vichuguu vikubwa na kufanya kazi bila kuchoka, hivyo 'kufanya kazi kwa bidii kama mchwa'."
        },
        {
            "id": "sq21",
            "questionNumber": 21,
            "questionText": "21. Chagua umoja wa: 'Majembe yatatumiwa kupalilia mipapai yao michanga'.",
            "questionType": "mcq",
            "options": [
                { "text": "Jembe litatumiwa kupalilia mipapai yake michanga.", "isCorrect": False },
                { "text": "Jembe litatumiwa kupalilia mmpapai yake mchanga.", "isCorrect": False },
                { "text": "Jembe litatumiwa kupalilia mpapai wake mchanga.", "isCorrect": True },
                { "text": "Jembe litatumiwa kupalilia mpapai wake michanga.", "isCorrect": False }
            ],
            "explanation": "Majembe (LI-YA) inakuwa Jembe. Yatatumiwa inakuwa litatumiwa. Mipapai (M-MI) inakuwa mpapai. Yao inakuwa wake. Michanga inakuwa mchanga. Jawabu kamili ni 'Jembe litatumiwa kupalilia mpapai wake mchanga'."
        },
        {
            "id": "sq22",
            "questionNumber": 22,
            "questionText": "22. Chagua jibu sahihi kujaza pengo. Jakaya amekuwa akiwasaidia _____ zamani.",
            "questionType": "mcq",
            "options": [
                { "text": "hadi", "isCorrect": False },
                { "text": "kisha", "isCorrect": False },
                { "text": "tena", "isCorrect": False },
                { "text": "tangu", "isCorrect": True }
            ],
            "explanation": "Kuonyesha asili au kianzio cha wakati, tunatumia neno 'tangu' (tangu zamani), likiwa na maana sawa na 'since' kwa lugha ya Kiingereza."
        },
        {
            "id": "sq23",
            "questionNumber": 23,
            "questionText": "23. Ukitaka kwenda chooni utamwomba mwalimu ruhusa kwa kumwambia unataka kwenda _____.",
            "questionType": "mcq",
            "options": [
                { "text": "bafuni.", "isCorrect": False },
                { "text": "majifichoni.", "isCorrect": False },
                { "text": "msalani.", "isCorrect": True },
                { "text": "chumbani.", "isCorrect": False }
            ],
            "explanation": "Kwa kutumia lugha ya adabu na staha ukiwa shuleni au mbele ya watu wazima, neno lenye heshima linalotumika badala ya 'chooni' ni 'msalani'."
        },
        {
            "id": "sq24",
            "questionNumber": 24,
            "questionText": "24. Matu ni fundi wa nguo. Rinda la Anna limeshonwa na Matu. Kwa hivyo, Anna ______ rinda na Matu.",
            "questionType": "mcq",
            "options": [
                { "text": "wameshonewa", "isCorrect": False },
                { "text": "wameshonesha", "isCorrect": False },
                { "text": "ameshonewa", "isCorrect": True },
                { "text": "ameshonesha", "isCorrect": False }
            ],
            "explanation": "Matu ndiye mtendaji (fundi). Anna ndiye mtendewa anayefanyiwa kazi. Kitenzi 'shona' katika kauli ya kutendewa kinakuwa 'shonewa'. Kwa kuwa Anna ni mmoja, inakuwa 'ameshonewa'."
        },
        {
            "id": "sq25",
            "questionNumber": 25,
            "questionText": "25. Chagua jibu sahihi kujaza nafasi. Mlango ______ darasa ni safi.",
            "questionType": "mcq",
            "options": [
                { "text": "za", "isCorrect": False },
                { "text": "ya", "isCorrect": False },
                { "text": "wa", "isCorrect": True },
                { "text": "la", "isCorrect": False }
            ],
            "explanation": "Neno 'Mlango' lipo katika ngeli ya M-MI. Kiunganishi-A cha ngeli hii katika umoja ni 'wa' (k.m. Mlango wa darasa)."
        },
        {
            "id": "sq26",
            "questionNumber": 26,
            "questionText": "26. Mjomba wako alikuletea zawadi juzi. Ikiwa leo ni Jumamosi, mjomba wako alikuletea zawadi siku gani?",
            "questionType": "mcq",
            "options": [
                { "text": "Jumanne.", "isCorrect": False },
                { "text": "Jumatano.", "isCorrect": False },
                { "text": "Alhamisi.", "isCorrect": True },
                { "text": "Ijumaa.", "isCorrect": False }
            ],
            "explanation": "Tupange siku kinyumenyume kuanzia leo: Leo ni Jumamosi. Jana ilikuwa Ijumaa. Juzi (siku kabla ya jana) ilikuwa Alhamisi."
        },
        {
            "id": "sq27",
            "questionNumber": 27,
            "questionText": "27. Tamu ni kwa chungu ilhali mwepesi ni kwa:",
            "questionType": "mcq",
            "options": [
                { "text": "mzito.", "isCorrect": True },
                { "text": "mkubwa.", "isCorrect": False },
                { "text": "mnene.", "isCorrect": False },
                { "text": "mpana.", "isCorrect": False }
            ],
            "explanation": "Hapa tunatafuta vinyume. Kinyume cha neno 'tamu' ni 'chungu'. Hali kadhalika, kinyume cha kitu 'mwepesi' ni kitu 'mzito'."
        },
        {
            "id": "sq28",
            "questionNumber": 28,
            "questionText": "28. Chagua jibu linaloonyesha ukanusho wa sentensi ifuatayo: Munira amesoma kitabu hicho.",
            "questionType": "mcq",
            "options": [
                { "text": "Munira hasomi kitabu hicho.", "isCorrect": False },
                { "text": "Munira hatasoma kitabu hicho.", "isCorrect": False },
                { "text": "Munira hakusoma kitabu hicho.", "isCorrect": False },
                { "text": "Munira hajasoma kitabu hicho.", "isCorrect": True }
            ],
            "explanation": "Sentensi ipo katika wakati mtimilifu (njeo ya 'me-'). Unapokanusha kitenzi chenye 'me' (amesoma), unatumia 'ja' (hajasoma)."
        },
        {
            "id": "sq29",
            "questionNumber": 29,
            "questionText": "29. Mtu anapomhimiza mwenzake kufanya kazi, tunasema anamtia shime. Je, mtu anapomsaidia mwenzake katika jambo fulani huwa:",
            "questionType": "mcq",
            "options": [
                { "text": "anamfanyia hima.", "isCorrect": False },
                { "text": "anampiga jeki.", "isCorrect": True },
                { "text": "anachapa kazi.", "isCorrect": False },
                { "text": "anatia fora.", "isCorrect": False }
            ],
            "explanation": "Nahau 'kumpiga mtu jeki' hutumika kumaanisha kumpa mtu msaada au ushirikiano anapokuwa anafanya jambo fulani zito."
        },
        {
            "id": "sq30",
            "questionNumber": 30,
            "questionText": "30. Katana na Kombo hawapendi kushirikiana na wenzao kufanya shughuli za vikundi darasani. Chagua methali inayoweza kutumiwa kuwashauri kubadilisha tabia hii.",
            "questionType": "mcq",
            "options": [
                { "text": "Asiyesikia la mkuu huvunjika guu.", "isCorrect": False },
                { "text": "Chelewa chelewa utakuta mwana si wako.", "isCorrect": False },
                { "text": "Mchagua jembe si mkulima.", "isCorrect": False },
                { "text": "Jifya moja haliinjiiki chungu.", "isCorrect": True }
            ],
            "explanation": "Jifya moja haliwezi kuweka chungu kikakaa sawa jikoni, inabidi yawe matatu. Hii ni methali inayotuhimiza umuhimu wa ushirikiano; mtu hawezi kufanikiwa akiwa peke yake bila kushirikiana na wengine."
        }
    ]
}

# Read current pastPapers.js
with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Insert the new Kiswahili paper object into the KPSEA array.
# The array begins like:
# export const PAST_PAPERS = {
#   KPSEA: [
#     { ... maths ... },
#     { ... english ... }
#   ],

import re
# Convert python dict to a well-formatted js string representation
json_str = json.dumps(kiswahili_paper, indent=2, ensure_ascii=False)

# The correct place to inject is right after the `KPSEA: [`
target = "KPSEA: ["
replacement = f"KPSEA: [\\n{json_str},"

if "kpsea-kiswahili-2023" not in js_content:
    new_js = js_content.replace(target, replacement)
    with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Added Kiswahili 2023!")
else:
    print("Kiswahili already exists!")
