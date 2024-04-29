class Stack:

    def __init__(self, items=[], limit=100):
        self.limit = limit
        self.items = items

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.size() < self.limit:
            self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def peek(self):
        if self.items > 0:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        if self.size() == self.limit:
            return True
        return False

    def search(self, target):
        distance = -1
        search_items = self.items.copy()
        i = 0
        while search_items:
            if search_items.pop() == target:
                distance = i
            i += 1
        return distance

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items[: self.limit]
