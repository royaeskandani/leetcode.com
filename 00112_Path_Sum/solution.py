from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  @classmethod
  def listToTree(cls, lst: List[Optional[int]], index: int) -> Optional['TreeNode']:
    if index >= len(lst) or lst[index] is None:
      return None

    root = cls(val=lst[index])
    root.left = cls.listToTree(lst, 2 * index + 1)
    root.right = cls.listToTree(lst, 2 * index + 2)
    return root


class Solution:
  def __init__(self) -> None:
    pass


  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(node: Optional[TreeNode]) -> bool:
      if not root: # empty tree
        return False
      
      if not root.left and not root.right: # leaf
        return targetSum == root.val
      
      return(
        self.hasPathSum(root.left, targetSum - root.val)
        or self.hasPathSum(root.right, targetSum - root.val))
    
    return dfs(root)
  

if __name__ == "__main__":
  test = Solution()

  tree_list = [4, 1, 2]
  root = TreeNode.listToTree(tree_list, 0)
  assert(test.hasPathSum(root = root, targetSum = 5) == True)

  tree_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
  root = TreeNode.listToTree(tree_list, 0)
  assert(test.hasPathSum(root = root, targetSum = 22) == True)

  tree_list = [1, 2, 3]
  root = TreeNode.listToTree(tree_list, 0)
  assert(test.hasPathSum(root = root, targetSum = 5) == False)

  tree_list = []
  root = TreeNode.listToTree(tree_list, 0)
  assert(test.hasPathSum(root = root, targetSum = 0) == False)