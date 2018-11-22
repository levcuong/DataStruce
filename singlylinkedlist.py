class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBegining(self, newData):
        newNode = Node(newData)

        # Update the new nodes next val to existing node
        newNode.nextval = self.headval
        self.headval = newNode
    def AtEnd(self, newData):
        newNode = Node(newData)
        if self.headval is None:
            self.headval = newNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = newNode
    def Inbetween(self, middleNode, newData):
        if middleNode is None:
            print('The mentioned node is absent')
            return
        newNode = Node(newData)
        newNode.nextval = middleNode.nextval
        middleNode.nextval = newNode
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

# Link first Node to second node
list1.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3

list1.Inbetween(list1.headval.nextval, "Wed")

list1.listprint()

