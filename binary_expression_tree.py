
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

   
    @classmethod
    def from_postfix(cls, expression):
        from stack import Stack

        if not expression or not expression.strip():
            raise ValueError("Postfix expression cannot be empty")

        stack = Stack()
        operators = {"+", "-", "*", "/"}

        for token in expression.split():
            if token in operators:
                if stack.size() < 2:
                    raise ValueError("Not enough operands")

                right_tree = stack.pop()
                left_tree = stack.pop()

                new_tree = cls()
                new_tree._root = cls._Node(token)
                new_tree._size = 1

                new_tree.attach_subtrees(left_tree, right_tree)
                stack.push(new_tree)

            else:
                try:
                    float(token)
                except ValueError:
                    raise ValueError(
                        f"Unsupported token: {token}"
                    )

                new_tree = cls()
                new_tree._root = cls._Node(token)
                new_tree._size = 1
                stack.push(new_tree)

        if stack.size() != 1:
            raise ValueError("Invalid postfix expression: extra operands")

        return stack.pop()

  
    def evaluate(self):
        if self.is_empty():
            raise ValueError("Cannot evaluate an empty tree")

        def _evaluate(p):
            if self.left(p) is None and self.right(p) is None:
                return float(p.element())

            left_value = _evaluate(self.left(p))
            right_value = _evaluate(self.right(p))
            operator = p.element()

            if operator == "+":
                return left_value + right_value
            elif operator == "-":
                return left_value - right_value
            elif operator == "*":
                return left_value * right_value
            elif operator == "/":
                if right_value == 0:
                    raise ZeroDivisionError("Division by zero")
                return left_value / right_value

            raise ValueError(f"Unknown operator: {operator}")

        return _evaluate(self.root())
      

    
    def to_infix(self):
        if self.is_empty():
            raise ValueError("Cannot format an empty tree")

        def _infix(p):
            if self.left(p) is None and self.right(p) is None:
                return p.element()

            left_expr = _infix(self.left(p))
            right_expr = _infix(self.right(p))

            return f"({left_expr} {p.element()} {right_expr})"

        return _infix(self.root())

    def to_postfix(self):
        if self.is_empty():
            raise ValueError("Cannot format an empty tree")

        def _postfix(p):
            if p is None:
                return []

            tokens = _postfix(self.left(p))
            tokens += _postfix(self.right(p))
            tokens.append(p.element())

            return tokens

        return " ".join(_postfix(self.root()))
  
     
     
    def preorder(self):
        def _walk(p):
            if p is not None:
                yield p
                yield from _walk(self.left(p))
                yield from _walk(self.right(p))

        yield from _walk(self.root())

    def inorder(self):
        def _walk(p):
            if p is not None:
                yield from _walk(self.left(p))
                yield p
                yield from _walk(self.right(p))

        yield from _walk(self.root())

    def postorder(self):
        def _walk(p):
            if p is not None:
                yield from _walk(self.left(p))
                yield from _walk(self.right(p))
                yield p

        yield from _walk(self.root())

    

