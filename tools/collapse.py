with open('src/data/pastPapers.js', 'rb') as f:
    raw = f.read()

content = raw.decode('utf-8')

MARKER = 'explanation: "'

result = []
i = 0
n = len(content)
while i < n:
    if content[i:i+len(MARKER)] == MARKER:
        result.append(MARKER)
        i += len(MARKER)
        # consume until closing unescaped double-quote
        while i < n:
            ch = content[i]
            if ch == '\\':
                result.append(ch)
                i += 1
                if i < n:
                    result.append(content[i])
                    i += 1
            elif ch == '"':
                result.append('"')
                i += 1
                break
            elif ch == '\r':
                i += 1  # skip carriage return
            elif ch == '\n':
                result.append('\\n')  # encode newline as \n escape
                i += 1
            else:
                result.append(ch)
                i += 1
    else:
        result.append(content[i])
        i += 1

fixed = ''.join(result)

with open('src/data/pastPapers.js', 'w', encoding='utf-8', newline='') as f:
    f.write(fixed)

# verify
with open('src/data/pastPapers.js', 'rb') as f:
    chunk = f.read(5000)
idx = chunk.find(b'explanation')
print(repr(chunk[idx:idx+150]))
print('Collapse complete.')
