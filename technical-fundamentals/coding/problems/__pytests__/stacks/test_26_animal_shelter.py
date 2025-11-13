from python_solutions.stacks import AnimalShelter


def test_enqueue_and_dequeue_elements_from_queue():
    shelter = AnimalShelter()

    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")

    assert getattr(shelter.dequeue_any(), "type", None) == "dog"
    assert getattr(shelter.dequeue_any(), "type", None) == "cat"

    shelter.enqueue("cat")
    shelter.enqueue("dog")

    assert getattr(shelter.dequeue_dog(), "type", None) == "dog"

    shelter.enqueue("dog")

    assert getattr(shelter.dequeue_cat(), "type", None) == "cat"


def test_dequeue_methods_return_none_when_shelter_is_empty():
    shelter = AnimalShelter()
    assert shelter.dequeue_any() is None
    assert shelter.dequeue_dog() is None
    assert shelter.dequeue_cat() is None








