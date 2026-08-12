import json
import base64

new_contexts = {
    "ctx-kisw-2025-q21-25": {
        "title": "Soma kifungu kifuatacho kisha ujibu swali la 21 hadi la 25.",
        "type": "text",
        "text": "(Ni uwanjani. Wanafunzi wanafanya mazoezi ya mwili. Tezi na Nira wanakimbia polepole huku wakizungumza.)\n\nTezi: (Akimsogelea.) Hali vipi Nira?\nNira: Nzuri sana dada. Nawe waendelea vipi?\nTezi: (Kwa furaha.) __21__. Ninaendelea kufanya mazoezi. Si unajua ni wakati wa matayarisho ya michuano ya futiboli? Timu yetu inajikaza kisabuni. Unajua, ajizi ni ...\nNira: (Akidakia.) Nyumba ya njaa, eti. Hata sisi tunajikakamua.\nTezi: (Akihema.) Hapo sawa mwenzangu! Mwaka jana tulinyakua kombe. Tunatumai mwaka huu pia tutalileta kwetu. Wavulana wote wameamua liwe liwalo, ushindi utabaki kwetu.\nNira: Hali kadhalika, kwa upande wa timu yetu, mabanati hawalali. Tumeamua kuwa sharti tulinyakue kombe mwaka huu. Mwaka jana lilitupita.\nTezi: (Akipunguza mwendo.) Wacha nipumue kidogo. Nimekimbia kwa muda mrefu; moyo wangu unadunda. Nikiendelea hivi nitaanguka.\nNira: (Akisimama.) __24__. Hakika hata mimi ninahitaji kupumzika sasa. Kwaheri. Tutaonana kesho tena.\nTezi: (Akimtazama.) Nami nitakufuata punde.\n(Wanaagana.)"
    },
    "ctx-kisw-2025-q26-35": {
        "title": "Kifungu kifuatacho kina nafasi 26 hadi 35. Chagua jibu lifaalo zaidi kujaza nafasi kati ya majibu manne uliyopewa baada ya kifungu.",
        "type": "text",
        "text": "\"Daktari __26__ tembe za kumezea hapa na __27__ za kubeba.\" Muuguzi alimweleza Topasa. \"Hakikisha kuwa __28__ mara tatu kwa siku,\" aliendelea muuguzi.\n\"__29__ Ninafahamu kuwa __30__ maradhi ni ghali kuliko kuyazuia.\" Topasa alijibu kwa sauti ya unyonge.\nTopasa __31__ unyounyo huku amebeba bahasha ya dawa na kuelekea nyumbani. Kwa siku tano __32__, Topasa __33__ maagizo ya daktari. Alikula chakula chenye virutubishi __34__ kumeza dawa. __35__ kazi ngumu, alipumzika nyumbani."
    }
}

