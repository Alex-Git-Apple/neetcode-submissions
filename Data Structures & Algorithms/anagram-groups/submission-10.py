from collections import defaultdict
#from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            dic[key].append(s)

        return list(dic.values())