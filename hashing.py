class ProductNode:
    def __init__(self, pid, pname, qty):
        self.product_id = pid
        self.name = pname
        self.quantity = qty
        self.next = None


class WareHouse:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, pid):
        return pid % self.size

    def add_product(self, pid, pname, qty):
        index = self.hash_function(pid)
        current = self.table[index]

        while current is not None:
            if current.product_id == pid:
                print(f"\nProduct ID {pid} already exists")
                return
            current = current.next

        new_node = ProductNode(pid, pname, qty)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search_product(self, pid):
        index = self.hash_function(pid)
        current = self.table[index]

        while current is not None:
            if current.product_id == pid:
                print(f"\n{index}. {current.name} with ID {current.product_id} has {current.quantity} items in stock")
                return
            current = current.next

        print("\nProduct not Found")

    def delete_product(self, pid):
        index = self.hash_function(pid)
        current = self.table[index]
        previous = None

        while current is not None:
            if current.product_id == pid:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next

                print(f"\nDeleted Product with ID {pid}.")
                return

            previous = current
            current = current.next

        print("\nProduct not Found")

    def display_table(self):
        print("\nWarehouse Hash Table Status")
        empty = True

        for index in range(self.size):
            print(f"Index {index}: ", end="")
            current = self.table[index]

            if current is None:
                print("[Empty]")
            else:
                empty = False
                result = ""

                while current is not None:
                    result += f"[ID: {current.product_id} | {current.name} | Qty: {current.quantity}] -> "
                    current = current.next

                result += "None"
                print(result)

        if empty:
            print("\nHash table is completely empty.")


if __name__ == "__main__":
    w = WareHouse(10)

    w.add_product(101, "Keyboard", 25)
    w.add_product(111, "Mouse", 40)
    w.add_product(121, "Monitor", 12)
    w.add_product(102, "USB Cable", 60)
    w.add_product(112, "Webcam", 18)
    w.add_product(131, "Headphones", 30)

    w.display_table()

    w.search_product(111)
    w.search_product(150)

    w.delete_product(111)

    w.display_table()

    w.add_product(101, "Keyboard", 25)
    w.delete_product(999)