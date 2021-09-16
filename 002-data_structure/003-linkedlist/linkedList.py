class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def printList(self):
        head = self.head
        while(head):
            print(head.data, end=' ')
            head = head.next
        print()
    
    @staticmethod
    def get(head, val):
        """
        Returns the position of the value 'val', if not present
        return -1
        """
        if not head:
            return -1
        if head.data == val:
            return 1
        else:
            res = LinkedList.get(head.next, val)
            if res < 0:
                return -1
            else:
                return res + 1


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(10)
    second = Node(20)
    third = Node(30)

    linked_list.head.next = second
    second.next = third
    # linked_list.printList()
    pos = LinkedList.get(linked_list.head, 100)
    print("Position: ", pos)
