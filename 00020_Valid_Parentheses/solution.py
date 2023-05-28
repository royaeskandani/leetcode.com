from enum import EnumMeta


class Solution:
  def __init__(self) -> None:
    pass
    
class Solution:
  def isValid(self, s: str) -> bool:
    if (len(s)%2 != 0):
      return False
    
    bracket_pair = dict(('()', '{}', '[]'))    
    stack = []
    
    for bracket in s:
      if bracket in bracket_pair:
        stack.append(bracket)
      elif len(stack) == 0 or bracket != bracket_pair[stack.pop()]:
        return False
    
    return len(stack) == 0
    

if __name__ == "__main__":
  test = Solution()

  assert(test.isValid(s = "({})"))
  assert(test.isValid(s = "({)}") == False)
  assert(test.isValid(s = "()"))
  assert(test.isValid(s = "()[]{}"))
  assert(test.isValid(s = "(]") == False)
  assert(test.isValid(s = "((") == False)
  assert(test.isValid(s = "(){}}{") == False)