# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    out = ListNode()
    current = out
    overflow = 0

    while l1 or l2 or overflow:
      value = overflow
      if l1:
          value += l1.val
          l1 = l1.next
      if l2:
          value += l2.val
          l2 = l2.next

      overflow, value = divmod(value, 10)
      current.next = ListNode(value)
      current = current.next

    return out.next