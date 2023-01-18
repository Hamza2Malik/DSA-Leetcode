class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmin, currmax = 0, 0
        globmin, globmax = nums[0], nums[0]
        total  = 0
        
        for n in nums:
            currmax = max(currmax+n, n)
            currmin = min(currmin+n, n)
            globmin = min(globmin, currmin)
            globmax = max(globmax, currmax)
            total += n
            
        return max(globmax, total - globmin) if globmax > 0 else globmax
            