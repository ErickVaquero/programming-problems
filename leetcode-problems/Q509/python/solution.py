class Solution:
    def fib(self, n: int) -> int:
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        else:
            fib = 0
            first = 0
            second = 1
            for x in range(n-1):
                fib = first + second
                first = second
                second = fib
            return fib


    def fib_r(self, n: int) -> int:
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        else:
            return self._fib_(0, 1, n-2)


    def _fib_(self, first, second, n):
        if (n == 0):
            return first + second
        return self._fib_(second, first + second, n-1)

