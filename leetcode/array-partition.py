# https://leetcode.com/problems/array-partition

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        answer = 0
        for i in range(0, len(nums), 2):
            answer += nums[i]

        return answer