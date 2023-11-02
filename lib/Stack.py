class Stack:
    
    def __init__(self, items = [], limit = 100):
        if len(items) <= limit:
            self.items = items
            self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop(len(self.items)-1)

    def peek(self):
        index = len(self.items) - 1
        return self.items[index]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) < self.limit:
            return False
        else:
            return True

    def search(self, target):
        if target in self.items:
            index = self.items.index(target)
            return (len(self.items)-1 ) - index
        else:
            return -1
