class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_recursive(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_recursive(data, current_node.right)

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, current_node):
        if current_node is None:
            return current_node

        if data < current_node.data:
            current_node.left = self._delete_recursive(data, current_node.left)
        elif data > current_node.data:
            current_node.right = self._delete_recursive(data, current_node.right)
        else:
            if current_node.left is None and current_node.right is None:
                current_node = None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                successor = self._find_min(current_node.right)
                current_node.data = successor.data
                current_node.right = self._delete_recursive(successor.data, current_node.right)

        return current_node

    def _find_min(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, current_node):
        if current_node is None:
            return False

        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search_recursive(data, current_node.left)
        else:
            return self._search_recursive(data, current_node.right)

    def in_order_traversal(self):
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, current_node):
        if current_node:
            self._in_order_recursive(current_node.left)
            print(current_node.data, end=" ")
            self._in_order_recursive(current_node.right)

    def pre_order_traversal(self):
        self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, current_node):
        if current_node:
            print(current_node.data, end=" ")
            self._pre_order_recursive(current_node.left)
            self._pre_order_recursive(current_node.right)

    def post_order_traversal(self):
        self._post_order_recursive(self.root)

    def _post_order_recursive(self, current_node):
        if current_node:
            self._post_order_recursive(current_node.left)
            self._post_order_recursive(current_node.right)
            print(current_node.data, end=" ")


# Usage Example
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

bst.in_order_traversal()  # Output: 20 30 40 50 60 70 80
print()

bst.delete(30)
bst.in_order_traversal()  # Output: 20 40 50 60 70 80
print()

print(bst.search(60))  # Output: True
print(bst.search(30))  # Output: False
