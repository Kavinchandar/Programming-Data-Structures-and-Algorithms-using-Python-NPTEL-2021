
class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None

    def isempty(self):
        return self.data == None

    def append(self, x):
        if self.isempty():
            self.data = x
        elif self.next == None:
            newnode = Node(x)
            self.next = newnode
        else:
            self.next.append(x)
        return

    def insert(self, x):
        if self.isempty():
            self.data = x
        else:
            newnode = Node(x)
            self.data, newnode.data = newnode.data, self.data
            self.next, newnode.next = newnode, self.next
        return

    def delete(self, x):
        if self.isempty():
            return
        if self.data == x:
            self.data = None
            if self.next != None:
                self.data = self.next.data
                self.next = self.next.next
        else:
            self.next.delete(x)
            if self.next.data == None:
                self.next = None
        return

    def __str__(self):
        lst = []
        if self.data == None:
            return str(lst)
        temp = self
        lst.append(temp.data)
        while temp.next != None:
            temp = temp.next
            lst.append(temp.data)
        return str(lst)


d = Node()
for i in range(1, 10):
    d.append(i)
d.insert(12)
d.delete(4)
d.delete(12)
d.delete(9)
print(d)
