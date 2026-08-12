import os
scripts = [
    'update_kiswahili_complete.py',
    'update_english_batch1.py',
    'update_english_batch2.py',
    'update_english_batch3.py',
    'update_english_batch4.py',
    'update_english_batch5.py',
    'update_english_batch6.py'
]

for s in scripts:
    print(f"Running {s}...")
    os.system(f"python {s}")
print("Done running all scripts!")
