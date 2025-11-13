from python_solutions.stacks import ThreeStacks


def test_push_and_pop_elements_from_stack_1():
    three = ThreeStacks(9)
    three.push(0, 1)
    three.push(0, 2)
    three.push(0, 3)
    assert three.pop(0) == 3
    assert three.pop(0) == 2
    assert three.pop(0) == 1
    assert three.pop(0) is None


def test_push_and_pop_elements_from_stack_2():
    three = ThreeStacks(9)
    three.push(1, 4)
    three.push(1, 5)
    three.push(1, 6)
    assert three.pop(1) == 6
    assert three.pop(1) == 5
    assert three.pop(1) == 4
    assert three.pop(1) is None


def test_push_and_pop_elements_from_stack_3():
    three = ThreeStacks(9)
    three.push(2, 7)
    three.push(2, 8)
    three.push(2, 9)
    assert three.pop(2) == 9
    assert three.pop(2) == 8
    assert three.pop(2) == 7
    assert three.pop(2) is None


def test_pop_elements_from_empty_stack():
    three = ThreeStacks(3)
    assert three.pop(0) is None
    assert three.pop(1) is None
    assert three.pop(2) is None


def test_peek_elements_from_stacks():
    three = ThreeStacks(3)
    three.push(0, 1)
    three.push(1, 2)
    three.push(2, 3)
    assert three.peek(0) == 1
    assert three.peek(1) == 2
    assert three.peek(2) == 3


def test_peek_elements_from_empty_stack():
    three = ThreeStacks(3)
    assert three.peek(0) is None
    assert three.peek(1) is None
    assert three.peek(2) is None








