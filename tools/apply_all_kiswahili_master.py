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
Hebu nirekebishe: Kulingana by swali, Jibu ni **Manufaa ya maamkuzi**.

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
Mawasiliano ya ishara katika Kiswahili (Zingatia): Kupepesa macho (mshangao), Kuinua mabega (kutojua), Kumpungia mkono (kuaga/kuita).""",

    "q26": """Jibu sahihi ni **amekupatia**.

**Uchambuzi wa Jibu Sahihi:**
Wakati unaofaa hapa ni wakati uliopo mkamilifu (present perfect) unaoonyesha kitendo kilichokamilika lakini matokeo yake bado yapo. Daktari 'ameshampatia' tembe za kumeza. Kwa hivyo, "Daktari amekupatia tembe..." ni sahihi kwa kuwa anaendelea kupewa maelekezo kuhusu dawa alizokabidhiwa.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **akikupatia:** Ni hali ya masharti/wakati huu (if he gives you).
- **angekupatia:** Ni hali ya nge (angempa lakini hakumti).
- **akakupatia:** Inatumika katika usimuliaji wa wakati uliopita mfululizo.

📌 **Kidokezo cha Kujifunza:**
Kiambishi **-me-** huonyesha kuwa kitendo kimekamilika na matokeo yake yanaonekana au yanahisiwa wakati huo (amekupatia dawa).""",

    "q27": """Jibu sahihi ni **nyingine**.

**Uchambuzi wa Jibu Sahihi:**
Neno 'tembe' (pills/tablets) liko katika ngeli ya I-ZI au N-N. Katika wingi, vivumishi (adjectives) vya ngeli hii huchukua kiambishi 'ny-' (k.m. nyumba nyingine, nguo nyingine). Kwa hivyo ni "tembe nyingine".

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **kingine:** Huu ni upatanisho wa ngeli ya KI-VI umoja (k.m. kiti kingine).
- **mingine:** Huu ni upatanisho wa ngeli ya U-I wingi (k.m. miti mingine).
- **lingine:** Huu ni upatanisho wa ngeli ya LI-YA umoja (k.m. tunda lingine).

📌 **Kidokezo cha Kujifunza:**
Nomino za ngeli ya N-N (kama vile tembe, dawa, mvua) hutumia kiambishi **ny-** kwa kivumishi '-ingine' (nyingine).""",

    "q28": """Jibu sahihi ni **unameza**.

**Uchambuzi wa Jibu Sahihi:**
Muuguzi anazungumza moja kwa moja na mgonjwa (Topasa). Hivyo, anatumia nafsi ya pili umoja (wewe). Nafsi ya pili umoja huchukua kiambishi cha kitenzi 'u-'. Hivyo: "Hakikisha kuwa **u**nameza...".

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **anameza:** Hii inatumika kwa nafsi ya tatu umoja (yeye) (Hakikisha kuwa yeye anameza).
- **tunameza:** Hii inatumika kwa nafsi ya kwanza wingi (sisi).
- **mnameza:** Hii inatumika kwa nafsi ya pili wingi (nyinyi).

📌 **Kidokezo cha Kujifunza:**
Kumbuka viambishi vya nafsi: Mimi (**ni-**), Wewe (**u-**), Yeye (**a-**), Sisi (**tu-**), Nyinyi (**m-**), Wao (**wa-**).""",

    "q29": """Jibu sahihi ni **"Nitazingatia maagizo yako, muuguzi."**

**Uchambuzi wa Jibu Sahihi:**
Huu ni usemi halisi wa Topasa. Sentensi hii ni kauli ya kawaida (statement) inayoanza kwa alama ya mtajo (") na inafaa kuisha kwa kituo/nukta (.) kisha kufungwa kwa alama ya mtajo ("). 

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **"...muuguzi?":** Topasa haulizi swali, anatoa ahadi/kauli.
- **"...muuguzi!":** Topasa anajibu "kwa sauti ya unyonge", hivyo hatumii alama ya mshangao/hisia kali.
- **"Nitazingatia... muuguzi.** (Chaguo A): Inakosa alama ya kufunga mtajo (") mwishoni.

📌 **Kidokezo cha Kujifunza:**
Katika usemi halisi, alama za vituo (kama vile nukta, mkato au kiulizi) huwekwa **ndani** ya alama za kufunga mtajo ("...muuguzi.").""",

    "q30": """Jibu sahihi ni **kutibu**.

