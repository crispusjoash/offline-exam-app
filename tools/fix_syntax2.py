with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

output = []
in_string = False
escape_next = False

for char in text:
    if escape_next:
        # If previous was backslash, this character is escaped. We just append it.
        # But what if the character is newline? In JS, \ followed by newline is a line continuation.
        # We probably didn't create that.
        output.append(char)
        escape_next = False
    elif char == '\\':
        output.append(char)
        escape_next = True
    elif char == '"':
        in_string = not in_string
        output.append(char)
    elif char == '\n':
        if in_string:
            # We are inside a string and found an actual newline!
            # Replace it with literal '\n'
            output.append('\\')
            output.append('n')
        else:
            output.append(char)
    else:
        output.append(char)

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write("".join(output))

print('Syntax fixed with char-by-char string parser!')
