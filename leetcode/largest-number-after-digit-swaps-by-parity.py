# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity

class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """

        is_evens, odds, evens = [], [], []
        while num:
            num, digit = divmod(num, 10)
            if digit % 2 == 0:
                is_evens.append(True)
                evens.append(digit)
            else:
                is_evens.append(False)
                odds.append(digit)

        odds.sort()
        evens.sort()

        answer = 0
        for i, is_even in enumerate(is_evens):
            if is_even:
                digit = evens.pop(0)
            else:
                digit = odds.pop(0)
            answer += digit * 10 ** i

        return answer