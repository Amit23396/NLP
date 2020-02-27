from nltk.corpus import shakespeare
from nltk.tokenize import sent_tokenize
sample = shakespeare.raw("dream.xml")

tok = sent_tokenize(sample)

print(tok[5:15])
