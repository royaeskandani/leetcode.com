import math

class Solution:
  def __init__(self) -> None:
    pass

  def isPalindrome(self, x: int) -> bool:
    if x in range(0,10):
      return True
    if x < 11:
      return False
    
    dimension = math.floor(math.log10(x))
    
    while dimension > 0:
      digit = x//(10**dimension)
      digit %= 10
      
      if digit != x%10:
        return False
      x //= 10
      
      dimension -= 2
      
    return True


if __name__ == "__main__":
  test = Solution()
  
  assert(test.isPalindrome(121))
  assert(test.isPalindrome(-121) == False)
  assert(test.isPalindrome(10) == False)
  assert(test.isPalindrome(1000021) == False)
  