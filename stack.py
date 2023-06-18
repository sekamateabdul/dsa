class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("\n>>>>Node pushed:", data)

    def pop(self):
        if self.top is None:
            print("\n>>>>Stack is empty.")
            return

        data = self.top.data
        self.top = self.top.next
        print("\n>>>>Node popped:", data)

    def display(self):
        if self.top is None:
            print("\n>>>>Stack is empty.")
            return

        current = self.top
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
stack = Stack()

while True:
    print("\n1. Push a node")
    print("2. Pop a node")
    print("3. Display the stack")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter the data to be pushed: ")
        stack.push(data)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        stack.display()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("\nInvalid choice. Please try again.")
