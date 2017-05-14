import word2vechelper
import nltk
import string
from nltk.corpus import wordnet as wn

word2vecmodel = word2vechelper.LoadModel(MakeNew=False)


def findSimilarWords(word, verbose=False):
    # TODO add in synonyms
    if word2vecmodel.__contains__(word):
        most_similar_words = word2vecmodel.most_similar(positive=[word], topn=10)
        return most_similar_words
    else:
        if verbose:
            print("The word \"{0}\" is not in the word2vec vocab".format(word))
        return []


def generatePhoneticsOfContext(context, verbose=False):
    # break the context up into words and generate a list of lists of the phonetic sounds of each word
    # tokenize by word, remove punctuation, and make a list of the sounds for each word
    ret = [generatePhoneticsOfWord(word.lower(), verbose) for word in nltk.word_tokenize(context) if word.isalpha()]

    return ret


def generatePhoneticsOfWord(word, verbose=False):
    # TODO! Use a better phonetics thing. This doesn't have phonetics for things like "cat"
    # takes in a word and returns a list of the phonetic sounds that make up the word
    # if it can't find the sounds, right now we just ignore it
    timitdict = nltk.corpus.timit.transcription_dict()
    if word in timitdict:
        if verbose:
            print("Phonetics for word \"{0}\" found".format(word))

        return timitdict[word]
    else:
        if verbose:
            print("Could not find phonetics for \"{0}\"".format(word))

        return []


def grabSubject(context, verbose=False):
    #  grab all of the nouns, verbs, and adjectives in the context string and return them as a list of strings
    text = nltk.word_tokenize(context)

    filtered_words = [word for word in text if word not in nltk.corpus.stopwords.words('english')]
    posTagged = nltk.pos_tag(filtered_words)

    if verbose:
        print(posTagged)

    ret = [word for (word, tag) in posTagged if tagIsSubject(tag)]

    return ret


def tagIsSubject(tag):
    subjectTags = ['NN', 'VB', 'VBP', 'VBD']

    if tag in subjectTags:
        return True
    else:
        return False
