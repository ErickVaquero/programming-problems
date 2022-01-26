import unittest
from solution import Solution
fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

class TestSum(unittest.TestCase):
    def test_iterative(self):
        print("running test_iterative")
        soln = Solution()
        for i in range(len(fib_list)):
            self.assertEqual(soln.fib(i), fib_list[i], f"f({i}) should be {fib_list[i]}")
        print("completed test_iterative\n")
    
    def test_recursive(self):
        print("running test_recursive")
        soln = Solution()
        for i in range(len(fib_list)):
            self.assertEqual(soln.fib_r(i), fib_list[i], f"f({i}) should be {fib_list[i]}")
        print("completed test_recursive")


if __name__ == '__main__':
    unittest.main()
