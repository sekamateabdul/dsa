class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print("\n>>>>Node inserted:", data)

    def delete(self, data):
        if self.head is None:
            print("\n>>>>Linked list is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            print("\n>>>>Node deleted:", data)
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:1
            current.next = current.next.next
            print("\n>>>>Node deleted:", data)
            return
        current = current.next

        # If the desired data was not found in the linked list
        print("\n>>>>Node not found:", data)

    def display(self):
        if self.head is None:
            print("\n>>>>Linked list is empty.")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = LinkedList()

while True:
    print("\n1. Insert a node")
    print("2. Delete a node")
    print("3. Display the linked list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter the data to be inserted: ")
        linked_list.insert(data)
    elif choice == "2":
        data = input("Enter the data to be deleted: ")
        linked_list.delete(data)
    elif choice == "3":
        linked_list.display()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("\nInvalid choice. Please try again.")
