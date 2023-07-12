from operator import index


class Solution:
  def __init__(self) -> None:
    pass
    
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    # Divide and conquer methode
    target_idx = 0
    
    while nums != []:

      mid_idx = len(nums)//2
      mid_num = nums[mid_idx]
      
      if mid_num == target:
        target_idx += mid_idx
        return target_idx
      elif mid_num > target: # left side
        nums = nums[:mid_idx]
      else:
        nums = nums[mid_idx+1:]
        target_idx += mid_idx+1
        
    return -1
                
        
if __name__ == "__main__":
  test = Solution()
  
  assert(test.search(nums = [], target = 7) == -1)
  assert(test.search(nums = [9], target = 9) == 0)
  assert(test.search(nums = [-1,0,3,5,9,12], target = 9) == 4)
  assert(test.search(nums = [-1,0,3,5,9,12], target = 2) == -1)