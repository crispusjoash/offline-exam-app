import json
import os

svg_table = """<svg viewBox="0 0 600 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <style>
    .header { font-weight: bold; font-family: sans-serif; font-size: 14px; }
    .row { font-family: sans-serif; font-size: 14px; }
    .line { stroke: black; stroke-width: 1; }
  </style>
  <rect width="600" height="300" fill="white"/>
  
  <!-- Vertical lines -->
  <line x1="10" y1="10" x2="10" y2="290" class="line"/>
  <line x1="150" y1="10" x2="150" y2="290" class="line"/>
  <line x1="240" y1="10" x2="240" y2="290" class="line"/>
  <line x1="330" y1="10" x2="330" y2="290" class="line"/>
  <line x1="420" y1="10" x2="420" y2="290" class="line"/>
  <line x1="510" y1="10" x2="510" y2="290" class="line"/>
  <line x1="590" y1="10" x2="590" y2="290" class="line"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="10" x2="590" y2="10" class="line" stroke-width="2"/>
  <line x1="10" y1="50" x2="590" y2="50" class="line" stroke-width="2"/>
  
  <line x1="10" y1="84" x2="590" y2="84" class="line"/>
  <line x1="10" y1="118" x2="590" y2="118" class="line"/>
  <line x1="10" y1="152" x2="590" y2="152" class="line"/>
  <line x1="10" y1="186" x2="590" y2="186" class="line"/>
  <line x1="10" y1="220" x2="590" y2="220" class="line"/>
  <line x1="10" y1="254" x2="590" y2="254" class="line"/>
  <line x1="10" y1="288" x2="590" y2="288" class="line" stroke-width="2"/>

  <!-- Headers -->
  <text x="20" y="35" class="header">Klabu</text>
  <text x="160" y="35" class="header">Jumatatu</text>
  <text x="250" y="35" class="header">Jumanne</text>
  <text x="340" y="35" class="header">Jumatano</text>
  <text x="430" y="35" class="header">Alhamisi</text>
  <text x="525" y="35" class="header">Ijumaa</text>

  <defs>
    <path id="check" d="M -5 0 L 0 5 L 10 -10" stroke="black" stroke-width="2" fill="none"/>
  </defs>

  <!-- Skauti -->
  <text x="20" y="72" class="row">Skauti</text>
  <use href="#check" x="195" y="70" />
  <use href="#check" x="285" y="70" />
  <use href="#check" x="465" y="70" />

  <!-- Michezo -->
  <text x="20" y="106" class="row">Michezo</text>
  <use href="#check" x="375" y="104" />

  <!-- Densi -->
  <text x="20" y="140" class="row">Densi</text>
  <use href="#check" x="195" y="138" />
  <use href="#check" x="465" y="138" />

  <!-- Majadiliano -->
  <text x="20" y="174" class="row">Majadiliano</text>
  <use href="#check" x="195" y="172" />
  <use href="#check" x="285" y="172" />
  <use href="#check" x="465" y="172" />
  <use href="#check" x="550" y="172" />

  <!-- Kilimo -->
  <text x="20" y="208" class="row">Kilimo</text>
  <use href="#check" x="375" y="206" />
  <use href="#check" x="550" y="206" />

  <!-- Mazingira -->
  <text x="20" y="242" class="row">Mazingira</text>
  <use href="#check" x="195" y="240" />
  <use href="#check" x="285" y="240" />
  <use href="#check" x="375" y="240" />
  <use href="#check" x="465" y="240" />
  <use href="#check" x="550" y="240" />

  <!-- Upishi -->
  <text x="20" y="276" class="row">Upishi</text>
  <use href="#check" x="285" y="274" />
  <use href="#check" x="550" y="274" />
</svg>"""

