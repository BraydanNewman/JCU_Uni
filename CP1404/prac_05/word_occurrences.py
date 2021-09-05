from operator import itemgetter

text = input("Text: ").split()

words = {}

for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

max_length = max([len(str(word)) for word in words.keys()])

for i in sorted(words.items()):
    print(f"{i[0]:{max_length}}: {i[1]}")
