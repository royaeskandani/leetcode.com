class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __eq__(self, other):
    if isinstance(other, ListNode):
      node1 = self
      node2 = other

      while node1 and node2:
        if node1.val != node2.val:
            return False
        node1 = node1.next
        node2 = node2.next

      if not node1 and not node2:
        return True

    return False

  def printListNode(self):
    values = []
    current = self
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

  @classmethod
  def fromList(cls, l: list) -> 'ListNode':
    head = cls()
    current = head

    for i in range(len(l)):
      current.next = cls(l[i])
      current = current.next

    return head.next

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

if __name__ == "__main__":
  test = Solution()

  l1 = ListNode.fromList([2,4,3])
  l2 = ListNode.fromList([5,6,4])
  l3 = ListNode.fromList([7,0,8])
  # test.addTwoNumbers(l1, l2).printListNode()
  assert(test.addTwoNumbers(l1, l2) == l3)

  assert(test.addTwoNumbers(ListNode.fromList([0]), ListNode.fromList([0])) == ListNode.fromList([0]))

  l4 = ListNode.fromList([9,9,9,9,9,9,9])
  l5 = ListNode.fromList([9,9,9,9])
  l6 = ListNode.fromList([8,9,9,9,0,0,0,1])
  assert(test.addTwoNumbers(l4, l5) == l6)
