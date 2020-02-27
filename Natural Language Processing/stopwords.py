from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence = "It is an example shows stop word filteration"

stop_words = set(stopwords.words("english"))

words = word_tokenize(sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)
