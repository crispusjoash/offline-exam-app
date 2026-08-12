import json

data = {
  "id": "kpsea-kiswahili-2022",
  "title": "KPSEA 2022 Kiswahili",
  "subject": "Kiswahili",
  "year": "2022",
  "durationMinutes": 60,
  "timeAllowed": 60,
  "sharedContexts": {
    "ctx-kisw-2022-q1-5": {
      "title": "Swali la 1 hadi la 5\nSoma mazungumzo yafuatayo kisha ujibu maswali.",
      "type": "text",
      "text": "*(Babu ameketi chini ya mti akisoma gazeti. Analiweka gazeti kando anapomwona Muli)*\n\n**Muli:** *(akimsogelea Babu)* Shikamoo Babu?\n\n**Babu:** *(kwa tabasamu)* Marahaba mjukuu wangu! Habari za shule?\n\n**Muli:** Njema babu! *(kimya)* Babu, nikwambie kitu?\n\n**Babu:** Naam, niambie mjukuu wangu.\n\n**Muli:** Wenzangu walinichagua kuwa kiranja wa darasa.\n\n**Babu:** Hongera! Jambo zuri.\n\n**Muli:** *(akijikuna kichwa)* Lakini Babu, sijui ninastahili kufanya nini ili niwe kiongozi bora.\n\n**Babu:** Aha! Muli, sikiliza, ili kuwa kiongozi bora unastahili kuwa na **maadili**.\n\n**Muli:** Ooh! **Maadili** ...\n\n**Babu:** Naam mjukuu wangu. Unaweza kuonyesha maadili kwa namna mbalimbali. Kwanza uwahudumie wenzako bila kuwabagua.\n\n**Muli:** Kweli Babu, ninafikiria pia ninastahili kuwaonyesha upendo.\n\n**Babu:** Ndiyo Muli. Unaweza kufanya hivyo kwa kuwajali na kuwasaidia wenzako.\n\n**Muli:** Kweli Babu! Ninaona kwamba heshima, umoja na ushirikiano pia ni mambo muhimu.\n\n**Babu:** Haswa! Heshima si utumwa. Je, unaweza kuonyesha heshima kwa njia gani?\n\n**Muli:** *(Kwa ujasiri)* Kwa kuwaamkua wote na kusikiliza wanayoyasema.\n\n**Babu:** Vyema! Unastahili pia kuwa mwaminifu. Tunaonyesha uaminifu kwa kusema ukweli na kufanya mambo inavyostahili.\n\n**Muli:** Asante babu! Hakika umenifunza mengi."
    },
    "ctx-kisw-2022-q6-9": {
      "title": "Swali la 6 hadi la 9\nSoma kifungu kifuatacho kisha ujibu maswali.",
      "type": "text",
      "text": "Sungura alirauka kabla ya jua kuchomoza. Alianza safari ya kwenda kumtembelea shangazi yake. Njiani alipanda milima na kuvuka mabonde. Jua lilipochomoza, aligundua kuwa alikuwa ametembea sana ila hakuwa amefika kwa shangazi yake. Alikuwa anaelekea kusini badala ya kaskazini. Kumbe alikuwa amepotea njia!\n\n\"Nitafanya nini? Nimepotea njia,\" Sungura alijisemea kwa sauti.\n\n\"Nitakusaidia,\" alisema Kobe aliyekuwa kichakani, hapo karibu.\n\n\"Asante sana Kobe. Sikuwa nimekuona. Tafadhali nisaidie,\" Sungura alimwomba Kobe.\n\n\"Unakwenda upande gani?\" Kobe alimuliza Sungura.\n\n\"Naelekea kaskazini, anakoishi shangazi yangu,\" Sungura alimjibu Kobe.\n\n\"Jua huchomoza upande wa Mashariki wa dira kila asubuhi. Ukitaka kwenda Kaskazini, simama kisha unyooshe mikono yako juu. Mkono wa kulia uelekeze kunakotoka jua. Huko ndiko Mashariki. Nao mkono wa kushoto uelekeze upande huo mwingine. Huko ndiko Magharibi,\" Kobe alimweleza Sungura huku akimwonyesha kwa vitendo.\n\n\"Kwa hivyo uso wangu utakuwa unaangalia Kaskazini huku mgongo wangu ukiwa upande wa Kusini\" Sungura alisema kwa furaha.\n\n\"Wewe ni mwanafunzi mzuri. Unaelewa haraka. Umelenga ndipo,\" Kobe alimwambia Sungura kwa bashasha.\n\n\"Undugu ni kufaana. Asante sana Kobe,\" Sungura aligeuka akarudi hadi kwake ili kuanza safari upya."
    },
    "ctx-kisw-2022-q10-12": {
      "title": "Swali la 10 hadi la 12\nSoma kifungu kifuatacho kisha ujibu maswali.",
      "type": "image",
      "imagePath": "/assets/kiswahili_2022_table_10_12.svg",
      "text": "Shule ya msingi ya Faulu huwa na siku tatu za michezo katika kila juma. Wanafunzi wa Gredi ya Sita wamegawanywa katika vikundi vinne kama ifuatavyo:\nSimba, Kifaru, Chui, Ndovu.\n\nKila kikundi hushiriki katika michezo tofauti kila juma. Tazama jedwali la juma hili kisha ujibu maswali."
    },
    "ctx-kisw-2022-q13-15": {
      "title": "Swali la 13 hadi la 15\nSoma kifungu kifuatacho kisha ujibu maswali.",
      "type": "text",
      "text": "Je, unajua kupika ugali? Kupika ugali ni rahisi. Kwanza, unahitaji unga wa mahindi, maji, sufuria, mwiko na jiko la kupikia lenye moto. Anza kwa kupima kiasi cha maji unayohitaji na kuyatia kwenye sufuria safi. Ibandike sufuria hiyo kwenye jiko. Funika sufuria ili uyapatie maji muda yachemke. Chukua unga kisha uutie kidogo kidogo ndani ya maji yanayochemka, huku ukikoroga kwa mwiko. Ongeza unga kulingana na unavyotaka ugali wako uwe. Kama unataka ugali mgumu, basi endelea kuongeza unga. Funika ugali wako, kisha upunguze moto jikoni ili ugali uive polepole.\n\nUnaweza kuandaa ugali kwa kitoweo vya aina mbalimbali. Kuna wale wanaopenda kula ugali kwa maziwa yaliyoganda na mboga za kienyeji kama mchicha. Wengine hula ugali kwa samaki au nyama. Mimi napenda kula ugali kwa dagaa na kachumbari. Je, wewe unapenda kula ugali kwa kitoweo gani?"
    },
    "ctx-kisw-2022-q16-20": {
      "title": "Swali la 16 hadi la 20\nSoma kifungu kifuatacho. Kina nafasi 16 hadi 20. Umepewa majibu manne hapo. Chagua jibu lifaalo zaidi kati ya yale uliyopewa.",
      "type": "text",
      "text": "Kanini ----16---- katika michezo mbalimbali tukiwa shuleni. Mchezo ----17---- alipenda zaidi ni netiboli. ----18---- na timu ya mchezo wa netiboli ----19---- alipoingia darasa la tano. Kanini alitia bidii kwenye mchezo huu na kuiletea timu yake ushindi. Alifahamu kuwa ----20----."
    },
    "ctx-kisw-2022-q21-30": {
      "title": "Swali la 21 hadi la 30\nKutoka swali la 21 hadi la 30, chagua jibu sahihi.",
      "type": "text",
      "text": ""
    }
  },
  "sectionA": [
    {
      "id": "kq1-2022",
      "questionNumber": 1,
      "questionText": "Muli alipoulizwa na babu kuhusu habari za shule, alimjibu",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q1-5",
      "options": [
        { "text": "Naam", "isCorrect": False },
        { "text": "Njema", "isCorrect": True },
        { "text": "Shikamoo", "isCorrect": False },
        { "text": "Marahaba", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Njema**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKatika mazungumzo, Babu anapomuuliza Muli: \"Habari za shule?\", Muli anajibu moja kwa moja: \"Njema babu!\".\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Naam:** Haya ni majibu ya kuitika unapoitwa au kukubaliana na jambo.\n- **Shikamoo:** Ni maamkizi ya heshima yanayotumiwa na mtu mdogo kwa mkubwa.\n- **Marahaba:** Ni jibu la maamkizi ya Shikamoo linalotolewa na mtu mkubwa.\n\n📌 **Kidokezo cha Kujifunza:**\nSwali la \"Habari za...?\" hujibiwa kwa maneno kama vile: Njema, Nzuri, Salama, au Njema sana."
    },
    {
      "id": "kq2-2022",
      "questionNumber": 2,
      "questionText": "Maneno yafuatayo yametumiwa katika mazungumzo. Lipi halionyeshi adabu?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q1-5",
      "options": [
        { "text": "Karibu", "isCorrect": False },
        { "text": "Naam", "isCorrect": False },
        { "text": "Asante", "isCorrect": False },
        { "text": "Kweli", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **Kweli**.\n\n**Uchambuzi wa Jibu Sahihi:**\nManeno kama \"Karibu\", \"Naam\", na \"Asante\" ni maneno ya adabu na nidhamu ya kijamii. Neno \"Kweli\" linatumika kuthibitisha au kusisitiza ukweli wa jambo wala si neno la maamkizi au nidhamu ya kipekee.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Karibu:** Ni neno la adabu la kumkaribisha mtu.\n- **Naam:** Ni neno la nidhamu la kuitika kwa heshima.\n- **Asante:** Ni neno la kuonyesha shukrani na adabu.\n\n📌 **Kidokezo cha Kujifunza:**\nManeno ya adabu ni pamoja na: Shikamoo, Marahaba, Asante, Karibu, Tafadhali, na Naam."
    },
    {
      "id": "kq3-2022",
      "questionNumber": 3,
      "questionText": "Ni jibu lipi linaloonyesha maadili ambayo Babu alimfunza Muli?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q1-5",
      "options": [
        { "text": "Kuhudumia, kuheshimu na kusikiliza.", "isCorrect": False },
        { "text": "Kuamkua, kusikiliza na kujali.", "isCorrect": False },
        { "text": "Kujali, kusaidia na kuwa mwaminifu.", "isCorrect": True },
        { "text": "Kuwa na heshima, kushirikiana na kusaidia.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Kujali, kusaidia na kuwa mwaminifu.**\n\n**Uchambuzi wa Jibu Sahihi:**\nKatika mazungumzo, Babu anamweleza Muli waziwazi: \"Unaweza kufanya hivyo kwa kuwajali na kuwasaidia wenzako... Unastahili pia kuwa mwaminifu.\"\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Chagua A, B, na D zimetaja vitendo au njia za kuonyesha heshima badala ya orodha kamili ya maadili aliyoelezwa na Babu.\n\n📌 **Kidokezo cha Kujifunza:**\nUnapojibu maswali ya ufahamu au mazungumzo, rejelea maneno halisi yaliyotumiwa na wazungumzaji."
    },
    {
      "id": "kq4-2022",
      "questionNumber": 4,
      "questionText": "Unafikiri Muli atafanya nini baada ya kumuaga Babu?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q1-5",
      "options": [
        { "text": "Atafurahia kuwa kiongozi shuleni.", "isCorrect": False },
        { "text": "Atazingatia mawaidha ya babu.", "isCorrect": True },
        { "text": "Atawaeleza wenzake kuhusu alivyokutana na babu.", "isCorrect": False },
        { "text": "Atawapongeza wenzake kwa kumchagua kuwa kiranja.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Atazingatia mawaidha ya babu.**\n\n**Uchambuzi wa Jibu Sahihi:**\nMuli anasema mwishoni: \"Asante babu! Hakika umenifunza mengi.\" Hii inaonyesha ameyapokea mafunzo na atayatumia (atazingatia mawaidha) ili awe kiongozi bora.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Atafurahia kuwa kiongozi...:** Alikuwa tayari kiranja lakini alitaka kujua jinsi ya kuwa kiongozi bora.\n- **Atawaeleza wenzake...:** Shabaha yake kuu ilikuwa kujua jinsi ya kuongoza vyema.\n- **Atawapongeza wenzake...:** Wenzake ndio waliomchagua yeye, na lengo lake lilikuwa kutekeleza wajibu wake.\n\n📌 **Kidokezo cha Kujifunza:**\nMawaidha mazuri kutoka kwa wazee na viongozi hutolewa ili yazingatiwe na kufanyiwa kazi."
    },
    {
      "id": "kq5-2022",
      "questionNumber": 5,
      "questionText": "Neno maadili limetumika katika mazungumzo maana yake ni",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q1-5",
      "options": [
        { "text": "Mienendo mizuri inayofaa kuzingatiwa na mtu.", "isCorrect": True },
        { "text": "Maonyo ambayo hutolewa mtu anapokosea.", "isCorrect": False },
        { "text": "Matendo ambayo mtu huwafanyia wenzake.", "isCorrect": False },
        { "text": "Mitindo mipya inayofuatwa na mtu.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Mienendo mizuri inayofaa kuzingatiwa na mtu.**\n\n**Uchambuzi wa Jibu Sahihi:**\nMaadili ni tabia, mienendo na utu wema ambao jamii inatarajia mtu au kiongozi kuwa nao (kama vile uaminifu, heshima, na ushirikiano).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Maonyo...:** Haya ni maadhibu au mawaidha ya kurekebisha makosa.\n- **Matendo...:** Matendo yanaweza kuwa mazuri au mabaya; maadili ni matendo na mienendo mizuri tu.\n- **Mitindo mipya...:** Hiyo ni mitindo au maendeleo wala si nidhamu na utu wema.\n\n📌 **Kidokezo cha Kujifunza:**\nMaadili ni msingi wa uongozi bora na tabia njema katika jamii."
    },
    {
      "id": "kq6-2022",
      "questionNumber": 6,
      "questionText": "Nyumbani kwa Shangazi kulikuwa upande gani kutoka kwa Sungura?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q6-9",
      "options": [
        { "text": "Mashariki", "isCorrect": False },
        { "text": "Magharibi", "isCorrect": False },
        { "text": "Kaskazini", "isCorrect": True },
        { "text": "Kusini", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Kaskazini**.\n\n**Uchambuzi wa Jibu Sahihi:**\nSungura anapoulizwa na Kobe anaelekea wapi, anajibu: \"Naelekea kaskazini, anakoishi shangazi yangu.\"\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Kusini:** Huku ndiko Sungura alikokuwa anaelekea kimakosa kabla ya kuelekezwa.\n- **Mashariki / Magharibi:** Ni pembe za dira zinazomsaidia mtu kujua mwelekeo.\n\n📌 **Kidokezo cha Kujifunza:**\nPembe kuu nne za dira ni Kaskazini (North), Kusini (South), Mashariki (East), na Magharibi (West)."
    },
    {
      "id": "kq7-2022",
      "questionNumber": 7,
      "questionText": "Kwa nini Sungura aliamka mapema? Ili",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q6-9",
      "options": [
        { "text": "apande milima na kuvuka mabonde.", "isCorrect": False },
        { "text": "aone jua likichomoza.", "isCorrect": False },
        { "text": "akutane na Kobe njiani.", "isCorrect": False },
        { "text": "aende kumtembelea Shangazi.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **aende kumtembelea Shangazi.**\n\n**Uchambuzi wa Jibu Sahihi:**\nSentence ya kwanza na ya pili kwenye kifungu inasema: \"Sungura alirauka kabla ya jua kuchomoza. Alianza safari ya kwenda kumtembelea shangazi yake.\"\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **apande milima...:** Kupanda milima kulikuwa sehemu ya changamoto za safari, si sababu ya kuamka mapema.\n- **aone jua...:** Kurauka ni kuamka mapema kabla ya jua kutoka ili kuwahi safari.\n- **akutane na Kobe...:** Mkutano wao ulikuwa wa bahati mbaya njiani.\n\n📌 **Kidokezo cha Kujifunza:**\nNeno \"kurauka\" lina maana ya kuamka mapema sana asubuhi na kuanza safari au kazi."
    },
    {
      "id": "kq8-2022",
      "questionNumber": 8,
      "questionText": "Kobe anawajali wengine. Chagua jibu linaloonyesha sifa hii ya Kobe.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q6-9",
      "options": [
        { "text": "Alimwelekeza Sungura alikokuwa akienda.", "isCorrect": True },
        { "text": "Anamsikiliza Sungura akizungumza.", "isCorrect": False },
        { "text": "Alikubali zawadi alizopewa na Shangazi.", "isCorrect": False },
        { "text": "Alifikiria Sungura alikuwa mwanafunzi mwerevu.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Alimwelekeza Sungura alikokuwa akienda.**\n\n**Uchambuzi wa Jibu Sahihi:**\nKobe alipoona Sungura amepotea, alijitolea kumsaidia na kumweleza kwa vitendo jinsi ya kutumia jua na mikono yake ili kupata mwelekeo wa Kaskazini.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Anamsikiliza...:** Kumsikiliza mtu ni jambo jema lakini msaada na maelekezo ndivyo vinavyoonyesha kuwajali wengine kwa vitendo.\n- **Alikubali zawadi...:** Hakuna mazungumzo ya zawadi za Shangazi kwenye kifungu.\n- **Alifikiria Sungura alikuwa...:** Haya ni maoni ya Kobe baada ya Sungura kuelewa.\n\n📌 **Kidokezo cha Kujifunza:**\nSifa ya \"kuwajali wengine\" huonekana kupitia matendo ya msaada wakati mtu anapokuwa kwenye shida."
    },
    {
      "id": "kq9-2022",
      "questionNumber": 9,
      "questionText": "Chagua jibu lenye neno ambalo Shangazi angetumia kumwita Sungura.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q6-9",
      "options": [
        { "text": "Binamu", "isCorrect": False },
        { "text": "Mpwa", "isCorrect": True },
        { "text": "Ndugu", "isCorrect": False },
        { "text": "Ami", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Mpwa**.\n\n**Uchambuzi wa Jibu Sahihi:**\nMjomba au Shangazi humwita mtoto wa kaka au dada yake **Mpwa**.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Binamu:** Ni mtoto wa mjomba, shangazi, baba mkubwa au baba mdogo.\n- **Ndugu:** Ni mtu wa familia au ukoo mmoja.\n- **Ami:** Ni baba mdogo (kaka au mdogo wa kiume wa baba yako).\n\n📌 **Kidokezo cha Kujifunza:**\nUhusiano wa Kifamilia: Mtoto wa dada au kaka yako anaitwa **mpwa**."
    },
    {
      "id": "kq10-2022",
      "questionNumber": 10,
      "questionText": "Ni kikundi kipi hakikushiriki kandanda?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q10-12",
      "options": [
        { "text": "Simba", "isCorrect": False },
        { "text": "Chui", "isCorrect": True },
        { "text": "Kifaru", "isCorrect": False },
        { "text": "Ndovu", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Chui**.\n\n**Uchambuzi wa Jibu Sahihi:**\nUkiangalia jedwali:\n- Simba: Kandanda (Jumatatu)\n- Kifaru: Kandanda (Ijumaa)\n- Ndovu: Kandanda (Jumatano)\n- **Chui:** Netiboli (Jumatatu), Riadha (Jumatano), Uogeleaji (Ijumaa). Kikundi cha Chui hakina Kandanda kabisa.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Simba, Kifaru na Ndovu vyote vinashiriki mchezo wa kandanda siku tofauti za juma.\n\n📌 **Kidokezo cha Kujifunza:**\nUnaposoma jedwali, kagua kila safu na safuwima ili kupata taarifa sahihi."
    },
    {
      "id": "kq11-2022",
      "questionNumber": 11,
      "questionText": "Ni kikundi kipi hakikushiriki uogeleaji?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q10-12",
      "options": [
        { "text": "Ndovu", "isCorrect": False },
        { "text": "Kifaru", "isCorrect": False },
        { "text": "Chui", "isCorrect": False },
        { "text": "Simba", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **Simba**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKwenye jedwali:\n- Kifaru: Uogeleaji (Jumatano)\n- Chui: Uogeleaji (Ijumaa)\n- Ndovu: Uogeleaji (Jumatatu)\n- **Simba:** Kandanda, Netiboli, Riadha. Kikundi cha Simba hakina mchezo wa Uogeleaji.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Ndovu, Kifaru, na Chui vinatekeleza mchezo wa uogeleaji katika siku tofauti.\n\n📌 **Kidokezo cha Kujifunza:**\nSoma maswali yenye neno \"hakikushiriki\" kwa umakini ili usichanganye jibu."
    },
    {
      "id": "kq12-2022",
      "questionNumber": 12,
      "questionText": "Ni kikundi kipi hakikushiriki riadha?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q10-12",
      "options": [
        { "text": "Simba", "isCorrect": False },
        { "text": "Chui", "isCorrect": False },
        { "text": "Ndovu", "isCorrect": True },
        { "text": "Kifaru", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Ndovu**.\n\n**Uchambuzi wa Jibu Sahihi:**\nJedwali linaonyesha michezo ya Ndovu kuwa: Uogeleaji (Jumatatu), Kandanda (Jumatano), na Netiboli (Ijumaa). Kikundi cha Ndovu hakishiriki Riadha.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Simba inashiriki Riadha Ijumaa.\n- Kifaru inashiriki Riadha Jumatatu.\n- Chui inashiriki Riadha Jumatano.\n\n📌 **Kidokezo cha Kujifunza:**\nKuhakikisha majibu ya jedwali ni jambo rahisi ukilinganisha safu ya kikundi na mchezo unaotajwa."
    },
    {
      "id": "kq13-2022",
      "questionNumber": 13,
      "questionText": "Wewe unajiandaa kupika ugali. Chagua jibu linaloonyesha hatua ya kwanza utakayozingatia.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q13-15",
      "options": [
        { "text": "Kuwa na vitu utakavyohitaji kupika ugali.", "isCorrect": True },
        { "text": "Kuinjika sufuria yenye maji jikoni.", "isCorrect": False },
        { "text": "Kuchukua mwiko na kuanza kukoroga.", "isCorrect": False },
        { "text": "Kuwa na kitoweo ambacho unahitaji.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Kuwa na vitu utakavyohitaji kupika ugali.**\n\n**Uchambuzi wa Jibu Sahihi:**\nKifungu kinasema wazi: \"Kwanza, unahitaji unga wa mahindi, maji, sufuria, mwiko na jiko la kupikia lenye moto.\" Hatua ya kwanza kabisa ni kuandaa vyombo na viungo unavyohitaji.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Kuinjika sufuria...:** Hii ni hatua inayofuata baada ya kupima maji na kuandaa vyombo.\n- **Kuchukua mwiko...:** Huku ni kukoroga baada ya maji kuchemka na kutia unga.\n- **Kuwa na kitoweo...:** Kitoweo ni cha kulia ugali baada ya kuiva au wakati wa kuandaa chakula.\n\n📌 **Kidokezo cha Kujifunza:**\nKatika uandishi wa maelekezo (resipi), hatua ya kwanza daima ni kukusanya vifaa na viungo vyote vinavyohitajika."
    },
    {
      "id": "kq14-2022",
      "questionNumber": 14,
      "questionText": "Unampikia nyanya kitoweo cha kuliwa kwa ugali. Chagua jibu linaloonyesha kitoweo chenye lishe bora.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q13-15",
      "options": [
        { "text": "Nyama na dagaa.", "isCorrect": False },
        { "text": "Kabeji na sukumawiki.", "isCorrect": False },
        { "text": "Samaki na mboga ya mchicha.", "isCorrect": True },
        { "text": "Maziwa na maharagwe.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Samaki na mboga ya mchicha.**\n\n**Uchambuzi wa Jibu Sahihi:**\nSamaki hutoa protini (ijengayo mwili) na mchicha hutoa vitamini na madini (yalindayo mwili). Mchanganyiko huu unaleta mlo kamili na wenye lishe bora kwa ugali (wanga).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Nyama na dagaa:** Vyote ni vyanzo vya protini bila mboga za majani (vitamini).\n- **Kabeji na sukumawiki:** Zote ni mboga za majani bila protini ya kutosha.\n- **Maziwa na maharagwe:** Vyote viwili ni vyanzo vya protini.\n\n📌 **Kidokezo cha Kujifunza:**\nMlo kamili wenye lishe bora una vyakula vya wanga (ugali), protini (samaki/nyama), na vitamini/madini (mchicha/mboga)."
    },
    {
      "id": "kq15-2022",
      "questionNumber": 15,
      "questionText": "Chagua jibu sahihi. Mchicha huupatia mwili vitamini, ugali huupatia mwili ____",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q13-15",
      "options": [
        { "text": "protini.", "isCorrect": False },
        { "text": "madini.", "isCorrect": False },
        { "text": "kinga.", "isCorrect": False },
        { "text": "wanga.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **wanga.**\n\n**Uchambuzi wa Jibu Sahihi:**\nUgali unaotokana na unga wa mahindi ni chakula cha kutia nguvu mwilini, yaani **wanga** (carbohydrates).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Protini:** Hupatikana katika nyama, samaki, maharagwe na maziwa (kujenga mwili).\n- **Madini / Kinga:** Hupatikana katika matunda na mboga za majani kama mchicha.\n\n📌 **Kidokezo cha Kujifunza:**\nVyakula vya wanga ni pamoja na ugali, mchele, muhogo, viazi na ngano. Neno la Kiswahili la Carbohydrates ni **wanga**."
    },
    {
      "id": "kq16-2022",
      "questionNumber": 16,
      "questionText": "Kanini ----16---- katika michezo mbalimbali tukiwa shuleni.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q16-20",
      "options": [
        { "text": "alishirikia", "isCorrect": False },
        { "text": "alishiriki", "isCorrect": True },
        { "text": "alishirikisha", "isCorrect": False },
        { "text": "alishirikiwa", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **alishiriki**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKitenzi cha msingi cha kujumuika au kufanya mchezo ni \"kushiriki\". Kwa hivyo, Kanini \"alishiriki katika michezo mbalimbali\".\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **alishirikia:** Kauli ya kutendea.\n- **alishirikisha:** Kauli ya kutendesha.\n- **alishirikiwa:** Kauli ya kutendwa.\n\n📌 **Kidokezo cha Kujifunza:**\nTumia kauli ya kutenda (alishiriki) badala ya miganyo ya mnyambuliko usiofaa."
    },
    {
      "id": "kq17-2022",
      "questionNumber": 17,
      "questionText": "Mchezo ----17---- alipenda zaidi ni netiboli.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q16-20",
      "options": [
        { "text": "ambao", "isCorrect": True },
        { "text": "ambaya", "isCorrect": False },
        { "text": "ambako", "isCorrect": False },
        { "text": "ambamo", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **ambao**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNeno \"Mchezo\" liko katika ngeli ya U-I (Umoja). Rejeshi ya o-rejeshi katika ngeli hii ni **ambao** (Mchezo ambao alipenda zaidi...).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **ambaya:** Neno lisilo sahihi kileksika.\n- **ambako / ambamo:** Haya ni marejeshi ya mahali (PO-KO-MO).\n\n📌 **Kidokezo cha Kujifunza:**\nNgeli ya U-I katika umoja hutumia rejeshi **ambao** (mfano: mti ambao, mchezo ambao)."
    },
    {
      "id": "kq18-2022",
      "questionNumber": 18,
      "questionText": "Kanini ----18---- na timu ya mchezo wa netiboli.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q16-20",
      "options": [
        { "text": "Alikuunga", "isCorrect": False },
        { "text": "Aliwaunga", "isCorrect": False },
        { "text": "Alijiunga", "isCorrect": True },
        { "text": "Alituunga", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Alijiunga**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNeno \"Alijiunga\" linamaanisha kuwa yeye mwenyewe alikua sehemu ya timu hiyo (\"Alijiunga na timu\").\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Alikuunga / Aliwaunga / Alituunga:** Yanahusu kuunga mtu mwingine au kikundi kingine.\n\n📌 **Kidokezo cha Kujifunza:**\nKiapishi cha irejeshi ya nafsi binafsi ni **-ji-** (mfano: alijikata, alijiunga)."
    },
    {
      "id": "kq19-2022",
      "questionNumber": 19,
      "questionText": "Netiboli ----19---- alipoingia darasa la tano.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q16-20",
      "options": [
        { "text": "huku", "isCorrect": False },
        { "text": "kama", "isCorrect": False },
        { "text": "tena", "isCorrect": False },
        { "text": "mara", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **mara**.\n\n**Uchambuzi wa Jibu Sahihi:**\nKiunganishi \"mara\" kinapotumiwa na \"-po-\" (mara alipoingia) kinaonyesha wakati sahihi ambapo kitendo kilitendeka mara tu alipofika darasa la tano.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **huku / kama / tena:** Havipatani na muundo wa kueleza wakati wa kuanza kwa kitendo mara moja.\n\n📌 **Kidokezo cha Kujifunza:**\nChetu cha wakati: \"mara alipo...\" ina maana ya mara tu kitendo kilipotokea."
    },
    {
      "id": "kq20-2022",
      "questionNumber": 20,
      "questionText": "Kanini alifahamu kuwa ----20----.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q16-20",
      "options": [
        { "text": "kila mwamba ngoma ngozi huivuta kwake", "isCorrect": False },
        { "text": "mtaka cha mvunguni sharti ainame", "isCorrect": True },
        { "text": "udongo upatilize uli maji", "isCorrect": False },
        { "text": "jifya moja haliinyiki chungu", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **mtaka cha mvunguni sharti ainame**.\n\n**Uchambuzi wa Jibu Sahihi:**\nMethali hii ina maana ya kwamba ukitaka kupata kitu kizuri au mafanikio (kama ushindi), lazima utie bidii na kufanya kazi kwa juhudi.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **kila mwamba ngoma...:** Inahusu ubinafsi wa mtu kujipendelea mwenyewe.\n- **udongo upatilize...:** Inahusu kufunza watoto wakiwa wadogo.\n- **jifya moja...:** Inahusu haja ya ushirikiano.\n\n📌 **Kidokezo cha Kujifunza:**\nMethali \"Mtaka cha mvunguni sharti ainame\" inahimiza bidii ili kupata mafanikio."
    },
    {
      "id": "kq21-2022",
      "questionNumber": 21,
      "questionText": "Wanafunzi wana nidhamu, ____ huheshimu walimu.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "wao", "isCorrect": True },
        { "text": "wewe", "isCorrect": False },
        { "text": "yeye", "isCorrect": False },
        { "text": "nyinyi", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **wao**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNeno \"Wanafunzi\" ni nomino ya wingi ya nafsi ya tatu (A-WA class). Kiwakilishi cha nafsi ya tatu wingi ni **wao**.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **wewe:** Nafsi ya pili umoja.\n- **yeye:** Nafsi ya tatu umoja.\n- **nyinyi:** Nafsi ya pili wingi.\n\n📌 **Kidokezo cha Kujifunza:**\nViwakilishi vya nafsi: Mimi (1 Umoja), Sisi (1 Wingi), Wewe (2 Umoja), Nyinyi (2 Wingi), Yeye (3 Umoja), Wao (3 Wingi)."
    },
    {
      "id": "kq22-2022",
      "questionNumber": 22,
      "questionText": "Tunasema, wingu ni kwa nzige. Tutasema, ____ ni kwa matunda.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "kitia", "isCorrect": False },
        { "text": "pakacha", "isCorrect": True },
        { "text": "bunda", "isCorrect": False },
        { "text": "robota", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **pakacha**.\n\n**Uchambuzi wa Jibu Sahihi:**\nNomino za makundi: Kundi la nzige wengi wanaoenda pamoja ni *wingu la nzige*. Kundi au kapu la matunda ni **pakacha la matunda**.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **bunda:** Mfano: bunda la fedha / noti.\n- **robota:** Mfano: robota la pamba / nguo.\n- **kitia:** Mfano: kitia cha chumvi / uta.\n\n📌 **Kidokezo cha Kujifunza:**\nNomino za Makundi: Pakacha la matunda, wingu la nzige, robota la pamba, bunda la noti."
    },
    {
      "id": "kq23-2022",
      "questionNumber": 23,
      "questionText": "Chagua wingi wa: Fundi yule hodari amejenga ukuta mrefu.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "Mafundi wale hodari wamejenga kuta ndefu.", "isCorrect": True },
        { "text": "Fundi wale hodari wamejenga ukuta mrefu.", "isCorrect": False },
        { "text": "Mafundi wale hodari wamejenga ukuta mrefu.", "isCorrect": False },
        { "text": "Fundi wale hodari wamejenga ukuta mrefu.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Mafundi wale hodari wamejenga kuta ndefu.**\n\n**Uchambuzi wa Jibu Sahihi:**\nKubadilisha sentensi nzima katika wingi:\n- Fundi -> Mafundi\n- yule -> wale\n- hodari -> hodari (kivumishi kisichobadilika)\n- amejenga -> wamejenga\n- ukuta mrefu -> kuta ndefu (Ngeli ya U-ZI: ukuta/kuta, mrefu/ndefu)\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Chagua zingine hazijabadilisha \"ukuta mrefu\" kuwa \"kuta ndefu\" au hazijabadilisha \"Fundi\" kuwa \"Mafundi\".\n\n📌 **Kidokezo cha Kujifunza:**\nKumbuka kubadilisha kila nomino, kivumishi, kiashiria na kitenzi katika wingi wake sahihi."
    },
    {
      "id": "kq24-2022",
      "questionNumber": 24,
      "questionText": "Kimeto alimsaidia Kamaa kuchora picha. Kamaa alikuwa ameumia mkono. Kwa hivyo, Kimeto ____",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "alimchoresha Kamaa picha.", "isCorrect": False },
        { "text": "alimchorea Kamaa picha.", "isCorrect": True },
        { "text": "alichoreshwa picha na Kamaa.", "isCorrect": False },
        { "text": "alichoreshea Kamaa picha.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **alimchorea Kamaa picha.**\n\n**Uchambuzi wa Jibu Sahihi:**\nKauli ya Kutendea hutumiwa kufanya kitendo kwa niaba ya mtu mwingine au kwa ajili yake. Kuchora -> Kuchorea. Kwa hivyo Kimeto \"alimchorea Kamaa picha\".\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **alimchoresha:** Kauli ya kutendesha.\n- **alichoreshwa:** Kauli ya kutendwa pasipo.\n- **alichoreshea:** Mnyambuliko usiofaa hapa.\n\n📌 **Kidokezo cha Kujifunza:**\nKauli ya Kutendea huonyesha kufanya kitendo kwa ajili ya mtu mwingine (mfano: soma -> somea, chora -> chorea)."
    },
    {
      "id": "kq25-2022",
      "questionNumber": 25,
      "questionText": "Ni sentensi ipi sahihi?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "Palipo na rutuba panafaa kwa kilimo.", "isCorrect": True },
        { "text": "Palipo na rutuba kunafaa kwa kilimo.", "isCorrect": False },
        { "text": "Mlimo na rutuba panafaa kwa kilimo.", "isCorrect": False },
        { "text": "Mlimo na rutuba kunafaa kwa kilimo.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Palipo na rutuba panafaa kwa kilimo.**\n\n**Uchambuzi wa Jibu Sahihi:**\nNgeli ya PA-KU-MU (Mahali). Kiambishi kinacholingana na \"Palipo\" (PA- mahali dhahiri) ni **panafaa** (PA-).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **kunafaa:** Kitatumiwa na \"Kuliko\".\n- **Mlimo na...:** Neno \"Mlimo\" kumaanisha kilimo halilingani na rutuba wala muundo sahihi.\n\n📌 **Kidokezo cha Kujifunza:**\nUpatanisho wa Kiarifa katika Ngeli ya Mahali: Palipo -> panafaa, Kuliko -> kunafaa, Mlimo -> munafaa."
    },
    {
      "id": "kq26-2022",
      "questionNumber": 26,
      "questionText": "Ni sentensi ipi iliyoafikishwa vyema?",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "Neema amefika: kwetu leo asubuhi.", "isCorrect": False },
        { "text": "Mwachia amenunua machungwa, maembe na papai.", "isCorrect": True },
        { "text": "Je, umeandika barua ya kuomba msamaha.", "isCorrect": False },
        { "text": "Salaale Kalama amefunga bao lingine.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Mwachia amenunua machungwa, maembe na papai.**\n\n**Uchambuzi wa Jibu Sahihi:**\nSentensi hii imetumia alama ya mkato (,) kutenganisha vitu vinavyoorodheshwa na kuishia na alama ya kituo (.).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **A:** Imetumia nukta mbili (:) mahali pasipofaa baada ya kitenzi.\n- **C:** Imetumia kituo (.) badala ya alama ya ulizo (?) mwishoni mwa swali linazoanza na \"Je,\".\n- **D:** Neno \"Salaale\" ni hisia/mshangao kwa hivyo lilihitaji alama ya hisi (!).\n\n📌 **Kidokezo cha Kujifunza:**\nAlama za Uandishi: Swali linaloanza na \"Je\" lazima liishe na **?**. Orodha ya vitu hutenganishwa na **,.**"
    },
    {
      "id": "kq27-2022",
      "questionNumber": 27,
      "questionText": "Chagua ukubwa wa sentensi ifuatayo: Mlango wa nyumba yake unapendeza.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "Lango la jumba lake linapendeza.", "isCorrect": True },
        { "text": "Mlango wa jumba lake linapendeza.", "isCorrect": False },
        { "text": "Lango la nyumba yake linapendeza.", "isCorrect": False },
        { "text": "Mlango wa nyumba yake linapendeza.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **Lango la jumba lake linapendeza.**\n\n**Uchambuzi wa Jibu Sahihi:**\nUbadilishaji wa Sentensi katika Ukubwa:\n- Mlango -> Lango\n- nyumba -> jumba\n- yake -> lake\n- unapendeza -> linapendeza (ngeli ya LI-YA katika ukubwa: Lango la jumba lake linapendeza).\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- Chagua zingine hazijabadilisha maneno yote katika hali ya ukubwa.\n\n📌 **Kidokezo cha Kujifunza:**\nKatika hali ya ukubwa, Nomino nyingi huingia katika ngeli ya LI-YA (mfano: mlango -> lango/la, nyumba -> jumba/la)."
    },
    {
      "id": "kq28-2022",
      "questionNumber": 28,
      "questionText": "Chagua jibu lisilo sahihi.",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "Tita la kuni.", "isCorrect": False },
        { "text": "Thureya ya nyota.", "isCorrect": False },
        { "text": "Kicha cha funguo.", "isCorrect": False },
        { "text": "Kilinge cha wanariadha.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **Kilinge cha wanariadha.**\n\n**Uchambuzi wa Jibu Sahihi:**\nNomino ya kundi \"Kilinge\" hutumika kwa waganga au wachawi (Kilinge cha waganga). Kundi la wanariadha huitwa *kikundi* au *timu ya wanariadha*.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **Tita la kuni:** Ni kundi sahihi la kuni zilizofungwa pamoja.\n- **Thureya ya nyota:** Ni kundi sahihi la nyota nyingi angani.\n- **Kicha cha funguo:** Ni kundi sahihi la funguo zilizoshikanishwa.\n\n📌 **Kidokezo cha Kujifunza:**\nNomino za Makundi: Kilinge cha waganga/wachawi, Tita la kuni, Kicha cha funguo, Thureya ya nyota."
    },
    {
      "id": "kq29-2022",
      "questionNumber": 29,
      "questionText": "Tunastahili kupiga chafya kwenye kiwiko cha mkono. Kupiga chafya ni ____",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "kuchemua.", "isCorrect": True },
        { "text": "kukohoa.", "isCorrect": False },
        { "text": "kutema.", "isCorrect": False },
        { "text": "kupenga.", "isCorrect": False }
      ],
      "explanation": "Jibu sahihi ni **kuchemua.**\n\n**Uchambuzi wa Jibu Sahihi:**\nKupiga chafya (sneeze) kwa Kiswahili ni **kuchemua**.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **kukohoa:** Ni kutoa sauti ya koo wakati wa kikohozi (cough).\n- **kutema:** Ni kutoa mate mdomoni (spit).\n- **kupenga:** Ni kutoa kamasi puani (blow nose).\n\n📌 **Kidokezo cha Kujifunza:**\nManeno ya vitendo vya mwili: Kupiga chafya = kuchemua, Kupenga = kutoa kamasi, Kukohoa = kutoa kikohozi."
    },
    {
      "id": "kq30-2022",
      "questionNumber": 30,
      "questionText": "Simon ni wembe masomoni. Kauli hii ina maana kuwa Simon ni:",
      "questionType": "mcq",
      "contextRef": "ctx-kisw-2022-q21-30",
      "options": [
        { "text": "mwenye subira.", "isCorrect": False },
        { "text": "jasiri.", "isCorrect": False },
        { "text": "mwenye bidii.", "isCorrect": False },
        { "text": "mwerevu.", "isCorrect": True }
      ],
      "explanation": "Jibu sahihi ni **mwerevu.**\n\n**Uchambuzi wa Jibu Sahihi:**\nNahau au msemo \"Kuwa wembe masomoni\" ina maana ya kuwa na akili nyingi au kuwa **mwerevu** mwingi masomoni.\n\n**Kwa Nini Majibu Mengine Siyo Sahihi:**\n- **mwenye subira:** Asiye na haraka au mvumilivu.\n- **jasiri:** Mtu asiyeogopa (shujaa).\n- **mwenye bidii:** Mtu anayejitahidi na kufanya kazi kwa juhudi.\n\n📌 **Kidokezo cha Kujifunza:**\nMsemo: \"Wembe masomoni\" humaanisha mtu mwerevu au mwenye akili sana masomoni."
    }
  ]
}

js_content = "export const kpseaKiswahili2022 = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"

with open('src/data/kpsea-kiswahili-2022.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('Successfully created src/data/kpsea-kiswahili-2022.js!')
