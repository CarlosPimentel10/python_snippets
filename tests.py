import unittest
from quicksort import quicksort


class TestQuickSort(unittest.TestCase):

    def test_sorted_array(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]),[1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
