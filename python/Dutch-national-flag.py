# Problem: Sort and array os 0s , 1s and 2s
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
# Time Complexity: O(n) - as we go through all the elements of array.
# Space Complexity: O(1) as we are only using pointers
# Approach: We use two pointers approach and if run a main for loop. If we find a 0 we increment left pointer to a non zero position and swap the elements and then increment left pointer again to swap to next non zero element.
# Also if we find a 2 then we decrement right pointer to a non 2 position and swap the elements and then check if the current element is 0 then we swap it with left pointer and increment left pointer again to swap to next non zero element.
# Approach2: Another main appraoch is to count the number of 0s, 1s and 2s and then fill the array with the counted number of 0s, 1s and 2s. This approach also has time complexity of O(n) but space complexity of O(1) as we are using only three variables to count the number of 0s, 1s and 2s.
# Another approach is to keep three pointers low, mid and high. low and mid are initialized to 0 and high is initialized to n-1. We run a loop until mid is less than or equal to high. If the element at mid is 0 then we swap it with the element at low and increment both low and mid. 
# If the element at mid is 1 then we just increment mid. If the element at mid is 2 then we swap it with the element at high and decrement high. This approach also has time complexity of O(n) and space complexity of O(1) as we are using only three pointers.


class Solution:
    def sort012(self, arr):
        # code here
        #two pointers
        left = 0
        right = len(arr)-1
        for i in range(len(arr)):
            if arr[i]==0:
                while left < i and arr[left] == arr[i]:
                    left+=1
            
                arr[i],arr[left] = arr[left],arr[i]
                left+=1
                    
                
           
            elif arr[i] == 2:
                
                while right >i and arr[right]==arr[i]:
                    right-=1
                
                arr[i],arr[right] = arr[right],arr[i]
                if arr[i] == 0:
                    arr[i],arr[left] = arr[left],arr[i]
                    left+=1
        
        return arr