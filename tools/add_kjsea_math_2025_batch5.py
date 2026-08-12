import json

new_questions = [
    {
      "id": "q39",
      "questionNumber": 39,
      "questionText": "The marks scored by 20 learners in a test were recorded as 19, 17, 19, 15, 17, 19, 22, 17, 17, 19, 18, 33, 17, 29, 18, 15, 19, 18, 22, and 19.\n(a) Prepare a frequency distribution table for the data.\n(b) Determine the:\n(i) mean mark;\n(ii) median mark.",
      "maxScore": 5,
      "modelAnswer": "(a) Frequency distribution table:\nMark (x) | Tally | Frequency (f)\n15       | ||    | 2\n17       | ////  | 5\n18       | ///   | 3\n19       | //// /| 6\n22       | //    | 2\n29       | /     | 1\n33       | /     | 1\nTotal    |       | \u03a3f = 20\n\n(b)(i) Mean mark:\nSum of all marks (\u03a3fx) = (15\u00d72) + (17\u00d75) + (18\u00d73) + (19\u00d76) + (22\u00d72) + (29\u00d71) + (33\u00d71)\n\u03a3fx = 30 + 85 + 54 + 114 + 44 + 29 + 33 = 389\nMean = \u03a3fx / \u03a3f = 389 / 20 = 19.45.\n\n(b)(ii) Median mark:\nThere are 20 data points (an even number), so the median is the average of the 10th and 11th values when arranged in order.\nUsing the frequency table, cumulative frequencies are:\nUp to 15: 2\nUp to 17: 2+5 = 7\nUp to 18: 7+3 = 10 (The 10th value is 18)\nUp to 19: 10+6 = 16 (The 11th value is 19)\nMedian = (18 + 19) / 2 = 18.5.",
      "rubric": "Award 5 marks:\n(a) 2 marks for a completely correct frequency distribution table (1 mark if there are minor tally/frequency errors).\n(b)(i) 1 mark for sum (\u03a3fx = 389) or method, 1 mark for correct mean (19.45).\n(b)(ii) 1 mark for correct median (18.5).",
      "questionType": "structured"
    },
    {
      "id": "q40",
      "questionNumber": 40,
      "questionText": "Rebecca tossed a coin and a die at the same time.\n(a) Write down the probability space to show the possible outcomes.\n(b) Determine the probability that Rebecca obtained a head on the coin and a 4 on the die.",
      "maxScore": 3,
      "modelAnswer": "(a) A coin has outcomes Head (H) and Tail (T). A die has outcomes 1, 2, 3, 4, 5, 6.\nThe probability space (sample space S) can be listed or drawn as a table/tree diagram:\nS = {(H,1), (H,2), (H,3), (H,4), (H,5), (H,6), (T,1), (T,2), (T,3), (T,4), (T,5), (T,6)}\nTotal possible outcomes = 12.\n\n(b) The probability of obtaining a Head and a 4:\nThe favorable outcome is just one specific pair: (H, 4).\nProbability = (Number of favorable outcomes) / (Total possible outcomes)\nP(H and 4) = 1 / 12.\n(Alternatively, using independent events: P(H) \u00d7 P(4) = 1/2 \u00d7 1/6 = 1/12).",
      "rubric": "Award 3 marks:\n(a) 2 marks for a fully correct sample space (list, table, or tree diagram showing all 12 combinations).\n(b) 1 mark for the correct probability (1/12).",
      "questionType": "structured"
    }
]

file_path = 'src/data/kjsea-math-2025.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of sectionB array (the last bracket before the closing brace)
insert_pos = content.rfind(']')

# Generate JSON for the new questions
new_json = json.dumps(new_questions, indent=2)
# Remove the outer brackets of the JSON list to inject the objects
new_json = new_json[new_json.find('{'):new_json.rfind('}')+1]

# Inject the new objects
prefix = content[:insert_pos].strip()
suffix = content[insert_pos:]

new_content = prefix + ',\n  ' + new_json + '\n' + suffix

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 5 (Q39-Q40) for KJSEA Math 2025 appended!")
