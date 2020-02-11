# poop

class BinTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def printme(self):
        print "("+self.data,
        if self.left is not None:
            self.left.printme()
        else:
            print "()",
        if self.right is not None:
            self.right.printme()
        else:
            print "()",
        print ")",
    # serialize data, left to right notation, with # as None
    def serialize(self):
        if self.left is None:
            left_ser = "#"
        else:
            left_ser = self.left.serialize()

        if self.right is None:
            right_ser = "#"
        else:
            right_ser = self.right.serialize()
        return "{} {} {}".format(self.data, left_ser, right_ser)

def main():
    t = BinTree('a', BinTree('b'), BinTree('C', BinTree('D'), BinTree('E', None, BinTree('F'))))
    print t.serialize()
main()
