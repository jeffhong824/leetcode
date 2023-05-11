class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        save_indices = {} # 用字典保存每個字符最近出現的位置
        start = 0 # 記錄當前子串的起始位置
        max_value = 0 # 記錄最長的不重複子串的長度
        for i, c in enumerate(s): # 遍歷字符串
            if c in save_indices and save_indices[c] >= start: # 如果當前字符已經在子串中出現過了
                start = save_indices[c] + 1 # 更新子串的起始位置
            save_indices[c] = i # 將這個字符的位置加入到字典中
            max_value = max(max_value, i - start + 1) # 計算當前子串的長度並更新 max_value 的值
        return max_value
        
# Time complexity: O(n) # 其中n是字符串的長度。因為在最壞情況下，我們需要遍歷一次字符串。    
# Space complexity: O(max(n,m)) # 其中m是字符集的大小。在最壞情況下，字符集的大小等於字符串的長度，此時空間複雜度為O(n)。在最好的情況下，字符集的大小是一個常數，此時空間複雜度是O(1)。    
