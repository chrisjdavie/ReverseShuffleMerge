'''
First go ran over the time limit, which isn't surprising as I brute
forced with permutations. Looking at this, there is a more elegant
solution, but it's not clear immediately how. But it's there.

Okay, this approach worked, but it's not the clearest what's going on.
Esentially, there are the merged counts and the reverse counts,
and I first deplete the merged counts and then the reverse counts,
always looking for the next best (and removing that from the reverse
counts when found.)

A better solution (in terms of code simplicity, probably takes much
longer in alg terms), that I can't be bothered to implement right now,
is finding the best characters, and then filling those up, adding in
any that go over the limit. There's also a trick, keeping track of the
previous minimum value, and if you hit a crappy one, substitute that
in, then reversing to that point (repopulating the arrays appropriately)
and starting again.

I'm not 100% I've got the reversing right in my alg, I think there 
might be some cases it doesn't work, but I'm not sure, I might be
okay. 

Created on 1 Jan 2016

@author: chris
'''
import copy
from collections import Counter


def smallercharBest(testString, highChar, charCountsRemain):
    
    # finds the smallest character in a test string (with some
    # constraints)
    
    minChar = 'zz'
    for testChar in testString:
        if testChar < minChar and charCountsRemain[testChar] > 0 \
                and testChar < highChar:
            minChar = testChar
    if minChar == 'zz':
        return minChar, -1
    else:
        return minChar, testString.index(minChar)


def updateBestChar(charBest, reversedCharsCounter, bestUnique):
    
    # Checks if all of the best character have been found,
    # and then sets the next best as the character to look for
    
    if reversedCharsCounter[charBest] == 0:
        if len(bestUnique) == 0:
            charBest = 'zz' 
        else:
            charBest = bestUnique.pop(0)
    return charBest    

mixedString = raw_input().strip()

# find characters in original string
elements = Counter(mixedString)

reversedCharsCounter = Counter()
for char in elements:
    reversedCharsCounter[char] = elements[char]/2

uniqueChars = set(reversedCharsCounter.elements())


# try with the most lexicographically ordered test

bestUnique = sorted(list(uniqueChars))

op = []
mergedCharsCounter = copy.deepcopy(reversedCharsCounter)
remainString = list(mixedString[::-1])


charBest = bestUnique.pop(0)

indsPop = []
prevCharInd = 0

for i, charRemain in enumerate(remainString):
    if charRemain == charBest:
        # found the best character, add to output
        op.append(charRemain)
        reversedCharsCounter[charRemain] -= 1
        prevCharInd = i
    elif mergedCharsCounter[charRemain] > 0:
        # skips this character, assigns it to the merged characters
        mergedCharsCounter[charRemain] -= 1
    elif reversedCharsCounter[charRemain] > 0:
        # if there are characters of charRemain to be found in the 
        # reversed character, seek lexiographically smaller characters
        # between this and the previous character.
        #
        # then append this character to the output.
        resetInd = i
        if ord(charRemain) - ord(charBest) > 1:
            
            smallerInd = 0
            while smallerInd > -1:
                smallChar, smallerInd = smallercharBest(remainString[prevCharInd+1:i], 
                                                        charRemain, 
                                                        reversedCharsCounter)
                if smallerInd > -1:
                    op.append(smallChar)
                    reversedCharsCounter[smallChar] -= 1
                    prevCharInd += 1 + smallerInd
                    mergedCharsCounter[smallChar]  += 1
            
            try:
                resetInd = prevCharInd + 1 + remainString[prevCharInd+1:i].index(charRemain)
                    
            except(ValueError):
                pass
            
        op.append(charRemain)
        reversedCharsCounter[charRemain] -= 1
        prevCharInd = resetInd
    
    charBest = updateBestChar(charBest, reversedCharsCounter, bestUnique)
    if charBest == 'zz':
        break
    
print "".join(op)
