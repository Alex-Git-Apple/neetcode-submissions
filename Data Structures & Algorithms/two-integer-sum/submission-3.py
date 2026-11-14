class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndexMap = {}
        for (i, v) in enumerate(nums):
            diff = target - v
            if diff in valueToIndexMap:
                return [valueToIndexMap[diff], i]
            if v not in valueToIndexMap:
                valueToIndexMap[v] = i
        return []