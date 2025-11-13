from python_solutions.stacks import SortStack


def test_push_elements_in_sorted_order():
    stack = SortStack()

    stack.push(3)
    assert stack.peek() == 3

    stack.push(1)
    assert stack.peek() == 1

    stack.push(5)
    assert stack.peek() == 1

    stack.push(2)
    assert stack.peek() == 1

    stack.push(4)
    assert stack.peek() == 1


def test_pop_elements_in_sorted_order():
    stack = SortStack()
    stack.push(3)
    stack.push(1)
    stack.push(5)
    stack.push(2)
    stack.push(4)

    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.pop() == 3
    assert stack.pop() == 4
    assert stack.pop() == 5
    assert stack.pop() is None


def test_peek_returns_the_top_element_without_removing_it():
    stack = SortStack()
    stack.push(3)
    stack.push(1)
    stack.push(5)
    assert stack.peek() == 1
    assert stack.peek() == 1


def test_is_empty_returns_true_for_empty_stack():
    stack = SortStack()
    assert stack.is_empty() is True


def test_is_empty_returns_false_for_non_empty_stack():
    stack = SortStack()
    stack.push(1)
    assert stack.is_empty() is False








