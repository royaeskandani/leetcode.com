from typing import Optional, List


class Solution:
  def __init__(self) -> None:
    pass
    
  def containsDuplicate(self, nums: List[int]) -> bool:
    nums_set = set()
    
    for num in nums:
      if num in nums_set:
        return True 
      nums_set.add(num)
    return False
        
        
if __name__ == "__main__":
  test = Solution()

  assert(test.containsDuplicate(nums = [1, 2, 3, 1]) == True)
  assert(test.containsDuplicate(nums = [1, 2, 3, 4]) == False)
  assert(test.containsDuplicate(nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)