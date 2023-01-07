https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits = int(''.join(map(str, digits)))
        digits += 1
        answer = list(map(int, str(digits)))
        return answer