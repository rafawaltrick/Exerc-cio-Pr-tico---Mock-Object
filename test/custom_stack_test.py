import pytest
from custom_stack.custom_stack_class import CustomStack, StackEmptyException, StackFullException

def test_push():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.size() == 1

def test_pop():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.pop() == 1

def test_pop_empty_stack():
    stack = CustomStack(3)
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_top():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.top() == 1

def test_top_empty_stack():
    stack = CustomStack(3)
    with pytest.raises(StackEmptyException):
        stack.top()

def test_is_empty():
    stack = CustomStack(3)
    assert stack.isEmpty() == True
    stack.push(1)
    assert stack.isEmpty() == False


def test_stack_full_exception():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)
    with pytest.raises(StackFullException):
        stack.push(3)

def test_stack_limit():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2

