class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_head = self._insert_into_sorted(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _insert_into_sorted(self, sorted_head, new_node):
        if sorted_head is None or new_node.data <= sorted_head.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head

        while current.next is not None and new_node.data > current.next.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_head

    def merge_sorted_lists(self, other_list):
        self.insertion_sort()
        other_list.insertion_sort()
        dummy = Node(0)
        current = dummy

        current1 = self.head
        current2 = other_list.head

        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next

            current = current.next

        if current1 is not None:
            current.next = current1
        elif current2 is not None:
            current.next = current2

        self.head = dummy.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


list1 = LinkedList()
list1.append(4)
list1.append(1)
list1.append(7)

list2 = LinkedList()
list2.append(6)
list2.append(2)
list2.append(5)

print("\nПерший відсортований список:")
list1.insertion_sort()
list1.display()

list1.reverse()
print("\nПерший список після реверсування:")
list1.display()

print("\nДругий відсортований список:")
list2.insertion_sort()
list2.display()

list2.reverse()
print("\nДругий список після реверсування:")
list2.display()

list1.merge_sorted_lists(list2)
print("\nОб'єднаний відсортований список:")
list1.display()