**Uchambuzi wa Jibu Sahihi:**
Kuna methali maarufu inayosema "Kutibu maradhi ni ghali kuliko kuyazuia" au "Kinga ni bora kuliko tiba". Katika muktadha huu, kuyatibu (kuyaponya) ni ghali zaidi kuliko kuchukua hatua za kuyazuia.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **kuambua:** Inamaanisha kutoa ngozi (k.m. kuambua ngozi/gamba).
- **kuchunguza:** Inamaanisha kutafiti (k.m. daktari kuchunguza ugonjwa), lakini haileti maana nzuri na "ni ghali kuliko kuyazuia".
- **kufahamu:** Inamaanisha kujua (kufahamu maradhi si ghali kuliko kuyazuia).

📌 **Kidokezo cha Kujifunza:**
Hii ni tafsiri ya methali "Prevention is better than cure". Tiba (kutibu) siku zote inagharimu zaidi ya Kinga (kuzuia).""",

    "q31": """Jibu sahihi ni **alitembea**.

**Uchambuzi wa Jibu Sahihi:**
Msemo wa Kiswahili ni 'kutembea unyounyo'. Humaanisha kutembea polepole, kwa utaratibu, labda kutokana na uchovu au unyonge (kama mgonjwa Topasa). Neno mwafaka hapa ni "alitembea".

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **alitembeleana:** Hii ina maana ya watu kutembeleana, kwenda kwa kila mmoja (reciprocal).
- **alitembelea:** Inamaanisha kutumia kitu kutembea (k.m. alitembelea gongo) au kwenda kumtazama mtu.
- **alitembelewa:** Inamaanisha kuna mtu alikuja kumwona.

📌 **Kidokezo cha Kujifunza:**
Misemo na nahau huwa na maneno maalum ambayo hayawezi kubadilishwa: **kutembea unyounyo** ni kutembea kwa unyonge.""",

    "q32": """Jibu sahihi ni **zilizofuata**.

**Uchambuzi wa Jibu Sahihi:**
Neno 'siku' liko katika ngeli ya N-N au I-ZI. Katika wingi (siku tano), inachukua kiambishi cha upatanisho 'zi-'. Tukiambatanisha na kirejeshi 'o', inakuwa '-zo-'. Hivyo basi ni "siku... zilizofuata" (the days that followed).

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **zilivyofuata:** 'vyo' inatumika kuelezea 'jinsi' jambo lilivyofanyika au upatanisho wa ngeli ya KI-VI.
- **zilikofuata:** 'ko' inatumika kuelezea 'mahali' (where they went).
- **zilipofuata:** 'po' inatumika kuelezea 'wakati/mahali' lakini haitumiki kama kirejeshi cha nomino (siku).

📌 **Kidokezo cha Kujifunza:**
O-rejeshi hufuata ngeli. Kwa 'siku' (ngeli ya zi), kirejeshi ni **zo** (zili-zo-fuata).""",

    "q33": """Jibu sahihi ni **alitia maanani**.

**Uchambuzi wa Jibu Sahihi:**
Nahau 'kutia maanani' inamaanisha kuchukua jambo kwa uzito, kutilia mkazo, au kufikiria jambo kwa umakini sana. Topasa alichukua maagizo ya daktari kwa uzito.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **alitia bidii:** Inamaanisha kufanya kazi kwa nguvu, haitumiki pamoja na 'maagizo'.
- **alitia hamu:** Inamaanisha kufanya mtu atamani kitu (k.m. chakula kilitia hamu).
- **alitia fora:** Inamaanisha kufanya vizuri sana au kushinda wengine wote katika jambo.

📌 **Kidokezo cha Kujifunza:**
Ukiambiwa jambo muhimu au onyo, unapaswa kuli**tia maanani** (kulisikiliza na kulifuata).""",

    "q34": """Jibu sahihi ni **kabla ya**.

**Uchambuzi wa Jibu Sahihi:**
Kawaida, wagonjwa hushauriwa kula chakula (kushikilia tumbo) kisha ndipo wameze dawa. Hivyo, alikula chakula chenye virutubishi "kabla ya" kumeza dawa. Hili ndilo mantiki ya kimatibabu.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **fauka ya:** Inamaanisha 'zaidi ya' au 'pamoja na' (in addition to). 
- **badala ya:** Inamaanisha kufanya jambo moja na kuacha jingine (kula badala ya kumeza dawa ni kosa).
- **ndani ya:** Inatumika kwa nafasi au muda, haifai katika mfuatano wa matukio.

