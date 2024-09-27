from sl_traversal import (
    singlylinkedlist,
)  # Ensure this matches the class name in sl_traversal


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(linked_list):
    """Reverse the linked list."""
    prev = None
    current = linked_list.head

    while current:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the link
        prev = current  # Move prev to current
        current = next_node  # Move to the next node
    linked_list.head = prev  # Update the head to the new front


if __name__ == "__main__":
    linked_list = singlylinkedlist()  # Create a new linked list
    linked_list.append(1)  # Append data to the linked list
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("Original linked list:")
    linked_list.traversal()  # Print the original linked list

    reverse(linked_list)  # Reverse the linked list

    print("Reversed linked list:")
    linked_list.traversal()  # Print the reversed linked list
