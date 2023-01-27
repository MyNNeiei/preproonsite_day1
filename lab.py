"""munn pai mud leaw"""
class DataNode:
    def __init__(self, input_name = ""):
        self.name = input_name
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
        else:
            pos = self.head
            while pos is not None:
                print('->', pos.name , end=" ")
                pos = pos.next
            print("")
    def insertFornt(self, data):
        pNew = DataNode(data)
        if self.head is None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1
        return
    def insertLast(self, data):
        pNew = DataNode(data)
        if self.head == pNew:
            print("This is an empty list.")
        else:
            pos = self.head
            while pos is not None:
                print('->', pos.name , end=" ")
                pos = pos.next
            print("")
mylist = SinglyLinkedList()
pNew = DataNode("John")
mylist.head = pNew
print(mylist.head.name)
pNew = DataNode("Tony")
mylist.head.next = pNew
print(mylist.head.next.name)
mylist.traverse()
pNew = DataNode("Bill")


