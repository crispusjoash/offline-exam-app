import json

filepath = r'C:\Users\JOASH\.gemini\antigravity-ide\brain\9d39c76d-2c71-4969-8f52-1885f6f7bfde\.system_generated\logs\transcript_full.jsonl'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines[-100:]:
    data = json.loads(line)
    if data.get('type') == 'USER_INPUT':
        print(f"Timestamp: {data.get('created_at')}")
        content = data.get('content', '')
        if "This is the image for question 7" in content:
            print("FOUND Q7 PROMPT!")
            
        # extract any artifacts mentioned
        import re
        artifacts = re.findall(r'\[ARTIFACT:\s*(media_[0-9_a-zA-Z-]+)\]', content)
        if artifacts:
            print("Artifacts in this prompt:", artifacts)

