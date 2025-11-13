from python_solutions.stacks import MyQueue


def test_enqueue_and_dequeue_elements_from_queue():
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() is None


def test_enqueue_and_dequeue_mixed_with_peek_operations():
    queue = MyQueue()

    queue.enqueue(1)
    assert queue.peek() == 1

    queue.enqueue(2)
    assert queue.peek() == 1

    assert queue.dequeue() == 1
    assert queue.peek() == 2

    queue.enqueue(3)
    assert queue.peek() == 2

    assert queue.dequeue() == 2
    assert queue.peek() == 3

    assert queue.dequeue() == 3
    assert queue.peek() is None


def test_peek_from_empty_queue_returns_none():
    queue = MyQueue()
    assert queue.peek() is None


def test_is_empty_true_for_empty_queue():
    queue = MyQueue()
    assert queue.is_empty() is True


def test_is_empty_false_for_non_empty_queue():
    queue = MyQueue()
    queue.enqueue(1)
    assert queue.is_empty() is False








