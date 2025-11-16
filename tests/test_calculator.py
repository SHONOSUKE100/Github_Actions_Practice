import math
import unittest

from calculator import average


class TestAverage(unittest.TestCase):
    def test_average_of_positive_numbers(self) -> None:
        self.assertTrue(math.isclose(average([1, 2, 3, 4]), 2.5))

    def test_average_handles_negative_values(self) -> None:
        self.assertTrue(math.isclose(average([-2, -4, -6]), -4.0))

    def test_average_single_value_returns_same_number(self) -> None:
        self.assertTrue(math.isclose(average([42]), 42))

    def test_average_raises_error_for_empty_sequence(self) -> None:
        with self.assertRaises(ValueError):
            average([])

    def test_average_is_consistent_with_math_fsum(self) -> None:
        data = [0.1, 0.2, 0.3, 0.4]
        expected = math.fsum(data) / len(data)
        self.assertTrue(math.isclose(average(data), expected))


if __name__ == "__main__":
    unittest.main()
