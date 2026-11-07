
from binary_expression_tree import BinaryExpressionTree


def main():
    expressions = [
        "5 3 8 * +",
        "8 2 / 3 -",
        "10 5 +",
        "-4 2.5 *",
        "7 0 /",
        "5 +",
        "2 3 4 +"
    ]

    for expression in expressions:
        print("-" * 40)
        print("Original Postfix:", expression)

        try:
            tree = BinaryExpressionTree.from_postfix(expression)

            print("Infix:", tree.to_infix())
            print("Generated Postfix:", tree.to_postfix())
            print("Result:", tree.evaluate())

        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)

    print("-" * 40)
    print("Program finished.")


if __name__ == "__main__":
    main()
