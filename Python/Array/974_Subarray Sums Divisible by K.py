################# Brute Force #################

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                currSum = nums[j]  if i == 0 else nums[j] - nums[i-1]
                if(currSum % k == 0):
                    count+=1
        return count

################ Optimal Solution ################

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        mp ={}
        
        currSum = 0
        
        result = 0
        
        mp[0] = 1
        
        for i in range(len(nums)):
            currSum += nums[i]
            
            rem = currSum % k
            if(rem <0):
                rem += k
            
            
            if rem in mp:
                result += mp[rem]
            mp[rem] = 1 + mp.get(rem, 0)
            
        return result