class AVLTreeMap(object):

    def __init__(self):
        self.root = None
        
    #nested node class
    class AVLNode(object):
        def __init__(self,key, value):
            self.key = key  #look up
            self.value = value  #value
            self.left = None
            self.right = None
            self.height = 0


    def get(self, key):
        #returns the values if the given key exists in the AVL tree
        #if key in AVL, return value

        #The key is not in the tree
        if self.isEmpty():
            return None
        #The value is in the tree
        else:
            return self.value

    def put(self, key, value):
        self.root = self.put_helper(self.root, key, value)
        
    def put_helper(self, curr, key, value):
        #insert a key-value pair
        #Perform the steps from Binary Search Tree
        if curr == None:
            return self.AVLNode(key,value)
        elif key < curr.key:
            curr.left = self.put_helper(curr.left,key,value)
        else:
            curr.right = self.put_helper(curr.right, key,value)

        #Update the height of the ancestor node
        curr.height = 1 + max(self.getHeight(curr.left), self.getHeight(curr.right))
        
        #Balance Factor
        balance = self.balanceFactor(curr)

        #Check if the nodes are unbalanced
        #Case 1- Left Left
        if balance < -1 and key < curr.left.key:
            return self.right_rotation(curr) #the first node

        #Case 2- Right Right
        elif balance > 1 and key > curr.right.key:
            return self.left_rotation(curr)

        #Case 3 - Left Right
        elif balance < -1 and key > curr.left.key:
            curr.left = self.left_rotation(curr.left) #change this
            return self.right_rotation(curr)

        #Case 4- Right Left
        elif balance > 1 and key < curr.right.key:
            curr.right = self.right_rotation(curr.right)  #change this
            return self.left_rotation(curr)
        
        return curr

    def right_rotation(self, value):
        node = value.left
        other = node.right

        #rotation
        node.right = value
        value.left = other

        #update heights
        value.height = 1 + max(self.getHeight(value.left), self.getHeight(value.right))
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        return node


    def left_rotation(self, node):
        value = node.right
        other = value.left

        #rotation
        value.left = node
        node.right = other

        #update heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        value.height = 1 + max(self.getHeight(value.left), self.getHeight(value.right))

        return value

    def getHeight(self, curr):
        if curr == None:
            return 0

        else:
            #run once for every node in the tree -> complexity = O(n)
            right_height = self.getHeight(curr.right)
            left_height = self.getHeight(curr.left)


            greater_height = max(right_height, left_height)
            height = greater_height + 1

            return height

    def balanceFactor(self, curr):
        if curr == None:
            return 0
        else:
            #balance factor
            balance = self.getHeight(curr.right) - self.getHeight(curr.left)
            return balance
            
    def isEmpty(self):
        if self.key == None:
            return 0

    #Print the tree     
    def print_tree(self):
        self.print_tree_helper(self.root,0)

    def print_tree_helper(self, curr, ident):
        if curr != None:
            self.print_tree_helper(curr.right, ident+1)
            print("   " * ident, end='')
            print(curr.key, ":",curr.value)
            self.print_tree_helper(curr.left, ident+1)
        
        
#testing
def main():
    print("AVL Tree: ")
    tree = AVLTreeMap()
    tree.put(15, "bob")
    tree.put(20, "anna")
    tree.put(24, "tom")
    tree.put(10, "david")
    tree.put(13, "david")
    tree.put(7, "ben")
    tree.put(30, "karen")
    tree.put(36, "erin")
    tree.put(25, "david")
    
    print(tree.print_tree())
main()
            
                
                
            
