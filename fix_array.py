import sys

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    text = f.read()

# We know the exact string that starts the english paper:
eng_start_str = '    },\n    {\n      id: "kpsea-english-2023",'
start_idx = text.find(eng_start_str)

if start_idx == -1:
    print("Could not find start string!")
    sys.exit(1)

# The KJSEA array ends with:
#   ]
# };
# Wait, look at the end of the file.
end_str = '    }\n  ]\n};'
end_idx = text.rfind(end_str)

if end_idx == -1:
    # maybe it's just '  ]\n};'
    end_idx = text.rfind('  ]\n};')
    if end_idx == -1:
        print("Could not find end string!")
        sys.exit(1)

# English paper block goes from start_idx to the end of the last paper.
# Let's extract it.
# We want to extract:
#     {\n      id: "kpsea-english-2023", ...     }
# Notice eng_start_str includes '    },\n' which we also want to extract if we are moving it.
# Let's extract the whole thing.
extracted = text[start_idx:end_idx]

# We should make sure the extracted block has a closing brace.
if extracted.strip().endswith(','):
    extracted = extracted.rstrip(',')

# Now remove it from the end of the file
# We are leaving `  ]\n};` at the end.
new_text = text[:start_idx] + end_str

# Now we need to insert `extracted` into the KPSEA array.
# The KPSEA array ends before `  ],\n  KJSEA: [`
insert_target = '    }\n  ],\n  KJSEA: ['
insert_idx = new_text.find(insert_target)

if insert_idx == -1:
    print("Could not find KPSEA end target!")
    sys.exit(1)

# Insert the extracted block
# We replace `    }\n  ],\n  KJSEA: [`
# with `    },\n` + (the english paper without its leading `    },\n`) + `\n  ],\n  KJSEA: [`
# Wait, `extracted` ALREADY starts with `    },\n`.
# So we can just replace `    }\n  ],\n  KJSEA: [`
# with `extracted` + `\n  ],\n  KJSEA: [`
# But wait, `extracted` starts with `    },\n    {\n`.
# So we actually want to find the LAST paper of KPSEA, which ends with `    }`, and append `,` then our english paper.
# So we can replace `    }\n  ],\n  KJSEA: [`
# with `extracted` + `\n  ],\n  KJSEA: [`  if `extracted` starts with `    },\n`.
# Let's verify `extracted` starts with `    },\n`.
if not extracted.startswith('    },\n'):
    extracted = '    },\n' + extracted.lstrip()

# wait, we need to replace `    }\n  ],\n  KJSEA: [` with `extracted` + `\n  ],\n  KJSEA: [`
final_text = new_text.replace(insert_target, extracted + '\n  ],\n  KJSEA: [')

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(final_text)

print("Successfully moved english paper!")
