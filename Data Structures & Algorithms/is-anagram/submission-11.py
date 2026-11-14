from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterS, counterT = {}, {}
        for i in range(len(s)):
            l = s[i]
            counterS[l] = counterS.get(l, 0) + 1
            l = t[i]
            counterT[l] = counterT.get(l, 0) + 1

        return counterS == counterT
