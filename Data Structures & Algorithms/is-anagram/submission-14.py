from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for i in range(len(s)):
            l = s[i]
            counter[ord(l) - ord("a")] += 1
            l = t[i]
            counter[ord(l) - ord("a")] -= 1
        
        for n in counter:
            if n != 0:
                return False

        return True
