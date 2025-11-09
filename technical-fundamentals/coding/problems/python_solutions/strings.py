# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# First version
def is_unique(string: str) -> bool:
    storage = set()
    for char in string:
        if char in storage:
            return False
        storage.add(char)
    return True


def is_unique_two(string: str) -> bool:
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if j == i:
                return False
    
    return True


# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
def is_permutation(s1: str, s2: str) -> bool:
    hashmap = {}
    

    if len(s1) != len(s2):
        return False
    
    for i, char in enumerate(s1):
        hashmap[char] = hashmap[char] + 1 if hashmap.get(char) else 1
    
    for i, char in enumerate(s2):
        if not hashmap.get(char):
            return False
    
        hashmap[char] = hashmap[char] - 1

    non_zeros = [v for v in hashmap.values() if v != 0]
    return False if non_zeros else True


# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
def urlify(s: str) -> str:
    s_list = []
    for c in s:
        if c == ' ':
            s_list.append('%20')
        else:
            s_list.append(c)

    return ''.join(s_list)
# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
def is_palindrome_permutation(s: str) -> bool:
    cleaned_s = s.lower().replace(' ', '')

    hashmap = {}

    for i, c in enumerate(cleaned_s):
        hashmap[c] = hashmap[c] + 1 if hashmap.get(c) else 1

    odds = [v for v in hashmap.values() if v % 2 != 0]

    return False if len(odds) > 1 else True

# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# aa / ab = true
# aba / aab = false
# aab / aa = true
# aba / aa = true

def is_one_away(s1: str, s2: str) -> bool:
    diffs = 0
    p1 = 0
    p2 = 0

    if abs(len(s1) - len(s2)) > 1:
        return False

    while p1 < len(s1) and p2 < len(s2):
        c1 = s1[p1]
        c2 = s2[p2]

        if c1 == c2:
            p1 += 1
            p2 += 1
            continue
        
        diffs += 1
        if diffs > 1:
            return False

        if len(s1) > len(s2):
            p1 += 1
        elif len(s2) > len(s1):
            p2 += 1
        else:
            p1 += 1
            p2 += 1


    return True
        

# 1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
def string_compressor(s: str) -> str:
    char_array = []

    prev = ""
    p = 1
    for i, c in enumerate(s):
        if c == prev:
           p += 1
           continue
        
        if prev != "":
            char_array.extend([prev, str(p)])
            p = 1
        prev = c

    char_array.extend([prev, str(p)])
    
    new_s = ''.join(char_array)

    return new_s if len(new_s) < len(s) else s


# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
#  [1, 2, 3]
#  [4, 5, 6]
#  [7, 8, 9]

# col, row
# 0, 0 - 0, 2
# 0, 1 - 1, 2
# 0, 2 - 2, 2

# 1, 0 - 0, 1
# 1, 1 - 1, 1
# 1, 2 - 2, 1


def rotate_matrix(matrix: list()):
    new_matrix = [[] for _ in range(len(matrix))]

    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            new_matrix[row].append(matrix[col][row])
    
    for col in range(len(new_matrix)):
        new_matrix[col].reverse()
    
    return new_matrix


def improved_rotate_matrix(matrix: list()):
    for col in range(len(matrix)):
        for row in range(col, len(matrix[col])):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
    
    for col in range(len(matrix)):
        matrix[col].reverse()
    
    return matrix



# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]

# [0, 0, 0]
# [0, 4, 5]
# [0, 7, 8]

def zero_matrix(matrix: list()):
    zeros = []
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if matrix[col][row] == 0:
                zeros.append(tuple([col, row]))
    
    if zeros == []:
        return matrix
    
    for tup in zeros:
        col = tup[0]
        row = tup[1]

        matrix[col] = [0 for _ in matrix[col]]
        for col in range(len(matrix)):
            matrix[col][row] = 0
    
    return matrix
        

# 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
def is_substring(s1: str, s2: str) -> bool:
    for i in range(len(s1)):
        rotation = s1[i:] + s1[:i]
        if rotation == s2:
            return True
    
    return False
        
