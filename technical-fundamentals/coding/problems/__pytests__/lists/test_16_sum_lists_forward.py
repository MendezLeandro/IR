from python_solutions.lists import sum_lists_forward
from python_solutions.lists import ListNode


def values(head):
    out = []
    curr = head
    while curr:
        out.append(curr.value)
        curr = getattr(curr, "next", None)
    return out


def test_sums_two_non_empty_lists_without_carryover():
    list1 = ListNode(value=1)
    list1.next = ListNode(value=2)
    list1.next.next = ListNode(value=3)  # 123

    list2 = ListNode(value=4)
    list2.next = ListNode(value=5)
    list2.next.next = ListNode(value=6)  # 456

    result = sum_lists_forward(list1, list2)  # 579 -> 5->7->9
    assert values(result) == [5, 7, 9]


def test_sums_two_non_empty_lists_with_carryover():
    list1 = ListNode(value=9)
    list1.next = ListNode(value=9)
    list1.next.next = ListNode(value=9)  # 999
    list2 = ListNode(value=1)  # 1
    result = sum_lists_forward(list1, list2)  # 1000 -> 1->0->0->0
    assert values(result) == [1, 0, 0, 0]


def test_sums_two_lists_with_different_lengths():
    list1 = ListNode(value=1)
    list1.next = ListNode(value=2)
    list1.next.next = ListNode(value=3)
    list1.next.next.next = ListNode(value=4)  # 1234

    list2 = ListNode(value=5)
    list2.next = ListNode(value=6)  # 56
    result = sum_lists_forward(list1, list2)  # 1290 -> 1->2->9->0
    assert values(result) == [1, 2, 9, 0]


def test_sums_two_empty_lists():
    result = sum_lists_forward(None, None)
    assert result is None


def test_sums_one_empty_list_and_one_non_empty_list():
    list1 = ListNode(value=1)
    list1.next = ListNode(value=2)
    list1.next.next = ListNode(value=3)
    result = sum_lists_forward(list1, None)
    assert values(result) == [1, 2, 3]
