class SinglyLinkedList:
    class Node:
        def __init__(self, val, nxt=None):
            self.val = val
            self.next = nxt
                 
    def __init__(self, seed):
        if isinstance(seed, int):
            self.root = self.Node(seed)
        elif isinstance(seed, self.Node):
            self.root = seed
        else:
            self.root = self.Node(None)
        self.last = self.root
 
    def append(self, val):
        dummy = self.root
        while dummy.next:
            dummy = dummy.next
        dummy.next = self.Node(val)

    def insert(self, index, val):
        dummyHead = self.Node(0, self.root)
        dummy = dummyHead
        while index > 0:
            index -= 1
            dummy = dummy.next
        tmp = dummy.next
        dummy.next = self.Node(val, tmp) 
        self.root = dummyHead.next

    def slice(self, index):
        dummyHead = self.Node(0, self.root)
        dummy = dummyHead
        while index > 0:
            index -= 1
            dummy = dummy.next
        tmp = dummy.next
        dummy.next = None
        secondHalf = SinglyLinkedList(tmp)
        return(SinglyLinkedList(dummyHead.next), secondHalf)

    def toList(self):
        lst = []
        dummy = self.root
        while dummy:
            lst.append(dummy.val)
            dummy = dummy.next
        return lst


def main():
    sl1 = SinglyLinkedList(3)
    sl1.append(4)
    sl1.append(5)
    sl1.append(7)
    sl1.insert(0, 66)
    print(sl1.toList())
    sl2, sl3 = sl1.slice(2)
    print(sl2.toList())
    print(sl3.toList())


if __name__ == '__main__':
    main()