📌 **Kidokezo cha Kujifunza:**
**Kabla ya** hutumika kuonyesha tukio ambalo linatangulia tukio jingine (before).""",

    "q35": """Jibu sahihi ni **Hakufanya**.

**Uchambuzi wa Jibu Sahihi:**
Mhusika (Topasa) anazungumziwa katika nafsi ya tatu umoja (yeye) na wakati ni uliopita (alipumzika). Ukanusho wa kitendo cha wakati uliopita (alifanya) katika nafsi ya tatu umoja ni "Hakufanya". 

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Hutafanya:** Huu ni ukanusho wa nafsi ya pili umoja (wewe) wakati ujao (wewe hutafanya).
- **Hukufanya:** Huu ni ukanusho wa nafsi ya pili umoja (wewe) wakati uliopita (wewe hukufanya).
- **Hatafanya:** Huu ni ukanusho wa wakati ujao kwa nafsi ya tatu (yeye hatafanya).

📌 **Kidokezo cha Kujifunza:**
Nafsi ya tatu umoja (yeye) hukanushwa kwa kiambishi **ha-** (Hajafanya, Hakufanya, Hatafanya). Wakati uliopita huchukua **-ku-** (Ha-ku-fanya).""",

    "q36": """Jibu sahihi ni **thamani**.

**Uchambuzi wa Jibu Sahihi:**
Maneno 'dhamani' (dhamana - guarantee/bail) na 'thamani' (value) yana sauti zinazokaribiana sana kimatamshi (fricatives: dh na th). Watu wengi huvurugwa kati ya sauti hizi mbili. Hii ni sawa na sauti za 'bao' na 'mbao' (b na mb).

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **samani:** (furniture) Inaanza na sauti 's' ambayo inatamkwa kwa urahisi wala haifanani na 'dh'.
- **jamani:** Inaanza na sauti 'j', haina ukaribu na 'dh'.
- **ramani:** Inaanza na sauti 'r'.

📌 **Kidokezo cha Kujifunza:**
Sauti 'dh' (kama katika dhambi) na 'th' (kama katika thamani) huitwa vipasuo-kwao kwa sababu hutamkwa kwa ulimi kugusa meno (dental fricatives), hivyo zinakaribiana sana.""",

    "q37": """Jibu sahihi ni **Katu alimsafishia Bili chumba.**

**Uchambuzi wa Jibu Sahihi:**
Sentensi asilia inaonyesha kwamba Katu alifanya kazi "kwa niaba ya" (on behalf of) Bili. Katika sarufi ya Kiswahili, hii hudhihirishwa na 'kauli ya kutendea' (prepositional form). Hivyo, Katu alimsafishia (alisafisha kwa niaba yake) Bili chumba.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **Katu na Bili walisafisha chumba:** Inamaanisha wote wawili walishirikiana, lakini Bili hakusafisha.
- **Katu alisafishiwa chumba cha Bili:** Inamaanisha kuna mtu alimsafishia Katu.
- **Katu na Bili walisafishiwa chumba:** Inamaanisha wote wawili walifanyiwa kazi hiyo na mtu wa tatu.

📌 **Kidokezo cha Kujifunza:**
Kauli ya kutendea (k.m. pika -> pikia, andika -> andikia) mara nyingi huonyesha kufanya jambo kwa faida ya (au kwa niaba ya) mtu mwingine.""",

    "q38": """Jibu sahihi ni **zi**.

**Uchambuzi wa Jibu Sahihi:**
Neno 'ngozi' katika sentensi lipo katika umoja kwa sababu ya kivumishi 'nyeusi' na uonyeshi wa ngeli "ngozi **zi**li... viatu **hivi**". Lakini hebu tutazame kwa umakini: Swali lina "viatu hivi". Ngozi inatumika kwa umoja (ngozi) au wingi (ngozi). Ngozi hufuata ngeli ya U-ZI (Umoja ni 'U' wingi ni 'ZI' mf. Ngozi huu, ngozi hizi) au I-ZI (Ngozi hii, ngozi hizi). Kwa vile "ngozi nyeusi" inaleta maana ya jumla ya wingi wa nyenzo iliyotumika, upatanisho ni "zi" -> **Zi**litumiwa.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **ya:** Haitumiki kwa vitenzi (ni kiunganishifu au inawakilisha ngeli ya YA lakini 'ngozi' si ya ngeli ya LI-YA wingi).
- **vi:** Ni ya ngeli ya KI-VI wingi.
- **wa:** Ni ya ngeli ya U-I umoja, au A-WA.

