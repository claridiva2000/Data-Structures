import sys
sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.items = []
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def isEmpty(self):
        return self.items == []

    def enqueue(self, value):
        self.size += 1
        self.items.append(value)

    def dequeue(self):
        if len(self.items):
            return self.items.pop(0)

    def len(self):
        return len(self.items)


q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.items)
q.dequeue()
print('\n')
print(q.items) 


