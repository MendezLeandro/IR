from python_solutions.lists import get_intersection_node
from python_solutions.lists import ListNode


def values(head):
    out = []
    curr = head
    while curr:
        out.append(curr.value)
        curr = getattr(curr, "next", None)
    return out


def test_returns_none_if_the_lists_do_not_intersect():
    list1 = ListNode(value=1)
    list1.next = ListNode(value=2)
    list1.next.next = ListNode(value=3)
    list1.next.next.next = ListNode(value=4)

    list2 = ListNode(value=5)
    list2.next = ListNode(value=6)
    list2.next.next = ListNode(value=7)
    list2.next.next.next = ListNode(value=8)

    result = get_intersection_node(list1, list2)
    assert result is None


def test_returns_intersection_node_when_lists_intersect():
    common = ListNode(value=7)
    common.next = ListNode(value=8)
    common.next.next = ListNode(value=9)

    list1 = ListNode(value=1)
    list1.next = ListNode(value=2)
    list1.next.next = ListNode(value=3)
    list1.next.next.next = ListNode(value=4)
    list1.next.next.next.next = common

    list2 = ListNode(value=5)
    list2.next = ListNode(value=6)
    list2.next.next = common

    result = get_intersection_node(list1, list2)
    assert values(result) == values(common)


def test_returns_intersection_node_when_lists_intersect_at_the_head():
    common = ListNode(value=1)
    common.next = ListNode(value=2)
    common.next.next = ListNode(value=3)

    result = get_intersection_node(common, common)
    assert values(result) == values(common)


def test_returns_intersection_node_when_lists_intersect_at_the_end():
    list1 = ListNode(value=1)
    list1.next = ListNode(value=2)
    list1.next.next = ListNode(value=3)
    list1.next.next.next = ListNode(value=4)
    list1.next.next.next.next = ListNode(value=5)
    list1.next.next.next.next.next = ListNode(value=6)
    list1.next.next.next.next.next.next = ListNode(value=7)

    list2 = ListNode(value=0)
    list2.next = list1

    result = get_intersection_node(list1, list2)
    assert values(result) == values(list1)
