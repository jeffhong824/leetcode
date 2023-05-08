# Definition for singly-linked list.
# class ListNode: # 鏈表
#     def __init__(self, val=0, next=None):
#         self.val = val # 當前值
#         self.next = next # 下一結點地址

# <鏈表> Python在其標準庫中沒有鏈接列表

# ■ 定義:
# head保存首地址
# item存儲數據
# next指向下一結點地址

# ■ 優點:
# 對儲存空間的使用要相對靈活，對插入和刪除操作有優秀性能
# E.g. [1,2,3,5,6,7]，要在3和5之間插入4，如果用數組就需要將5之後的數據都往後退，但使用鏈表，便直接在3和5中間插入4就行

# ■ 缺點:
# 1. 鏈表數據結構是通過指針來連結，訪問結點順序只能是從頭到尾一個個地訪問，不能像數組進行隨機讀取
# 2. 因添加了指針域，因此空間開銷也較大

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: # l1 和 l2 是函數的兩個參數，它們的類型為 Optional[ListNode]，Optional 表示該參數可以為空，也就是說可以是 None 值。 而 -> 後面的 Optional[ListNode] 則是函數的返回值類型，也就是說，函數返回一個 ListNode 的可選值（即可能為 None）。
        # 設定虛擬結點，不存值，作為指針永遠指向真正的 head
        dummy = ListNode() # 在鍊錶操作中，經常需要使用一個啞節點（dummy node）來簡化操作。啞節點通常是一個不存儲數據的空節點，其主要作用是作為鍊錶的頭節點，使得鍊錶操作更加方便。
        cur = dummy # cur 可以指向當前的節點，而 dummy 則可以始終指向鍊錶的頭節點

        # 運算與存鏈表值
        carry = 0 # 進位數
        while l1 or l2 or carry: # 當l1、l2任一不是None 或 carry 不為0時，執行迴圈
            val1 = l1.val if l1 else 0 # 三元運算符 代表 if l1: val1 = l1.val | else: val1 = 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // 10 # 進位 = 商數
            value = value % 10 # 值 = 餘數
            cur.next = ListNode(val=value) # 鏈表開頭
            
            # 替換 將 cur、l1、l2替換到下一筆
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next # 將 dummy node 的下一筆 return
    
    
# Time complexity: O(max(n,m))     
# Space complexity: O(max(n,m))     
          
# Reference from: https://www.youtube.com/watch?v=-UBiYuIVErM
          
          
