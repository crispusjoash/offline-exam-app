import re
exp='always start with *"May I..."* rather than stating desires (*"I want to..."*) or commands (*"I will..."*).'
exp = re.sub(r'\(\*\"(.*?)\"\*\)', r'("\1")', exp)
exp = re.sub(r'\*\"(.*?)\"\*', r'"\1"', exp)
print(exp)
