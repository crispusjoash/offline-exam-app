import re

with open("c:/Users/JOASH/Desktop/CBC/offline-exam-app/src/data/pastPapers.js", "r", encoding="utf-8") as f:
    content = f.read()

# Fix all multi-line explanation strings by joining lines within quotes
# Find explanation: "..." spanning multiple lines and collapse them
def collapse_explanation(match):
    inner = match.group(1)
    # Replace actual CRLF or LF with \n escape sequence
    inner = inner.replace('\r\n', '\\n').replace('\n', '\\n')
    return 'explanation: "' + inner + '"'

# Match explanation: "...multiline..." 
content = re.sub(r'explanation: "((?:[^"\\]|\\.)*)?"', collapse_explanation, content, flags=re.DOTALL)

with open("c:/Users/JOASH/Desktop/CBC/offline-exam-app/src/data/pastPapers.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed multi-line strings successfully.")
