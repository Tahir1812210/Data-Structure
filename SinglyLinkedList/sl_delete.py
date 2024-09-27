class Node:
    def __init__(self, data):
        """Initialize a new node with the given data and no next node."""
        self.data = data
        self.next = None  # This is the reference to the next node


class SinglyLinkedList:
    def __init__(self):
        """Initialize the singly linked list with an empty head."""
        self.head = None  # The head is the starting point of the list

    def delete_at_start(self):
        """Delete the first node (head) of the linked list."""
        # If the list is empty, no deletion is possible
        if self.head is None:
            print("List is empty, no nodes to delete.")
            return

        # Set the head to the next node, effectively removing the first node
        deleted_data = (
            self.head.data
        )  # Save the data of the node being deleted for display
        self.head = self.head.next  # Move the head to the next node
        print(f"Deleted {deleted_data} from the start of the list.")

    def delete_at_end(self):
        """Delete the last node of the linked list."""
        # If the list is empty, no deletion is possible
        if self.head is None:
            print("List is empty, no nodes to delete.")
            return

        # If there is only one node, simply set the head to None
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            print(f"Deleted {deleted_data} from the end of the list (only node).")
            return

        # Traverse to the second last node
        temp = self.head
        while temp.next.next:  # Stop when temp is the second last node
            temp = temp.next

        # Now temp is the second last node
        deleted_data = temp.next.data  # Save the data of the node being deleted
        temp.next = None  # Remove the last node
        print(f"Deleted {deleted_data} from the end of the list.")

    def delete_at_position(self, position):
        """Delete the node at the specified position (1-based index)."""
        if self.head is None:
            print("List is empty, no nodes to delete.")
            return

        if position == 1:
            self.delete_at_start()
            return

        temp = self.head
        current_position = 1

        # Traverse to the node just before the position
        while temp is not None and current_position < position - 1:
            temp = temp.next
            current_position += 1

        # Check if the position is out of bounds
        if temp is None or temp.next is None:
            print(f"Position {position} is out of bounds.")
            return

        # Now temp.next is the node to be deleted
        deleted_data = temp.next.data
        temp.next = temp.next.next  # Remove the node from the list
        print(f"Deleted {deleted_data} from position {position}.")

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

    # Display the current linked list
    print("Initial linked list:")
    linked_list.traversal()

    # Attempt to delete at the start
    linked_list.delete_at_start()
    print("After deleting at the start:")
    linked_list.traversal()

    # Attempt to delete at the end
    linked_list.delete_at_end()
    print("After deleting at the end:")
    linked_list.traversal()
