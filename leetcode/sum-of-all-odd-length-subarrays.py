# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n = len(arr)
        answer = 0

        for i, a in enumerate(arr):
            odd_left  = i // 2 + 1
            odd_right = (n - i - 1) // 2 + 1
            even_left = (i + 1) // 2
            even_right = (n - i) // 2

            freq = (odd_left * odd_right) + (even_left * even_right)
            answer += freq * a

        return answer