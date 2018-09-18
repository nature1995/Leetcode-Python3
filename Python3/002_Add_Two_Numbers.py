#!usr/bin/env python
# -*- coding:utf-8 -*-
'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def my_test(self):
        print(self.val)
        if self.next:
            self.next.my_test()


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur = result
        while l1 or l2:
            cur.val += self.AddTwoNodes(l1, l2)
            if cur.val >= 10:
                cur.val -= 10
                cur.next = ListNode(1)
            else:
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result


    def AddTwoNodes(self, n1, n2):
        if not n1 and not n2:
            None
        if not n1:
            return n2.val
        if not n2:
            return n1.val
        return n1.val + n2.val






if __name__ == "__main__":
    list = ListNode(2)
    list.next = ListNode(4)
    list.next.next = ListNode(3)
    list1 = ListNode(5)
    list1.next = ListNode(6)
    list1.next.next = ListNode(4)

    print(Solution().addTwoNumbers(list, list1).my_test())
