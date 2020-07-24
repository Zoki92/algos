"""Write a function that takes an array of words and groups anagrams together
Anagrams are strings made up of exactly the same letters where order does not matter
"""

def groupAnagrams(words):
    group_anagrams = []
    taken = []
    for idx, word in enumerate(words):
        j = idx + 1
        anagrams = [word]
        while j <= len(words) - 1:
            if checkAnagram(word, words[j]):
                taken.append(j)
                anagrams.append(words[j])
            j += 1
        if idx not in taken:
            group_anagrams.append(anagrams)
        else:
            pass
    return group_anagrams



def checkAnagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    return False



# O(w * n * log(n)) time and O(wn) space
# w = number of words and n is the length of the longest word
# n*log(n) is because we are using a sorting method on the words
def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

test =["yo", "act", "flop", "tac", "cat", "oy", "olfp"]

print(group_anagrams(test))