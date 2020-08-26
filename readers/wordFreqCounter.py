import nltk
from readers import pdfReader as pdf

file = '../data_files/IBM Business Consultant.pdf'
file_read = pdf.getTextPDF(file)
print(file_read)

# 	
# file = 'IBM Business Consultant.txt'
# for word in file_read:
# 	print(word)
# 
fdist = nltk.FreqDist(pdf.getTextPDF(file))
print("the number of distinct words in the bag: ", fdist.N())
print(fdist[fdist.max()])
print(fdist.most_common())