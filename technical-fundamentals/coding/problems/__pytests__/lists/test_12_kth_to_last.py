from python_solutions.lists import kth_to_last
from python_solutions.lists import ListNode


def test_returns_none_if_k_is_less_than_1():
    node1 = ListNode(value=1)
    result = kth_to_last(node1, 0)
    assert result is None


def test_returns_none_if_k_is_greater_than_length():
    node1 = ListNode(value=1)
    result = kth_to_last(node1, 2)
    assert result is None


def test_returns_kth_to_last_element_when_k_is_valid():
    node1 = ListNode(value=1)
    node2 = ListNode(value=2)
    node3 = ListNode(value=3)
    node4 = ListNode(value=4)
    node5 = ListNode(value=5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = kth_to_last(node1, 2)
    assert result and result.value == 4


def test_returns_head_if_k_is_equal_to_length():
    node1 = ListNode(value=1)
    node2 = ListNode(value=2)
    node3 = ListNode(value=3)
    node4 = ListNode(value=4)
    node5 = ListNode(value=5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = kth_to_last(node1, 5)
    assert result and result.value == 1
