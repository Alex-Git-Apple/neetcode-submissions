class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndexMap = {}
        for (i, v) in enumerate(nums):
            diff = target - v
            if diff in valueToIndexMap:
                return [valueToIndexMap[diff], i]
            valueToIndexMap[v] = i
        return []