class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        self._insert_value(self.root, data)

    def _insert_value(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
            return node

    def search(self, data):
        return self._search_node(self.root, data)

    def _search_node(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self._search_node(node.right, data)
        return self._search_node(node.left, data)

    def print_inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data),
            self._inorder(node.right)
