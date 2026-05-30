# Problem: Minimum jumps
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/minimum-jumps/1
# Time Complexity: O(n) - as we go through all the elements of array.
# Space Complexity: O(1) as we are only using pointers
# Approach: We use a greedy appraoch and keep a track of furthert index we can jump. everytime we reach the end of current jump we increment jump and we increase end to the furthest jump.
# This is similar to leetcode question but with exception that its not possible to reach the last index. In this case we introduce a check that if i == end meaning we reached the end of current jump 
# and if farthest is also equal to i meaning we cannot jump further then we break the loop and return -1 as its not possible to reach the last index.


class Solution:
    def minJumps(self, arr):
        # code here
        jumps = 0
        farthest = 0
        end = 0
        notPossible = False
        for i in range(len(arr)-1):
            farthest = max(farthest,i+arr[i])
            

            
            if i == end:
                if farthest == i:
                    notPossible = True
                    break
                jumps+=1
                end = farthest
       
            
        if notPossible:
            return -1
       
        return jumps