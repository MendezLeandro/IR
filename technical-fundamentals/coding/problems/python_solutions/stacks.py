# 3.1 Three in One: Describe how you could use a single array to implement three stacks.


class ThreeStacks:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = [None] * (capacity * 3)
        self.elems = [0, 0, 0]
    
    def top_index(self, stack: int) -> int:
        return (stack * self.capacity) + self.elems[stack] - 1

    def push(self, stack: int, value):
        if self.elems[stack] == self.capacity:
            raise IndexError()
        
        self.elems[stack] += 1
        self.values[self.top_index(stack)] = value

    def pop(self, stack: int):
        if self.elems[stack] == 0:
            raise IndexError()

        top_index = self.top_index(stack)
        value = self.values[top_index]
        self.values[top_index] = None
        self.elems[stack] -= 1
        return value

    def peek(self, stack: int):
        if self.elems[stack] == 0:
            raise IndexError()
        return self.values[self.top_index(stack)]


# 3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.
# 3, 5, 1, 9
# self.min = [3, 3, 1, 1]


class StackMin:
    def __init__(self):
        self._min = []
        self.values = []

    def push(self, value: int) -> None:
        self.values.append(value)
        if (self._min == []) or (value < self._min[-1][0]):
            self._min.append((value, 1))
        elif value == self._min[-1][0]:
            self._min[-1][1] += 1
    
    def pop(self) -> int:
        if self._min[-1][1] == 1:
            self._min.pop()
        else:
            self._min[-1][1] -= 1
        return self.values.pop()
    
    def get_min(self) -> int | None:
        return self._min[-1] if self._min else None


# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks.push() and SetOfStacks.pop()
# should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

# Follow up: Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.
class SetOfStacks:
    def __init__(self, threshold: int):
        self.threshold = threshold
        self.stacks = []

    def push(self, value: int) -> None:
        if not self.stacks:
            self.stacks = [[value]]
            return
        
        latest_stack = self.stacks[-1]
        if len(latest_stack) >= self.threshold:
            self.stacks.append([value])
        else:
            self.stacks[-1].append(value)
    
    def pop(self) -> int | None:
        if not self.stacks:
            return None
        
        popped_item = self.stacks[-1].pop()
        if self.stacks[-1] == []:
            self.stacks.pop()
        return popped_item
    
    def pop_at(self, index: int) int | None:
        if not self.stacks:
            return None
        
        popped_item = self.stacks[-(len(self.stacks)-index)].pop()
        if self.stacks[-(len(stacks) - index)] == []:
            del self.stacks[-(len(stacks - index))]
        return popped_item

# This pop_at func will operate based on the assumption that we are OK with the tradeoff of having some stacks not operating at full capacity
# Doing a rollover on subsequent stacks would raise time complexity by a fair margin

# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

# New = [3, 4, 5, 6]
# Old = [6, 5, 4, 3]
class MyQueue:
    def __init__(self):
        self.new_items = []
        self.old_items = []
    
    def add(self, value: int) -> None:
        self.new_items.append(value)

    def remove(self) -> int | None:
        self._move_new_to_old()
        return self.old_items.pop() if self.old_items else None

    def peek(self) -> int | None:
        if not self.new_items and not self.old_items:
            return None
        return self.old_items[-1] if self.old_items else self.new_items[0]

    def is_empty(self) -> bool:
        return not (self.old_items or self.new_items)

    def _move_new_to_old(self) -> None:
        if not self.old_items:
            while self.new_items:
                self.old_items.append(self.new_items.pop())


# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and isEmpty.

class SortStack:
    def __init__(self):
        self.temp_stack = []
        self.stack = []
    
    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            return
        
        if value <= self.stack[-1]:
            self.stack.append(value)
        else:
            while self.stack and (value > self.stack[-1]):
                self.temp_stack.append(self.stack.pop())
            
            self.stack.append(value)
            while self.temp_stack:
                self.stack.append(self.temp_stack.pop())

    def pop(self) -> int | None:
        if not self.stack:
            return None
        
        return self.stack.pop()

    def peek(self) -> int | None:
        if not self.stack:
            return None
        
        return self.stack[-1]

    def is_empty(self) -> bool:
        return not self.stack


# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like.
# Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
# You may use the built-in LinkedList data structure.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def enqueue(self, value) -> None:
        node = Node(value)
        if self.tail:
            self.tail.next = node

        self.tail = node
        if self.head is None:
            self.head = node

    def dequeue(self):
        if self.head is None:
            return None

        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return val

    def peek(self):
        return self.head.value if self.head else None

    def is_empty(self) -> bool:
        return self.head is None


class Animal:
    def __init__(self, kind: str, name: str | None, order: int):
        if kind not in ("dog", "cat"):
            raise ValueError("kind must be 'dog' or 'cat'")

        self.kind = kind
        self.name = name
        self.order = order


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self._order = 0

    def enqueue(self, kind: str, name: str | None = None) -> None:
        animal = Animal(kind, name, self._order)
        self._order += 1
        if kind == "dog":
            self.dogs.enqueue(animal)
        else:
            self.cats.enqueue(animal)

    def dequeue_any(self) -> Animal | None:
        if self.dogs.is_empty() and self.cats.is_empty():
            return None

        if self.dogs.is_empty():
            return self.cats.dequeue()

        if self.cats.is_empty():
            return self.dogs.dequeue()

        if self.dogs.peek().order < self.cats.peek().order:
            return self.dogs.dequeue()
        else:
            return self.cats.dequeue()

    def dequeue_dog(self) -> Animal | None:
        return self.dogs.dequeue()

    def dequeue_cat(self) -> Animal | None:
        return self.cats.dequeue()
