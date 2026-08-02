import re

def clean_latex_raw(text):
    # Remove double dollar block markers
    text = text.replace('$$', '')
    # Remove single dollar inline markers
    text = re.compile(r'\$([^\$]+)\$').sub(r'\1', text)
    
    # Replace LaTeX commands
    text = re.compile(r'\\\\text\{([^}]+)\}').sub(r'\1', text)
    
    text = text.replace('\\\\times', '×')
    text = text.replace('\\\\div', '÷')
    text = text.replace('\\\\implies', '➔')
    text = text.replace('^2', '²')
    text = text.replace('\\\\%', '%')
    
    def frac_repl(m):
        top = m.group(1)
        bot = m.group(2)
        if len(top) > 2 or ' ' in top:
            top = f"({top})"
        if len(bot) > 2 or ' ' in bot:
            bot = f"({bot})"
        
        res = f"{top}/{bot}"
        if res == '1/2': return '½'
        if res == '1/4': return '¼'
        if res == '3/4': return '¾'
        return res
    
    text = re.compile(r'\\\\frac\{([^}]+)\}\{([^}]+)\}').sub(frac_repl, text)
    text = re.compile(r'\\\\sqrt\{([^}]+)\}').sub(r'√\1', text)
    
    # Cleanup any lingering \\
    # but be careful not to remove \\n!
    # actually, only remove loose backslashes if they are followed by space
    # it's better to just leave them if they don't match, or manually fix if needed
    return text

with open('src/data/kpsea-math-2022.js', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(m):
    return m.group(1) + clean_latex_raw(m.group(2)) + m.group(3)

# Update explanations only
new_content = re.sub(r'("explanation":\s*")(.*?)(")', replacer, content, flags=re.DOTALL)

with open('src/data/kpsea-math-2022.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Formatting cleaned successfully.")
