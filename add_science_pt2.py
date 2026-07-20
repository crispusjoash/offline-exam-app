import json
import re

with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

science_pt2 = """      ,
      {
        questionNumber: 14,
        questionText: "A learner used a ladder as a simple machine to reach and fix a bulb in a house. The ladder is a simple machine because it makes it easier to",
        options: [
          { text: "move loads in circles", isCorrect: false },
          { text: "move loads horizontally", isCorrect: false },
          { text: "overcome loads in the opposite direction of force", isCorrect: false },
          { text: "move loads through heights.", isCorrect: true }
        ],
        explanation: "A ladder acts as an inclined plane, which is a simple machine that makes it easier to move loads (like a person) upwards through heights. It does not move loads horizontally, in circles, or in opposite directions (which describes a pulley)."
      },
      {
        questionNumber: 15,
        questionText: "Learners observed a cloud which appeared long, curled, feather-like and light. The cloud observed is most likely to be",
        options: [
          { text: "cirrus", isCorrect: true },
          { text: "nimbus", isCorrect: false },
          { text: "stratus", isCorrect: false },
          { text: "cumulus.", isCorrect: false }
        ],
        explanation: "Cirrus clouds are high-altitude clouds that are characterized by their thin, wispy, curled, and feather-like appearance. Nimbus clouds are dark rain clouds, stratus clouds are flat featureless layers, and cumulus clouds are large, puffy, cotton-like clouds."
      },
      {
        questionNumber: 16,
        questionText: "The following photograph shows a farmer constructing a structure for controlling soil erosion. Study it and answer questions 16 and 17.\\n![Farmer structure](/assets/q16_farmer.png)\\nIdentify the structure in the picture.",
        options: [
          { text: "Gabion.", isCorrect: false },
          { text: "Grass strip.", isCorrect: false },
          { text: "Terrace.", isCorrect: true },
          { text: "Trash line.", isCorrect: false }
        ],
        explanation: "The farmer is constructing a stepped ridge along the contour of a slope, which is a terrace. A gabion is a wire mesh box filled with stones, a grass strip is a planted band of grass, and a trash line is a pile of dry vegetation."
      },
      {
        questionNumber: 17,
        questionText: "How does the structure control soil erosion?",
        options: [
          { text: "Intercepts rain drops.", isCorrect: false },
          { text: "Reduces speed of water.", isCorrect: true },
          { text: "Stores water.", isCorrect: false },
          { text: "Holds the soil back.", isCorrect: false }
        ],
        explanation: "Terraces work primarily by breaking a long slope into a series of shorter, flatter steps. This effectively reduces the speed of surface runoff water, preventing it from washing away the topsoil. While it can also hold soil back, reducing the speed of water is the fundamental mechanism of terracing. Intercepting raindrops is the role of vegetation cover."
      },
      {
        questionNumber: 18,
        questionText: "The picture below shows farm produce labelled 'ORGANIC' on the market.\\n![Organic produce](/assets/q18_organic.png)\\nWhat does the label 'ORGANIC' mean? The farm produce is",
        options: [
          { text: "free from artificial chemicals", isCorrect: true },
          { text: "free from pests and diseases", isCorrect: false },
          { text: "fresh", isCorrect: false },
          { text: "more tasty.", isCorrect: false }
        ],
        explanation: "In agriculture, the term 'organic' refers to produce that has been grown without the use of artificial fertilizers, synthetic pesticides, or other synthetic chemicals. It does not necessarily mean it is free from pests (though farmers use natural methods), nor does it automatically mean it is fresher or tastier than conventionally grown produce."
      },
      {
        questionNumber: 19,
        questionText: "The following photograph shows a method of protecting livestock. Use it to answer questions 19 and 20.\\n![Livestock method](/assets/q19_livestock.png)\\nThe method protects the livestock by",
        options: [
          { text: "preventing entry of the wild animals", isCorrect: true },
          { text: "producing flashing lights at night", isCorrect: false },
          { text: "scaring wild animals away", isCorrect: false },
          { text: "trapping the wild animals.", isCorrect: false }
        ],
        explanation: "The photograph shows a physical fence or boma surrounding the livestock. This physical barrier works by preventing the entry of predators and wild animals. It does not produce flashing lights, actively scare animals (like a scarecrow), or trap them."
      },
      {
        questionNumber: 20,
        questionText: "How can you describe the animals in the photograph? They are",
        options: [
          { text: "carnivorous", isCorrect: false },
          { text: "decomposers", isCorrect: false },
          { text: "omnivorous", isCorrect: false },
          { text: "herbivorous.", isCorrect: true }
        ],
        explanation: "The animals in the photograph are goats and sheep. Goats and sheep are ruminants that feed exclusively on plant matter (grass and leaves), which makes them herbivores. Carnivores eat meat, omnivores eat both meat and plants, and decomposers break down dead matter."
      },
      {
        questionNumber: 21,
        questionText: "The following photograph shows a farmer carrying out a practice after germination of maize. Study it and answer questions 21 to 23.\\n![Farmer practice](/assets/q21_farmer.png)\\nIdentify the practice.",
        options: [
          { text: "Gapping.", isCorrect: false },
          { text: "Pruning.", isCorrect: false },
          { text: "Thinning.", isCorrect: true },
          { text: "Training.", isCorrect: false }
        ],
        explanation: "The farmer is removing excess seedlings from the soil to reduce competition for nutrients, light, and water among the remaining plants. This practice is known as thinning. Gapping is replacing dead seeds, pruning is cutting off branches, and training is supporting a plant to grow in a certain direction."
      },
      {
        questionNumber: 22,
        questionText: "Which one of the following wild animals most likely interferes with germination of seeds?",
        options: [
          { text: "Mole.", isCorrect: false },
          { text: "Monkey.", isCorrect: false },
          { text: "Squirrel.", isCorrect: true },
          { text: "Weaver bird.", isCorrect: false }
        ],
        explanation: "Squirrels are known to dig up and eat planted seeds like maize before or during germination, directly interfering with the process. Moles primarily damage roots, monkeys eat mature fruits or cobs, and weaver birds are notorious pests for mature cereal grains (like wheat or sorghum heads) rather than germinating seeds."
      },
      {
        questionNumber: 23,
        questionText: "From the photograph, name the other caring practice the farmer carried out on the maize.",
        options: [
          { text: "Harvesting.", isCorrect: false },
          { text: "Pruning.", isCorrect: false },
          { text: "Training.", isCorrect: false },
          { text: "Weed control.", isCorrect: true }
        ],
        explanation: "In the photograph, while the farmer is uprooting excess maize plants (thinning), they are also simultaneously clearing the surrounding soil of unwanted plants. This secondary caring practice is weed control. The maize plants are far too young for harvesting or pruning, and maize does not require training."
      },
      {
        questionNumber: 24,
        questionText: "Which one of the following is an indigenous vegetable crop?",
        options: [
          { text: "Cabbage.", isCorrect: false },
          { text: "Kales.", isCorrect: false },
          { text: "Pigweed.", isCorrect: true },
          { text: "Spinach.", isCorrect: false }
        ],
        explanation: "Pigweed (Amaranthus, commonly known as Terere) is an indigenous African leafy vegetable. Cabbage, kales (sukuma wiki), and spinach are all exotic vegetables that were introduced from other parts of the world."
      },
      {
        questionNumber: 25,
        questionText: "Which one of the following pairs of crops consists of indigenous root crops?",
        options: [
          { text: "Arrowroots and carrots.", isCorrect: false },
          { text: "Beetroot and cassava.", isCorrect: false },
          { text: "Carrots and yams.", isCorrect: false },
          { text: "Cassava and arrowroots.", isCorrect: true }
        ],
        explanation: "Cassava and arrowroots (nduma) are considered traditional or indigenous root and tuber crops heavily cultivated in local farming. Carrots and beetroots are exotic root crops that were introduced from temperate regions."
      }
"""

# Insert right before the closing bracket of the entire file where we left off
match = re.search(r"(\s*)\],\n\s*KJSEA:\s*\[\]", content)
if match:
    insert_pos = match.start()
    new_content = content[:insert_pos] + science_pt2 + content[insert_pos:]
    with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Q14-Q25 Added!")
else:
    print("Could not find insertion point for pt2!")
