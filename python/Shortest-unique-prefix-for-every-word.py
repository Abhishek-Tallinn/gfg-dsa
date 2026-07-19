# Problem: Shortest unique prefix for every word
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/shortest-unique-prefix-for-every-word/minimum-jumps/1
# Time Complexity: O(nxL) - where we have n strings and L is the avg length
# Space Complexity: O(nxL)
# Approach: We make a trie and instead of trie just giving prefix added a counter to each node 
# to see how many strings pass through it. then we only take the nodes where the count is 1


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def findPrefixes(self, arr):
        # code here
        #build
        root = TrieNode()
        for word in arr:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count+=1
        ans = []
        for word in arr:
            node = root
            prefix = ""
            for ch in word:
                node = node.children[ch]
                prefix+=ch
                if node.count == 1:
                    break
            ans.append(prefix)
    
        return ans