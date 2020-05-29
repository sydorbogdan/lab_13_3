class LinkedBinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        self.left_child = LinkedBinaryTree(new_node)
        print(self.get_left_child().key)

    def insert_right(self, new_node):
        self.right_child = LinkedBinaryTree(new_node)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key