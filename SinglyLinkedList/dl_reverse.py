class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head node of the doubly linked list

    # Traverse forward and then backward (reverse)
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        # Traverse to the end of the list
        while current.next:
            current = current.next

        # Traverse backward from the last node and print the data
        while current:
            print(current.data, end=" ")  # Print in reverse order
            current = current.prev
        print()


# Example usage
dll = DoublyLinkedList()
dll.traverse()  # Output: List is empty
