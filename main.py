class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()

    def insert_at_begining(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.traversal()
        return

    def insert_at_index(self, data, index):
        if self.search(index) == None:
            print("Invalid Index")
            return
        node = Node(data)
        ptr1 = self.head
        ptr2 = self.head   
        for i in range(index+1):
            ptr1 = ptr1.next
        for i in range(index):
            ptr2 = ptr2.next 
        ptr2.next = node
        node.next = ptr1
        self.traversal()
        return

    def insert_at_end(self, data):
        node = Node(data)
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = node
        self.traversal()
        return
    
    def remove(self,index):
        if self.search(index) == None:
            print("Invalid Index")
            return
        curr_node = self.head
        prev_node = self.head
        for i in range(index+1):
            prev_node = curr_node
            curr_node = curr_node.next       
        print(f"{curr_node.data} has been removed")
        curr_node = curr_node.next
        prev_node.next = curr_node
        self.traversal()
        return

    def traversal(self):
        arr = []
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
            arr.append(ptr.data)
        print(arr)
        return

    def length(self):
        ptr = self.head
        count = 0
        while ptr.next != None:
            count += 1
            ptr = ptr.next
        return count

    def search(self, index):
        if index > self.length():
            print("Invalid Index")
            return None
        ptr = self.head
        counter = -1
        while counter != index:
            ptr = ptr.next
            counter += 1
        return ptr.data

    def clear(self):
        self.head.next = None
        self.traversal()
        return

if __name__ == "__main__":

    ll = LinkedList()

    while True:
        try:
            choice = int(input("""
***************************************************
1. Print all the Elements
2. Display an Element
3. View the Number of Elements
4. Insert at the Begining
5. Insert at the End
6. Insert at a Specific Index
7. Clear/Reset
0. Exit
***************************************************
: """))
        except:
            print("Invalid Input")
            break
        print("***************************************************")
        if choice == 1:
            ll.traversal()
        elif choice == 2:
            ll.search(int(input("Enter The Index Of Element To Display : ")))
        elif choice == 3:
            print(ll.length())
        elif choice == 4:
            ll.insert_at_begining(input("Enter The Value Of Element To Insert : "))
        elif choice == 5:
            ll.insert_at_end(input("Enter The Value Of Element To Insert : "))
        elif choice == 6:
            ll.insert_at_index(input("Enter The Value Of Element To Insert : "),int(input("Enter The Index Of Element To Insert : ")))
        elif choice == 7:
            ll.clear()
        else:
            break
