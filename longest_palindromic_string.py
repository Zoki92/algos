"""Write a function that receives a string and returns its longest
palindromic substric.
"""


def longest_palindromic_substring(string):
    longest = None
    for i in range(len(string)):
        for j in reversed(range(len(string))):
            if string[j] == string[i]:
                if longest:
                    if is_palindrom(i, j, string) and len(longest) < len(string[i:j+1]):
                        longest = string[i:j+1]
                else:
                    if is_palindrom(i, j, string):
                        longest = string[i:j+1]
    return longest

def is_palindrom(first, second, string):
    while first < second:
        if string[first] != string[second]:
            return False
        first += 1
        second -= 1
    return True

test = "abaxyzzyxf"
print(longest_palindromic_substring(test))