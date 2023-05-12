class Solution:
    def reverse(self, x: int) -> int:

        # save numbers type
        positive_and_negative_numbers = 1
        if x < 0 :
            positive_and_negative_numbers = -1

        # reverse 
        new_x = int(str(int(x*positive_and_negative_numbers))[::-1])

        if new_x > 2**31 :
            return 0
        else:
            return positive_and_negative_numbers*new_x

#時間複雜度：該函數中的操作基本上都與x的位數成比例，而不是與x本身成比例。因此，其時間複雜度為O(log(x))，其中x為輸入整數。
#空間複雜度：該函數使用了固定數量的變量（positive_and_negative_numbers, new_x）和常量數量的其他變量（字串）來存儲輸入和輸出。因此，其空間複雜度為O(1)。
