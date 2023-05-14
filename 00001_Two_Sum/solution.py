from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {} # switch idx and value dependency

    for idx, value in enumerate(nums):
      rest = target - value

      if rest in dic:
          return [dic[rest], idx]
      dic[value] = idx

if __name__ == "__main__":
  test = Solution()

  assert(test.twoSum(nums = [2,7,11,15], target = 9) == [0,1])
  assert(test.twoSum(nums = [3,2,4], target = 6) == [1,2])
  assert(test.twoSum(nums = [3,3], target = 6) == [0,1])