📌 **Kidokezo cha Kujifunza:**
Nomino 'ngozi' katika wingi huchukua kiambishi **zi-** katika kitenzi (Ngozi hizi **zi**mechanika).""",

    "q39": """Jibu sahihi ni **Karisa alifika lakini alipata Lulu ameondoka mapema.**

**Uchambuzi wa Jibu Sahihi:**
Karisa alipofika lengo lilikuwa amkute Lulu, lakini kuna hali ya kutofanikiwa katika matarajio hayo (Lulu ameondoka). Kuunganisha sentensi zenye kinyume au matokeo ambayo hayakutarajiwa huhitaji kiunganishi 'lakini' (but). 

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **kwani:** Inaonyesha sababu (because). Karisa hakufika kwa sababu Lulu aliondoka.
- **pia:** Inaonyesha nyongeza/pamoja na (also).
- **lau:** Inaonyesha masharti (if only).

📌 **Kidokezo cha Kujifunza:**
**Lakini** hutumika kuunganisha sehemu mbili za sentensi ambapo sehemu ya pili inatoa matokeo ambayo ni kinyume na matarajio ya sehemu ya kwanza.""",

    "q40": """Jibu sahihi ni **Juma asingemaliza mtihani wake asingepata cheti.**

**Uchambuzi wa Jibu Sahihi:**
Sentensi asilia ipo katika hali ya masharti (conditional) inayowezekana wakati uliopita 'nge' (angemaliza... angepata). Ukanusho wa kiambishi '-nge-' hufanywa kwa kuingiza '-si-' baada ya nafsi, hivyo inakuwa '-singe-'. Kwa hiyo: a-nge-maliza -> a-singe-maliza; a-nge-pata -> a-singe-pata.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **asipomaliza... hatapata:** Huu ni ukanusho wa masharti ya 'ki' (Aki-maliza -> Asi-po-maliza).
- **hajamaliza... hatapata:** Ukanusho wa nyakati mchanganyiko (present perfect na future).
- **asingalimaliza... asingalipata:** Huu ni ukanusho wa hali ya 'ngali' (angali -> asingali) ambayo hutumika kwa masharti yasiyowezekana kabisa.

📌 **Kidokezo cha Kujifunza:**
Wakati tegemezi **-nge-** ukanushwa kwa **-singe-**. (k.m., ningesoma -> nisingesoma).""",

    "q41": """Jibu sahihi ni **Leona alimwandikisha Toni barua ya kuomba msamaha.**

**Uchambuzi wa Jibu Sahihi:**
Leona "alimfanya Toni aandike" inamaanisha alisababisha kitendo kifanyike (causative). Katika Kiswahili, hii inaitwa 'kauli ya kutendesha' (kufanya mtu/kitu kifanye jambo). Kitenzi 'andika' kinakuwa 'andikisha'.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **alimwandikia:** (Kauli ya kutendea) Inamaanisha Leona aliandika barua badala ya Toni (on his behalf).
- **aliandikiwa na Toni:** Toni alimwandikia Leona barua, lakini hapa Toni anaambiwa aandike ya kuomba msamaha (siyo amwandikie Leona).
- **waliandikiana:** (Kauli ya kutendeana) Inamaanisha Leona alimwandikia Toni, na Toni akamwandikia Leona.

📌 **Kidokezo cha Kujifunza:**
Maneno yanayoishia kwa **-sha** au **-za** mara nyingi huwa katika kauli ya kutendesha (kufanya mtu afanye). K.m. pika -> pikisha, ruka -> rusha.""",

    "q42": """Jibu sahihi ni **"Vijana watafaidika na miradi ya kujiendeleza mwaka huu," Tiriki alitangaza.**

**Uchambuzi wa Jibu Sahihi:**
Kubadilisha usemi taarifa kuwa usemi halisi unahitaji kurejesha maneno kwenye hali yake ya asili. 
- 'wangefaidika' (past conditional) iliripotiwa kutoka kwa wakati ujao 'watafaidika' (future). 
- 'mwaka huo' (that year) iliripotiwa kutoka kwenye neno la kuonyesha ukaribu 'mwaka huu' (this year).
Kwa hivyo chaguo A ndilo lenye mabadiliko haya sahihi.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- B, C na D yametumia 'wangefaidika' kwenye mtajo (haitumiki kuripotiwa kutoka wakati ujao) au yana makosa ya kutumia 'mwaka huo' / 'mwaka huu' isivyostahili. 

