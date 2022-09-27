from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Using Linked List Solution
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data = []
        for list in lists:
            while list:
                data.append(list.val)
                list = list.next

        data.sort()
        tmp = ListNode()
        head = tmp
        for item in data:
            tmp.next = ListNode(item)
            tmp = tmp.next

        return head.next
