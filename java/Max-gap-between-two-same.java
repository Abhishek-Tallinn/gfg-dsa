/* 
# Problem: Max gap between two same
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/problems/maximum-number-of-characters-between-any-two-same-character4552/1
# Time Complexity: O(n) - as we iterate on the string
# Space Complexity: O(n) as we make a dictionary
# Approach: We simple iterate on the dictionary and add the previous index in it and if the 
# character exists in dictionary we calculate the characters between them.
*/

import java.util.HashMap;

class Solution {
    public int maxCharGap(String s) {
        // code here
        HashMap<Character, Integer> d = new HashMap<>();
        int mx_d = -1;
        for (int i=0;i<s.length();i++){
            if (d.containsKey(s.charAt(i))){
                mx_d = Math.max(mx_d,i-d.get(s.charAt(i))-1);
            }
            else{
                d.put(s.charAt(i),i);
            }
        }
        return mx_d;
    }
};