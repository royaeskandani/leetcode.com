from scipy.special import binom

class Solution:
  def __init__(self) -> None:
    pass

  def climbStairs(self, n: int) -> int:
    output = 1
    # print(f"n = {n}")
    
    for i in range(n):
      output += binom(i, n-i)
      # print(binom(i, n-i))

    # print(output)
    return output


if __name__ == "__main__":
  test = Solution()

  assert(test.climbStairs(n = 2) == 2)
  assert(test.climbStairs(n = 3) == 3)
  assert(test.climbStairs(n = 4) == 5)
  assert(test.climbStairs(n = 5) == 8)