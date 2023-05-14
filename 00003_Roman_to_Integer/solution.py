class Solution:
  def __init__(self):
    self.roman = ''

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
  test.roman = 'MCMXCIV'

  print(test.romanToInt(test.roman))
