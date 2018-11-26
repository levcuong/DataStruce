class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    # Print the linked list
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def AtBegining(self, newData):
        newNode = Node(newData)

        # Update the new nodes next val to existing node
        newNode.next = self.head
        self.head = newNode
        
    def AtEnd(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next = newNode

    def Inbetween(self, middleNode, newData):
        if middleNode is None:
            print('The mentioned node is absent.')
            return
        newNode = Node(newData)
        newNode.next = middleNode.next
        middleNode.next = newNode
    def removeNode(self, removeKey):
        
        headVal = self.head
        if(headVal is not None):
            if(headVal.data == removeKey):
                self.head = headVal.next
                headVal = None
                return
        while(headVal is not None):
            if headVal.data == removeKey:
                break
            previous = headVal
            headVal = headVal.next

        if(headVal == None):
            return
        previous.next = headVal.next

        headVal = None

list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")
e5 = Node("Tue")

# Link first Node to second node
list1.head.next = e2
# Link second Node to third node
e2.next = e3
e3.next = e4
e4.next = e5

list1.removeNode("Tue")
# list1.Inbetween(list1.head.next, "Wed")

list1.listprint()

