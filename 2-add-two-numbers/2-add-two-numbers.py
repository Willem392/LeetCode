# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = ""
        list2 = ""
        while l1:
            list1 = str(l1.val) + list1
            l1 = l1.next
        while l2:
            list2 = str(l2.val) + list2
            l2 = l2.next
        output = ""
        for ch in (str(int(list1)+int(list2))):
            output = ch + output
        head = ListNode(output[0])
        curr = head
        for i in range(1, len(output)):
            curr.next = ListNode(output[i])
            curr = curr.next
        return head

    