from python_solutions.stacks import StackOfPlates


def test_push_and_pop_elements_from_stack():
    stack = StackOfPlates(3)

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None

    stack.push(4)
    stack.push(5)
    stack.push(6)

    assert stack.pop() == 6
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() is None


def test_push_and_pop_elements_from_multiple_stacks():
    stack = StackOfPlates(2)

    stack.push(1)
    stack.push(2)

    stack.push(3)  # new stack
    stack.push(4)

    stack.push(5)  # new stack

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None


def test_pop_from_empty_stack_returns_none():
    stack = StackOfPlates(2)
    assert stack.pop() is None


def test_push_beyond_capacity_creates_new_stack():
    stack = StackOfPlates(2)

    stack.push(1)
    stack.push(2)

    stack.push(3)  # new stack
    stack.push(4)

    assert stack.pop() == 4
    assert stack.pop() == 3








