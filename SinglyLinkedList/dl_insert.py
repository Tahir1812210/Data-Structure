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

    # Insert a new node at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If list is empty, the new node becomes head
            return
        else:
            new_node.next = self.head  # Link new node's next to current head
            self.head.prev = new_node  # Link current head's prev to new node
            self.head = new_node  # Update head to the new node

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If list is empty, the new node becomes head
            return

        current = self.head  # Start from head
        while current.next:  # Traverse to the end
            current = current.next

        current.next = new_node  # Link the last node's next to the new node
        new_node.prev = current  # Link new node's prev to the last node

    # Insert a new node at a given position
    def insert_at_position(self, position, data):
        if position == 0:  # If inserting at the start
            self.insert_at_start(data)
            return

        new_node = Node(data)
        current = self.head
        index = 0

        # Traverse to the position
        while current and index < position - 1:
            current = current.next
            index += 1

        if current is None:  # If the position is out of bounds
            print("Position out of bounds")
            return

        if current.next is None:  # If inserting at the end
            self.insert_at_end(data)
        else:
            new_node.next = current.next
            new_node.prev = current  # Link new node's prev to current
            current.next.prev = new_node
            current.next = new_node  # Link current's next to the new node


# Example usage
dll = DoublyLinkedList()
dll.insert_at_start(10)  # Inserting at the start
dll.insert_at_end(30)  # Inserting at the end
dll.insert_at_position(1, 20)  # Inserting at position 1 (between 10 and 30)
dll.traverse()  # Output: 10 20 30