data = {
  "id": "kjsea-kiswahili-2025",
  "title": "Kiswahili Lugha",
  "subject": "Kiswahili",
  "year": "2025",
  "durationMinutes": 120,
  "timeAllowed": 120,
  "sharedContexts": {
    "ctx-kisw-2025-q1-6": {
      "title": "Soma kifungu kifuatacho kisha ujibu swali la 1 hadi la 6.",
      "type": "text",
      "text": "Sonita alitembea halahala kuelekea nyumbani kutoka shuleni. Alikuwa ameagana na wanafunzi wenzake na kila mtu akashika njia ya kwao. Mwendo wa kutoka mahali alipokuwa hadi kwao haukuwa mrefu. Sonita alitamani kufika nyumbani apumzike kwani alikuwa amechoka. Siku hiyo, alikuwa ameshiriki michezo shuleni. Ghafla bin vuu mawazo ya Sonita yalitekwa na sauti ya mtoto mchanga.\n\n\"Ala! Sauti ya mtoto? **Mtoto anafanya nini peke yake kando ya barabara?**\" Maswali haya na mengine mengi yalimjia Sonita kwa wakati mmoja.\n\nSonita alinyatia na kuchungulia ilikotoka sauti hiyo. Alipigwa na bumbuazi kumwona mtoto mchanga amefungwafungwa kwa nguo za mararu na kutiwa ndani ya kapu kuukuu. Moyo ulimpapa. Hakujua afanye nini. Sonita aliamua kutimua mbio ili kukikwepa kioja hicho lakini kabla ya kufanya hivyo, aliyaona mengine mbele yake. Jibwa kubwa lilikuwa limelala nyuma ya kapu hilo. **Lilikuwa limetulia kama maji mtungini.** Sonita alidhani kuwa bila shaka azma ya jibwa hilo ilikuwa moja, kumtafuna mtoto yule. Alinyakua kapu hilo na kukimbia. Jibwa lilimwangalia kwa jicho la pembeni. Lilibaki pale likinusanusa. Sonita alifika nyumbani akihema kwa mshtuko.\n\n\"Sijui nimfanyie nini mtoto huyu? Baba na mama hawajafika nyumbani. Mtoto mwenyewe anahitaji chakula, mavazi na malazi. Afadhali niwapigie wazazi wangu simu waje haraka. Jukumu hili siliwezi peke yangu.\" Sonita alisema huku akimfunika mtoto kwa blanketi ili aache kutetemeka. Mtoto mwenyewe hakulia bali alirambaramba midomo, ishara ya kutafuta riziki ya tumboni.\n\nWazazi wa Sonita waliwasili nyumbani haraka. Walipishana kwa sekunde tu. Aliwaeleza yote yaliyojiri. Mama alimshughulikia mtoto vyema. Alimwosha, akamfunga vizuri kwa nguo safi na kumnywesha maziwa. Mtoto alilala usingizi wa pono. Baba na Sonita nao walishika njia hadi kwenye kituo cha polisi kuripoti tukio hilo."
    },
    "ctx-kisw-2025-q7-12": {
      "title": "Soma kifungu kifuatacho kisha ujibu swali la 7 hadi la 12.",
      "type": "text",
      "text": "Zakaria alikutana na Kiberenge njiani. \"Unaenda wapi?\" Kiberenge alimuuliza Zakaria. \"Hakuna hata salamu bwana?\" Zakaria alimuuliza Kiberenge.\n\n\"Sina muda wa salamu. Nachelewa. Nataka kwenda kupanga meza zangu. Wateja wangu wanakaribia kutoka kazini. Kwanza, naomba univunjie noti hii.\" Kiberenge alisema akiwa na haraka huku akimpatia Zakaria noti ya mia tano. Zakaria aliwaza na kuwazua. Hakujua amvunjie Kiberenge pesa au la. Hakumwamini Kiberenge hata kiduchu. Alimfahamu Kiberenge ndani nje. Kiberenge hakuwa mtu mwenye maadili. Alitumia kila fursa aliyopata kuwalaghai watu.\n\n\"Haidhuru!\" Zakaria alijisemea na kumpa Kiberenge pesa alizohitaji. Kiberenge alizipokea pesa hizo huku akicheka na kutoa gego la mwisho.\n\nHaukupita muda mrefu, Zakaria akafika dukani akiwa na haja ya kununua bidhaa. Alishangaa alipoambiwa kuwa pesa alizokuwa nazo zilikuwa bandia. Alirudisha mawazo nyuma na kusema, \"Ala! Kumbe Kiberenge amenichezea. Sawa tu. Leo atampata pwaguzi.\" Zakaria alifululiza moja kwa moja hadi mahali ambapo Kiberenge alichezeshea watu kamari. Alitumaini kuwa angempata kwani mara nyingi alikuwa akijificha asikamatwe na askari kanzu.\n\nZakaria alimkuta Kiberenge akiwashawishi wapita njia kucheza kamari. Aliwaita kwa sauti, \"Njooni magwiji. Haraka yako ndio bahati yako. Hapa pesa zako zitazaa pacha.\"\n\nZakaria alijibanza pembeni na kutafuta kwenye mtandao nambari ya kituo cha polisi kilichokuwa karibu. Aliipata na **kuwataarifu** kuhusu uhuni wa Kiberenge. Polisi walimshauri Zakaria kujidai kuwa alitaka kucheza kamari. Walimwambia atumie pesa ghushi alizopewa na Kiberenge. Zakaria alifululiza kwenda kucheza kamari kama alivyoshauriwa.\n\nKiberenge alimkaribisha Zakaria kwa mikono miwili. Zakaria naye hakusita; alianza kucheza mara moja kwa pesa bandia. \"Hahaha! umeliwa. Wajinga ndio waliwao. Wekelea pesa zaidi ili ukomboe zilizopotea.\" Kiberenge alisema huku akicheka kama fisi.\n\nKicheko cha Kiberenge kiligeuka kilio askari kanzu walipowasili wakiandamana na askari polisi. Askari hawa waliwazingira Kiberenge na wachezaji kamari wenzake. Zakaria alisimama kando tu na kujionea sinema."
    },
    "ctx-kisw-2025-q13-17": {
      "title": "Soma kifungu kifuatacho kisha ujibu swali la 13 hadi la 17.",
      "type": "text",
      "text": "Haki ndio msingi wa mahitaji yote ya kila mtu. Mahitaji hayo ni kama vile: lishe bora, mavazi, malazi na elimu. Swali ni je, ni nani anayefaa kuwatimizia watu haki zao?\n\nWatu tofauti hupata haki zao kupitia njia mbalimbali. Watoto kwa mfano hutimiziwa haki zao na wazazi, walezi au walimu wao. Kwa upande mwingine, wakongwe hutimiziwa mahitaji yao na wana wao na jamii kwa jumla.\n\nKunayo mambo mengi ambayo huathiri upataji wa haki za kibinadamu. Mambo hayo ni kama vile sheria na sera za jamii fulani. Jamii inayowajali watu wake huweka utaratibu wa kuhakikisha kuwa kila mwanajamii anapokea haki zake. Taratibu hizi huwalinda wanajamii dhidi ya **dhuluma** zinazotokana na ukiukaji wa haki za kibinadamu kama vile ukosefu wa elimu.\n\nHaki za kibinadamu zinapokiukwa jamii hutamauka na kufarakana. Watu huanza kuvunja sheria na kuwadhulumu wenzao. Wengine huwatumia vibaya watu wasio na uwezo wa kiuchumi ndiposa wawatimizie angalau baadhi ya mahitaji yao.\n\nKumnyima mtu haki yake ni kumnyima ubinadamu wake. Ni kumfanya mtu kuwa zuzu asiyewaza chochote bali kutii analoambiwa bila kuhoji. Jamii kamili ni ile ambayo inatimiza haki za kila mwanajamii na kuzilinda kwa jino na ukucha."
    },
    "ctx-kisw-2025-q18-20": {
      "title": "Soma kifungu kifuatacho kisha ujibu swali la 18 hadi la 20.",
      "type": "text",
      "text": "Wanafunzi wa shule ya Junia huwa na ratiba ya Klabu mbalimbali kila siku ya wiki kama ilivyo kwenye jedwali lifuatalo:\n\n" + svg_table
    }
  },
  "sectionA": [
    {
      "id": "q1", "questionNumber": 1,
      "questionText": "Kulingana na aya ya **kwanza**, Sonita alitembea haraka kuelekea nyumbani ili",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q1-6",
      "options": [
        {"text": "kufika nyumbani mapema kama wenzake.", "isCorrect": False},
        {"text": "kuonyesha kuwa kwao kulikuwa karibu.", "isCorrect": False},
        {"text": "kupata nafasi ya kuondoa uchovu.", "isCorrect": True},
        {"text": "kutambua ilikotoka sauti aliyoisikia.", "isCorrect": False}
      ],
      "explanation": "Aya ya kwanza inaeleza wazi kuwa \"Sonita alitamani kufika nyumbani apumzike kwani alikuwa amechoka.\" Kwa hivyo, aliharakisha ili apate nafasi ya kupumzika na kuondoa uchovu wake."
    },
    {
      "id": "q2", "questionNumber": 2,
      "questionText": "Mawazo ya Sonita katika aya ya pili **'Mtoto anafanya nini peke yake kando ya barabara?'** yanadhihirisha nini kuhusu jamii ya Sonita?",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q1-6",
      "options": [
        {"text": "Wanafunzi wengi ni wadadisi wa mambo katika mazingira yao.", "isCorrect": False},
        {"text": "Sio kawaida kumpata mtoto ameachwa barabarani.", "isCorrect": True},
        {"text": "Watu wengi wamezoea kuwaacha watoto barabarani.", "isCorrect": False},
        {"text": "Baadhi ya watu hujishughulisha na mambo yanayowahusu pekee.", "isCorrect": False}
      ],
      "explanation": "Kushangazwa kwa Sonita mpaka akauliza swali hilo kunaonyesha kuwa kitendo cha mtoto kuachwa kando ya barabara ni jambo geni na ambalo sio la kawaida katika jamii yake."
    },
    {
      "id": "q3", "questionNumber": 3,
      "questionText": "Chagua jibu linaloonyesha kuwa Sonita ni mwenye maadili.",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q1-6",
      "options": [
        {"text": "Alitembea haraka ili afike nyumbani.", "isCorrect": False},
        {"text": "Alijiuliza maswali mengi ili kujua ukweli.", "isCorrect": False},
        {"text": "Alifikiria kumuokoa mtoto asiliwe na jibwa.", "isCorrect": False},
        {"text": "Alimfunika mtoto ili aache kutetemeka.", "isCorrect": True}
      ],
      "explanation": "Kitendo cha kumhurumia mtoto mchanga anayetetemeka kwa baridi na kumfunika kwa blanketi kinadhihirisha maadili mema, utu, na utu wema wa Sonita."
    },
    {
      "id": "q4", "questionNumber": 4,
      "questionText": "Chagua jibu linaloonyesha mfuatano sahihi wa matukio katika kifungu.\n(i) Sonita kuwapigia wazazi simu.\n(ii) Sonita kuwaeleza yaliyojiri.\n(iii) Sonita kuagana na wenzake.\n(iv) Sonita kunyakua mtoto.",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q1-6",
      "options": [
        {"text": "(iii), (iv), (i), (ii)", "isCorrect": True},
        {"text": "(iv), (iii), (ii), (i)", "isCorrect": False},
        {"text": "(iii), (i), (ii), (iv)", "isCorrect": False},
        {"text": "(iv), (ii), (i), (iii)", "isCorrect": False}
      ],
      "explanation": "Kwanza aliagana na wenzake shuleni (iii), kisha akiwa njiani akanyakua kapu la mtoto ili asiliwe na mbwa (iv). Alipofika nyumbani aliwapigia wazazi simu (i), na walipowasili aliwaeleza yaliyojiri (ii). Hivyo mfuatano ni (iii), (iv), (i), (ii)."
    },
    {
      "id": "q5", "questionNumber": 5,
      "questionText": "Kauli, **'lilikuwa limetulia kama maji mtungini,'** imetumia tamathali gani ya usemi?",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q1-6",
      "options": [
        {"text": "Nahau", "isCorrect": False},
        {"text": "Sitiari", "isCorrect": False},
        {"text": "Tashbihi", "isCorrect": True},
        {"text": "Methali", "isCorrect": False}
      ],
      "explanation": "Matumizi ya neno la kulinganisha 'kama' kudhihirisha mfanano (limetulia kama...) ni ishara wazi ya tamathali ya usemi inayoitwa tashbihi (simile)."
    },
    {
      "id": "q6", "questionNumber": 6,
      "questionText": "Je, unafikiri polisi walichukua hatua gani baada ya kisa cha mtoto kuripotiwa?",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q1-6",
      "options": [
        {"text": "Walianza kuwatafuta wazazi wa mtoto.", "isCorrect": True},
        {"text": "Walimchukua mtoto na kumweka kituoni.", "isCorrect": False},
        {"text": "Waliwaleta watoto wengine waliokuwa wamepotea.", "isCorrect": False},
        {"text": "Waliwapatia zawadi waliofika kupiga ripoti.", "isCorrect": False}
      ],
      "explanation": "Kisa cha mtoto kutelekezwa kinaporipotiwa, hatua ya kimantiki na ya kisheria kwa polisi ni kuanza uchunguzi kuwatafuta wazazi wa mtoto huyo aliyetelekezwa."
    },
    {
      "id": "q7", "questionNumber": 7,
      "questionText": "Kulingana na kifungu, Kiberenge hakumwamkua Zakaria kwa sababu alikuwa na",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q7-12",
      "options": [
        {"text": "wateja wengi waliokuwa wanamsubiri.", "isCorrect": False},
        {"text": "haraka ya kufungua biashara yake.", "isCorrect": True},
        {"text": "noti aliyotaka kuvunjiwa.", "isCorrect": False},
        {"text": "swali ambalo alitaka kujibiwa.", "isCorrect": False}
      ],
      "explanation": "Kiberenge alisema waziwazi: \"Sina muda wa salamu. Nachelewa. Nataka kwenda kupanga meza zangu.\" Hii inamaanisha alikuwa na haraka ya kupanga meza ili afungue biashara yake (ya kamari)."
    },
    {
      "id": "q8", "questionNumber": 8,
      "questionText": "Ni jibu lipi linaonyesha uhusiano kati ya Zakaria na Kiberenge?",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q7-12",
      "options": [
        {"text": "Walikuwa na mazoea ya kuvunjiana pesa.", "isCorrect": False},
        {"text": "Kiberenge alipenda kusaidiwa na Zakaria.", "isCorrect": False},
        {"text": "Walikuwa na urafiki wa dhati.", "isCorrect": False},
        {"text": "Zakaria alijua mienendo ya Kiberenge.", "isCorrect": True}
      ],
      "explanation": "Kifungu kinasema kuhusu Zakaria: \"Alimfahamu Kiberenge ndani nje. Kiberenge hakuwa mtu mwenye maadili. Alitumia kila fursa...\" Hii inaonyesha Zakaria alijua fika mienendo na tabia (uhuni) wa Kiberenge."
    },
    {
      "id": "q9", "questionNumber": 9,
      "questionText": "Neno '**kuwataarifu**' limetumiwa katika kifungu.\nChagua kisawe cha neno hilo.",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q7-12",
      "options": [
        {"text": "kuwakumbusha", "isCorrect": False},
        {"text": "kuwajulisha", "isCorrect": True},
        {"text": "kuwasisitizia", "isCorrect": False},
        {"text": "kuwapendekeza", "isCorrect": False}
      ],
      "explanation": "Kuwataarifu kunamaanisha kuwapa taarifa au habari fulani. Kwa hivyo, kisawe chake ambacho kinaleta maana sawa ni 'kuwajulisha'."
    },
    {
      "id": "q10", "questionNumber": 10,
      "questionText": "Je, unadhani Kiberenge alifanya nini baada ya kukamatwa na askari?",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q7-12",
      "options": [
        {"text": "Aliwaita wateja aliokuwa anacheza nao kamari.", "isCorrect": False},
        {"text": "Alitaka kumrudishia Zakaria pesa bandia.", "isCorrect": False},
        {"text": "Alikubali na kuandamana nao hadi kituoni.", "isCorrect": True},
        {"text": "Aliwafundisha askari jinsi ya kucheza kamari.", "isCorrect": False}
      ],
      "explanation": "Mtu anapozingirwa na kukamatwa na polisi (askari kanzu na askari polisi), jambo linalofuata na la kutarajiwa ni yeye kukubali na kuandamana nao hadi kituo cha polisi kwa hatua za kisheria."
    },
    {
      "id": "q11", "questionNumber": 11,
      "questionText": "Chagua methali ambayo inaweza kutumiwa kumshauri Kiberenge.",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q7-12",
      "options": [
        {"text": "Siku za mwizi ni arobaini.", "isCorrect": True},
        {"text": "Usiache mbachao kwa msala upitao.", "isCorrect": False},
        {"text": "Asiyesikia la mkuu huvunjika guu.", "isCorrect": False},
        {"text": "Kidole kimoja hakivunji chawa.", "isCorrect": False}
      ],
      "explanation": "Kiberenge alikuwa tapeli na mwizi aliyewalaghai watu kila mara. Kukamatwa kwake kunadhihirisha methali 'Siku za mwizi ni arobaini', ikimaanisha mwishowe mwizi au mhalifu atakamatwa."
    },
    {
      "id": "q12", "questionNumber": 12,
      "questionText": "Chagua jibu ambalo **si** kichwa mwafaka kwa kifungu hiki.",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q7-12",
      "options": [
        {"text": "Kuwajibika kwa wanajamii.", "isCorrect": False},
        {"text": "Biashara za mjini.", "isCorrect": False},
        {"text": "Manufaa ya maamkuzi.", "isCorrect": True},
        {"text": "Udanganyifu haufai.", "isCorrect": False}
      ],
      "explanation": "Kifungu hakizungumzii manufaa ya maamkuzi; badala yake kinaangazia udanganyifu, uhuni, na uwajibikaji wa mwanajamii (Zakaria aliyeita polisi). Hivyo basi, 'Manufaa ya maamkuzi' sio kichwa mwafaka kwa stori hii."
    },
    {
      "id": "q13", "questionNumber": 13,
      "questionText": "Kulingana na kifungu,",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q13-17",
      "options": [
        {"text": "wazee huwa na mahitaji mengi zaidi katika jamii.", "isCorrect": False},
        {"text": "watu wote wana jukumu la kuwatimizia watoto haki zao.", "isCorrect": False},
        {"text": "kuna njia maalum za kushughulikia mahitaji ya wanajamii.", "isCorrect": True},
        {"text": "kila mwanadamu anastahili kupata vyakula vyenye virutubishi.", "isCorrect": False}
      ],
      "explanation": "Kifungu kinasema: \"Watu tofauti hupata haki zao kupitia njia mbalimbali.\" Watoto kwa wazazi, wakongwe kwa wana wao na jamii. Hii inaonyesha kuna njia maalumu (mbalimbali) za kushughulikia haki na mahitaji ya wanajamii."
    },
    {
      "id": "q14", "questionNumber": 14,
      "questionText": "Kuwatimizia wakongwe haki zao ni njia moja ya kukuza",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q13-17",
      "options": [
        {"text": "kusameheana.", "isCorrect": False},
        {"text": "bidii.", "isCorrect": False},
        {"text": "makini.", "isCorrect": False},
        {"text": "uwajibikaji.", "isCorrect": True}
      ],
      "explanation": "Jamii inapotimiza mahitaji ya wakongwe inayoishi nao, inadhihirisha jukumu na uwajibikaji mkubwa miongoni mwa wanajamii kusaidia wasiojiweza."
    },
    {
      "id": "q15", "questionNumber": 15,
      "questionText": "Chagua jibu ambalo ni sahihi kwa mujibu wa kifungu.",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q13-17",
      "options": [
        {"text": "Jamii ikikosa kutekeleza haki, watu hupotoka kimaadili.", "isCorrect": True},
        {"text": "Wanajamii huzungumza mambo mengi kuhusu haki zao.", "isCorrect": False},
        {"text": "Haki za watu hufikiriwa na wanajamii wenyewe.", "isCorrect": False},
        {"text": "Ukosefu wa haki hutegemea tofauti za kiuchumi.", "isCorrect": False}
      ],
      "explanation": "Kifungu kinasema haki zinapokiukwa \"Watu huanza kuvunja sheria na kuwadhulumu wenzao. Wengine huwatumia vibaya watu...\" Haya yote ni mapotovu ya kimaadili (immorality) yanayochipuka kutokana na ukosefu wa kutekeleza haki."
    },
    {
      "id": "q16", "questionNumber": 16,
      "questionText": "Ukiukaji wa haki za kibinadamu husababisha",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q13-17",
      "options": [
        {"text": "wanaonyimwa haki kuwa mazuzu.", "isCorrect": True},
        {"text": "uundaji wa sheria na sera mpya.", "isCorrect": False},
        {"text": "kuzoroteka kwa hali ya uchumi.", "isCorrect": False},
        {"text": "wanajamii kuzilinda mali zao.", "isCorrect": False}
      ],
      "explanation": "Aya ya mwisho inasema: \"Kumnyima mtu haki yake ni kumnyima ubinadamu wake. Ni kumfanya mtu kuwa zuzu asiyewaza chochote bali kutii analoambiwa...\" Hivyo basi inasababisha wanaonyimwa haki kugeuzwa mazuzu."
    },
    {
      "id": "q17", "questionNumber": 17,
      "questionText": "Kulingana na kifungu, maana ya neno **dhuluma** ni",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q13-17",
      "options": [
        {"text": "makosa.", "isCorrect": False},
        {"text": "uonevu.", "isCorrect": True},
        {"text": "chuki.", "isCorrect": False},
        {"text": "hasara.", "isCorrect": False}
      ],
      "explanation": "Neno dhuluma linamaanisha ukiukaji mkubwa wa haki, kuwaonea au kuwatendea wengine ukatili usio na haki. Kwa hivyo maana mwafaka hapa ni uonevu (oppression/bullying)."
    },
    {
      "id": "q18", "questionNumber": 18,
      "questionText": "Chagua jibu linaloonyesha wanaklabu wanaokutana mara mbili pekee kwa wiki.",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q18-20",
      "options": [
        {"text": "Upishi, skauti, densi", "isCorrect": False},
        {"text": "Densi, skauti, majadiliano", "isCorrect": False},
        {"text": "Upishi, kilimo, densi", "isCorrect": True},
        {"text": "Kilimo, densi, majadiliano", "isCorrect": False}
      ],
      "explanation": "Ukitazama jedwali, klabu zinazokutana mara mbili pekee ni Densi (Jumatatu na Alhamisi), Kilimo (Jumatano na Ijumaa), na Upishi (Jumanne na Ijumaa)."
    },
    {
      "id": "q19", "questionNumber": 19,
      "questionText": "Ni siku gani wanafunzi wa shule ya Junia hushiriki katika klabu chache zaidi?",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q18-20",
      "options": [
        {"text": "Jumanne", "isCorrect": False},
        {"text": "Jumatano", "isCorrect": True},
        {"text": "Alhamisi", "isCorrect": False},
        {"text": "Ijumaa", "isCorrect": False}
      ],
      "explanation": "Tukihesabu klabu kwa kila siku, Jumatatu zina klabu 4, Jumanne 4, Jumatano ina klabu 3 pekee (Michezo, Kilimo, Mazingira), Alhamisi 4, na Ijumaa 4. Hivyo Jumatano ndiyo siku yenye klabu chache."
    },
    {
      "id": "q20", "questionNumber": 20,
      "questionText": "Chagua jibu linaloonyesha klabu ambayo wanafunzi hushiriki kila siku ya wiki.",
      "questionType": "multiple-choice", "contextRef": "ctx-kisw-2025-q18-20",
      "options": [
        {"text": "Kilimo", "isCorrect": False},
        {"text": "Majadiliano", "isCorrect": False},
        {"text": "Mazingira", "isCorrect": True},
        {"text": "Upishi", "isCorrect": False}
      ],
      "explanation": "Klabu ya Mazingira ina alama ya kupe (✓) kwenye kila siku ya wiki kuanzia Jumatatu hadi Ijumaa, ikionyesha kwamba hushirikiwa kila siku ya wiki."
    }
  ]
}

with open("src/data/kjsea-kiswahili-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaKiswahili2025 = {json.dumps(data, indent=2)};\n")
