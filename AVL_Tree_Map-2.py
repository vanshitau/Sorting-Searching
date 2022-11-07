class AVLTreeMap(object):

    def __init__(self):
        self.root = None
    
    #nested node class
    class AVLNode(object):
        def __init__(self,key,value):
            self.key = key  #look up
            self.left = None
            self.right = None
            self.height = 0
            self.index_list = [value]


    def get(self, key):
        #returns the values if the given key exists in the AVL tree
        #if key in AVL, return value

        #The key is not in the tree
        if self.isEmpty():
            return None
        #The value is in the tree
        else:
            node = self.get_helper(self.root, key)
            return node

    def get_helper(self, curr, key):
        if curr == None:
            return None
      
        if key < curr.key:
            return self.get_helper(curr.left,key)
        elif key > curr.key:
            return self.get_helper(curr.right, key)
        else:
           
            return curr
            

    def put(self, key, value):
        self.root = self.put_helper(self.root, key, value)
        
    def put_helper(self, curr, key, value):
        #insert a key-value pair
        #Perform the steps from Binary Search Tree
        if curr == None:
            return self.AVLNode(key,value)

        elif key < curr.key:
            curr.left = self.put_helper(curr.left,key,value)
        elif key > curr.key:
            curr.right = self.put_helper(curr.right, key,value)
        else:
            curr.index_list.append(value)
            
        
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
        if self.root == None:
            return True
        else:
            return False

    #Print the tree     
    def print_tree(self):
        self.print_tree_helper(self.root,0)

    def print_tree_helper(self, curr, ident):
        if curr != None:
            self.print_tree_helper(curr.right, ident+1)
            print("   " * ident, end='')
            print(curr.key, ":",curr.index_list)
            self.print_tree_helper(curr.left, ident+1)
    

#1.1
class WebPageIndex:
    def __init__(self, file):
        #the code for AVL tree was used from the last assignment
        self.avl = AVLTreeMap()
        file = open(file, 'r') #open the file in read mode
        data = file.read()
        index = 0
        #convert all the elements of the file into lower case
        data = data.lower()
        
        for word in data.split():
            self.avl.put(word,index)
            index+=1
        self.avl.print_tree()

    def getCount(self, s):
        node = self.avl.get(s) #get all the indexes of the word--> get returns a list
        if node == None:
            return 0
        else:
            count = len(node.index_list)
            return count

#1.2
class WebpagePriorityQueue:
    #initialization function that takes string and webpage index as an input
    def __init__(self, query, index_list):
        #create a maxheap where each node in the max heap represents a webpage index instance
        self.query = query
        self.index_list = index_list
        self.data_queue = []
        self.size = 0

    
        #priority of a WebpageIndex
        for index in self.index_list:
            priority = 0
            #the word in the query that we need to count in the file
            for word in self.query.split():
                word = word.strip()
                priority += index.getCount(word)

            self.insert(index,priority)    
            self.printQueue()
            #call the get count function to get the number of times the query appears in the list
            
    def insert(self, index, priority):
        
        #takes all the elements and inserts it to a heap
        self.data_queue.append((index, priority))
        count = self.size
        while count > 0:
            if self.data_queue[-1][1] > self.data_queue[(len(self.data_queue)-1-1)//2][1]:
                #swap
                self.data_queue[-1], self.data_queue[(len(self.data_queue)-1-1)//2] = self.data_queue[(len(self.data_queue)-1-1)//2], self.data_queue[-1]
            else:
                #when at proper place or top of the array
                break
            count-=count
        self.size+=1
        

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def peek(self):
        if isEmpty():
            return 0 
        else: #first element in the queue
            return self.data_queue[0] 
        
    def poll(self):
        #take the heap in as a parameter
        if len(self.data_queue) == 0:
            return False
        elif len(self.data_queue) == 1:
            #delete that value and return it
            element = self.data_queue.pop()
            self.size-=1
            return element
        else:
            #copy the value from the right-most, bottom-most node to the root node
            self.data_queue[0] = self.data_queue[-1]
            #delete the right most node in the bottom most row
            right_node = self.data_queue.remove(self.data_queue[-1])
            self.size-=1
            #if left child > parent or right child > parent --> swap
            for i in range(self.size - 1):
                if (2*i + 1) < self.size and self.data_queue[i][1] < self.data_queue[2*i + 1][1]:
                    #swap
                    self.data_queue[i], self.data_queue[2*i + 1] = self.data_queue[2*i + 1], self.data_queue[i]
               
                elif (2*i + 2) < self.size and self.data_queue[i][1] < self.data_queue[2*i + 2][1]:
                    #swap
                    self.data_queue[i], self.data_queue[2*i + 2] = self.data_queue[2*i + 2], self.data_queue[i]
                    
        return self.data_queue[0]
    
    def reheap(self, query):
        #priority of a WebpageIndex
        for index in self.index_list:
            priority = 0
            #the word in the query that we need to count in the file
            for word in self.query.split():
                word = word.strip()
                priority += index.getCount(word)

            self.insert(index,priority)    
            self.printQueue()
                
    def printQueue(self):
        for i in range(self.size):
            print(i,self.data_queue[i][1])
        
#testing
def main():
    wpi = WebPageIndex("doc1-arraylist.txt")
    file = open("doc1-arraylist.txt", 'r')
    data = file.read()
    print(data)
    index = 0
    #converts it to lowercase
    data = data.lower()

    #test with 3 files
    wpi2 = WebPageIndex("doc2-graph.txt")
    wpi3 = WebPageIndex("doc3-binarysearchtree.txt")
    
    #priority queue
    wpq = WebpagePriorityQueue("are and", [wpi, wpi2, wpi3])
    
    #test the poll function
    while not wpq.isEmpty():
        t = wpq.poll()
            
    

main()
    
        