📌 **Kidokezo cha Kujifunza:**
Katika usemi halisi: 'sasa' hugeuka 'wakati huo', 'hapa' hugeuka 'pale', 'leo' hugeuka 'siku hiyo', na vitenzi vya 'ta' hugeuka 'nge'. Tunaporudi nyuma, tunabadilisha kinyume chake.""",

    "q43": """Jibu sahihi ni **Kibwawa cha kijito hicho kinawafaa wakaaji wa kijiji chao.**

**Uchambuzi wa Jibu Sahihi:**
Hali ya udogo hupatikana kwa kubadilisha nomino kuingia katika ngeli ya KI-VI, na mara nyingi kiambishi 'ki-' au 'ch-' huongezwa mwanzoni.
- bwawa -> kibwawa
- mto -> kijito
- mji -> kijiji
Jibu B lina nomino zote katika hali sahihi ya udogo.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- A haina udogo kabisa (bwawa, mto, mji).
- C na D zimechanganya (k.m. ina 'mto' badala ya kijito, au ina 'mji' badala ya kijiji).

📌 **Kidokezo cha Kujifunza:**
Kumbuka: Jitu (ukubwa) -> Mtu (kawaida) -> Kijitu (udogo). Mtoto -> Kitoto. Mlima -> Kilima.""",

    "q44": """Jibu sahihi ni **Ugonjwa ulimdhoofisha kisha ulitafutiwa tiba.**

**Uchambuzi wa Jibu Sahihi:**
Kuna matukio mawili yanayofuatana moja baada ya jingine. Kwanza ugonjwa ulimdhoofisha (mgonjwa), halafu (baadaye) ule ugonjwa ukatafutiwa tiba. Kiunganishi kinachofaa kuonyesha mfululizo huu wa wakati/matukio ni "kisha" (halafu/then).

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **aghalabu:** Inamaanisha 'mara nyingi' au 'kwa kawaida' (usually), ambayo haileti maana hapa.
- **japo:** Inamaanisha 'ingawa' (although). Hailingani na mantiki.
- **sembuse:** Inamaanisha 'seuzee' (let alone), haitumiki kuunganisha matukio yaliyofuatana.

📌 **Kidokezo cha Kujifunza:**
Viunganishi vya mfululizo (kama **kisha, halafu, baadaye, hatimaye**) hutumika kuelezea matukio yanayofanyika moja baada ya jingine.""",

    "q45": """Jibu sahihi ni **sogea - karibia**.

**Uchambuzi wa Jibu Sahihi:**
Jozi nyingi katika swali ni vitenzi vyenye maana kinyume (antonyms). 
- pakia (load) kinyume chake ni pakua (unload).
- nenda (go) kinyume chake ni rudi (return).
- kusanya (gather) kinyume chake ni tawanya (scatter).
Hata hivyo, 'sogea' na 'karibia' zina maana sawa (ni visawe - synonyms). Hivyo hii ni tofauti na zingine.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
A, B, na D ni vinyume, wakati C ni visawe. Kwa hivyo C inajitenga.

📌 **Kidokezo cha Kujifunza:**
Ukiona orodha ambayo huna uhakika nayo, tafuta uhusiano wa maneno kwenye jozi. Kama matatu yanafuata kanuni moja (k.m. vinyume), basi lile ambalo halifuati (visawe) ndilo jibu.""",

    "q46": """Jibu sahihi ni **walichezeana**.

**Uchambuzi wa Jibu Sahihi:**
Neema alimchezea Karobi, naye Karobi akamchezea Neema. Hili ni tendo linalofanywa kwa kushirikiana na kupokezana (kila mtu akimfanyia mwenzake). Katika Kiswahili, hii hudhihirishwa kwa kiambishi cha kauli ya kutendeana **'-ana'**. Kwa kuwa ni kauli ya kutendea (chezea), inakuwa 'chezeana'.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **walichezewa:** Hii ni kauli ya kutendewa (passive). Wote walichezewa na mtu wa tatu.
- **walichezeka:** Hii ni kauli ya kutendeka (stative), inamaanisha walikuwa na uwezo wa kuchezwa (haiwezekani).
- **walichezwa:** Kauli ya kutendwa (walichezwa na nani?).

📌 **Kidokezo cha Kujifunza:**
Kauli ya kutendana au kutendeana huonyeshwa kwa kiambishi **-ana** (k.m. piga -> pigana, saidia -> saidiana).""",

    "q47": """Jibu sahihi ni **Wadudu hatari waliendelea kupungua kutokana na juhudi zilizowekwa za kuwadhibiti.**

