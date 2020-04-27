class Solution:
    def __init__(self,arr,r,l):
        self.arr = arr
        self.r = r
        self.l = l
        
    def middle(self):

        
        mid = self.l + (self.r - self.l) // 2
        print(self.arr[mid])
result = Solution([1,2,3,4,5],0,len([1,2,3,4,5])-1)
result.middle()
