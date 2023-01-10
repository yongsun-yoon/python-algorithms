# https://leetcode.com/problems/number-of-unequal-triplets-in-array/submissions/875078201/

from collections import Counter

class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        c = Counter(nums)
        answer = 0

        left = 0
        right = len(nums)

        for _, freq in c.items():
            right -= freq
            answer += left * freq * right
            left += freq

        return answer