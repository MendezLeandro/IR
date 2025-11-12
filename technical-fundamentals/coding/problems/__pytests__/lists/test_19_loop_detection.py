from python_solutions.lists import detect_loop_start
from python_solutions.lists import ListNode


def test_returns_none_if_the_list_has_only_one_node():
    node = ListNode(value=1)
    result = detect_loop_start(node)
    assert result is None


def test_returns_none_if_the_list_does_not_have_a_loop():
    list_head = ListNode(value=1)
    list_head.next = ListNode(value=2)
    list_head.next.next = ListNode(value=3)
    list_head.next.next.next = ListNode(value=4)
    list_head.next.next.next.next = ListNode(value=5)

    result = detect_loop_start(list_head)
    assert result is None


def test_returns_the_node_at_the_beginning_of_the_loop():
    loop_node = ListNode(value=31)
    loop_node.next = ListNode(value=32)
    loop_node.next.next = loop_node

    list_head = ListNode(value=1)
    list_head.next = ListNode(value=2)
    list_head.next.next = ListNode(value=3)
    list_head.next.next.next = ListNode(value=4)
    list_head.next.next.next.next = ListNode(value=5)
    list_head.next.next.next.next.next = ListNode(value=6)
    list_head.next.next.next.next.next.next = ListNode(value=7)
    list_head.next.next.next.next.next.next.next = ListNode(value=8)
    list_head.next.next.next.next.next.next.next.next = ListNode(value=9)
    list_head.next.next.next.next.next.next.next.next.next = loop_node

    result = detect_loop_start(list_head)
    assert result and result.value == loop_node.value


def test_returns_the_node_at_the_beginning_of_the_loop_longer_loop():
    loop_node = ListNode(value=11)
    loop_node.next = ListNode(value=12)
    loop_node.next.next = ListNode(value=13)
    loop_node.next.next.next = loop_node

    list_head = ListNode(value=1)
    list_head.next = ListNode(value=2)
    list_head.next.next = ListNode(value=3)
    list_head.next.next.next = ListNode(value=4)
    list_head.next.next.next.next = ListNode(value=5)
    list_head.next.next.next.next.next = ListNode(value=6)
    list_head.next.next.next.next.next.next = ListNode(value=7)
    list_head.next.next.next.next.next.next.next = ListNode(value=8)
    list_head.next.next.next.next.next.next.next.next = ListNode(value=9)
    list_head.next.next.next.next.next.next.next.next.next = ListNode(value=10)
    list_head.next.next.next.next.next.next.next.next.next.next = loop_node

    result = detect_loop_start(list_head)
    assert result and result.value == loop_node.value
