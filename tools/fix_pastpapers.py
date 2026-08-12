import glob
import re

files = glob.glob('src/data/*.js')
imports = []
kpsea_vars = []
kjsea_vars = []

for f in sorted(files):
    if 'pastPapers' in f:
        continue
    basename = f.replace('\\', '/').split('/')[-1]
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    match = re.search(r'export\s+const\s+(\w+)', content)
    if match:
        var_name = match.group(1)
        imports.append(f"import {{ {var_name} }} from './{basename}';")
        if var_name.startswith('kpsea'):
            kpsea_vars.append(var_name)
        elif var_name.startswith('kjsea'):
            kjsea_vars.append(var_name)

out = '\n'.join(imports) + '\n\nexport const PAST_PAPERS = {\n  KPSEA: [\n'
out += ',\n'.join(['    ' + v for v in kpsea_vars])
out += '\n  ],\n  KJSEA: [\n'
out += ',\n'.join(['    ' + v for v in kjsea_vars])
out += '\n  ]\n};\n'

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as fp:
    fp.write(out)

print(f"Successfully updated pastPapers.js with {len(kpsea_vars)} KPSEA papers and {len(kjsea_vars)} KJSEA papers.")
