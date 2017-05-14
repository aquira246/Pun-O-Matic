import nltk
from nltk.corpus import wordnet as wn


def printSeperator():
    print()
    print("=" * 50)
    print()


def findSynsForWord(word, pos):
    if pos == "noun":
        syns = wn.synsets(word, wn.NOUN)
    else:
        syns = wn.synsets(word, wn.VERB)

    print(syns)

    synonyms = []
    antonyms = []
    hyponyms = []
    hypernyms = []

    for syn in syns:
        for l in syn.lemmas():
            synonyms.append(l.name().replace("_", " "))
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name().replace("_", " "))
        for hyper in syn.hypernyms():
            for lem in hyper.lemmas():
                hypernyms.append(lem.name().replace("_", " "))
        for hypo in syn.hyponyms():
            for lem in hypo.lemmas():
                hyponyms.append(lem.name().replace("_", " "))

    printSeperator()
    print(set(synonyms))
    printSeperator()
    print(set(antonyms))
    printSeperator()
    print(set(hyponyms))
    printSeperator()
    print(set(hypernyms))
    printSeperator()

    words = {}
    for w in synonyms:
        for tok in nltk.word_tokenize(w):
            words[tok] = "synonym"

    for w in antonyms:
        for tok in nltk.word_tokenize(w):
            words[tok] = "antonyms"

    for w in hypernyms:
        for tok in nltk.word_tokenize(w):
            words[tok] = "hypernyms"

    for w in hyponyms:
        for tok in nltk.word_tokenize(w):
            words[tok] = "hyponyms"

    print(words)


"""MAIN"""
if __name__ == '__main__':
    findSynsForWord("sandal", "noun")
