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
        if head==None:
            return None

        prev = None
        curr = head
        while curr!=None:
            nNext = curr.next
            curr.next = prev
            prev = curr
            curr = nNext
        return prev
    
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