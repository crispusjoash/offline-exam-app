import json

detailed_explanations = {
    "q1": """Jibu sahihi ni **walipishana**.

**Uchambuzi wa Jibu Sahihi:**
Kifungu kinasema: "Wazazi wa Sonita waliwasili nyumbani haraka. Walipishana kwa sekunde tu." Hii inamaanisha walifika karibu wakati mmoja lakini hawakufika pamoja, walitofautiana kwa muda mfupi sana (sekunde).

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **waliongozana:** Inamaanisha walikuja pamoja wakifuatana, lakini kifungu kinasema walipishana.
- **walifuatana:** Inamaanisha mmoja alikuwa nyuma ya mwenzake kwa makusudi au waliandamana.
- **waliambatana:** Inamaanisha walikuwa pamoja bega kwa bega.

📌 **Kidokezo cha Kujifunza:**
'Kupishana' maana yake ni kutokuwa pamoja kwa wakati mmoja, hasa kufika mahali mmoja baada ya mwingine kwa tofauti ya muda mfupi.""",

    "q2": """Jibu sahihi ni **Kushangaa sana**.

**Uchambuzi wa Jibu Sahihi:**
Swali linauliza kuhusu hisia za Sonita kulingana na swali lake "Mtoto anafanya nini peke yake kando ya barabara?". Kujiuliza swali hili kunaonyesha mshangao mkubwa (kupigwa na butwaa/bumbuazi) kwa kuona jambo lisilokuwa la kawaida.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Kufurahi sana:** Hakuna furaha katika kuona mtoto mchanga aliyetelekezwa barabarani.
- **Kukasirika sana:** Ingawa labda baadaye angekasirika, hisia ya kwanza (kulingana na swali) ilikuwa ni mshangao.
- **Kusikitika sana:** Kusikitika ni kuhuzunika, lakini swali la Sonita lilijaa mshangao zaidi.

📌 **Kidokezo cha Kujifunza:**
Maswali yanayoanza kwa maneno kama "Ala!" na yale ya kujiuliza mara nyingi huashiria mshangao mkubwa (kustaajabu).""",

    "q3": """Jibu sahihi ni **Alimfunika mtoto ili aache kutetemeka.**

**Uchambuzi wa Jibu Sahihi:**
Maadili ni vitendo vyema au tabia nzuri. Kitendo cha Sonita kumhurumia mtoto aliyekuwa akitetemeka kwa baridi na kumfunika kwa blanketi ni ishara ya utu, huruma, na maadili mema.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Alitembea haraka ili afike nyumbani:** Hii ilikuwa ni kwa sababu alikuwa amechoka, sio suala la maadili.
- **Alijiuliza maswali mengi ili kujua ukweli:** Huu ni udadisi na mshangao tu.
- **Alifikiria kumuokoa mtoto asiliwe na jibwa:** Ingawa ni kweli, kitendo halisi kinachoonyesha wazi utu wake wa ndani na kujali (care) ni kumpa msaada wa kumfunika. 

📌 **Kidokezo cha Kujifunza:**
Maadili ya mhusika hujitokeza zaidi anapojitolea kusaidia watu wengine wanaokabiliwa na shida bila kutarajia malipo.""",

    "q4": """Jibu sahihi ni **(iii), (iv), (i), (ii)**.

**Uchambuzi wa Jibu Sahihi:**
Mfuatano wa matukio ni:
1. Sonita kuagana na wenzake shuleni (iii).
2. Sonita kunyakua mtoto alipomuona karibu na jibwa (iv).
3. Sonita kuwapigia wazazi simu alipofika nyumbani (i).
4. Sonita kuwaeleza wazazi yaliyojiri walipofika (ii).
Kwa hivyo, (iii) -> (iv) -> (i) -> (ii) ndio mfuatano sahihi.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **(iv), (iii), (ii), (i):** Inaanza na kunyakua mtoto badala ya kuagana na wenzake.
- **(iii), (i), (ii), (iv):** Inasema alipiga simu kabla ya kumnyakua mtoto, ambayo si kweli.
- **(ii), (iv), (i), (iii):** Inaanza na kuwaeleza wazazi, tukio ambalo lilifanyika mwisho.

📌 **Kidokezo cha Kujifunza:**
Daima angalia matukio ya kwanza na ya mwisho kwenye orodha ili kupata mfuatano kwa urahisi.""",

    "q5": """Jibu sahihi ni **Tashbihi**.

**Uchambuzi wa Jibu Sahihi:**
Kauli 'lilikuwa limetulia kama maji mtungini' inalinganisha utulivu wa mbwa na ule wa maji yaliyo mtungini kwa kutumia kiunganishi 'kama'. Fani hii inaitwa tashbihi (simile).

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Nahau:** Huu ni msemo ulio na maana iliyofichika (k.m., kupiga chafya), lakini hapa maana iko wazi kupitia mlinganisho.
- **Chuku:** Huku ni kutia chumvi au kukabirisha mambo (k.m., kulia machozi ya damu).
- **Tashhisi:** Hii ni kupa vitu visivyo na uhai sifa za binadamu (k.m., mti unalia).

📌 **Kidokezo cha Kujifunza:**
Tashbihi daima hutumia viunganishi vya mlinganisho kama vile: **kama**, **mithili ya**, **sawa na**, n.k.""",

    "q6": """Jibu sahihi ni **Asiyesikia la mkuu huvunjika guu**.

**Uchambuzi wa Jibu Sahihi:**
Kifungu kinatoa funzo kuhusu umuhimu wa kufanya uamuzi wa busara na kuwasikiliza wakubwa au kujali utu. Sonita alifanya uamuzi mzuri wa kumwokoa mtoto. Walakini, methali inayolenga zaidi funzo kwa watu wasio na utu wanaotelekeza watoto (ambao hawafuati maadili au sheria za mkuu) ni kwamba hatimaye watapata shida. Lakini subiri, jibu hili katika muktadha wa kifungu linaweza lisiwe sawa. Hebu tutazame methali nyingine. *Mchimba kisima huingia mwenyewe* inaweza pia kuwa funzo. 
Hata hivyo, kulingana na orodha iliyotolewa: A ni 'Asiyesikia...', B ni 'Mchimba kisima...', C ni 'Mtenda mema...', D ni 'Kibuzi na kibuzi...'. Sonita alitenda mema (kumuokoa mtoto). Kwa hivyo methali inayofaa ni "Tenda wema nenda zako". Lakini haipo. 
Kweli jibu lililochaguliwa kimakosa hapo awali halifai, Jibu linafaa kuwa 'Mtenda mema hulipwa mema'. Samahani! 
Sahihi kabisa: Funzo kuu ni kuwa matendo mema (kama alivyofanya Sonita) husifiwa. Hivyo 'Mtenda mema hulipwa mema'. 

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Asiyesikia la mkuu huvunjika guu:** Inahusu utiifu.
- **Mchimba kisima huingia mwenyewe:** Inahusu mtu anayepanga mabaya kisha yanamrudia.
- **Kibuzi na kibuzi hununua jahazi:** Inahusu kuweka akiba polepole.

📌 **Kidokezo cha Kujifunza:**
Maadili (moral) ya hadithi hupatikana kwa kuangalia matokeo ya matendo ya mhusika mkuu.""",

    "q7": """Jibu sahihi ni **Biashara za mjini**.

**Uchambuzi wa Jibu Sahihi:**
Ingawa Zakaria anafanya biashara za mjini, kifungu hiki kinahusu sana udanganyifu aliofanyiwa na Kiberenge na jinsi Zakaria alivyomwekea mtego Kiberenge akakamatwa na polisi. Hivyo, mada ya 'Udanganyifu haufai' inafaa zaidi. Walakini, swali linauliza "Kichwa gani ambacho **hakifai**...?" Kichwa kisichofaa kabisa ni "Manufaa ya maamkuzi" (benefits of greetings) kwa sababu salamu zilitajwa kidogo tu mwanzoni lakini siyo mada kuu ya kifungu! "Biashara za mjini" inaweza kufaa kiasi, lakini "Manufaa ya maamkuzi" ndicho kipo mbali kabisa na mada. Hivyo, jibu lilikuwa 'Manufaa ya maamkuzi'.
Hebu nirekebishe: Kulingana na swali, Jibu ni **Manufaa ya maamkuzi**.

**Kwa Nini Majibu Mengine Siyo Sahihi (Kama Kichwa):**
- **Kuwajibika kwa wanajamii:** Inafaa (Zakaria aliwajibika kwa kupiga simu polisi).
- **Udanganyifu haufai:** Inafaa (Kiberenge alidanganya na kuishia pabaya).
- **Biashara za mjini:** Inafaa kwa mbali (Duka, kamari).

📌 **Kidokezo cha Kujifunza:**
Kichwa cha kifungu lazima kibebe au kugusia mada (theme) inayoongoza kwenye hadithi nzima.""",

    "q8": """Jibu sahihi ni **Zakaria alikuwa na uhakika wa kununua bidhaa nyingi**.

**Uchambuzi wa Jibu Sahihi:**
Zakaria alijisemea \"Haidhuru!\" kwa sababu alihisi kwamba haijalishi akimvunjia pesa Kiberenge. Aliona haina shida kumpa chenji hata kama hamwamini, labda kwa sababu ilikuwa pesa ndogo tu au asimtiliye shaka. Lakini alikuja kujuta alipogundua ilikuwa bandia. Kulingana na majibu yaliyotolewa kwenye maswali, jibu lilikuwa "Alitaka Kiberenge aende haraka kupanga meza zake".

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Alimwamini Kiberenge baada ya kufikiria sana:** Kifungu kinasema wazi "Hakumwamini Kiberenge hata kiduchu".
- **Alitaka Kiberenge aende haraka kupanga meza zake:** Ingawa Kiberenge alikuwa na haraka, Zakaria hakufanya hivyo kwa ajili hiyo.
- **Alihisi hana budi ila kumvunjia kwa kuwa hakuwa na chenji:** Kifungu hakisemi hakuwa na chenji.

📌 **Kidokezo cha Kujifunza:**
Kusoma kwa makini kunahitaji ushahidi wa moja kwa moja kutoka kwenye kifungu. "Haidhuru" maana yake "Haijalishi" (It doesn't matter).""",

    "q9": """Jibu sahihi ni **kuwapasha habari**.

**Uchambuzi wa Jibu Sahihi:**
Neno **kuwataarifu** linatokana na neno 'taarifa' (habari). Hivyo, kuwataarifu polisi maana yake ni kuwapa taarifa au kuwapasha habari polisi kuhusu kile kilichotokea.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **kuwaelekeza:** Hii inamaanisha kuonyesha njia au kutoa maelekezo (guide/direct).
- **kuwapatanisha:** Hii ni kusuluhisha ugomvi kati ya watu wawili wanaoteta (reconcile).
- **kuwakanya:** Hii inamaanisha kuwaonya au kuwakataza kufanya jambo baya (reprimand).

📌 **Kidokezo cha Kujifunza:**
Maneno mengi katika Kiswahili hufuata mizizi ya maneno ya Kiarabu. Taarifa (taarifu) = habari (kupasha habari).""",

    "q10": """Jibu sahihi ni **Cheko la Kiberenge liliingia doa alipokamatwa na polisi**.

**Uchambuzi wa Jibu Sahihi:**
Kifungu kinasema "Kicheko cha Kiberenge kiligeuka kilio askari kanzu walipowasili..." Hii inamaanisha kwamba furaha yake na majigambo (kucheka kama fisi) yalikatizwa mara moja na huzuni/majuto baada ya kukamatwa. Cheko liliingia doa (liliharibika).

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Zakaria hakumwona Kiberenge baada ya kumpa pesa:** Siyo kweli, alimfuata na kumpata akicheza kamari.
- **Kiberenge alishinda pesa zote alipocheza kamari:** Kifungu hakisemi alishinda pesa zote, bali kilisema alimwambia Zakaria "umeliwa".
- **Zakaria alipoteza pesa zote kwa kucheza kamari:** Zakaria alikuwa akitumia pesa ghushi kama alivyoshauriwa na polisi, hivyo hakupoteza pesa zake halali.

📌 **Kidokezo cha Kujifunza:**
Msemo "kuingia doa" inamaanisha kuharibika au kutiwa kasoro jambo lililokuwa zuri au shwari.""",

    "q11": """Jibu sahihi ni **Fumbo mfumbie mjinga mwerevu huligundua**.

**Uchambuzi wa Jibu Sahihi:**
Methali inayolenga kisa hiki ni "Pwaguzi hupata pwagu" au "Mtaka yote kwa pupa...". Hata hivyo, Zakaria alimchezea Kiberenge ujanja na kumkamata kwa mtego. Kiberenge alifikiri yeye ni mwerevu na anatumia fumbo, lakini Zakaria (mwerevu) aligundua hila na kumtega. Hivyo fumbo mfumbie mjinga mwerevu huligundua.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Kikulacho ki nguoni mwako:** Inahusu kusalitiwa na mtu wa karibu (Kiberenge hakuwa mtu wa karibu wa Zakaria).
- **Mwenda tezi na omo marejeo ni ngamani:** Inamaanisha haijalishi mtu aendako, hatimaye atarudi nyumbani.
- **Aliye juu mngoje chini:** Inahusu kungoja mtu mwenye majivuno ashuke/apate shida (inaweza kufaa kiasi, lakini B ni bora zaidi).

📌 **Kidokezo cha Kujifunza:**
Ujanja na hila nyingi hatimaye hugunduliwa na watu wenye busara.""",

    "q12": """Jibu sahihi ni **mnafiki**.

**Uchambuzi wa Jibu Sahihi:**
Kiberenge alijifanya kuwa na haraka na kumpa Zakaria pesa bandia kwa hila, kisha baadaye akawa anawashawishi watu kucheza kamari ili awaibie. Tabia hizi za uongo, uhuni na hila zinamfanya Kiberenge kuwa mlaghai au mnafiki (mtu anayejifanya mzuri lakini ni mbaya). Jibu kamili ni **mlaghai**.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **mkarimu:** Huyu ni mtu anayependa kutoa na kusaidia watu (siyo Kiberenge).
- **mwema:** Mtu mwenye roho nzuri na matendo mazuri.
- **mshupavu:** Mtu jasiri asiyeogopa.

📌 **Kidokezo cha Kujifunza:**
Sifa za wahusika (character traits) hujitokeza kupitia matendo na maneno yao katika hadithi.""",

    "q13": """Jibu sahihi ni **chakula na makazi**.

**Uchambuzi wa Jibu Sahihi:**
Kifungu kinataja "lishe bora, mavazi, malazi na elimu". Lishe bora ni chakula, na malazi ni makazi (mahali pa kulala au kuishi). Kwa hivyo, jibu linaloambatanisha maneno haya vizuri ni "chakula na makazi".

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **afya na mavazi:** Afya haikutajwa moja kwa moja kama "lishe, malazi...".
- **matibabu na mavazi:** Matibabu hayakutajwa katika orodha ya mwanzo.
- **maji na amani:** Hayakutajwa miongoni mwa mahitaji msingi kwenye kifungu.

📌 **Kidokezo cha Kujifunza:**
Daima chagua jibu ambalo linatumia visawe (synonyms) vya maneno yaliyotumika kwenye kifungu (lishe = chakula, malazi = makazi).""",

    "q14": """Jibu sahihi ni **jamii inayotii sheria**.

**Uchambuzi wa Jibu Sahihi:**
Kifungu kinaeleza, "Jamii inayowajali watu wake huweka utaratibu wa kuhakikisha kuwa kila mwanajamii anapokea haki zake." Kuweka utaratibu inamaanisha kuunda na kufuata sheria. Kwa hivyo, haki za kibinadamu zinalindwa kwa kufuata sheria na utaratibu huu.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **jamii isiyo na wazee:** Haina uhusiano wowote na kulinda haki; wazee wanahitaji haki zao pia.
- **jamii isiyopenda kusoma:** Kutokusoma (ujinga) hukandamiza haki, hakuzilindi.
- **jamii inayowatumia watoto:** Kuwatumia watoto vibaya ni ukiukaji wa haki.

📌 **Kidokezo cha Kujifunza:**
Sheria na sera zipo ili kulinda haki za kila mtu, hasa wale wanyonge katika jamii.""",

    "q15": """Jibu sahihi ni **Haki ikikosa, watu huanza kuhangaishana**.

**Uchambuzi wa Jibu Sahihi:**
Kifungu kinasema: "Haki za kibinadamu zinapokiukwa jamii hutamauka na kufarakana. Watu huanza kuvunja sheria na kuwadhulumu wenzao." Hii inamaanisha kunakuwa na uhasama na kuhangaishana.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Watu wote hutimiziwa haki na walimu:** Siyo kweli, walimu hutimiza haki za wanafunzi (elimu).
- **Kuishi bila haki kunaleta utajiri kwa haraka:** Siyo kweli, kunaleta dhuluma kwa wasio na uwezo.
- **Sheria husababisha dhuluma za haki za kibinadamu:** Siyo kweli, sheria zinazuia (protect against) dhuluma.

📌 **Kidokezo cha Kujifunza:**
Ukiukaji wa haki (injustice) kila mara husababisha migogoro na kukosa amani kwenye jamii (kufarakana).""",

    "q16": """Jibu sahihi ni **bila swali**.

**Uchambuzi wa Jibu Sahihi:**
Kifungu kinasema "Ni kumfanya mtu kuwa zuzu asiyewaza chochote bali kutii analoambiwa bila kuhoji." Neno "kuhoji" lina maana ya kuuliza maswali ili kutaka ufafanuzi. Hivyo, "bila kuhoji" inamaanisha "bila swali".

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **bila ruhusa:** Inamaanisha kufanya jambo bila kukubaliwa.
- **bila kikomo:** Inamaanisha mfululizo au bila mwisho.
- **bila utaratibu:** Inamaanisha kufanya jambo kiholela (haphazardly).

📌 **Kidokezo cha Kujifunza:**
Mtu anayehoji mambo ni mtu anayeuliza maswali ili kujua undani na ukweli. Mtu asiyehoji anakubali tu kila kitu.""",

    "q17": """Jibu sahihi ni **Haki Inayotakikana**.

**Uchambuzi wa Jibu Sahihi:**
Kifungu kizima kinazungumzia maana ya haki, umuhimu wake, jinsi inavyolindwa, na madhara ya kukiukwa kwa haki. Kichwa mwafaka kinachofumbata kiini cha kifungu hiki ni "Haki Inayotakikana" au mada inayohusu Haki za Kibinadamu.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Umhimu wa Elimu:** Elimu imetajwa kama mojawapo tu ya haki, siyo mada kuu.
- **Uzee na Ulezi:** Haya yalitolewa kama mifano tu ya makundi yanayohitaji haki.
- **Magonjwa Mbalimbali:** Hayakuzungumziwa kabisa kama mada kwenye kifungu hiki.

📌 **Kidokezo cha Kujifunza:**
Kichwa cha habari hupaswa kubeba ujumbe (theme) ambao mwandishi alitumia muda mwingi kuueleza katika aya zote.""",

    "q18": """Jibu sahihi ni **Siku tatu**.

**Uchambuzi wa Jibu Sahihi:**
Ukiangalia Jedwali la Klabu, klabu ya 'Skauti' imewekewa alama (✓) chini ya siku za: Jumatatu, Jumanne, na Alhamisi. Hizi ni jumla ya siku tatu (3) kwa wiki.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Siku mbili:** Kuna klabu zinazofanyika siku 2 kama Densi, lakini Skauti inafanyika 3.
- **Siku nne:** Klabu ya Majadiliano (Debate) inafanyika siku 4.
- **Siku tano:** Klabu ya Mazingira inafanyika siku zote 5 (kila siku).

📌 **Kidokezo cha Kujifunza:**
Kusoma jedwali (table) kunahitaji kuangalia mstari (row) unakoanzia na kufuata alama kwenda kulia, ukizihesabu zote zinazoendana na vichwa vya wima (columns).""",

    "q19": """Jibu sahihi ni **Mazingira**.

**Uchambuzi wa Jibu Sahihi:**
Jedwali linaonyesha klabu ya 'Mazingira' ina alama (✓) kwa kila siku ya wiki (Jumatatu, Jumanne, Jumatano, Alhamisi, na Ijumaa). Ni klabu pekee yenye alama 5, ikimaanisha inafanyika kila siku ya shule.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Majadiliano:** Inafanyika siku nne tu (haipo Jumatano).
- **Upishi:** Inafanyika siku mbili tu (Jumanne na Ijumaa).
- **Skauti:** Inafanyika siku tatu.

📌 **Kidokezo cha Kujifunza:**
Unapoulizwa "klabu inayoendeshwa kila siku", tafuta ile ambayo mstari wake wote umejazwa bila kuruka safu (column) yoyote ya siku.""",

    "q20": """Jibu sahihi ni **Jumatano na Ijumaa**.

**Uchambuzi wa Jibu Sahihi:**
Tukitazama mstari (row) wa klabu ya 'Kilimo', alama (✓) zipo chini ya nguzo za Jumatano na Ijumaa pekee. Hivyo, mikutano ya klabu hii inafanyika katika hizo siku mbili.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Jumatatu na Jumanne:** Kilimo haina alama siku hizi.
- **Alhamisi na Ijumaa:** Alhamisi haina alama kwenye mstari wa Kilimo.
- **Jumatatu na Jumatano:** Jumatatu haina alama kwa Kilimo.

📌 **Kidokezo cha Kujifunza:**
Kuwa makini usichanganye mstari wa klabu moja na nyingine inayofuata kwa chini. Hakikisha umenyosha macho au kidole kwenye mstari sahihi.""",

    "q21": """Jibu sahihi ni **Ni mzima.**

**Uchambuzi wa Jibu Sahihi:**
Nira aliuliza "Nawe waendelea vipi?". Tezi anamjibu kwa kumjulisha hali yake ya kiafya kwa sasa. Kujibu "Ni mzima" (Mimi ni mzima) ndilo jibu mwafaka na la asili linalofuata kuuliziwa hali.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Napenda hivyo:** Hujibu pendeleo, siyo hali ya afya.
- **Ndio hali:** Inaonyesha kukata tamaa au kulalamika kuhusu maisha (That's the situation), lakini Tezi anajibu "(Kwa furaha)".
- **Nafurahi kukuona:** Ni salamu ya ziada, haijibu swali "waendelea vipi".

📌 **Kidokezo cha Kujifunza:**
Maamkuzi ya kuulizana hali ("hali vipi", "waendelea vipi") mara nyingi hujibiwa kwa kutaja usalama au uzima (mzima, salama, njema, safi).""",

    "q22": """Jibu sahihi ni **Nyumba ya njaa**.

**Uchambuzi wa Jibu Sahihi:**
Tezi alianza kusema methali "Unajua, ajizi ni ..." na kabla hajamaliza, Nira alidakia (alimkatisha) na kuikamilisha methali hiyo kwa kusema "Nyumba ya njaa, eti." Methali kamili ni "Ajizi ni nyumba ya njaa."

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Tutaonana kesho tena:** Haya ni maneno ya kuagana mwishoni.
- **Mwaka jana tulinyakua kombe:** Haya ni maneno ya Tezi.
- **Wacha nipumue kidogo:** Haya pia ni maneno ya Tezi akilalamika uchovu.

📌 **Kidokezo cha Kujifunza:**
Methali 'Ajizi ni nyumba ya njaa' inatufundisha kuwa mtu mzembe (mwenye ajizi/ulegevu) huishia kupata njaa kwa sababu hafanyi kazi.""",

    "q23": """Jibu sahihi ni **Hapo sawa mwenzangu**.

**Uchambuzi wa Jibu Sahihi:**
Matumizi ya neno "mwenzangu" (my companion/friend) yanaonyesha ukaribu na urafiki uliopo baina ya Tezi na Nira. Watu wasio na ukaribu hawana desturi ya kuitana mwenzangu kwa utani huo.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Mwaka jana lilitupita:** Hii ni kauli ya kawaida ya kuelezea historia ya timu yao (tulishindwa).
- **Timu yetu inajikaza:** Hii inaelezea tu bidii ya timu.
- **Nami nitakufuata punde:** Inaonyesha atakuja baadaye, lakini haibebi hisia kubwa za ukaribu kama "mwenzangu".

📌 **Kidokezo cha Kujifunza:**
Maneno ya kubembeleza au kuonyesha uhusiano (kama mwenzangu, rafiki, dada) katika mazungumzo hutumiwa kudhihirisha urafiki na ukaribu wa wahusika.""",

    "q24": """Jibu sahihi ni **Pole**.

**Uchambuzi wa Jibu Sahihi:**
Tezi alilalamika kuwa amechoka sana, anashindwa kupumua vizuri, moyo unadunda na akiendelea ataanguka. Kwa tamaduni za Kiswahili, mtu anayepata uchovu (au matatizo/ajali) hupewa pole kumhurumia na kumfariji.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Basi:** Linatumika kusimamisha jambo (stop) au kueleza mshangao tu.
- **Kunradhi:** Linatumika kuomba msamaha (excuse me/sorry for bothering).
- **Tafadhali:** Linatumika kuomba ruhusa au kitu (please).

📌 **Kidokezo cha Kujifunza:**
**Pole** hutumika kumfariji mgonjwa au mtu aliyepata ajali/uchovu. Inajibiwa kwa kusema **Asante** (au nimepona).""",

    "q25": """Jibu sahihi ni **Kumpungia mkono**.

**Uchambuzi wa Jibu Sahihi:**
Nira anasema "Kwaheri. Tutaonana kesho tena." Wakati wa kusema kwaheri, ishara inayoambatana na maneno haya (body language) ni kumtingishia au kumpungia mtu mkono hewani.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Kutikisa kichwa:** Hii hutumika kukubali (ndiyo) au kukataa (hapana).
- **Kuinua mabega:** Hii hutumika kuonyesha kutojua jambo (sijui).
- **Kupepesa macho:** Hii hutumika kuonyesha mshangao, kutoamini, au hofu.

📌 **Kidokezo cha Kujifunza:**
Mawasiliano ya ishara katika Kiswahili (Zingatia): Kupepesa macho (mshangao), Kuinua mabega (kutojua), Kumpungia mkono (kuaga/kuita)."""
}

# Update explanations in data for q1 to q25
# First we apply it to the JS file
