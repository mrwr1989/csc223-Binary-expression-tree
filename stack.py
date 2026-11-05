
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)



if __name__ == "__main__":
    stack = Stack()

    # Test empty stack
    assert stack.is_empty()
    print("Empty stack test passed")

    # Test push and size
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.size() == 3
    print("Push and size tests passed")

    # Test peek
    assert stack.peek() == 30
    assert stack.size() == 3
    print("Peek test passed")

    # Test LIFO order
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty()
    print("LIFO and pop tests passed")

    # Test pop on empty stack
    try:
        stack.pop()
        assert False, "Expected IndexError"
    except IndexError:
        print("Empty pop error test passed")

    # Test peek on empty stack
    try:
        stack.peek()
        assert False, "Expected IndexError"
    except IndexError:
        print("Empty peek error test passed")

    print("All Stack tests passed!")