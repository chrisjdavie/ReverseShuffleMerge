'''
Solving the Reverse Shuffle Merge puzzle from hackerrank

https://www.hackerrank.com/challenges/reverse-shuffle-merge

---------------------

Problem Statement

Given a string, S, we define some operations on the string as follows:

a. reverse(S) denotes the string obtained by reversing string S. E.g.: reverse("abc") = "cba"

b. shuffle(S) denotes any string that's a permutation of string S. E.g.: shuffle("god") produces one of ['god', 'gdo', 'ogd', 'odg', 'dgo', 'dog']

c. merge(S1,S2) denotes any string that's obtained by interspersing the two strings S1 & S2, maintaining the order of characters in both. 
E.g.: S1 = "abc" & S2 = "def", one possible result of merge(S1,S2) could be "abcdef", another could be "abdecf", another could be "adbecf" and so on.

Given a string S such that S is produced from merge(reverse(A), shuffle(A)), for some string A, can you find the lexicographically smallest A?

Input Format

A single line containing the string S.

Constraints: 
S contains only lower-case English letters.
The length of string S is less than or equal to 10000.

Output Format

A string which is the lexicographically smallest valid A.

---------------------

Hmmm. I wonder if there's a non-brute force way to tackle this.

This takes N! time. Too long, broke the test, must be a non-brute
force approach.

Created on 1 Jan 2016

@author: chris
'''
from collections import Counter
from itertools import permutations

mixedString = raw_input().strip()

# find characters in original string
elements = Counter(mixedString)

originalCharsCounter = Counter()
for char in elements:
    originalCharsCounter[char] = elements[char]/2

testOriginal = list(originalCharsCounter.elements())


# try with the most lexicographically ordered test

testOriginal.sort()
possPerms = list(permutations(testOriginal))
permsTested = []

for perm in possPerms:
    if perm not in permsTested:
        permsTested.append(perm)
        
        i = 0
        testOriginalShuff = []
        for charMix in mixedString[::-1]:
            if i < len(testOriginal) and charMix == perm[i]:
                i += 1
            else:
                testOriginalShuff.append(charMix)
        
        if len(testOriginalShuff) == len(mixedString)/2:
            break

print ''.join(perm)


# if it's long enough, it's a permutation of the original

# print testStringMerge

