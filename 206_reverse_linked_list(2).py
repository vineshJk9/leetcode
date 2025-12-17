# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        nHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nHead
    
    def print1(self, head):
        temp = head
        while temp!=None:
            print(temp.val)
            temp=temp.next


     
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s = Solution()
head1 = s.reverseList(head)
s.print1(head1)