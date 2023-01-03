#################### Approach 1 #######################

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    ans+=1
                    break
        return ans

#################### Approach 2 #####################

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))

""" str = ["cba", "daf", "ghi"]

for col in zip(*str) = unzip (c,d,g) (b,a,h) (a,f,i)
list(col) == [c,d,g] [b,a,h] [a,f,i]
 similary by sorting we can find unsorted col 


"""