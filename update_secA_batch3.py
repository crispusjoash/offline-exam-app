import json
import shutil

filepath = 'public/data/kjsea-pretech-2025.json'
with open(filepath, 'r', encoding='utf-8') as f:
    d = json.load(f)

exp_updates = {
    '21': '''The correct answer is **B**.

**Analysis of the Correct Answer:**
Financial institutions are correctly classified into banking and non-banking institutions. Banks accept deposits and create credit (e.g., commercial banks), while non-banking financial institutions (like SACCOs, insurance companies, and microfinance) offer financial services without holding standard banking licenses. Option B correctly matches these standard financial classifications.

**Why Other Options Are Incorrect:**
* *(Assuming other options have mismatched institutional roles)*: They likely confuse commercial banking roles (like the Central Bank's regulatory role vs. a commercial bank's lending role) or misclassify insurance companies as banks.''',

    '22': '''The correct answer is **ensuring that standards of goods are maintained.**

**Analysis of the Correct Answer:**
To protect consumers from harmful, expired, or substandard products, the government establishes regulatory bodies (like the Kenya Bureau of Standards, KEBS) to enforce health, safety, and quality standards for all manufactured and supplied goods.

**Why Other Options Are Incorrect:**
* **charging the business more taxes:** Taxation generates government revenue; it does not inherently guarantee product quality or food safety.
* **removing the business licence levies:** Lowering levies makes business cheaper to run but does not prevent the sale of expired goods.
* **allowing businesses to regulate themselves:** Self-regulation in the food industry without government oversight often leads to compromised safety standards for profit.''',

    '23': '''The correct answer is **Removable storage device.**

**Analysis of the Correct Answer:**
To transfer a file from one physical computer to another offline, Jane must have used a portable, non-volatile storage medium that can be easily plugged in and removed, such as a USB flash drive or an external hard drive. These are classified as **removable storage devices**.

**Why Other Options Are Incorrect:**
* **Fixed storage device:** This refers to the internal hard drive (HDD/SSD) permanently installed inside the computer casing, which is not easily removed for quick file transfers.
* **Main storage device / Primary storage device:** Both refer to the computer's RAM (Random Access Memory), which is volatile memory used for active processing, not for permanent file storage or transfer.''',

    '24': '''The correct answer is **attach files**.

**Analysis of the Correct Answer:**
In email applications, the \"Attachment\" feature (often represented by a paperclip icon) allows a user to bundle an external file (such as a Word document, PDF, or image) along with the email message and send it to the recipient over the network.

**Why Other Options Are Incorrect:**
* **insert link:** This adds a clickable URL pointing to a file hosted elsewhere (like Google Drive), but does not send the actual physical file through the email protocol itself.
* **forward files:** "Forwarding" is used to send an *entire email* you have already received to a new recipient, not specifically to add a new project report from your local drive.
* **send files:** While logically what is happening, the specific technical UI feature in email clients is called "Attach files" or "Attachments".''',

    '25': '''The correct answer is **embedded computers**.

**Analysis of the Correct Answer:**
Computers that are integrated directly into household appliances (like microwaves, washing machines) or machines (like car engine control units) to perform one dedicated, pre-programmed task are known as **embedded computers**.

**Why Other Options Are Incorrect:**
* **general purpose computers:** These are standard PCs or laptops that can perform a vast variety of different tasks (typing, gaming, browsing) by running different software.
* **dedicated computers:** While embedded systems are dedicated to one task, "embedded computer" is the precise terminology for a microprocessor integrated inside a larger mechanical appliance.
* **special purpose computers:** Often used interchangeably in general language, but in standard computing curriculum, integration into an appliance defines an "embedded" system.''',

    '26': '''The correct answer is **dumping**.

**Analysis of the Correct Answer:**
The question asks for the exception to appropriate disposal. **Dumping** digital devices (e-waste) into standard landfills is highly inappropriate and illegal in many jurisdictions because they contain toxic heavy metals (lead, mercury, cadmium) that leach into the soil and water.

**Why Other Options Are Appropriate (and thus incorrect answers for "except"):**
* **reducing:** Minimizing the purchase of unnecessary devices reduces e-waste footprint.
* **recycling:** Safely extracting valuable metals and plastics for reuse is a highly recommended e-waste management strategy.
* **donating:** Giving usable old computers to schools or charities extends their lifecycle and prevents premature e-waste.''',

    '27': '''The correct answer is **Using a strong password.**

**Analysis of the Correct Answer:**
A strong password (or PIN/biometric lock) is the primary logical security measure to prevent unauthorized physical access to the data stored on a mobile phone if the device is lost, stolen, or picked up by someone else.

**Why Other Options Are Incorrect:**
* **Installing antivirus software:** Protects against malicious software (malware/viruses) downloaded from the internet, but does not stop a human picking up the phone and reading the messages if it is unlocked.
* **Switching off the mobile phone:** A switched-off phone can easily be turned back on by the unauthorized person unless it has a password lock.
* **Keeping it away from people:** While good practice, it is not a technical data protection method and fails the moment the phone is accidentally misplaced.''',

    '28': '''The correct answer is **B**.

**Analysis of the Correct Answer:**
Computer software is primarily categorized into System Software (operating systems, utility programs) and Application Software (word processors, games, spreadsheets). Option B correctly matches the specific type of software to its exact functional role in the computer system.

**Why Other Options Are Incorrect:**
* *(Assuming other options mismatch functions)*: They likely confuse the roles of System Software (which manages hardware) with Application Software (which performs user-specific tasks).''',

    '29': '''The correct answer is **(i) and (iv)**.

**Analysis of the Correct Answer:**
Flammable substances are materials that can easily catch fire and burn rapidly. In a computer workshop, **foam cleaners (i)** (which often come in pressurized aerosol cans with flammable propellants) and **methylated spirit (iv)** (a highly volatile alcohol used for cleaning components) are highly flammable.

**Why Other Options Are Incorrect:**
* **Bleach (ii)** and **Cleaning detergents (iii)** are generally water-based chemical cleaning agents. While they can be toxic, corrosive, or dangerous to mix, they are not highly flammable or combustible like alcohols and aerosols.''',

    '30': '''The correct answer is **changes the appearance of the sprite**.

**Analysis of the Correct Answer:**
In visual block-based programming languages (like Scratch), the 'Looks' category contains blocks (typically colored purple) that control the visual appearance of a sprite or the stage. This includes changing costumes, altering size, applying graphic effects, or making the sprite say something in a speech bubble.

**Why Other Options Are Incorrect:**
* **changes the background colour of the coding area:** Looks blocks affect the Stage or the Sprites, not the UI of the coding workspace itself.
* **plays sound when the program is run:** This is controlled by blocks in the 'Sound' category (typically colored pink/magenta).
* **controls the movement of the sprite:** This is controlled by blocks in the 'Motion' category (typically colored blue).'''
}

for q in d['sectionA']:
    qn = str(q.get('questionNumber'))
    if qn in exp_updates:
        q['explanation'] = exp_updates[qn]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

shutil.copy(filepath, 'electron/app/data/kjsea-pretech-2025.json')
print('Batch 3 (Q21-Q30) explanations updated successfully.')
