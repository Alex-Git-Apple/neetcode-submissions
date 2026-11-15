class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freqDict = defaultdict(list)

        for n, count in counter.items():
            freqDict[count].append(n)

        res = []

        for freq in sorted(freqDict, reverse=True):
            for n in freqDict[freq]:
                res.append(n)
            if len(res) == k:
                return res
        return []