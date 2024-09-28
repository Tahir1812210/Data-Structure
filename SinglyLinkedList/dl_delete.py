class Node:
    # Initialize a node with data and pointers to next and previous
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node (default None)
        self.prev = None  # Pointer to the previous node (default None)


class DoublyLinkedList:
    # Initialize the doubly linked list
    def __init__(self):
        self.head = None  # Head of the list, initially empty

    # Traverse the list from the head to the end
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head  # Start from the head node
        while current:
            print(current.data, end=" ")  # Print the current node's data
            current = current.next  # Move to the next node
        print()

    # Delete a node at the start of the list
    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:  # If there's only one node
            self.head = None  # Set head to None
        else:
            self.head = self.head.next  # Move head to the next node
            self.head.prev = None  # Remove reference to the old head

    # Delete a node at the end of the list
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:  # If there's only one node
            self.head = None  # Set head to None
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next

            current.prev.next = (
                None  # Remove the last node by setting the previous node's next to None
            )

    # Delete a node at a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:  # If deleting the first node
            self.delete_at_start()
            return

        current = self.head
        index = 0

        # Traverse to the node at the given position
        while current and index < position:
            current = current.next
            index += 1

        if current is None:  # If position is out of range
            print("Position out of range")
        elif current.next is None:  # If it's the last node
            self.delete_at_end()
        else:
            current.prev.next = current.next  # Bypass the current node
            current.next.prev = current.prev  # Maintain the double linkage


# Example usage
dll = DoublyLinkedList()
dll.delete_at_start()  # Output: List is empty
