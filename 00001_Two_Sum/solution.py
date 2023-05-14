class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} # switch idx and value dependency

        for idx, value in enumerate(nums):
            rest = target - value

            if rest in dic:
                return [dic[rest], idx]
            dic[value] = idx