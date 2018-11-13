"""OOP stack."""
from typing import Any


class StackOverflowException(Exception):
    """Exception for when stack is full and a push is attempted."""
    # Erind, mis tõstetakse, kui täis stacki püütakse panna elementi.
    pass


class StackUnderflowException(Exception):
    """Exception for when stack is empty and a pop is attempted."""
    # Erind, mis tõstetakse, kui tühjast stackist püütakse elementi võtta.
    pass


class Stack:
    """Simple stack implementation."""

    def __init__(self, capacity: int) -> None:
        """
        Initialise the stack.

        :param capacity: the maximum number of objects that stack can hold.
        """
        self.capacity = capacity
        self.stack = []

    def push(self, item: Any) -> None:
        """
        Add the element to the collection.

        If stack has no more room, raises StackOverflowException.
        """
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            raise StackOverflowException

    def pop(self) -> Any:
        """
        Remove the most recently added element that was not yet removed.

        If stack is empty, raises StackUnderflowException.
        """
        if len(self.stack) > 0:
            element = self.stack[-1]
            self.stack.pop(-1)
            return element
        else:
            raise StackUnderflowException

    def peek(self) -> Any:
        """
        Show the most recently added element without removing it from the stack.

        If stack is empty returns None.
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def is_empty(self) -> bool:
        """Return True if empty."""
        return not len(self.stack)

    def is_full(self) -> bool:
        """Return True if full."""
        return not (len(self.stack) - self.capacity)

    def __str__(self) -> str:
        """
        Get string representation of stack.

        If top element is present should return:
            "Stack(capacity={capacity}, top_element={top_element})"
        Else
            "Stack(capacity={capacity})"
        """
        if len(self.stack):
            return f"Stack(capacity={self.capacity}, top_element={self.stack[-1]})"
        return f"Stack(capacity={self.capacity})"
