class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        # 1: find the minimum and extract offset
        L = len(nums)
        lo, hi = 0, L-1
        while lo < hi:
            mid = (lo+hi) // 2
            if nums[hi] < nums[mid]:
                lo = mid+1
            else:
                hi = mid
        offset = lo

        # 2: do a normal bisection search with offset indices
        lo, hi = 0 + offset, L-1 + offset
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid % L] < target:
                lo = mid+1
            else:
                hi = mid
        
        return lo % L if nums[lo % L] == target else -1
