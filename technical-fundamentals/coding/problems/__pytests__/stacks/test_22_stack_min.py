from python_solutions.stacks import StackMin


def test_push_and_pop_elements_from_stack():
    stack = StackMin()
    stack.push(5)
    stack.push(2)
    stack.push(8)
    stack.push(1)

    assert stack.min() == 1

    assert stack.pop() == 1
    assert stack.min() == 2

    assert stack.pop() == 8
    assert stack.min() == 2

    assert stack.pop() == 2
    assert stack.min() == 5

    assert stack.pop() == 5
    assert stack.min() is None


def test_min_method_returns_none_when_stack_is_empty():
    stack = StackMin()
    assert stack.min() is None


def test_push_and_pop_mixed_with_min_operations():
    stack = StackMin()
    stack.push(3)
    assert stack.min() == 3

    stack.push(5)
    assert stack.min() == 3

    stack.push(2)
    assert stack.min() == 2

    stack.push(1)
    assert stack.min() == 1

    assert stack.pop() == 1
    assert stack.min() == 2

    assert stack.pop() == 2
    assert stack.min() == 3

    stack.push(0)
    assert stack.min() == 0

    assert stack.pop() == 0
    assert stack.min() == 3

    assert stack.pop() == 5
    assert stack.min() == 3

    assert stack.pop() == 3
    assert stack.min() is None








