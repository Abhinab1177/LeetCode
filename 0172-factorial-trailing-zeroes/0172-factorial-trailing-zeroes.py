class Solution:
    def trailingZeroes(self, n: int) -> int:

        # Approach 1: Calculate factorial
        # fact = 1
        # count = 0
        #
        # for i in range(1, n + 1):
        #     fact = fact * i
        #
        # while fact % 10 == 0:
        #     count += 1
        #     fact //= 10
        #
        # return count


        # Approach 2: Optimal
        count = 0

        while n > 0:
            n //= 5
            count += n

        return count