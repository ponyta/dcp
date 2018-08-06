class Node:
    def __init__(self, data, link=0):
        self.data = data
        self.link = link

class XORLinkedList:
    def __init__(self):
        self.head = 0
        self.tail = 0
    def add(self, element):
        if self.head == 0:
            self.head = Node(element)
            self.head.link = self.head
            self.tail = self.head
            return self
        else:
            self.tail.link = self.tail.link ^ 0


if __name__ == '__main__':
    mylist = XORLinkedList(5)
    mylist.add(4).add(3).add(2).add(1).add(0)
    print(mylist)
