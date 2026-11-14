class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevIndex = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in prevIndex:
                return [prevIndex[diff], i]
            if v not in prevIndex:
                prevIndex[v] = i
        return []