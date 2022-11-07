class BinarySearchTree:
    
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value
            
    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = self.insert_helper(self.root, x)
    
    def insert_helper(self,curr, x):
        if curr == None:
            return self.Node(x)
        elif x < curr.value:
            curr.left = self.insert_helper(curr.left,x)
        else:
            curr.right = self.insert_helper(curr.right, x)

        return curr

    def get_total_height(self,curr):
        if curr == None:
            return 0
        else:
            total = self.get_total_height_helper(curr)+ self.get_total_height(curr.left) + self.get_total_height(curr.right)
            return total

        
    def get_total_height_helper(self,curr):
        if curr == None:
            return -1

        else:
            #run once for every node in the tree -> complexity = O(n)
            right_height = self.get_total_height_helper(curr.right)
            left_height = self.get_total_height_helper(curr.left)

            greater_height = max(right_height, left_height)
            total_height = greater_height + 1
 
            return total_height
    
    def get_weight_balance_factor(self):
        balance_list = []
        self.get_weight_balance_factor_helper(self.root, balance_list)
     
        #Find the greatest value in the list 
        return max(balance_list)-1


    def get_weight_balance_factor_helper(self, curr, balance_list):
        #start at the bottom
        if curr == None:
            return 0

        else:
            left_side = self.get_weight_balance_factor_helper(curr.left, balance_list)
            right_side = self.get_weight_balance_factor_helper(curr.right, balance_list)

            #Find the absolute difference
            difference = abs(left_side - right_side) + 1
            #Add the difference to a list
            balance_list.append(difference)
            return difference

    def serialize(self):
        data = []
        file = open("binaryTree.txt", 'w')
        self.serialize_helper(self.root, data)
        
        #write the data to the file
        s = ""
        #the data will become a string
        for x in data:
            s += str(x)+" "
        file.write(s)
        file.close()

    
    def serialize_helper(self,root, data):
        if root == None:
            #When the parent does not have a child, add '#'
            data.append("#")
        else:
            data.append(root.value)
            #the left subtree of the node
            self.serialize_helper(root.left, data)
            #the right subtree of  the node
            self.serialize_helper(root.right, data)
    

    def deserialization(self):
        data = []
        file = open("binaryTree.txt", 'r')
        #Read the whole file into a list
        data = file.readlines() 
        
        #Sperate each element with a comma
        data = data[0].split()

        self.root = self.deserialization_helper(data)
        file.close()
    
    def deserialization_helper(self, data):
        #reconstruct the tree
        if len(data) == 0:
            return None

        #Prints the data starting at the first element
        x = data.pop(0)
        
        if x == "#":
            return None
        
        curr= self.Node(int(x))
        curr.left = self.deserialization_helper(data)
        curr.right = self.deserialization_helper(data)
        return curr

            
    #Print the tree
    def print_tree(self):
        self.print_tree_helper(self.root,0)

    def print_tree_helper(self, curr, ident):
        if curr != None:
            self.print_tree_helper(curr.right, ident+1)
            print("   " * ident, end='')
            print(curr.value)
            self.print_tree_helper(curr.left, ident+1)
        
        
#testing
def main():
    print("Binary Search Tree:")
    tree = BinarySearchTree()
    tree.insert(6)
    tree.insert(4)
    tree.insert(9)
    tree.insert(5)
    tree.insert(8)
    tree.insert(7)

    print("Total height: ", tree.get_total_height(tree.root))  
    print("Balance factor: ", tree.get_weight_balance_factor())
    
    tree.serialize()
 
    tree.deserialization()
    print(tree.print_tree())
main()
                
