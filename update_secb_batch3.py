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
    "q49a": "Here is a list of acceptable indigenous board games played in Kenya:\n\n1. Ajua (also known as Bao or Mancala)\n2. Shisima\n3. Giuthi\n4. Enkeshui\n5. Coro\n6. Morabaraba\n*(Accept any culturally accurate traditional Kenyan board/alignment game)*",
    
    "q49b": "Here is a list of acceptable descriptions depending on the game identified in (a):\n\n**For Ajua / Mancala / Bao:**\n1. Players \"sow\" seeds (or stones/marbles) into pits or holes carved into a wooden board.\n2. The game involves scooping seeds from one pit and dropping them sequentially one by one into subsequent pits.\n3. The goal is to capture more seeds than the opponent by ending a turn in a specific manner (e.g., dropping the last seed into an occupied hole to \"eat\" the opponent's seeds), following turn-based rules.\n\n**For Shisima:**\n1. It is an alignment game played on an octagonal board with a center point (the 'shisima' or water source).\n2. Players take turns sliding their pieces along the lines towards the center or around the edges.\n3. The objective is to be the first to align three pieces in a straight row passing through the center.",
    
    "q49c": "Here is a list of acceptable benefits of playing indigenous board games:\n\n1. **Cognitive skills:** Improves critical thinking, counting, mental arithmetic, and strategic planning.\n2. **Socialization:** Promotes social interaction, bonding, turn-taking, and communication among peers.\n3. **Cultural preservation:** Helps pass down traditions, cultural heritage, and folklore to younger generations.\n4. **Entertainment:** Provides fun, recreation, and healthy use of leisure time.\n5. **Moral values:** Promotes sportsmanship, fair play, honesty, and learning how to win or lose gracefully.\n6. **Focus:** Improves concentration, patience, and attention span.\n7. **Resourcefulness:** Encourages the use of locally available materials (stones, seeds, carved wood) to create play items.",
    
    "q50a": "Here is a list of acceptable steps for making a mat using the coil technique:\n\n1. **Step 1 (Preparation):** Collect, wash, and cut the old fabric into long, even strips.\n2. **Step 2 (Twisting/Braiding):** Twist, plait, or braid the fabric strips together to form a continuous thick rope or cord.\n3. **Step 3 (Coiling):** Start coiling the fabric rope tightly from the center point, gradually spiraling outward on a flat surface to form the base.\n4. **Step 4 (Stitching):** Stitch, sew, or bind the adjacent coils together firmly using a strong needle and thread to secure the mat's shape as you coil.\n5. **Step 5 (Finishing):** Tuck in the final end of the fabric rope and securely stitch the edge to prevent unraveling.",
    
    "q51a": "Here is a list of acceptable steps for preparing a paper stencil for fabric printing:\n\n1. **Step 1 (Design):** Sketch or draw the desired motif/design on a piece of thick paper, manila, or cardboard.\n2. **Step 2 (Planning):** Mark out the positive and negative spaces, ensuring that \"ties\" or \"bridges\" are left in the design to hold the inner parts of the stencil together.\n3. **Step 3 (Setup):** Place the paper flat on a protective cutting mat or wooden board.\n4. **Step 4 (Cutting):** Use a sharp craft knife, scalpel, or cutter to carefully cut out and remove the positive spaces (the areas where ink should pass through onto the fabric).\n5. **Step 5 (Testing):** Test the stencil on a scrap piece of paper to ensure the \"ties\" hold and the design prints correctly.",
    
    "q52a": "Here is a list of acceptable titles for the artwork:\n\n1. \"Sunset Swing\"\n2. \"Evening Play\"\n3. \"Silhouette at Dusk\"\n4. \"The Joy of Swinging\"\n5. \"Golden Hour Play\"\n6. \"Childhood Memories\"\n7. \"Swinging into the Sunset\"\n8. \"Nature and Play\"\n*(Accept any creative and relevant title that captures the essence of a child swinging during a sunset/sunrise)*",
    
    "q52b": "Here is a list of acceptable forms present in the painting:\n\n1. A tree / large tree branch / foliage.\n2. A swing with ropes or chains.\n3. A human figure / a child / a girl sitting on the swing.\n4. The ground / hill profile in the foreground.\n5. The sun / sunset in the background sky.",
    
    "q52c": "Here is a list of acceptable points on the use of colour:\n\n1. **Warm Colours:** Prominent use of warm colors (orange, yellow, red) to depict the sunset/sunrise and evoke a warm, nostalgic mood.\n2. **Cool Colours:** A band of dark violet/blue at the top to represent the darkening evening sky.\n3. **Silhouette / Contrast:** Solid black is used for the foreground forms (tree, swing, child, ground) to create a striking silhouette and extreme contrast against the bright sky.\n4. **Gradation / Wash:** Smooth blending (gradation) of colors in the background from dark blue down to bright yellow to simulate a natural sky gradient.\n5. **Monochromatic foreground:** The foreground uses entirely black to focus the viewer's attention on the shapes and outlines rather than interior details.",
    
    "q52d": "Here is a list of acceptable points on the use of space:\n\n1. **Negative Space:** The vast, colorful sky forms the negative space, giving a sense of openness, freedom, and tranquility.\n2. **Positive Space:** The black silhouette of the tree, swing, and child occupies the positive space on the left and bottom.\n3. **Asymmetrical Balance:** The artwork uses asymmetrical balance; the heavy visual weight of the tree and swing on the left is balanced by the expansive, bright negative space on the right.\n4. **Depth / Overlapping:** The solid black foreground overlapping the gradient background creates a shallow but effective sense of depth, typical of silhouette art.\n5. **Rule of Thirds:** The main subject (the child on the swing) is placed slightly off-center, following compositional rules for a more dynamic and engaging layout."
}

update_question(data["sectionB"], updates)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("c:\\Users\\JOASH\\Desktop\\CBC\\offline-exam-app\\electron\\app\\data\\kjsea-creative-arts-sports-sectionb-2025.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Section B Batch 3 updated successfully.")
