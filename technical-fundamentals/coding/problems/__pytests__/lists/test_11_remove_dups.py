from python_solutions.lists import remove_dups
from python_solutions.lists import ListNode

def values(head):
    out = []
    curr = head
    while curr:
        out.append(curr.value)
        curr = getattr(curr, "next", None)
    return out

def test_remove_duplicates_on_linked_list():
    node1 = ListNode(value="a")
    node2 = ListNode(value="a")
    node3 = ListNode(value="b")
    node1.next = node2
    node2.next = node3

    result = remove_dups(node1)
    assert values(result) == ["a", "b"]

def test_no_duplicates_in_linked_list():
    node1 = ListNode(value="a")
    node2 = ListNode(value="b")
    node3 = ListNode(value="c")
    node1.next = node2
    node2.next = node3

    result = remove_dups(node1)
    assert values(result) == ["a", "b", "c"]

def test_multiple_duplicates_in_linked_list():
    node1 = ListNode(value="a")
    node2 = ListNode(value="a")
    node3 = ListNode(value="a")
    node1.next = node2
    node2.next = node3

    result = remove_dups(node1)
    assert values(result) == ["a"]

def test_empty_linked_list():
    result = remove_dups(None)
    assert result is None

def test_linked_list_with_one_node():
    node1 = ListNode(value="a")
    result = remove_dups(node1)
    assert values(result) == ["a"]
