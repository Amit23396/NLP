import nltk
from nltk.corpus import treebank


text="Hello I am here to stand to improve your qualities"

tok = nltk.word_tokenize(text)
print("text to token ",tok)

tagged = nltk.pos_tag(tok)
print("Tagged text ",tagged[0:])

entities = nltk.chunk.ne_chunk(tagged)
print("Chunks are ", entities)
