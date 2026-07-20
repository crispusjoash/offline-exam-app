with open('src/data/pastPapers.js', 'r', encoding='utf-8') as f:
    content = f.read()

old = "In the passage, the writer specifically mentions that the father wrote the 'prices' on the list, which helped Hassan know the total cost and expect exactly seventy-five shillings in balance.\\nWhile people often use shopping lists to avoid forgetting items, the emphasis here on prices and calculating the expected balance points to ensuring Hassan gets the correct change from the busy shopkeeper!"

new = "In the passage, the writer specifically mentions that the father wrote the 'prices' on the list, which helped Hassan know the total cost and expect exactly seventy-five shillings in balance.\\nWhile Option A (didn't want him to forget) and Option B (didn't want him to delay) sound like logical real-world reasons to write a list, reading comprehension questions require you to find the reason supported by the text. The text specifically highlights that the father calculated the prices so Hassan would know his exact balance."

content = content.replace(old, new)

with open('src/data/pastPapers.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Q10 fixed.')
