

class Node:
    left, right = None, None
    data = None

    def __init__(self, data) -> None:
        self.data = data

    def insert(self, value):
        if self.data <= value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def contains(self, value):
        if self.data == value:
            print("Found")
        elif self.data < value:
            if self.left:
                self.left.contains(value)
            else: 
                print("%s Not Found", value)
        else:
            if self.right:
                self.right.contains(value)
            else:
                print("%s Not Found", value)

    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()

        print(self.data)

        if self.right !=None:
            self.right.printInOrder()


            
