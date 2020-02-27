from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

s1 = ["python","pythoner","pythonner","pythoned","pythonly"]
for w in s1:
    print(ps.stem(w))

new_s = "It is very important and importantly importantest to be pythonly while you are pythonning. All pythoned program are cool pythonner"

words = word_tokenize(new_s)

for w in words:
    print(ps.stem(w))
