import docx

def getTextWord(wordFileName):

	doc = docx.Document(wordFileName)
	full_text = []

	for para in doc.paragraphs:
		full_text.append(para.text)

	return '\n'.join(full_text)

file = getTextWord('IBM Business Consultant.docx')

print(file)