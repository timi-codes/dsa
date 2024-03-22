

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
        Using level-order traversal method
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
    
    def getFullNodeCount_Recursive(root):
        """
        Using depth-first postorder approach
        TC: O(n)
        SC: O(n)
        """
        if root == None: 
            return 0
        
        count = 0

        if root.left and root.right:
            count += 1

        if root.left or root.right:                
            count += Node.getFullNodeCount_Recursive(root.left) + Node.getFullNodeCount_Recursive(root.right)
        
        return count
    
    def getDepthWithLevelOrder(root):
        if root == None: 
            return 0
        
        queue = [root, None]
        depth = 0

        while len(queue) > 0:
            current = queue.pop(0)

            if current == None:
                depth += 1


            if current != None:
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)   

            elif len(queue) > 0:
                queue.append(None)


            print(queue)

        return depth

    def getDepthWithRecursion(root):
        if root is None: 
            return 0
        
        left = Node.getDepthWithRecursion(root.left)
        right = Node.getDepthWithRecursion(root.right)
        
        return 1 + max(left, right)

    def inverse(self, node):
        if node is None:
            return None

        right = self.inverse(node.right)
        left = self.inverse(node.left)

        node.right = left
        node.left = right


def testData1():
    #        15
    #     /      \
    #   10       20
    #   \        /
    #   12      17
    #  /  \      \
    # 11  14     18
    #            /
    #           16
    root = Node(15)

    root.left = Node(10)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    root.right = Node(20)
    root.right.left = Node(17)
    root.right.left.right = Node(18)
    root.right.left.right.left = Node(16)

    return root

def testData2():
    #        1
    #       / \
    #      2  3
    #     /\
    #    4 5
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    return root

testDataRoot1 = testData1()
testDataRoot2 = testData2()

print(testDataRoot1.printInOrder())
testDataRoot1.inverse(testDataRoot1)
print(testDataRoot1.printInOrder())
