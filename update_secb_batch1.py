import json

file_path = "c:\\Users\\JOASH\\Desktop\\CBC\\offline-exam-app\\public\\data\\kjsea-creative-arts-sports-sectionb-2025.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# We will recursively find questions by their id and update the modelAnswer
def update_question(q_list, updates):
    for q in q_list:
        if q["id"] in updates:
            q["modelAnswer"] = updates[q["id"]]
        if "subQuestions" in q:
            update_question(q["subQuestions"], updates)

updates = {
    "q41a": "Here is the comprehensive guide for the F major scale drawing:\n\n1. **Clef:** Must be written on the treble staff.\n2. **Notes:** The notes must be F, G, A, B\u266d, C, D, E, F.\n3. **Note Value:** All notes must be semi-breves (whole notes, open ovals with no stems).\n4. **Ascending:** The notes must go strictly up from F4 (first space) to F5 (fifth line).\n5. **Key Signature:** NO key signature should be at the start of the staff.\n6. **Accidental:** A flat sign (\u266d) MUST be placed immediately to the left of the B note on the middle line.",
    
    "q42a": "Here is a list of acceptable guidelines/options for a correct answering phrase:\n\n1. **Length:** It must be exactly a four-bar melody in total (meaning the added phrase is two bars long if the antecedent is two bars).\n2. **Rhythm Match:** The answering phrase should generally mirror or closely resemble the rhythmic pattern of the opening phrase.\n3. **Resolution (Cadence):** The final note of the answering phrase must resolve to the tonic (home note) to create a sense of completion (perfect cadence).\n4. **Melodic Shape:** It can be an exact sequence, an inversion, or a complementary melodic curve to the first phrase.\n5. **Example (Twinkle Twinkle):** If antecedent is (G G D D | E E D rest), a valid consequent is (C C B B | A A G rest).",
    
    "q43ai": "Here is a list of acceptable meanings for **mf**:\n\n1. Mezzo-forte\n2. Moderately loud\n3. Medium loud\n4. Half loud\n5. Fairly loud",
    
    "q43aii": "Here is a list of acceptable meanings for **p**:\n\n1. Piano\n2. Soft\n3. Quiet\n4. Softly\n5. Gently",
    
    "q43aiii": "Here is a list of acceptable meanings for **||:  :||**:\n\n1. Repeat marks\n2. Repeat the music enclosed within the signs\n3. Go back and play the section again\n4. Repeat section\n5. Play twice",
    
    "q43a_ii": "Here is a list of acceptable answers for bars with exact repetition:\n\n1. Bars 1 and 2\n2. Bars 5 and 6\n3. Bars 9 and 10 (depending on the arrangement)\n*(Accept any two bars that are visually and musically identical in the provided score)*",
    
    "q43a_iii": "Here is a list of acceptable answers for the lowest pitch:\n\n1. Middle C\n2. C4\n3. Doh (if in key of C major)\n4. C natural",
    
    "q43b_i": "Here is a list of acceptable roles of music during a football match:\n\n1. **Motivation:** To encourage and boost the morale of the players on the field.\n2. **Entertainment:** To entertain the spectators before the match, during halftime, or after the match.\n3. **Intimidation:** Loud chants and songs used to intimidate or psych out the opposing team.\n4. **Unity/Identity:** Singing club anthems or national anthems fosters a sense of belonging and solidarity among fans.\n5. **Celebration:** To celebrate goals, victories, or lifting a trophy.\n6. **Atmosphere:** To create a lively, vibrant, and festive stadium atmosphere.\n7. **Communication:** Fans use specific chants to communicate with the referee (expressing dissatisfaction) or players.\n8. **Cultural Expression:** To display the cultural heritage of the home team or country.\n9. **Pacing:** Drum beats help coordinate the rhythmic clapping or dancing of the fans.\n10. **Commercial:** Playing sponsor jingles or walk-out music to build anticipation.",
    
    "q43b_ii": "Here is a list of acceptable ways a soloist exercises freedom in a traditional dance:\n\n1. **Improvisation of Lyrics:** Making up words spontaneously to praise an individual or fit the occasion.\n2. **Melodic Variation:** Changing the tune, pitch, or adding vocal ornaments (ululations) freely.\n3. **Movement/Dancing:** Moving freely around the stage, dancing differently from the rest of the choir.\n4. **Tempo Control:** Dictating how fast or slow the song goes, prompting the instrumentalists to follow.\n5. **Call and Response:** Deciding when to cue the choir (response) and how long their solo section lasts.\n6. **Audience Interaction:** Stepping out to interact, sing to, or dance with specific audience members.\n7. **Costume and Props:** Sometimes wearing a distinct costume or carrying a special prop (like a fly whisk or spear) that they use freely.",
    
    "q44a": "Here is a list of acceptable aspects that need to be brought out at the beginning (exposition) of a story's plot:\n\n1. **Setting (Time):** When the story takes place (e.g., \"A long time ago\", specific year).\n2. **Setting (Place):** Where the story is located (e.g., a village, a forest, a city).\n3. **Characters:** Introduction of the main characters (protagonist) and their basic traits.\n4. **Mood/Atmosphere:** Establishing the emotional tone of the story (e.g., spooky, cheerful, tense).\n5. **The Inciting Incident:** The initial problem or conflict that sets the story in motion.\n6. **Background Information:** Context about the society, rules, or situation the characters live in.\n7. **Point of View:** Establishing who is telling the story (first person, third person).",
    
    "q44b": "Here is a list of acceptable reasons for engaging in vocal and physical warm-ups before a play:\n\n1. **Prevent Physical Injury:** Loosens up muscles and joints, preventing strains or sprains during active scenes.\n2. **Prevent Vocal Cord Strain:** Warms up the vocal cords to prevent hoarseness, damage, or losing one's voice.\n3. **Improve Vocal Projection:** Helps actors breathe deeply and project their voices to reach the back of the audience.\n4. **Enhance Articulation:** Exercises the lips, jaw, and tongue for clear, understandable diction.\n5. **Reduce Stage Fright:** Calms the nerves, releases adrenaline, and relaxes the actor.\n6. **Build Mental Focus:** Helps actors concentrate, get into character, and leave outside distractions behind.\n7. **Increase Flexibility/Agility:** Prepares the body for quick, expressive, or exaggerated theatrical movements.\n8. **Ensemble Building:** Group warm-ups build teamwork, trust, and synchronicity among the cast.\n9. **Clear the Throat:** Helps clear mucus and ensures smooth vocal delivery.\n10. **Breath Control:** Engages the diaphragm for sustained speaking without running out of breath."
}

update_question(data["sectionB"], updates)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("c:\\Users\\JOASH\\Desktop\\CBC\\offline-exam-app\\electron\\app\\data\\kjsea-creative-arts-sports-sectionb-2025.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Section B Batch 1 updated successfully.")
