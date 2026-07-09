# Problem: Ways to represent a number as sum of consecutives
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/ways-to-represent-a-number-as-sum-of-consecutives/1
# Time Complexity: O(n//2) as we loop through i values
# Space Complexity: O(1)
# Approach: We understand that only the odd factors of n matters in adding up to n as consecutives and hence we only have to count odd factors.
# but since we have to find pairs we return count of factors-1.
 
class Solution:
    def getCount(self, n):
        # code here 
        
        count = 0
        i = 1
        while i*i<=n:
            if n%i == 0:
                j = n//i
                if i%2==1:
                    count+=1
                if j!=i and j%2==1:
                    count+=1
            i+=1
        return count-1