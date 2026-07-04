# Problem: Indexes of subarray with given sum
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/indexes-of-subarray-with-given-sum/1
# Time Complexity: O(n) - as we calculate prefix sum and then we go through the prefix sum array once to find the subarray with given sum.
# Space Complexity: O(n) as we are using a dictionary to store the prefix sum and its index.
# Approach: We go through the prefix sum array and if we find the target directly we return [1,idx+1] as that means that subarray has been formed from the first element
# If we dont find the target directly then that means that we check for current prefix value - target to be present in the dictionary. if it is we return dictionary key value +2 as subarray with 
# start from next value and also we have to return it 1-indexed as stated in the question and idx+1


#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        if target < min(arr):
            return [-1]
        prefix = [arr[0]]
        for num in arr[1:]:
            prefix.append(prefix[-1]+num)
        #print(prefix)
        m = {}
        for idx,num in enumerate(prefix):
            if num == target:
                return [1,idx+1]
            elif (prefix[idx] - target) in m:
                return [m[prefix[idx]-target]+2,idx+1]
            m[num] = idx
            #print(m)
        return [-1]
        