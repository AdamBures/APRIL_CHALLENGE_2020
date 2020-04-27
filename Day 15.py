class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        before = [1]*len(nums)
        after = [1]*len(nums)
        product = [0]*len(nums)

        for i in range(1, len(nums)):
            before[i] = before[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            after[i] = after[i+1]*nums[i+1]

        for i in range(0, len(nums)):
            product[i] = before[i]*after[i]

        return product
