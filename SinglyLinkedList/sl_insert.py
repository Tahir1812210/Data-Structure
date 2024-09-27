class Node:
    def __init__(self, data):
        """Initialize a new node with the given data and no next node."""
        self.data = data
        self.next = None  # This is the reference to the next node


class SinglyLinkedList:
    def __init__(self):
        """Initialize the singly linked list with an empty head."""
        self.head = None  # The head is the starting point of the list

    def insert_at_start(self, data):
        """Insert a new node at the start of the linked list."""
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Make the new node the head of the list
        print(f"Inserted {data} at the start of the list.")

    def insert_at_end(self, data):
        """Insert a new node at the end of the linked list."""
        new_node = Node(data)  # Create a new node with the given data

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end of the list (first element).")
            return

        # Traverse to the last node of the list
        temp = self.head
        while temp.next:  # Move until the last node
            temp = temp.next

        temp.next = new_node  # Link the last node to the new node
        print(f"Inserted {data} at the end of the list.")

    def insert_at_position(self, data, position):
        """Insert a new node at the specified position in the linked list."""
        if position < 1:
            print("Position should be greater than or equal to 1.")
            return

        new_node = Node(data)  # Create a new node with the given data

        # If inserting at the head (position 1)
        if position == 1:
            new_node.next = self.head  # Link new node to the current head
            self.head = new_node  # Make the new node the head
            print(f"Inserted {data} at position {position} (start of the list).")
            return

        # Traverse the list to find the position before the desired one
        temp = self.head
        current_position = 1

        while temp is not None and current_position < position - 1:
            temp = temp.next
            current_position += 1

        # If we reach the end of the list or the position is out of bounds
        if temp is None:
            print(f"Position {position} is out of bounds.")
            return

        new_node.next = temp.next  # Link new node to the next node
        temp.next = new_node  # Link the previous node to the new node
        print(f"Inserted {data} at position {position}.")

    def traversal(self):
        """Traverse and print all elements of the linked list."""
        if self.head is None:
            print("The linked list is empty.")
            return

        temp = self.head
        while temp:  # Traverse the list until we reach the end
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next


# Example usage of the SinglyLinkedList
if __name__ == "__main__":
    # Create a new linked list instance
    linked_list = SinglyLinkedList()

    # Insert elements at the end of the list
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(50)

    # Display the current linked list
    print("After inserting 30 and 50 at the end:")
    linked_list.traversal()

    # Insert an element at the start of the list
    linked_list.insert_at_start(10)

    # Display the updated linked list
    print("After inserting 10 at the start:")
    linked_list.traversal()

    # Insert an element at position 3 (middle of the list)
    linked_list.insert_at_position(40, 3)

    # Display the updated linked list
    print("After inserting 40 at position 3 (middle):")
    linked_list.traversal()

    # Insert another element at the end of the list
    linked_list.insert_at_end(60)

    # Display the updated linked list
    print("After inserting 60 at the end:")
    linked_list.traversal()

    # Insert an element at position 2 (another middle position)
    linked_list.insert_at_position(20, 2)

    # Display the updated linked list
    print("After inserting 20 at position 2 (middle):")
    linked_list.traversal()
