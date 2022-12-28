class Solution:
    def halveArray(self, nums: List[int]) -> int:
        q, s, k, i = [], sum(nums), 0, 0
        for x in nums:
            
            heappush(q, -x)
        while s - k > s / 2:
            x = -heappop(q)
            k += x / 2
            heappush(q, -x / 2)
            i += 1
        return i
        