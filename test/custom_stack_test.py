from src.custom_stack_class import *
import pytest

def test_push_one_elementinstack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()

def test_push_multiple_elements():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)
    cut.push(3)
    assert cut.size() == 3
    assert cut.top() == 3

def test_push_to_full_stack():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)
    with pytest.raises(StackFullException):
        cut.push(3)

def test_pop_element():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)
    popped = cut.pop()
    assert popped == 2
    assert cut.size() == 1
    assert cut.top() == 1

def test_pop_from_empty_stack():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.pop()

def test_top_empty_stack():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.top()

def test_is_empty_on_new_stack():
    cut = CustomStack(3)
    assert cut.is_empty() == True

def test_is_empty_after_operations():
    cut = CustomStack(3)
    cut.push(1)
    cut.pop()
    assert cut.is_empty() == True