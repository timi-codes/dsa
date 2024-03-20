

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

    def getFullNodeCount(root):
        """
        Using level-order traversal 
        """
        if root == None: return 0

        queue = [root]
        count = 0

        while len(queue) != 0:
            current = queue.pop(0)

            if current.left and current.right:
                count +=1

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
        
        return count
    
#         2
#     /      \
#   7         5
#   \          \
#   6          9
#  / \        /
# 1  11      4
root = Node(2)

root.left = Node(7)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)

root.right = Node(5)
root.right.right = Node(9)
root.right.right.left = Node(4)

print(Node.getFullNodeCount(root))
