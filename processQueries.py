from AVL_Tree_Map-2 import WebPageIndex
from AVL_Tree_Map-2 import WebpagePriorityQueue
import os


def readFiles(folder_name):
    webpageList = []

    #look at all the files in the current directory
    for f in os.listdir(folder):
        #joins the full path
        file_name = WebPageIndex.join('data/' + f)
        webpageList.append(file_name)
        
        
    
def main():
    wpi = WebPagePriorityQueue("queries.txt")
    #open the queries file
    file = open("queries.txt", 'r')
    data = file.read()
    print(data)
    index = 0
 
    count = 0
    #call the reheap function
    for query in file:
        data.reheap(query)
        
        #look at each line of the data
        for name in WebPageIndex.data:
            while count<= 3:
                #check if the query matches the string inside the the WebPageIndex 
                if WebPageIndex.data[name] == query:
                    count+=1
                
            
        
        
   
