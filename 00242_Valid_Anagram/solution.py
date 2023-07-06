import enum
from typing import Optional, List


class Solution:
  def __init__(self) -> None:
    pass
    
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    for e in set(s):
      if s.count(e) != t.count(e):
        return False
    return True
                
        
        
if __name__ == "__main__":
  test = Solution()
  
  assert(test.isAnagram(s = "anagram", t = "nagaram") == True)
  assert(test.isAnagram(s = "rat", t = "car") == False)