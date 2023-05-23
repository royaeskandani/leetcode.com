from re import A
from typing import Optional, List

class Solution:
  def __init__(self) -> None:
    pass
    
class Solution:
  def isPalindrome(self, s: str) -> bool:
    s_converted = ''.join(i for i in s if (64<ord(i)<91) or (96<ord(i)<123) or 47<ord(i)<58)
    s_converted = s_converted.lower()
    
    if s_converted == "":
      return True
    
    length = len(s_converted)
    for i in range(length//2):
      if s_converted[i] != s_converted[length-1-i]:
        return False
      
    return True


if __name__ == "__main__":
  test = Solution()
  
  assert(test.isPalindrome(s="A man, a plan, a canal: Panama"))
  assert(test.isPalindrome(s="race a car") == False)
  assert(test.isPalindrome(s=" "))
  assert(test.isPalindrome(s="0P") == False)