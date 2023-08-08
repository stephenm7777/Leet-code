"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # case where s is not the same length as t 
        if len(s) != len(t): 
            return False
        # creating hashmaps to store the letters 
        countS = {}
        countT = {}
        
        for i in range(len(s)): # doesnt matter we can use t here since at this point we have confirmed that s == t in length 
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0) 
        return countS == countT