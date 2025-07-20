class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListShoppingListManagerClass:
    def __init__(self):
        self.head = None

    def insert_item(self, item_name):
        # Inserts a new node at the front (head) of the list
        new_node = Node(item_name)
        new_node.next = self.head
        self.head = new_node

    def print_items(self):
        # Prints the linked list in the format [ item1 item2 ... ]
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        print("[" + " ".join(items) + "]")

    def delete_item(self, item):
        current = self.head
        previous = None
        while current:
            if current.data == item:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    def get_last_item(self):
        # returns the last item name from the linked list.
        current = self.head
        if not current:
            return None
        while current.next:
            current = current.next
        return current.data

    def find_smallest(self):
        # returns the smallest item from linked list. (ex. [ apple banana cheese] -> apple is smallest)
        if not self.head:
            return None  # List is empty
        current = self.head
        smallest = current
        while current:
            if current.data < smallest.data:
                smallest = current
            current = current.next
        return smallest.data  # return the data (string) instead of the node
