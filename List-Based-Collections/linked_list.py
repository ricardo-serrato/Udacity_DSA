class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        count = 1
        current = self.head

        while current:
            if count == position:
                return current
            else:
                current = current.next
                count += 1
        return None

    def insert(self, new_element, position):
        current = self.head
        count = 1
        if position == 1:
            new_element.next = current
            self.head = new_element

        while current:
            if count == position-1:
                new_element.next = current.next
                current.next = new_element

            count += 1
            current = current.next

    def delete(self, value):
        """Delete the first node with a given value"""
        current = self.head

        if current.value == value:
            self.head = current.next
            return

        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

        print(f'{value} is not in the list')





    def print(self):
        lst = []
        current = self.head

        while current:
            lst.append(current.value)
            current = current.next

        print(lst)

    def length(self):
        current = self.head
        count = 0

        while current:
            current = current.next
            count += 1

        print(count)

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print(ll.head.next.next.value)
print(ll.get_position(3).value)
ll.print()
ll.insert(e4,3)
print(ll.get_position(3).value)
ll.print()




