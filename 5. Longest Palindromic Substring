class Solution: # (1)對稱 (2)最長 --> 對稱分兩種 奇、偶數 + 對稱在長字串中不易發生
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0 # 紀錄對稱substring位置
        for i in range(n):
            # 檢查以 i 為中心的奇數長度回文串
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > end - start:
                start, end = l + 1, r - 1
            # 檢查以 i 和 i+1 為中心的偶數長度回文串
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > end - start:
                start, end = l + 1, r - 1
        return s[start:end+1]
        
# Time complexity: $O(n^2)$  
# Space complexity: $O(1)$ 
