with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix English Q1-3 telephone conversation passage
# Add bold to speaker names and proper paragraph spacing
old_text = '"Pupil: Hello, Teacher.\\nClass teacher: Hello, ____1____.\\nPupil: I am Barasa Kabengi, a pupil in Grade 6 Yellow.\\nClass teacher: Yes, Barasa, how can I help you?\\nPupil: ____2____.\\nClass teacher: Is there a problem at home?\\nPupil: My young sister is joining Grade 1 today. She has been crying. She wants me to accompany her to school. Grade 1 learners are to report at 8:30 a.m. today.\\nClass teacher: Okay, Barasa. You can come along with her. Make sure you come to see me after she settles down in her classroom.\\nPupil: ____3____."'

new_text = '"**Pupil:** Hello, Teacher.\\n\\n**Class teacher:** Hello, ____1____.\\n\\n**Pupil:** I am Barasa Kabengi, a pupil in Grade 6 Yellow.\\n\\n**Class teacher:** Yes, Barasa, how can I help you?\\n\\n**Pupil:** ____2____.\\n\\n**Class teacher:** Is there a problem at home?\\n\\n**Pupil:** My young sister is joining Grade 1 today. She has been crying. She wants me to accompany her to school. Grade 1 learners are to report at 8:30 a.m. today.\\n\\n**Class teacher:** Okay, Barasa. You can come along with her. Make sure you come to see me after she settles down in her classroom.\\n\\n**Pupil:** ____3____."'

if old_text in text:
    text = text.replace(old_text, new_text)
    print('Fixed telephone conversation passage')
else:
    print('ERROR: Could not find telephone conversation passage')

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(text)
