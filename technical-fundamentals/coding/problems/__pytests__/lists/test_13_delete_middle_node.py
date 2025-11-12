from python_solutions.lists import delete_middle_node
from python_solutions.lists import ListNode


def values(head):
    out = []
    curr = head
    while curr:
        out.append(curr.value)
        curr = getattr(curr, "next", None)
    return out


def test_deletes_middle_node_at_position_1():
    # 0 -> 1 -> 2 -> 3
    n0 = ListNode(value=0)
    n1 = ListNode(value=1)
    n2 = ListNode(value=2)
    n3 = ListNode(value=3)
    n0.next = n1
    n1.next = n2
    n2.next = n3

    result = delete_middle_node(n0, 1)
    assert values(result) == [0, 2, 3]


def test_no_deletion_if_position_is_out_of_range():
    head = ListNode(value=1)
    head.next = ListNode(value=2)
    head.next.next = ListNode(value=3)

    result = delete_middle_node(head, 4)
    assert values(result) == [1, 2, 3]


def test_no_deletion_if_position_is_less_than_1():
    head = ListNode(value=1)
    head.next = ListNode(value=2)
    head.next.next = ListNode(value=3)

    result = delete_middle_node(head, 0)
    assert values(result) == [1, 2, 3]


def test_no_deletion_if_list_has_only_one_node():
    head = ListNode(value=1)

    result = delete_middle_node(head, 2)
    assert values(result) == [1]


def test_no_deletion_if_list_has_only_two_nodes():
    head = ListNode(value=1)
    head.next = ListNode(value=2)

    result = delete_middle_node(head, 2)
    assert values(result) == [1, 2]
