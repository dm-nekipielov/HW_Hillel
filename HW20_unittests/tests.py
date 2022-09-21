import unittest

from HW20_unittests.funcs import Fibonacci, formatted_name


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_regular_param_0(self):
        res = self.fibonacci(0)
        self.assertEqual(res, 0)

    def test_regular_param_1(self):
        res = self.fibonacci(1)
        self.assertEqual(res, 1)

    def test_regular_param_2(self):
        res = self.fibonacci(2)
        self.assertEqual(res, 1)

    def test_regular_param_10(self):
        res = self.fibonacci(10)
        self.assertEqual(res, 55)

    def test_negative_param(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)

    def test_float_param(self):
        with self.assertRaises(ValueError):
            self.fibonacci(1.5)

    def test_wrong_type_param(self):
        with self.assertRaises(ValueError):
            self.fibonacci("1")

    def test_empty_param(self):
        with self.assertRaises(TypeError):
            self.fibonacci()


class TestFormattedName(unittest.TestCase):

    def test_regular_2_param(self):
        self.assertEqual(
            formatted_name(first_name="Dmytro", last_name="Nekipielov"),
            "Dmytro Nekipielov"
        )

    def test_regular_3_param(self):
        self.assertEqual(
            formatted_name(first_name="Dmytro", last_name="Nekipielov", middle_name="Oleksandrovych"),
            "Dmytro Oleksandrovych Nekipielov"
        )

    def test_lower_uppercase_param(self):
        self.assertEqual(
            formatted_name(first_name="dmytro", last_name="NEKIPIELOV"),
            "Dmytro Nekipielov"
        )

    def test_empty_param(self):
        self.assertEqual(formatted_name(first_name="", last_name=""), " ")

    def test_wrong_type_param(self):
        with self.assertRaises(TypeError):
            formatted_name(first_name=1, last_name=2)

    def test_no_param(self):
        with self.assertRaises(TypeError):
            formatted_name()


if __name__ == '__main__':
    unittest.main()
