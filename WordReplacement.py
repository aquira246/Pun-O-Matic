addCost = 1


def findOptimalWordLocation(phoneticsByWord, replacementWord):
    breaks = []
    phoneticStream = []

    current = 0
    for phone in phoneticsByWord:
        current += len(phone) + 1  # to cover adding "_"
        breaks.append(current)
        phoneticStream.extend(phone + "_")
    pass


def function(phoneticStream, replacementWord):
    repWordLen = len(replacementWord)
    tableLength = repWordLen + len(phoneticStream) + 1
    table = [0 for i in range(tableLength)]
    endLocs = [0 for i in range(tableLength)]
    endLocs[-1] = tableLength

    for i in range(repWordLen):
        table[tableLength - i - 1] = table[i] = (repWordLen - i) * addCost
        endLocs[i] = i

    print("Table looks like this:")
    print(table)

    best = 0
    for i in range(1, tableLength - 1):
        (costToAdd, placeStopped) = calculatePlaceCost(i, phoneticStream, replacementWord)
        table[i] += costToAdd
        endLocs[i] = placeStopped
        if table[i] < table[best]:
            best = i

    return (best, table[best])


# TODO make a better replace cost so that if you replace phonetics that sound
# similar, it is less than replacing phonetics that sound different
def calculatePlaceCost(index, phoneticStream, replacementWord):
    cost = 0
    costStoppingAtSpaces = -1
    placeStopped = -1
    for x in range(len(replacementWord)):
        # the table already calculates the cost of hitting the end
        if len(phoneticStream) >= index + x:
            if cost <= costStoppingAtSpaces:
                return (cost, index + len(replacementWord))
            else:
                return (costStoppingAtSpaces, placeStopped)

        # if we hit a space the replacement cost is 0, also we can choose to
        # keep going or just add the rest of the word to the end
        if phoneticStream[index + x] == "_":
            cost += 0
            curStopAtSpaces = cost + (len(replacementWord) - x) * addCost
            if costStoppingAtSpaces == -1 or costStoppingAtSpaces > curStopAtSpaces:
                costStoppingAtSpaces = curStopAtSpaces
                placeStopped = index + x

        # currently calculate replacement cost by seing if the phonetics are
        # the same. If they are different, the replacement cost is 1
        elif phoneticStream[index + x] != replacementWord[x]:
            cost += 1

    if cost <= costStoppingAtSpaces:
        return (cost, index + len(replacementWord))
    else:
        return (costStoppingAtSpaces, placeStopped)


if __name__ == '__main__':
    pass
