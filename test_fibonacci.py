import unittest
from fibonacci_search import fibonacci_search  # 確保你的主程式檔名為 fibonacci_search.py

class TestFibonacciSearch(unittest.TestCase):

    def setUp(self):
        """準備測試資料"""
        self.sorted_list = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

    def test_target_found(self):
        """測試：目標值存在於陣列中"""
        self.assertEqual(fibonacci_search(self.sorted_list, 85), 8)
        self.assertEqual(fibonacci_search(self.sorted_list, 10), 0)
        self.assertEqual(fibonacci_search(self.sorted_list, 100), 10)

    def test_target_not_found(self):
        """測試：目標值不存在於陣列中"""
        self.assertEqual(fibonacci_search(self.sorted_list, 55), -1)
        self.assertEqual(fibonacci_search(self.sorted_list, 5), -1)
        self.assertEqual(fibonacci_search(self.sorted_list, 105), -1)

    def test_empty_list(self):
        """測試：空陣列邊界情況"""
        self.assertEqual(fibonacci_search([], 10), -1)

    def test_single_element(self):
        """測試：單一元素陣列"""
        self.assertEqual(fibonacci_search([50], 50), 0)
        self.assertEqual(fibonacci_search([50], 20), -1)

    def test_large_list(self):
        """測試：較大型陣列的穩定性"""
        large_list = list(range(0, 10000, 2)) # 0 到 9998 的偶數
        self.assertEqual(fibonacci_search(large_list, 5000), 2500)
        self.assertEqual(fibonacci_search(large_list, 5001), -1)

if __name__ == '__main__':
    unittest.main()

