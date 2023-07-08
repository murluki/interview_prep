class Node:
    #value and next value
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #beginning
    def __init__(self):

        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    def is_empty(self):
        return self.head is None

    def get_length(self):
        return self.length

#add Node to the end
    def append(self,data):
        new_node = Node(data)
        #base case
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node


        #add Node to the beginning
        #do the shifting
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_after(self, node, data):
        new_node = Node(data)
    #base case
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = node.next
            node.next = new_node

    #link then node
    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        prev = None
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def delete_at_position(self, position):
        if position < 1:
            return

        if position == 1:
            self.head = self.head.next
            return

        current = self.head
        previous = None
        count = 1

        while current and count < position:
            previous = current
            current = current.next
            count += 1

        if current:
            previous.next = current.next
            current.next = None


# Create the nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link the nodes together
node1.next = node2
node2.next = node3
