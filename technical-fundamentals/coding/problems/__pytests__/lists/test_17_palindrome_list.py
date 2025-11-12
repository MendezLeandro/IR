from python_solutions.lists import is_palindrome_list
from python_solutions.lists import ListNode


def test_single_node_list_is_palindrome():
    node = ListNode(value=1)
    assert is_palindrome_list(node) is True


def test_palindrome_list_with_odd_number_of_nodes():
    node1 = ListNode(value=1)
    node2 = ListNode(value=2)
    node3 = ListNode(value=3)
    node4 = ListNode(value=2)
    node5 = ListNode(value=1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    assert is_palindrome_list(node1) is True


def test_non_palindrome_list():
    node1 = ListNode(value=1)
    node2 = ListNode(value=2)
    node3 = ListNode(value=3)
    node4 = ListNode(value=4)
    node5 = ListNode(value=5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    assert is_palindrome_list(node1) is False


def test_palindrome_list_with_even_number_of_nodes():
    node1 = ListNode(value=1)
    node2 = ListNode(value=2)
    node3 = ListNode(value=2)
    node4 = ListNode(value=1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    assert is_palindrome_list(node1) is True
