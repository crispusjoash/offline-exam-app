import json
import shutil

filepath = 'public/data/kjsea-pretech-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    d = json.load(f)

# Update data
for q in d['sectionB']:
    qn = str(q.get('questionNumber'))
    
    if qn == '38':
        sqa = q['subQuestions'][0]
        sqb = q['subQuestions'][1]
        
        sqa['modelAnswer'] = '/assets/kjsea_pretech_2025_q38a_answer.svg'
        sqa['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for drawing a line of 6 cm length with the correct break line convention:\n  - Continuous thin line with freehand zig-zags (for long break), OR\n  - Continuous thin wavy/freehand line (for short break).\n* **Flexibility:** Accept both long-break (straight line with sharp zig-zags) and short-break (wavy freehand) conventions.'
        if 'gradingRubric' in sqa: del sqa['gradingRubric']

        sqb['modelAnswer'] = '/assets/kjsea_pretech_2025_q38b_answer.svg'
        sqb['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for drawing a line of 6 cm length with the correct centre line convention:\n  - Long dash followed by short dash / dot in a repeating pattern (chain thin line: "——— · ——— · ———").\n* **Flexibility:** Line must be thin with clear alternating long and short dashes.'
        if 'gradingRubric' in sqb: del sqb['gradingRubric']

    elif qn == '39':
        sqa = q['subQuestions'][0]
        sqb = q['subQuestions'][1]
        
        sqa['modelAnswer'] = 'Here is an exhaustive list of acceptable items made of metallic materials found in a school compound:\n\n1. **School Gates, Fences, and Grills:** Main iron gates, chain-link wire fences, and window/door burglar-proof security grilles.\n2. **Desks and Chairs:** Metal frames of classroom desks, laboratory stools, and dining hall benches.\n3. **Water Pipes, Taps, and Storage Tanks:** Galvanized iron water pipes, brass/steel water taps, and metallic water tanks.\n4. **Roofing Sheets and Gutters:** Corrugated iron / zinc-aluminium sheets, roof trusses, and metal rainwater gutters.\n5. **Doors and Windows:** Steel door frames, window casements, metallic hinges, handles, and padlocks.\n6. **Flag Post / Mast:** Steel pipe flag mast in the assembly ground.\n7. **Sports Equipment:** Football goalposts, volleyball/netball poles, and athletics shot puts.\n8. **Workshop and Garden Tools:** Hoes (jembes), pangas, shovels, rakes, wheelbarrows, claw hammers, and saws.\n9. **Kitchen Utensils and Equipment:** Large cooking pots (sufurias), metal ladles, food warmers, and gas cylinders.\n10. **School Bell:** Traditional brass/steel hanging bell or rim used for sounding school periods.'
        sqa['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award ½ mark for each valid metallic item named (4 items = Max 2 marks).\n* **Flexibility:** Accept any genuine metallic item typically found in a school environment.'
        if 'gradingRubric' in sqa: del sqa['gradingRubric']

        sqb['modelAnswer'] = 'Here is an exhaustive list of acceptable types of metals / alloys used:\n\n1. **Mild Steel (Carbon Steel):** Used for gates, window grills, desk frames, roof trusses, and doors.\n2. **Aluminium:** Used for cooking pots (sufurias), lightweight window frames, and roofing sheets.\n3. **Copper:** Used for electrical wiring, water heating pipes, and lightning arresters.\n4. **Brass (Copper-Zinc alloy):** Used for water taps, valves, padlocks, and musical instruments.\n5. **Cast Iron:** Used for heavy machinery bases, manhole covers, and bench vices.\n6. **Stainless Steel:** Used for kitchen sinks, cutlery, and scientific equipment.\n7. **Galvanized Iron / Zinc-coated Steel:** Used for water pipes, barbed wire, chain links, and corrugated roofing sheets.\n8. **Lead:** Used for roof flashing and battery terminals.\n9. **Bronze:** Used for bearings, bells, and plaques.'
        sqb['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid type of metal or alloy named (Max 2 marks).\n* **Flexibility:** Accept specific metal names (e.g. Mild steel, Aluminium, Copper, Brass, Iron, Stainless steel) or general classifications (Ferrous metals, Non-ferrous metals, Alloys).'
        if 'gradingRubric' in sqb: del sqb['gradingRubric']

    elif qn == '40':
        q['modelAnswer'] = 'Here is an exhaustive list of acceptable benefits of the e-Citizen platform to businesses:\n\n1. **Convenience and 24/7 Accessibility:** Business owners can access government services anytime, anywhere without visiting physical government offices.\n2. **Time Saving and Efficiency:** Eliminates long queues and reduces turnaround time for business name registration, licensing, and permit approvals.\n3. **Cost Reduction:** Lowers operational and transport costs associated with traveling to government agencies and submitting paper documents.\n4. **Transparency and Corruption Reduction:** Digital transactions with fixed official fees eliminate extortion, bribery, and middlemen (brokers).\n5. **Instant Payment and Automated Receipts:** Integration with mobile money (M-Pesa) and banking cards provides instant proof of payment and electronic official receipts.\n6. **Secure and Centralized Record Keeping:** All business licenses, tax records, and official documents are securely archived and easily retrievable online.\n7. **Faster Business Compliance and Licensing:** Simplifies statutory renewals such as single business permits, NTSA vehicle inspections, and environmental compliance.\n8. **Ease of Starting a Business:** Streamlined online company incorporation and registration stimulates formal business establishment.'
        q['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid benefit to businesses stated (Max 3 marks).\n* **Flexibility:** Accept any clearly stated advantage related to convenience, cost, speed, transparency, security, or compliance.'
        if 'gradingRubric' in q: del q['gradingRubric']

    elif qn == '41':
        q['modelAnswer'] = 'Here is an exhaustive list of acceptable commercial banking services for international business travel:\n\n1. **Foreign Currency Exchange (Forex Services):** Converting local currency (Ksh) into foreign currencies (e.g., US Dollars, Euros, British Pounds) for use abroad.\n2. **International Payment Cards (Debit / Credit / Prepaid Cards):** Issuing Visa or Mastercard debit/credit cards that can be used for cashless payments and ATM cash withdrawals globally.\n3. **Electronic Funds Transfer / Wire Transfers (SWIFT / RTGS):** Facilitating cross-border wire transfers to send or receive business funds internationally.\n4. **Letters of Credit (LC) and Bank Guarantees:** Providing trade finance instruments to guarantee payment to foreign suppliers or partners.\n5. **Online and Mobile Banking Services:** Enabling 24/7 remote monitoring of business accounts, bill payments, and international transactions via bank mobile apps or web portals.\n6. **Traveller\'s Cheques / International Banker\'s Drafts:** Providing secure monetary instruments accepted by foreign institutions.\n7. **Safe Custody Services:** Safekeeping valuable business documents, securities, and assets while the owner is away.\n8. **Travel Insurance Assistance:** Linking travelers with partnered insurance packages covering medical emergencies, lost baggage, or trip cancellations.'
        q['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid banking service stated (Max 2 marks).\n* **Flexibility:** Accept specific banking products (e.g., credit/debit cards, foreign exchange, mobile banking, wire transfer, letter of credit).'
        if 'gradingRubric' in q: del q['gradingRubric']

    elif qn == '42':
        q['modelAnswer'] = 'Here is an exhaustive list of acceptable reasons why a business plan is needed:\n\n1. **Securing Financing and Loans:** Financial institutions, investors, and SACCOs require a realistic business plan before approving business loans or capital.\n2. **Providing a Clear Roadmap and Direction:** Outlines the vision, goals, and step-by-step strategies needed to launch and operate the egg supply business successfully.\n3. **Identifying Potential Risks and Challenges:** Helps anticipate market fluctuations, disease outbreaks in poultry, price competition, and plan mitigation strategies in advance.\n4. **Budgeting and Resource Allocation:** Helps estimate required startup capital, operating expenses, pricing of eggs, and projected profit margins.\n5. **Understanding the Target Market and Competitors:** Guides market research on customer demand, potential institutional clients (schools, hotels, bakeries), and existing egg suppliers.\n6. **Monitoring and Evaluating Performance:** Acts as a benchmark to assess whether the business is meeting its operational and financial targets over time.\n7. **Motivating the Business Owner and Team:** Sets clear targets and responsibilities, keeping the entrepreneur focused on achieving measurable milestones.'
        q['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid reason for having a business plan (Max 2 marks).\n* **Flexibility:** Accept any logical explanation covering financing, planning, risk management, budgeting, or performance evaluation.'
        if 'gradingRubric' in q: del q['gradingRubric']

    elif qn == '43':
        q['modelAnswer'] = '**Biashara Club**\n**Statement of Financial Position as at 30th August, 2024**\n\n| **Assets** | **Amount (Ksh)** | **Capital & Liabilities** | **Amount (Ksh)** |\n| :--- | :--- | :--- | :--- |\n| **Current Assets:** | | **Capital:** | |\n| Stock | 2,000 | Owner\'s Capital | 20,000 |\n| Cash at Bank | 10,000 | | |\n| Cash in Hand | 15,000 | **Liabilities:** | |\n| | | **Long-term Liabilities:** | |\n| | | Loans | 5,000 |\n| | | **Current Liabilities:** | |\n| | | Creditors | 2,000 |\n| **Total Assets** | **27,000** | **Total Capital & Liabilities** | **27,000** |\n\n*(Alternative Vertical / Order of Liquidity Format)*:\n* **Total Assets:** Stock (2,000) + Cash at Bank (10,000) + Cash in Hand (15,000) = **Ksh 27,000**\n* **Financed by:** Capital (20,000) + Loan (5,000) + Creditors (2,000) = **Ksh 27,000**\n* **Accounting Equation Verified:** $\\text{Assets} = \\text{Capital} + \\text{Liabilities} \\implies 27,000 = 20,000 + 7,000$.'
        q['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks (Total 3 Marks):**\n  - **Title & Proper Heading (½ Mark):** Name of club and date ("Biashara Club Statement of Financial Position as at 30th August 2024").\n  - **Listing and Totaling Assets (1 Mark):** Correct placement of Stock (2,000), Bank (10,000), Cash (15,000) totaling **Ksh 27,000**.\n  - **Listing and Totaling Capital & Liabilities (1 Mark):** Correct placement of Capital (20,000), Loans (5,000), Creditors (2,000) totaling **Ksh 27,000**.\n  - **Balancing & Mathematical Accuracy (½ Mark):** Both sides correctly balanced at Ksh 27,000.\n* **Flexibility:** Accept horizontal (T-format) or vertical report format.'
        if 'gradingRubric' in q: del q['gradingRubric']

    elif qn == '44':
        q['modelAnswer'] = 'Here is an exhaustive list of acceptable factors to consider when setting financial goals:\n\n1. **Essential Needs versus Wants (Priorities):** Prioritizing must-have items (such as stationery, toiletries, emergency fare) over non-essential wants (such as luxury snacks or entertainment).\n2. **Duration of the Term (Time Frame):** Distributing the Ksh 800 proportionally across the weeks of the school term to avoid running out of funds prematurely.\n3. **Savings Target:** Setting aside a specific portion of the pocket money (e.g. 10%–20%) for personal savings or future unexpected emergencies.\n4. **Expected Total Expenses:** Estimating the anticipated total cost of items and services needed throughout the term against the fixed Ksh 800 budget.\n5. **Emergency and Contingency Fund:** Leaving a small buffer for unexpected occurrences such as minor medical expenses or replacement of lost stationery.\n6. **Opportunities for Value / Discounts:** Considering purchasing bulk items or affordable options to maximize purchasing power.'
        q['rubric'] = '📌 **Marking Scheme Guide:**\n\n* **Awarding Marks:** Award 1 mark for each valid factor stated (Max 2 marks).\n* **Flexibility:** Accept any logical factor related to needs vs wants, duration/timeline, budgeting, saving, total costs, or emergency preparation.'
        if 'gradingRubric' in q: del q['gradingRubric']

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-pretech-2025.json')
print('Batch 2 (Q38-Q44) complete')
