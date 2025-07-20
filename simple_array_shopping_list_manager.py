class SimpleArrayShoppingListManagerClass:
    def __init__(self): #  initializes simple array to be used throughout object life.
        # Initializes an empty list (array) to hold shopping items
        self.items = []

    def insert_item(self, item):
        # inserts item at the front of the array.
        self.items.insert(0, item)

    def print_items(self):
        # Prints items in the array as a space-separated list inside brackets
        print("[", end=" ")
        for item in self.items:
            print("'" + item + "'",  end=" ")
        print("]")

    def delete_item(self, item):
        # Deletes item using index() and pop(). Avoids using remove() as instructed.
        try:
            index = self.items.index(item)
            self.items.pop(index)
        except ValueError:
            pass  # Item not found, do nothing

    def get_last_item(self):
        # Returns the last item in the array
        if self.items:
            return self.items[-1]
        return None

    def selection_sort(self):
        # Implements selection sort to sort the items alphabetically
        for i in range(len(self.items)):
            smallest_index = i
            for j in range(i + 1, len(self.items)):
                if self.items[j] < self.items[smallest_index]:
                    smallest_index = j
            self.items[i], self.items[smallest_index] = self.items[smallest_index], self.items[i]
