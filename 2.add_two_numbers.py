"""
@author: Xiaoyu Li
Created on 10/3/2018
You are given two non-empty linked lists representing two non-negative integers. The digits are stored
in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def add_two_numbers(l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next

        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(add_two_numbers(l1, l2).next.next.val)


