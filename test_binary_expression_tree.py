
import unittest
from binary_expression_tree import BinaryExpressionTree


class TestBinaryExpressionTree(unittest.TestCase):

    def test_addition(self):
        tree = BinaryExpressionTree.from_postfix("5 3 +")
        self.assertEqual(tree.evaluate(), 8.0)

    def test_mixed_operations(self):
        tree = BinaryExpressionTree.from_postfix("5 3 8 * +")
        self.assertEqual(tree.to_infix(), "(5 + (3 * 8))")
        self.assertAlmostEqual(tree.evaluate(), 29.0)

    def test_operand_order(self):
        tree = BinaryExpressionTree.from_postfix("8 2 / 3 -")
        self.assertAlmostEqual(tree.evaluate(), 1.0)

    def test_negative_decimal(self):
        tree = BinaryExpressionTree.from_postfix("-4 2.5 *")
        self.assertAlmostEqual(tree.evaluate(), -10.0)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree.from_postfix("5 +")

    def test_extra_operands(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree.from_postfix("2 3 4 +")

    def test_division_by_zero(self):
        tree = BinaryExpressionTree.from_postfix("7 0 /")
        with self.assertRaises(ZeroDivisionError):
            tree.evaluate()

    def test_postfix_output(self):
        expression = "5 3 8 * +"
        tree = BinaryExpressionTree.from_postfix(expression)
        self.assertEqual(tree.to_postfix(), expression)

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree.from_postfix("")

    def test_unsupported_token(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree.from_postfix("5 abc +")


if __name__ == "__main__":
    unittest.main()
