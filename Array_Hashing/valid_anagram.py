""" Question
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters. """

#Solution
def isAnagram(s: str, t: str) -> bool:
    countS, countT = {}, {}
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) +1
        countT[t[i]] = countT.get(t[i], 0) + 1
    
    return countS == countT

#Solution 2
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


print(isAnagram("racecar", "carrace"))
print(isAnagram("jar", "jamm"))
