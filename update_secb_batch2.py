import json

file_path = "c:\\Users\\JOASH\\Desktop\\CBC\\offline-exam-app\\public\\data\\kjsea-creative-arts-sports-sectionb-2025.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

def update_question(q_list, updates):
    for q in q_list:
        if q["id"] in updates:
            q["modelAnswer"] = updates[q["id"]]
        if "subQuestions" in q:
            update_question(q["subQuestions"], updates)

updates = {
    "q45": "Here is a list of acceptable activities to develop strength:\n\n1. **Push-ups:** To develop upper body and arm strength.\n2. **Squats:** To build leg and lower body strength.\n3. **Weightlifting:** Lifting dumbbells, barbells, or locally improvised heavy objects.\n4. **Pull-ups / Chin-ups:** For back, shoulder, and arm strength.\n5. **Planks:** To build core abdominal and back strength.\n6. **Sit-ups / Crunches:** For abdominal muscle strength.\n7. **Lunges:** To strengthen the quadriceps and glutes.\n8. **Resistance band exercises:** Using elastic bands for muscle resistance.\n9. **Tug-of-war:** A fun sport activity that builds full-body pulling strength.\n10. **Climbing:** Rope climbing or hill climbing.\n11. **Carrying heavy loads:** Such as medicine balls or sandbags.",
    
    "q46a": "Here is a list of acceptable descriptions for the Approach phase in triple jump:\n\n1. Running along the runway to build maximum controllable speed before reaching the take-off board.\n2. Taking long, powerful, and rhythmic strides towards the board.\n3. Initially leaning slightly forward to accelerate, then transitioning to a tall, upright running posture just before the board.\n4. Focusing the eyes forward (not looking down at the feet) to maintain balance and speed into the jump.",
    
    "q46b": "Here is a list of acceptable descriptions for the Take-off phase in triple jump:\n\n1. Planting the take-off foot firmly on the board without stepping over the foul line (plasticine indicator).\n2. Driving the body forward and upward to initiate the 'hop' phase (the first of the three jumps).\n3. Swinging the free leg forward and upward powerfully to generate lift and momentum.\n4. Using a vigorous double-arm swing forward and upward to assist the upward drive off the board.",
    
    "q47a": "Here is a list of acceptable descriptions for Marking in netball:\n\n1. A defensive technique where a player stays close to an opponent to prevent them from receiving a pass.\n2. A strategy to prevent the opponent with the ball from making a pass or shooting.\n3. Defending a player by standing in front of them with arms raised to block the ball's path, while strictly maintaining the required distance (usually 3 feet or 0.9 meters).\n4. Shadowing the opponent's movements around the court to deny them free space to operate.",
    
    "q47b": "Here is a list of acceptable strategies for successful marking in netball:\n\n1. **Positioning:** Staying on the toes and keeping the body between the opponent and the ball.\n2. **Anticipation / Reading the game:** Watching the passer's eyes or body language to intercept the ball before it reaches the opponent.\n3. **Arm positioning:** Raising arms to block the vision of the passer or the path of the ball (while maintaining the 3ft distance).\n4. **Communication:** Talking with teammates to switch marking assignments or call out screens/picks.\n5. **Maintaining the 3ft distance:** Being careful not to step too close, which would result in an obstruction penalty.\n6. **Quick reaction time and balance:** Being ready to change direction quickly as the opponent dodges or fakes.\n7. **Peripheral vision:** Tracking both the ball in the air and the specific opponent being marked.",
    
    "q48a": "Here is a list of acceptable descriptions of the butterfly stroke:\n\n1. A swimming stroke where the swimmer lies on their breast and moves both arms simultaneously over the water in a forward circular motion (recovery).\n2. It is accompanied by a continuous dolphin kick, where both legs are kept together and move up and down simultaneously like a mermaid/dolphin tail.\n3. The body undergoes a continuous, undulating, wave-like movement driven by the core and chest pressing down into the water.\n4. Breathing is done by lifting the head forward or to the side just as the arms finish their pull phase.",
    
    "q48b": "Here is a list of acceptable challenges learners might experience with the butterfly stroke:\n\n1. **Fatigue / Exhaustion:** It is the most physically demanding stroke and requires immense upper body strength and cardiovascular stamina.\n2. **Coordination:** Struggling to synchronize the simultaneous arm pulls with the continuous dolphin kick.\n3. **Breathing timing:** Finding it difficult to lift the head to breathe at the correct moment without sinking the hips or breaking the stroke rhythm.\n4. **Water resistance / Drag:** Failing to maintain a streamlined body position, causing the body to plow through the water rather than glide.\n5. **Lack of upper body strength:** Unable to lift both arms out of the water simultaneously during the recovery phase.\n6. **Muscle cramps:** Intense, simultaneous leg movements can easily cause calf or foot cramps.\n7. **Swallowing water:** Due to improper breathing timing or not clearing the water surface completely."
}

update_question(data["sectionB"], updates)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("c:\\Users\\JOASH\\Desktop\\CBC\\offline-exam-app\\electron\\app\\data\\kjsea-creative-arts-sports-sectionb-2025.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Section B Batch 2 updated successfully.")
