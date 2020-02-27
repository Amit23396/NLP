from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

#pos = 'n' - default
#pos = 'a' - adjective

print(lemmatizer.lemmatize("better", pos="a"))
