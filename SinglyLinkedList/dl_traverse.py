class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head node of the doubly linked list

    # Method to traverse the list from the head to the end
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head  # Start from the head node
        while current:
            print(current.data, end=" ")  # Print the current node's data
            current = current.next  # Move to the next node
        print()


# Example usage
dll = DoublyLinkedList()
dll.traverse()  # Output: List is empty
