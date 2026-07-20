import re
import sys

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

updates = [
    # KISWAHILI
    (
        r"Bajeti inaposomwa bungeni na 'kuidhinishwa', ina maana kuwa imepitishwa au 'kukubaliwa' rasmi kutumika\.",
        r"Bajeti inaposomwa bungeni na 'kuidhinishwa', ina maana kuwa imepitishwa au 'kukubaliwa' rasmi kutumika. Maneno mengine hapa yana maana tofauti: 'kuwasilishwa' ni kuipeleka tu bila uamuzi kufanywa, 'kuchunguzwa' ni kuitazama kwa kina ili kutafuta makosa, na 'kukamilika' ni kufikia mwisho wa matayarisho yake. Kuidhinishwa ni kitendo cha mwisho cha kuikubali kisheria."
    ),
    (
        r"Neno 'njia' lipo katika ngeli ya I-ZI\. Kivumishi kikubaliano chake lazima kianze na herufi 'n' iwapo ni kimoja \(njia nzuri\) au nyingi \(njia nzuri\)\.",
        r"Neno 'njia' lipo katika ngeli ya I-ZI. Katika ngeli hii, vivumishi huchukua kiambishi 'n-' au 'm-', hivyo 'nzuri' ni sahihi (njia nzuri). Chaguo zingine ni makosa kwa sababu 'kuzuri' hutumika kwa mahali (Ngeli ya PA-KU-MU), 'mzuri' hutumika kwa watu au mimea (Ngeli ya A-WA au U-I), na 'vizuri' ni kielezi cha namna, si kivumishi cha nomino."
    ),
    (
        r"Majembe \(LI-YA\) inakuwa Jembe\. Yatatumiwa inakuwa litatumiwa\. Mipapai \(M-MI\) inakuwa mpapai\. Yao inakuwa wake\. Michanga inakuwa mchanga\. Jawabu kamili ni 'Jembe litatumiwa kupalilia mpapai wake mchanga'\.",
        r"Katika kubadili sentensi hii kuwa umoja: 'Majembe' (LI-YA) inakuwa 'Jembe'. 'Yatatumiwa' inakuwa 'litatumiwa'. 'Mipapai' (M-MI) inakuwa 'mpapai'. 'Yao' inakuwa 'wake'. 'Michanga' inakuwa 'mchanga'. Chaguo A ni kosa kwa sababu 'yake' inatumika kwa ngeli ya I-ZI. Chaguo B ni kosa kwa sababu lina 'mmpapai'. Chaguo D ni kosa kwa sababu liliacha 'michanga' katika wingi badala ya 'mchanga'."
    ),
    (
        r"Matu ndiye mtendaji \(fundi\)\. Anna ndiye mtendewa anayefanyiwa kazi\. Kitenzi 'shona' katika kauli ya kutendewa kinakuwa 'shonewa'\. Kwa kuwa Anna ni mmoja, inakuwa 'ameshonewa'\.",
        r"Matu ndiye mtendaji (fundi). Anna ndiye mtendewa anayefanyiwa kazi. Kitenzi 'shona' katika kauli ya kutendewa kinakuwa 'shonewa'. Kwa kuwa Anna ni mmoja, inakuwa 'ameshonewa'. Chaguo la 'ameshonesha' (kauli ya kutendeshwa) linamaanisha Anna alimpa mtu mwingine kazi ya kushona, lakini hapa yeye ndiye anayefanyiwa. 'Wameshonewa' na 'wameshonesha' ni makosa kwa sababu yako katika wingi ilhali Anna ni mmoja."
    ),
    (
        r"Nahau 'kumpiga mtu jeki' hutumika kumaanisha kumpa mtu msaada au ushirikiano anapokuwa anafanya jambo fulani zito\.",
        r"Nahau 'kumpiga mtu jeki' hutumika kumaanisha kumpa mtu msaada au ushirikiano anapokuwa anafanya jambo fulani zito. Chaguo zingine hazihusiani na kusaidia: 'kufanya hima' inamaanisha kuharakisha, 'kuchapa kazi' inamaanisha kufanya kazi kwa bidii, na 'kutia fora' inamaanisha kushinda au kufanya vizuri zaidi ya wengine."
    ),
    
    # ENGLISH
    (
        r"The teacher is asking for the identity of the caller in a polite and formal manner suitable for a school setting\. 'Whom am I speaking to\?' is the most grammatically correct and polite way to ask this over the phone\.",
        r"The teacher is asking for the identity of the caller in a polite and formal manner suitable for a school setting. 'Whom am I speaking to?' is the most grammatically correct and polite way to ask this over the phone. 'Who are you?' is considered very rude and confrontational. 'Who is this?' is slightly better but still informal. 'Whom do you want to speak to?' is incorrect because the teacher is asking who the caller is, not who they are looking for."
    ),
    (
        r"The pupil is making a polite request to the teacher\. 'May I' is the correct modal verb for asking permission politely\.",
        r"The pupil is making a polite request to the teacher. 'May I' is the correct modal verb for asking permission politely. 'I want to' is too demanding and informal for a student addressing a teacher. 'I will' is a statement of future action, not a request for permission. 'Must I' asks if it is mandatory to be late, which completely changes the meaning of the conversation."
    ),
    (
        r"This is a Type 2 conditional sentence, which talks about a hypothetical or unlikely situation in the present or future\. The structure is 'If \+ past simple, \.\.\. would \+ infinitive'\. Therefore, 'would' is the correct choice\.",
        r"This is a Type 2 conditional sentence, which talks about a hypothetical or unlikely situation in the present or future. The structure is 'If + past simple, ... would + infinitive'. Therefore, 'would' is the correct choice. 'Will' is used for Type 1 conditionals (real possibilities, e.g., 'If I have money, I will...'). 'Should' and 'can' do not fit the grammatical structure of a hypothetical past-tense condition."
    ),
    (
        r"In the passage, the writer specifically mentions that the father wrote the 'prices' on the list, which helped Hassan know the total cost and expect exactly seventy-five shillings in balance\.\nWhile people often use shopping lists to avoid forgetting items, the emphasis here on prices and calculating the expected balance points to ensuring Hassan gets the correct change from the busy shopkeeper!",
        r"In the passage, the writer specifically mentions that the father wrote the 'prices' on the list, which helped Hassan know the total cost and expect exactly seventy-five shillings in balance. While Option A (didn't want him to forget) and Option B (didn't want him to delay) sound like logical real-world reasons to write a list, reading comprehension questions require you to find the reason supported by the text. The text specifically highlights that the father calculated the prices so Hassan would know his exact balance."
    ),
    (
        r"In a garden, you grow raw, living plants\. 'Dry' and 'cooked' don't make sense for growing vegetables\. 'Plenty' requires 'of' \(plenty of vegetables\)\. 'Different' perfectly describes a variety of vegetables growing in a garden\.",
        r"In a garden, you grow raw, living plants. 'Dry' and 'cooked' don't make sense for growing vegetables. Option D ('plenty') is extremely tempting because a garden can have plenty of vegetables, but it is grammatically incorrect to say 'plenty vegetables'; you must include the preposition 'of' (plenty of vegetables). Therefore, 'different' is the only grammatically and logically correct choice."
    ),
    (
        r"This is a question tag\. The main sentence is positive \('are planting'\), so the tag must be negative\. 'The children' is plural \(they\)\. Therefore, the correct tag is 'aren't they\?'",
        r"This is a question tag. The main sentence is positive ('are planting'), so the tag must be negative, eliminating 'are they?' and 'are we?'. The subject is 'The children', which is a third-person plural noun that must be replaced by the pronoun 'they'. The pronoun 'we' would only be used if the sentence was 'We are planting trees'. Therefore, the correct tag is 'aren't they?'"
    ),
    (
        r"The egg belongs to the hen\. To show possession linking a noun to its owner in a relative clause, we use the word 'whose'\.",
        r"The egg belongs to the hen. To show possession linking a noun to its owner in a relative clause, we use the word 'whose'. The other relative pronouns are incorrect here: 'who' and 'whom' are used for people, not animals or things. 'Which' is used for animals and things, but it cannot show possession (you cannot say 'the hen which egg'). Only 'whose' correctly shows that the egg belongs to the hen."
    )
]

for old, new in updates:
    # Use re.sub to find the old text and replace with new text
    # The old text is provided as a regex pattern to handle any minor whitespace differences
    content, count = re.subn(old, new, content)
    if count == 0:
        print(f"Warning: Could not find match for:\n{old}\n")
    else:
        print(f"Updated {count} occurrence(s) for a pattern.")

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Explanations successfully updated in pastPapers.js!")
