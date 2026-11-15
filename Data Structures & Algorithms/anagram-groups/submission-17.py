
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = defaultdict(list)

        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            anaDict[key].append(s)
        
        return list(anaDict.values())