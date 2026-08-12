import json
import re

file_path = 'src/data/kpsea-sst-parta-2024.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON part
match = re.search(r'export const \w+ = (\{.*\});?', content, re.DOTALL)
if not match:
    print("Could not parse file")
    exit(1)
    
data = json.loads(match.group(1))

# We need to make sure sharedContexts is updated properly
if "sharedContexts" not in data:
    data["sharedContexts"] = {}

data["sharedContexts"]["ctx-sst-2024-q1"] = {
    "type": "image",
    "text": "A Grade 6 learner mounted and framed the following picture in readiness for an exhibition.",
    "imagePath": "/assets/images/sst-2024-q1.png",
    "title": "Question 1 Image"
}

data["sharedContexts"]["ctx-sst-2024-q3"] = {
    "type": "image",
    "text": "The following image shows a passing skill in netball.",
    "imagePath": "/assets/images/sst-2024-q3.png",
    "title": "Question 3 Image"
}

data["sharedContexts"]["ctx-sst-2024-q10"] = {
    "type": "image",
    "imagePath": "/assets/images/sst-2024-q10.png",
    "title": "Question 10 Image"
}

data["sharedContexts"]["ctx-sst-2024-q11"] = {
    "type": "image",
    "imagePath": "/assets/images/sst-2024-q11.svg",
    "title": "Question 11 Image"
}

data["sharedContexts"]["ctx-sst-2024-q30"] = {
    "type": "image",
    "text": "The following picture shows a learner playing the ball in a game of volleyball.",
    "imagePath": "/assets/images/sst-2024-q30.png",
    "title": "Question 30 Image"
}

data["sharedContexts"]["ctx-sst-2024-q31-32"] = {
    "type": "image",
    "text": "Study the following map of Eastern Africa and use it to answer questions 31 and 32.",
    "imagePath": "/assets/images/sst-2024-q31-32.png",
    "title": "Question 31-32 Image"
}

# Update questions
for q in data["sectionA"]:
    num = q["questionNumber"]
    
    if num == 1:
        q["contextRef"] = "ctx-sst-2024-q1"
        q["questionText"] = "Why was the picture mounted and framed?"
        if "questionSuffix" in q: del q["questionSuffix"]
        if "imagePath" in q: del q["imagePath"]
        if "imageUrl" in q: del q["imageUrl"]
        
    elif num == 3:
        q["contextRef"] = "ctx-sst-2024-q3"
        q["questionText"] = "What type of pass does the image represent?"
        if "questionSuffix" in q: del q["questionSuffix"]
        if "imagePath" in q: del q["imagePath"]
        if "imageUrl" in q: del q["imageUrl"]
        
    elif num == 10:
        q["contextRef"] = "ctx-sst-2024-q10"
        q["questionText"] = "Which basketry technique is presented in the following picture?"
        if "questionSuffix" in q: del q["questionSuffix"]
        if "imagePath" in q: del q["imagePath"]
        if "imageUrl" in q: del q["imageUrl"]
        
    elif num == 11:
        q["contextRef"] = "ctx-sst-2024-q11"
        q["questionText"] = "Which of the following types of songs is not correctly matched with its function?"
        if "questionSuffix" in q: del q["questionSuffix"]
        if "imagePath" in q: del q["imagePath"]
        if "imageUrl" in q: del q["imageUrl"]
        
    elif num == 30:
        q["contextRef"] = "ctx-sst-2024-q30"
        q["questionText"] = "The skill that the learner is using to play the ball is known as"
        if "questionSuffix" in q: del q["questionSuffix"]
        if "imagePath" in q: del q["imagePath"]
        if "imageUrl" in q: del q["imageUrl"]
        
    elif num == 31:
        q["contextRef"] = "ctx-sst-2024-q31-32"
        q["questionText"] = "The climatic region marked F is"
        if "questionSuffix" in q: del q["questionSuffix"]
        if "imagePath" in q: del q["imagePath"]
        if "imageUrl" in q: del q["imageUrl"]
        
    elif num == 32:
        q["contextRef"] = "ctx-sst-2024-q31-32"
        q["questionText"] = "Which language group migrated into Eastern Africa using the route marked G?"
        if "questionSuffix" in q: del q["questionSuffix"]
        if "imagePath" in q: del q["imagePath"]
        if "imageUrl" in q: del q["imageUrl"]

# Write it back
new_content = "export const kpseaSstParta2024 = " + json.dumps(data, indent=2) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully fixed SST 2024 images.")
