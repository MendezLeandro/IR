from python_solutions.lists import partition_list
from python_solutions.lists import ListNode


def values(head):
    out = []
    curr = head
    while curr:
        out.append(curr.value)
        curr = getattr(curr, "next", None)
    return out


def test_partitions_the_list_correctly():
    node1 = ListNode(value=3)
    node2 = ListNode(value=5)
    node3 = ListNode(value=8)
    node4 = ListNode(value=5)
    node5 = ListNode(value=10)
    node6 = ListNode(value=2)
    node7 = ListNode(value=1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    result = partition_list(node1, 5)
    assert values(result) == [3, 2, 1, 5, 8, 5, 10]


def test_handles_single_node_list_correctly():
    node1 = ListNode(value=5)
    result = partition_list(node1, 5)
    assert values(result) == [5]


def test_handles_all_nodes_less_than_x():
    node1 = ListNode(value=3)
    node2 = ListNode(value=2)
    node3 = ListNode(value=1)
    node4 = ListNode(value=4)
    node5 = ListNode(value=5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = partition_list(node1, 6)
    assert values(result) == [3, 2, 1, 4, 5]


def test_handles_all_nodes_greater_than_or_equal_to_x():
    node1 = ListNode(value=3)
    node2 = ListNode(value=2)
    node3 = ListNode(value=1)
    node4 = ListNode(value=4)
    node5 = ListNode(value=5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = partition_list(node1, 0)
    assert values(result) == [3, 2, 1, 4, 5]
