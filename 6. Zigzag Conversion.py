class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # row[0] P 
        # row[1] A
        # row[2] Y
        # row[1] P
        # row[0] A

        if len(s) == 1 or numRows >= len(s) or numRows == 1: # make sure the situation that don't need to calculate
            return s
        
        save_row = ['' for row in range(numRows)] # each row case
        row , step = 0 , 1 
        for string_id , string in enumerate(s):
            if row == 0 : 
                step = 1
            elif row == numRows-1 :
                step = -1
            
            save_row[row] += string
            row += step

        return ''.join(save_row) 

# 時間複雜度：

# 首先，在判斷 len(s) == 1 或 numRows >= len(s) 或 numRows == 1 時直接返回 s，其時間複雜度為 O(1)。

# 接下來創建了一個長度為 numRows 的列表 save_row，其時間複雜度為 O(numRows)。

# 在循環中，遍歷字符串 s，每次都執行常數時間的操作，即判斷行的變化，將字符添加到 save_row[row] 中，然後 row += step。因此，該循環的時間複雜度為 O(len(s))。

# 最後，使用 join() 函數將 save_row 中的元素結合成字符串，其時間複雜度為 O(numRows)。

# 因此，總時間複雜度為 O(len(s) * numRows)。

# 空間複雜度：

# 除了 s 字符串之外，使用了一個長度為 numRows 的列表 save_row，其空間複雜度為 O(numRows)。

# 因此，總空間複雜度為 O(numRows)。

