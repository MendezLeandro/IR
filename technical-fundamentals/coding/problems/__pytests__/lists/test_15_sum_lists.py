from python_solutions.lists import sum_lists
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
    list1.next.next = ListNode(value=3)  # 321

    list2 = ListNode(value=4)
    list2.next = ListNode(value=5)
    list2.next.next = ListNode(value=6)  # 654

    result = sum_lists(list1, list2)  # 975 -> 5->7->9
    assert values(result) == [5, 7, 9]


def test_sums_two_non_empty_lists_with_carryover():
    list1 = ListNode(value=9)
    list1.next = ListNode(value=9)
    list1.next.next = ListNode(value=9)  # 999
    list2 = ListNode(value=1)

    result = sum_lists(list1, list2)  # 1000 -> 0->0->0->1
    assert values(result) == [0, 0, 0, 1]


def test_sums_two_lists_with_different_lengths():
    list1 = ListNode(value=1)
    list1.next = ListNode(value=2)
    list1.next.next = ListNode(value=3)
    list1.next.next.next = ListNode(value=4)  # 4321

    list2 = ListNode(value=5)
    list2.next = ListNode(value=6)  # 65

    result = sum_lists(list1, list2)  # 4386 -> 6->8->3->4
    assert values(result) == [6, 8, 3, 4]
