
class BinaryExpressionTree:
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position:
        def __init__(self, tree, node):
            self._tree = tree
            self._node = node

        def element(self):
            return self._node.element

    def __init__(self):
        self._root = None
        self._size = 0

        
    def _make_position(self, node):
        if node is None:
            return None
        return self.Position(self, node)

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        return self._make_position(p._node.parent)

    def left(self, p):
        return self._make_position(p._node.left)

    def right(self, p):
        return self._make_position(p._node.right)

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    
    def attach_subtrees(self, left_tree, right_tree):
        if not self._root:
            raise ValueError("The parent tree must have a root")

        if self._root.left is not None or self._root.right is not None:
            raise ValueError("The root already has children")

        if left_tree is self or right_tree is self or left_tree is right_tree:
            raise ValueError("Trees must be separate")

        if left_tree.is_empty() or right_tree.is_empty():
            raise ValueError("Cannot attach empty subtrees")

        self._root.left = left_tree._root
        self._root.right = right_tree._root

        left_tree._root.parent = self._root
        right_tree._root.parent = self._root

        self._size += len(left_tree) + len(right_tree)

        left_tree._root = None
        left_tree._size = 0
        right_tree._root = None
        right_tree._size = 0
    