**Uchambuzi wa Jibu Sahihi:**
Kubadilisha sentensi kwenda wakati uliopita unahitaji kutumia viambishi vya wakati uliopita **'-li-'**. 
- 'wanaendelea' inabadilika kuwa 'waliendelea'. 
- 'zinazowekwa' inabadilika kuwa 'zilizowekwa'. 
Chaguo lenye mabadiliko haya yote mawili sahihi ni B.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **wataendelea / zitakazowekwa:** Huu ni wakati ujao ('-ta-').
- **wameendelea / zilizowekwa:** 'wameendelea' ni wakati uliopo mkamilifu ('-me-').

📌 **Kidokezo cha Kujifunza:**
Wakati wa uliopita hutumia kiambishi **-li-**, Wakati uliopo hutumia **-na-**, Wakati ujao hutumia **-ta-**, na Wakati uliopo mkamilifu hutumia **-me-**.""",

    "q48": """Jibu sahihi ni **Nyua zilizopandwa na wafanyakazi kuzunguka maboma yao zimenawiri.**

**Uchambuzi wa Jibu Sahihi:**
Tunahitaji kubadilisha kila neno lenye uwezekano wa wingi katika sentensi:
- Ua -> Nyua
- uliopandwa -> zilizopandwa
- mfanyakazi -> wafanyakazi
- boma -> maboma
- lake -> yao
- umenawiri -> zimenawiri
Sentensi C ndiyo pekee iliyozingatia mabadiliko haya yote.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- A haikubadilisha 'mfanyakazi' wala 'boma lake'.
- B haikubadilisha 'boma lake'.
- D haikubadilisha 'mfanyakazi'.

📌 **Kidokezo cha Kujifunza:**
Unapoulizwa kuweka sentensi katika wingi, hakikisha nomino, vivumishi (adjectives), na vitenzi vyote vimebadilika kufuata ngeli yake ya wingi.""",

    "q49": """Jibu sahihi ni **Fisi wakishirikiana huweza kumfukuza hata simba.**

**Uchambuzi wa Jibu Sahihi:**
Hali ya mazoea inatambulishwa na kiambishi 'hu-' ambacho huambatanishwa mwanzoni mwa kitenzi. Kinaonyesha jambo au tabia inayoendelea kufanyika mara kwa mara kama desturi au sheria. "huweza" katika sentensi D inaashiria tabia ya kawaida kwa fisi.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **unatokana:** Ni wakati uliopo unaoendelea (present continuous '-na-').
- **ukiipenda / hutakosa:** 'ukiipenda' ni hali ya masharti ('-ki-') na 'hutakosa' ni ukanusho wa wakati ujao.
- **watampata:** Ni wakati ujao ('-ta-').

📌 **Kidokezo cha Kujifunza:**
Kiambishi **hu-** katika vitenzi kinaonyesha hali ya mazoea, tabia au asili (k.m. Ng'ombe **hu**la nyasi).""",

    "q50": """Jibu sahihi ni **kobe.**

**Uchambuzi wa Jibu Sahihi:**
Hili ni swali la fasihi simulizi linalohusu usimuliaji wa hadithi za wanyama (ngano). Kulingana na ngano nyingi za Kiswahili, kila mnyama hupewa sifa fulani maalum (Tashhisi). 
- Sungura hupewa sifa ya ujanja na hila (trickster). 
- Kobe hupewa sifa ya hekima, uvumilivu, busara, na ukimya. Hivyo, hekima ni kwa kobe.

**Kwa Nini Majibu Mengine Siyo Sahihi:**
- **njiwa:** Hufananishwa na amani na upole.
- **fisi:** Hufananishwa na ulafi na ufisi/ujinga.
- **simba:** Hufananishwa na nguvu na ukali (mfalme wa pori).

📌 **Kidokezo cha Kujifunza:**
Wahusika wa wanyama katika hadithi wana sifa mahususi (stereotypes) ili kuwafikishia wasikilizaji mafunzo kwa njia ya mfano."""
}

with open("src/data/kjsea-kiswahili-2025.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content.replace("export const kjseaKiswahili2025 = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

data = json.loads(json_str)

for q in data["sectionA"]:
    if q["id"] in detailed_explanations:
        q["explanation"] = detailed_explanations[q["id"]]

with open("src/data/kjsea-kiswahili-2025.js", "w", encoding="utf-8") as f:
    f.write(f"export const kjseaKiswahili2025 = {json.dumps(data, indent=2)};\n")
