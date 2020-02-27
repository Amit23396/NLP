from nltk.corpus import wordnet

#synset
syns = wordnet.synsets("program")

#word
print(syns[0].lemmas()[0].name())

#defination
print(syns[0].definition())

#examples
print(syns[0].examples())



synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))





w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))


w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))


w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("Dog.n.01")
print(w1.wup_similarity(w2))
