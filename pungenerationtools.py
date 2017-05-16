import word2vechelper
import nltk
from nltk.corpus import wordnet as wn

word2vecmodel = word2vechelper.LoadModel(MakeNew=False)


# creates of a list of tuples looking like the one below
# (string similar to word passed in, it's connection to the original word)
# TODO make sure that the input word is not in the list of similar words
def findSimilarWords(word, unfilteredPosTag, verbose=False):
    subjectTagsNouns = ['NN']
    subjectTagsVerbs = ['VB', 'VBP', 'VBD']
    pos = ""

    if unfilteredPosTag in subjectTagsNouns:
        pos = "noun"
    elif unfilteredPosTag in subjectTagsVerbs:
        pos = "verb"
    else:
        pos = "unknown"

    return findSynsForWord(word, pos, verbose)


# break the context up into words and generate a list of lists of the phonetic
# sounds of each word tokenize by word, remove punctuation, and make a list
# of the sounds for each word
def generatePhoneticsOfContext(context, verbose=False):
    ret = [generatePhoneticsOfWord(word.lower(), verbose) for word in nltk.word_tokenize(context) if word.isalpha()]

    return ret


# TODO! Use a better phonetics thing. This doesn't have phonetics for things like "cat"
# takes in a word and returns a list of the phonetic sounds that make up the word
# if it can't find the sounds, right now we just ignore it
def generatePhoneticsOfWord(word, verbose=False):
    timitdict = nltk.corpus.timit.transcription_dict()
    if word in timitdict:
        if verbose:
            print("Phonetics for word \"{0}\" found".format(word))

        return timitdict[word]
    else:
        if verbose:
            print("Could not find phonetics for \"{0}\"".format(word))

        return []


#  grab all of the nouns, verbs, and adjectives in the context string and
#  return them as a list of tuples looking likek (string, POS tag)
def grabSubject(context, verbose=False):
    text = nltk.word_tokenize(context)

    filtered_words = [word for word in text if word not in nltk.corpus.stopwords.words('english')]
    posTagged = nltk.pos_tag(filtered_words)

    if verbose:
        print(posTagged)

    ret = [(word, tag) for (word, tag) in posTagged if tagIsSubject(tag)]

    return ret


def tagIsSubject(tag):
    subjectTags = ['NN', 'VB', 'VBP', 'VBD']

    if tag in subjectTags:
        return True
    else:
        return False


def printSeperator():
    print()
    print("=" * 50)
    print()


# finds the synonyms, antonyms, hypernyms, and hyponyms for the input word,
# the words found are based on the POS
def findSynsForWord(word, pos, verbose=False):
    if pos == "noun":
        syns = wn.synsets(word, wn.NOUN)
    else:
        syns = wn.synsets(word, wn.VERB)

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

    if verbose:
        printSeperator()
        print("Synonyms for " + word)
        print(set(synonyms))
        printSeperator()
        print("Antonyms for " + word)
        print(set(antonyms))
        printSeperator()
        print("Hyponyms for " + word)
        print(set(hyponyms))
        printSeperator()
        print("Hypernyms for " + word)
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

    return words.items()
