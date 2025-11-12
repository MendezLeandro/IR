from typing import Iterable, Optional

class ListNode:
    def __init__(self, value: int = 0, next: Optional['ListNode'] = None):
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        return f"ListNode(value={self.value}, next={self.next})"
    
    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_list(cls, values: Iterable[int]) -> Optional['ListNode']:
        head = tail = None
        for v in values:
            node = cls(v)
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
        return head

# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
def remove_dups(node: ListNode) -> ListNode:
    if not node:
        return

    duplicates = set()

    p = node
    duplicates.add(node.value)
    while p is not None:
        _next = p.next
        if not _next:
            break
        
        if _next.value in duplicates:
            p.next = _next.next
            continue
        
        duplicates.add(_next.value)
        p = p.next
    
    return node

# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
def kth_to_last(head: ListNode, k: int) -> ListNode:
    if k < 1:
        return None

    slow = head
    fast = head

    for _ in range(k-1):
        if fast.next is None:
            return None # k < len(listnode)
        
        fast = fast.next
    
    if fast is None:
        return None # k steps, no more elements

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    return slow
# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.


def delete_middle_node(head: ListNode, position: int) -> ListNode:
    curr = 0
    p = head
    while p.next is not None:
        if (curr + 1) == position:
            p.next = p.next.next
            return head
        
        curr += 1
        p = p.next
    return head

# 2.4 Partition: Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only need to be after the elements less than x (see below).
# The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

# 8 -> 3 -> 4 -> 1 -> 9 -> 2. 4
# S: 3 -> 1 -> 2 | 8 -> 4 -> 9
def partition_list(head: ListNode, x: int) -> ListNode:
    greater = ListNode(0)
    lower = ListNode(0)

    g_tail = greater
    l_tail = lower

    p = head
    while p is not None:
        _next = p.next
        p.next = None

        if p.value < x:
            l_tail.next = p
            l_tail = p
        else:
            g_tail.next = p
            g_tail = p
        
        p = _next
    
    l_tail.next = greater.next

    return lower.next

# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the Vs digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
# A: 7483 -> 3 -> 8 -> 4 -> 7
# B: 9123 -> 3 -> 2 -> 1 -> 9
# Ret: Sum A + B inverted -> 16606 -> 6 -> 0 -> 6 -> 6 -> 1
def sum_lists(head1: ListNode, head2: ListNode) -> ListNode:
    if not head1 or not head2:
        return None

    num1 = []
    p1 = head1
    while p1 is not None:
        num1.append(str(p1.value))
        p1 = p1.next

    num2 = []
    p2 = head2
    while p2 is not None:
        num2.append(str(p2.value))
        p2 = p2.next
    
    num1.reverse()
    num2.reverse()
    num1 = int(''.join(num1))
    num2 = int(''.join(num2))

    _sum = num1 + num2
    _sum = str(_sum)[::-1]

    head = ListNode(int(_sum[0]))
    tail = head
    for char in _sum[1:]:
        tail.next = ListNode(int(char))
        tail = tail.next
    
    return head

def sum_lists_forward(head1: ListNode, head2: ListNode) -> ListNode | None:
    if not head1 and not head2:
        return None

    num1 = []
    p1 = head1
    while p1 is not None:
        num1.append(str(p1.value))
        p1 = p1.next

    num2 = []
    p2 = head2
    while p2 is not None:
        num2.append(str(p2.value))
        p2 = p2.next
    
    num1 = int(''.join(num1) if num1 else '0')
    num2 = int(''.join(num2) if num2 else '0')

    _sum = num1 + num2
    _sum = str(_sum)

    head = ListNode(int(_sum[0]))
    tail = head
    for char in _sum[1:]:
        tail.next = ListNode(int(char))
        tail = tail.next
    
    return head

# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
def is_palindrome_list(head: ListNode) -> bool:
    hashmap = {}

    p = head
    index = 0
    while p is not None:
        hashmap[index] = p.value

        p = p.next
        index += 1
    
    for k, v in hashmap.items():
        if v != hashmap[index-k-1]:
            return False
    
    return True
# 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
def get_intersection_node(head1: ListNode, head2: ListNode) -> ListNode:
    if not head1 or not head2:
        return None
    
    p1 = head1
    p2 = head2
    while p1 is not p2:
        p1 = p1.next if p1 else head2
        p2 = p2.next if p2 else head1
    
    # Will return none if there´s no intersection
    return p1

# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
def detect_loop_start(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None
    
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    
    return slow