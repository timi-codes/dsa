class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        O(n)
        """
        current = self.head
        count = 0

        while current:
            count +=1
            current = current.next_node
        
        return count

    def add(self, data):
        """
        O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            elif current.next_node is None:
                return None
            else:
                current = current.next_node

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) but finding the node at the insertion point takes O(n) time

        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -=1

            prev_node = current
            next_node = current.next_node
            new.next_node = next_node
            prev_node.next_node = new

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the Node or None  if the key doesn't exist
        Takes 0(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

    def removeAt(self, index):
        current = self.head
        previous = None
        found = False
        position = 0

        while current and not found:
            previous = current
            current = current.next_node

        
        
    def nodeAtIndex(self, index):
        current = self.head
        position = 0

        if index == 0:
            return current

        while position < index:
            current = current.next_node
            position += 1

        return current

    def __repr__(self):
        """
        Return a string representation of the list
        Tkes O(n) time
        """
        nodes = []
        current = self.head

        while(current):
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)