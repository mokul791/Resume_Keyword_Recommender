keywordFreq = []

for word in open('keywordDict.tex', 'r'):
	words = word.split(",")
	for w in words:
		keywordFreq.append(words.count(w))
		pairs = list(zip(words, keywordFreq))
	print(pairs)

print(pairs[0][0])