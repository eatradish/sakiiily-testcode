class Solution:
    def reverse_2(self, x):
        r = 0
        while(x != 0):
            if x > 0:
                r = (r * 10) + (x % 10)
            if x < 0:
                r = (r * 10) + -(-x % 10)
            x = x / 10
            r = int(r)
            x = int(x)

        if r > -2 ** 31 and r < 2 ** 31 - 1:
            return r
        else:
            return 0

print(Solution().reverse_2(-123))