new_questions = [
    {
        "id": "q21", "questionNumber": 21,
        "questionText": "Chagua jibu lenye kauli sahihi kujaza nafasi ya 21 katika kifungu.",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q21-25",
        "options": [
            {"text": "Napenda hivyo.", "isCorrect": False},
            {"text": "Ni mzima.", "isCorrect": True},
            {"text": "Ndio hali.", "isCorrect": False},
            {"text": "Nafurahi kukuona.", "isCorrect": False}
        ],
        "explanation": "Nira aliuliza \"Nawe waendelea vipi?\". Jibu mwafaka la kujulisha hali yake ya kiafya ni \"Ni mzima\" (Mimi ni mzima)."
    },
    {
        "id": "q22", "questionNumber": 22,
        "questionText": "Chagua maneno yanayoonyesha kuwa Nira aliweza kukamilisha kauli ya Tezi wakati wa mazungumzo.",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q21-25",
        "options": [
            {"text": "Tutaonana kesho tena", "isCorrect": False},
            {"text": "Nyumba ya njaa", "isCorrect": True},
            {"text": "Mwaka jana tulinyakua kombe", "isCorrect": False},
            {"text": "Wacha nipumue kidogo", "isCorrect": False}
        ],
        "explanation": "Tezi alianza kusema methali \"Unajua, ajizi ni ...\" na kabla hajamaliza, Nira alidakia na kuikamilisha kwa kusema \"Nyumba ya njaa, eti.\""
    },
    {
        "id": "q23", "questionNumber": 23,
        "questionText": "Ni yepi kati ya maneno yafuatayo yanayoonyesha kuwa wahusika walikuwa na uhusiano wa karibu?",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q21-25",
        "options": [
            {"text": "Hapo sawa mwenzangu", "isCorrect": True},
            {"text": "Mwaka jana lilitupita", "isCorrect": False},
            {"text": "Timu yetu inajikaza", "isCorrect": False},
            {"text": "Nami nitakufuata punde", "isCorrect": False}
        ],
        "explanation": "Matumizi ya neno \"mwenzangu\" (my companion/friend) yanaonyesha ukaribu na urafiki uliopo baina ya Tezi na Nira."
    },
    {
        "id": "q24", "questionNumber": 24,
        "questionText": "Chagua neno ambalo Nira angetumia katika nafasi ya 24 kwenye mazungumzo.",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q21-25",
        "options": [
            {"text": "Basi", "isCorrect": False},
            {"text": "Pole", "isCorrect": True},
            {"text": "Kunradhi", "isCorrect": False},
            {"text": "Tafadhali", "isCorrect": False}
        ],
        "explanation": "Tezi alilalamika kuwa amechoka, anashindwa kupumua vizuri, na akiendelea ataanguka. Jibu mwafaka la kumpa pole au kumhurumia kwa uchovu huo ni kumwambia \"Pole\"."
    },
    {
        "id": "q25", "questionNumber": 25,
        "questionText": "Ni ishara gani ambayo Nira alistahili kutumia alipomuaga Tezi?",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q21-25",
        "options": [
            {"text": "Kutikisa kichwa", "isCorrect": False},
            {"text": "Kuinua mabega", "isCorrect": False},
            {"text": "Kupepesa macho", "isCorrect": False},
            {"text": "Kumpungia mkono", "isCorrect": True}
        ],
        "explanation": "Nira anasema \"Kwaheri. Tutaonana kesho tena.\" Ishara inayoambatana na kusema kwaheri ni kumpungia mtu mkono."
    },
    {
        "id": "q26", "questionNumber": 26,
        "questionText": "Nafasi ya 26:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "amekupatia", "isCorrect": True},
            {"text": "akikupatia", "isCorrect": False},
            {"text": "angekupatia", "isCorrect": False},
            {"text": "akakupatia", "isCorrect": False}
        ],
        "explanation": "Wakati unaofaa ni wakati uliopo mkamilifu (present perfect) kwa sababu kitendo cha kupewa dawa kimefanyika na matokeo bado yapo. Kwa hivyo, 'amekupatia' ni sahihi."
    },
    {
        "id": "q27", "questionNumber": 27,
        "questionText": "Nafasi ya 27:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "kingine", "isCorrect": False},
            {"text": "mingine", "isCorrect": False},
            {"text": "nyingine", "isCorrect": True},
            {"text": "lingine", "isCorrect": False}
        ],
        "explanation": "Neno 'tembe' liko katika ngeli ya I-ZI au N-N. Wingi wake huchukua kiambishi 'ny' (tembe nyingine)."
    },
    {
        "id": "q28", "questionNumber": 28,
        "questionText": "Nafasi ya 28:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "anameza", "isCorrect": False},
            {"text": "unameza", "isCorrect": True},
            {"text": "tunameza", "isCorrect": False},
            {"text": "mnameza", "isCorrect": False}
        ],
        "explanation": "Muuguzi anazungumza moja kwa moja na Topasa. Hivyo, anatumia nafsi ya pili umoja (wewe), ambayo huchukua kiambishi 'u' -> unameza."
    },
    {
        "id": "q29", "questionNumber": 29,
        "questionText": "Nafasi ya 29:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "\"Nitazingatia maagizo yako, muuguzi.", "isCorrect": False},
            {"text": "\"Nitazingatia maagizo yako, muuguzi?", "isCorrect": False},
            {"text": "\"Nitazingatia maagizo yako, muuguzi!\"", "isCorrect": False},
            {"text": "\"Nitazingatia maagizo yako, muuguzi.\"", "isCorrect": True}
        ],
        "explanation": "Sentensi hii inaanza kwa alama ya mtajo (\") na ni kauli ya kawaida, kwa hivyo inafaa kuisha kwa kituo/nukta na kufungwa kwa alama ya mtajo (\")."
    },
    {
        "id": "q30", "questionNumber": 30,
        "questionText": "Nafasi ya 30:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "kuambua", "isCorrect": False},
            {"text": "kuchunguza", "isCorrect": False},
            {"text": "kufahamu", "isCorrect": False},
            {"text": "kutibu", "isCorrect": True}
        ],
        "explanation": "Methali inasema, \"Kutibu maradhi ni ghali kuliko kuyazuia\" (Prevention is better than cure)."
    },
    {
        "id": "q31", "questionNumber": 31,
        "questionText": "Nafasi ya 31:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "alitembeleana", "isCorrect": False},
            {"text": "alitembelea", "isCorrect": False},
            {"text": "alitembea", "isCorrect": True},
            {"text": "alitembelewa", "isCorrect": False}
        ],
        "explanation": "Msemo 'kutembea unyounyo' humaanisha kutembea polepole, labda kutokana na uchovu au unyonge. Neno mwafaka ni 'alitembea'."
    },
    {
        "id": "q32", "questionNumber": 32,
        "questionText": "Nafasi ya 32:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "zilivyofuata", "isCorrect": False},
            {"text": "zilizofuata", "isCorrect": True},
            {"text": "zilikofuata", "isCorrect": False},
            {"text": "zilipofuata", "isCorrect": False}
        ],
        "explanation": "Siku ni nomino ya ngeli ya I-ZI, kwa hivyo wingi wake (siku tano) unachukua kiambishi 'zi'. Kwa hiyo, 'zilizofuata' (zile ambazo zilifuata)."
    },
    {
        "id": "q33", "questionNumber": 33,
        "questionText": "Nafasi ya 33:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "alitia bidii", "isCorrect": False},
            {"text": "alitia hamu", "isCorrect": False},
            {"text": "alitia fora", "isCorrect": False},
            {"text": "alitia maanani", "isCorrect": True}
        ],
        "explanation": "Kutia maanani inamaanisha kuchukua jambo kwa uzito au kutilia mkazo. Topasa alitilia maanani maagizo ya daktari."
    },
    {
        "id": "q34", "questionNumber": 34,
        "questionText": "Nafasi ya 34:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "kabla ya", "isCorrect": True},
            {"text": "fauka ya", "isCorrect": False},
            {"text": "badala ya", "isCorrect": False},
            {"text": "ndani ya", "isCorrect": False}
        ],
        "explanation": "Kawaida, wagonjwa hushauriwa kula kwanza kabla ya kumeza dawa. Hivyo 'kabla ya' ndilo jibu mwafaka."
    },
    {
        "id": "q35", "questionNumber": 35,
        "questionText": "Nafasi ya 35:",
        "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q26-35",
        "options": [
            {"text": "Hutafanya", "isCorrect": False},
            {"text": "Hukufanya", "isCorrect": False},
            {"text": "Hatafanya", "isCorrect": False},
            {"text": "Hakufanya", "isCorrect": True}
        ],
        "explanation": "Mhusika anazungumziwa katika nafsi ya tatu umoja (yeye) na wakati uliopita, ambayo huchukua kiambishi cha ukanusho 'haku-'. Kwa hivyo 'Hakufanya'."
    },
    {
        "id": "q36", "questionNumber": 36,
        "questionText": "Kutoka swali la 36 hadi la 50, chagua jibu sahihi.\n\nManeno bao na mbao yana sauti zinazokaribiana. Je, ni neno lipi lenye sauti zinazokaribiana kimatamshi na neno dhamani.",
        "questionType": "multiple-choice",
        "options": [
            {"text": "samani", "isCorrect": False},
            {"text": "thamani", "isCorrect": True},
            {"text": "jamani", "isCorrect": False},
            {"text": "ramani", "isCorrect": False}
        ],
        "explanation": "Sauti 'dh' na 'th' zinakaribiana sana kimatamshi (fricatives) katika lugha ya Kiswahili, hivyo 'dhamani' na 'thamani' yana sauti zinazokaribiana."
    },
    {
        "id": "q37", "questionNumber": 37,
        "questionText": "Chagua jibu lenye maana kuwa 'Katu alisafisha chumba kwa niaba ya Bili.'",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Katu na Bili walisafisha chumba.", "isCorrect": False},
            {"text": "Katu alisafishiwa chumba cha Bili.", "isCorrect": False},
            {"text": "Katu alimsafishia Bili chumba.", "isCorrect": True},
            {"text": "Katu na Bili walisafishiwa chumba.", "isCorrect": False}
        ],
        "explanation": "Kauli ya kutendea (prepositional form) inatumika kuonyesha kufanya jambo kwa niaba ya mtu mwingine. 'Kusafishia' inamaanisha kusafisha kwa niaba ya au kwa faida ya (Bili)."
    },
    {
        "id": "q38", "questionNumber": 38,
        "questionText": "Chagua kiambishi sahihi kukamilisha nafasi katika sentensi ifuatayo:\nNgozi nyeusi __litumiwa kutengeneza viatu hivi.",
        "questionType": "multiple-choice",
        "options": [
            {"text": "zi", "isCorrect": True},
            {"text": "ya", "isCorrect": False},
            {"text": "vi", "isCorrect": False},
            {"text": "wa", "isCorrect": False}
        ],
        "explanation": "Neno 'ngozi' likiwa katika wingi linafuata upatanisho wa ngeli ya U-ZI (ngozi hizi). Kiambishi chake cha kitenzi ni 'zi' (zilitumiwa)."
    },
    {
        "id": "q39", "questionNumber": 39,
        "questionText": "Karisa alipofika alipata Lulu ameondoka mapema. Kwa hivyo,",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Karisa alifika kwani alipata Lulu ameondoka mapema.", "isCorrect": False},
            {"text": "Karisa alifika lakini alipata Lulu ameondoka mapema.", "isCorrect": True},
            {"text": "Karisa alifika pia alimpata Lulu ameondoka mapema.", "isCorrect": False},
            {"text": "Karisa alifika lau alimpata Lulu ameondoka mapema.", "isCorrect": False}
        ],
        "explanation": "Kuna hali ya kinyume au kutofanikiwa katika matarajio. Karisa alifika ili amkute Lulu, lakini kwa bahati mbaya akampata ameondoka. 'Lakini' ndicho kiunganishi mwafaka."
    },
    {
        "id": "q40", "questionNumber": 40,
        "questionText": "Chagua sentensi ambayo ni ukanusho wa sentensi ifuatayo:\nJuma angemaliza mtihani wake angepata cheti.",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Juma asipomaliza mtihani wake hatapata cheti.", "isCorrect": False},
            {"text": "Juma hajamaliza mtihani wake hatapata cheti.", "isCorrect": False},
            {"text": "Juma asingalimaliza mtihani wake asingalipata cheti.", "isCorrect": False},
            {"text": "Juma asingemaliza mtihani wake asingepata cheti.", "isCorrect": True}
        ],
        "explanation": "Wakati tegemezi '-nge-' unakanushwa kwa kutumia '-singe-'. Kwa hiyo, 'angemaliza' -> 'asingemaliza' na 'angepata' -> 'asingepata'."
    },
    {
        "id": "q41", "questionNumber": 41,
        "questionText": "Leona alimfanya Toni aandike barua ya kuomba msamaha. Chagua jibu sahihi kutokana na maelezo haya:",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Leona alimwandikia Toni barua ya kuomba msamaha.", "isCorrect": False},
            {"text": "Leona aliandikiwa na Toni barua ya kuomba msamaha.", "isCorrect": False},
            {"text": "Leona alimwandikisha Toni barua ya kuomba msamaha.", "isCorrect": True},
            {"text": "Leona na Toni waliandikiana barua ya kuomba msamaha.", "isCorrect": False}
        ],
        "explanation": "Kauli ya kutendesha (causative) inatumika hapa. Kumfanya mtu afanye jambo (andika) inakuwa 'andikisha'. Hivyo Leona alimwandikisha Toni."
    },
    {
        "id": "q42", "questionNumber": 42,
        "questionText": "Usemi halisi wa sentensi, Tiriki alitangaza kuwa vijana wangefaidika na miradi ya kujiendeleza mwaka huo, ni",
        "questionType": "multiple-choice",
        "options": [
            {"text": "\"Vijana watafaidika na miradi ya kujiendeleza mwaka huu,\" Tiriki alitangaza.", "isCorrect": True},
            {"text": "\"Vijana wangefaidika na miradi ya kujiendeleza mwaka huo.\" Tiriki alitangaza.", "isCorrect": False},
            {"text": "\"Vijana watafaidika na miradi ya kujiendeleza mwaka huo.\" Tiriki alitangaza.", "isCorrect": False},
            {"text": "\"Vijana wangefaidika na miradi ya kujiendeleza mwaka huu,\" Tiriki alitangaza.", "isCorrect": False}
        ],
        "explanation": "Katika usemi halisi, 'wangefaidika' (past conditional) inarudi kuwa 'watafaidika' (future), na 'mwaka huo' (that year) inarudi kuwa 'mwaka huu' (this year)."
    },
    {
        "id": "q43", "questionNumber": 43,
        "questionText": "Chagua sentensi iliyo katika hali ya udogo.",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Bwawa la mto huo linawafaa wakaaji wa kijiji hicho.", "isCorrect": False},
            {"text": "Kibwawa cha kijito hicho kinawafaa wakaaji wa kijiji chao.", "isCorrect": True},
            {"text": "Kibwawa cha mto huo kinawafaa wakaaji wa mji huo.", "isCorrect": False},
            {"text": "Bwawa la kijito hicho linawafaa wakaaji wa mji wao.", "isCorrect": False}
        ],
        "explanation": "Udogo wa bwawa ni kibwawa, mto ni kijito, na mji ni kijiji. Jibu lenye nomino zote katika hali ya udogo ni B (Kibwawa, kijito, kijiji)."
    },
    {
        "id": "q44", "questionNumber": 44,
        "questionText": "Chagua jibu lenye sentensi iliyounganishwa ifaavyo kutokana na sentensi:\nUgonjwa ulimdhoofisha. Ugonjwa ulitafutiwa tiba.",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Ugonjwa ulimdhoofisha kisha ulitafutiwa tiba.", "isCorrect": True},
            {"text": "Ugonjwa ulimdhoofisha aghalabu ulitafutiwa tiba.", "isCorrect": False},
            {"text": "Ugonjwa ulimdhoofisha japo ulitafutiwa tiba.", "isCorrect": False},
            {"text": "Ugonjwa ulimdhoofisha sembuse ulitafutiwa tiba.", "isCorrect": False}
        ],
        "explanation": "Kuunganisha matukio mawili yaliyofuatana kimantiki inahitaji kiunganishi cha mfululizo. 'Kisha' (then) inaonyesha mfuatano sahihi (kwanza ulimdhoofisha, kisha ukatafutiwa tiba)."
    },
    {
        "id": "q45", "questionNumber": 45,
        "questionText": "Ni maneno yepi ambayo yameambatanishwa tofauti na mengine?",
        "questionType": "multiple-choice",
        "options": [
            {"text": "pakia - pakua", "isCorrect": False},
            {"text": "nenda - rudi", "isCorrect": False},
            {"text": "sogea - karibia", "isCorrect": True},
            {"text": "kusanya - tawanya", "isCorrect": False}
        ],
        "explanation": "Jozi ya A, B, na D zinaonyesha maneno yenye maana kinyume (antonyms). Hata hivyo, 'sogea' na 'karibia' yana maana sawa (visawe/synonyms). Hivyo yameambatanishwa tofauti."
    },
    {
        "id": "q46", "questionNumber": 46,
        "questionText": "Chagua jibu sahihi.\nNeema alimchezea Karobi gitaa naye Karobi akamchezea Neema gitaa. Kwa hivyo:",
        "questionType": "multiple-choice",
        "options": [
            {"text": "walichezeana", "isCorrect": True},
            {"text": "walichezewa", "isCorrect": False},
            {"text": "walichezeka", "isCorrect": False},
            {"text": "walichezwa", "isCorrect": False}
        ],
        "explanation": "Kitendo kilichofanywa na pande zote mbili (reciprocal) huchukua kiambishi cha kauli ya kutendeana, yaani '-ana'. Kwa hivyo walichezeana gitaa."
    },
    {
        "id": "q47", "questionNumber": 47,
        "questionText": "Sentensi, 'Wadudu hatari wanaendelea kupungua kutokana na juhudi zinazowekwa za kuwadhibiti' katika wakati uliopita ni:",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Wadudu hatari wataendelea kupungua kutokana na juhudi zitakazowekwa za kuwadhibiti.", "isCorrect": False},
            {"text": "Wadudu hatari waliendelea kupungua kutokana na juhudi zilizowekwa za kuwadhibiti.", "isCorrect": True},
            {"text": "Wadudu hatari wameendelea kupungua kutokana na juhudi zilizowekwa za kuwadhibiti.", "isCorrect": False},
            {"text": "Wadudu hatari wanaendelea kupungua kutokana na juhudi zitakazowekwa za kuwadhibiti.", "isCorrect": False}
        ],
        "explanation": "Wakati uliopita hutumia kiambishi '-li-'. Kwa hivyo 'wanaendelea' inakuwa 'waliendelea' na 'zinazowekwa' inakuwa 'zilizowekwa'."
    },
    {
        "id": "q48", "questionNumber": 48,
        "questionText": "Ni jibu lipi ambalo ni wingi wa sentensi: 'Ua uliopandwa na mfanyakazi kuzunguka boma lake umenawiri.'",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Nyua zilizopandwa na mfanyakazi kuzunguka boma lake zimenawiri.", "isCorrect": False},
            {"text": "Nyua zilizopandwa na wafanyakazi kuzunguka boma lake zimenawiri.", "isCorrect": False},
            {"text": "Nyua zilizopandwa na wafanyakazi kuzunguka maboma yao zimenawiri.", "isCorrect": True},
            {"text": "Nyua zilizopandwa na mfanyakazi kuzunguka maboma yao zimenawiri.", "isCorrect": False}
        ],
        "explanation": "Wingi wa 'ua' (fence) ni 'nyua'. Wingi wa 'mfanyakazi' ni 'wafanyakazi', 'boma lake' inakuwa 'maboma yao', na 'umenawiri' inakuwa 'zimenawiri'. Chaguo C liko sahihi kwa maneno yote."
    },
    {
        "id": "q49", "questionNumber": 49,
        "questionText": "Ni sentensi ipi iliyo katika hali ya mazoea?",
        "questionType": "multiple-choice",
        "options": [
            {"text": "Mwangaza huo unatokana na taa hiyo.", "isCorrect": False},
            {"text": "Ukiipenda nguo hiyo hutakosa pesa za kuinunua.", "isCorrect": False},
            {"text": "Huenda watampata nyumbani kwake kesho.", "isCorrect": False},
            {"text": "Fisi wakishirikiana huweza kumfukuza hata simba.", "isCorrect": True}
        ],
        "explanation": "Hali ya mazoea inatambulishwa na kiambishi 'hu-' ambacho kinatumika kuonyesha tabia au jambo linalofanyika mara kwa mara. Katika jibu D, neno 'huweza' linaonyesha hali hii."
    },
    {
        "id": "q50", "questionNumber": 50,
        "questionText": "Ujanja ni kwa sungura ilhali hekima ni kwa",
        "questionType": "multiple-choice",
        "options": [
            {"text": "kobe.", "isCorrect": True},
            {"text": "njiwa.", "isCorrect": False},
            {"text": "fisi.", "isCorrect": False},
            {"text": "simba.", "isCorrect": False}
        ],
        "explanation": "Katika hadithi za fasihi simulizi za Kiswahili, sungura huaminika kuwa na ujanja/hila nyingi ilhali kobe hujulikana kwa hekima na busara."
    }
]

with open("src/data/kjsea-kiswahili-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaKiswahili2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

data["sharedContexts"].update(new_contexts)
data["sectionA"].extend(new_questions)

with open("src/data/kjsea-kiswahili-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaKiswahili2025 = {json.dumps(data, indent=2)};\n")
