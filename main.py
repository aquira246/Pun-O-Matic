import pungenerationtools as pgt


def main():
    input = ["The sandal flew", "I like pie"]

    for context in input:
        print()
        print("=" * 30)
        print()
        print("For context: {0}".format(context))

        # grab the phonetics of the current input
        contextPhonetics = pgt.generatePhoneticsOfContext(context, verbose=True)

        print("phonetics: {0}".format(contextPhonetics))

        # grab what the subjects are in the current input
        subjects = pgt.grabSubject(context, verbose=True)

        print("subjects: {0}".format(subjects))

        # find words that are similar to the subjects within a certain cosine similarity
        replacements = []
        for sub in subjects:
            repsForSub = pgt.findSimilarWords(sub, True)
            replacements += repsForSub
            print("    Replacements for \"{0}\": {1}".format(sub, repsForSub))

        # fine the phonetics of each of the subject words
        subjectPhonetics = []
        for (word, cos) in replacements:
            subjectPhonetics.append(pgt.generatePhoneticsOfWord(word))

        # Identify any matching series of sounds between the replacements and the original input and make the substitution
        #TODO


if __name__ == '__main__':
    main()
