# Daily coding problem #208

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next is None:
            return str(self.data)
        return str(self.data) + " -> " + str(self.next)

    def last(self):
        if self.next is None:
            return self
        return self.next.last()

class LinkedList:
    def __init__(self, node=None):
        if node is None:
            self.head = None
            self.tail = None
        else:
            self.head = node
            while node.next is not None:
                node = node.next
            self.tail = node

    def __str__(self):
        return str(self.head)

    def append(self, el):
        """ Appends el to the end of the list """
        new_node = Node(el, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def push(self, el):
        """ Pushes el to the front of the list """
        if self.head is None:
            self.head = Node(el, None)
            self.tail = self.head
        else:
            new_head = Node(el, self.head)
            self.head = new_head

    def piviot(self, k):
        new_lst = LinkedList()
        itr = self.head
        while itr is not None:
            if itr.data < k:
                new_lst.push(itr.data)
            else:
                new_lst.append(itr.data)
            itr = itr.next
        return new_lst

def main():
    lst = LinkedList(Node(5, Node(1, Node(8, Node(0, Node(3, None))))))
    print(lst)
    lst = lst.piviot(3)
    print(lst)

main()
