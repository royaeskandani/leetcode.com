class Solution:
  def __init__(self):
    pass

  def romanToInt(self, s: str) -> int:
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    roman = [num for num in s]

    output = dic[roman[len(roman) - 1]]
    for i in range(len(roman) - 1):
      if dic[roman[i]] < dic[roman[i+1]]:
        output -= dic[roman[i]]
      else:
        output += dic[roman[i]]

    return output

    
if __name__ == "__main__":
  test = Solution()
  assert(test.romanToInt(s="III") == 3)
  assert(test.romanToInt(s="LVIII") == 58)
  assert(test.romanToInt(s="MCMXCIV") == 1994)
