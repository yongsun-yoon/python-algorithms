# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cnt = 0

        n = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        cnt += 1
        
        return cnt