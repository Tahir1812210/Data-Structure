#initialization

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 


#method to add node at the end of list

class singlylinkedlist:
    def __init__(self):
        self.head = None #initialize head node
    
    def append(self , data):
        new_node = Node(data)

        if not self.head: #if list is empty
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traversal(self):
        current = self.head

        while current.next:
            print(current.data)
            current = current.next


#usage

linked_list = singlylinkedlist()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.traversal()
        
        
        



