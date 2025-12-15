# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = set()
        while head!=None:
            if head in a:
                return True
            a.add(head)
            head=head.next
        return False
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next = head.next
s = Solution()
print(s.hasCycle(head))