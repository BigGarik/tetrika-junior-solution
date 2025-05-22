import unittest
from solution import strict


class TestStrictDecorator(unittest.TestCase):

    def test_correct_types(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(10, 20), 30)

    def test_wrong_types(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

        with self.assertRaises(TypeError):
            sum_two(1.5, 2)

    def test_string_function(self):
        @strict
        def greet(name: str) -> str:
            return f"Hello, {name}!"

        self.assertEqual(greet("Alice"), "Hello, Alice!")

        with self.assertRaises(TypeError):
            greet(123)

    def test_mixed_types(self):
        @strict
        def test_func(a: int, b: str, c: bool) -> str:
            return f"{a}-{b}-{c}"

        self.assertEqual(test_func(1, "hello", True), "1-hello-True")

        with self.assertRaises(TypeError):
            test_func("1", "hello", True)

        with self.assertRaises(TypeError):
            test_func(1, 123, True)


if __name__ == "__main__":
    unittest.main()