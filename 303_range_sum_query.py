class NumArray(object):
    currNum = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.currNum = [0]
        for i in range(0, len(nums)):
            self.currNum.append(self.currNum[i]+nums[i])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.currNum[right+1] - self.currNum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
nums = [-2, 0, 3, -5, 2, -1]  ## [0, -2, -2, -1, -6, -4, -5]
lr = [[0, 2], [2, 5], [0, 5]]
obj = NumArray(nums)
l = [None]
for i in lr:
    param_1 = obj.sumRange(i[0],i[1])
    l.append(param_1)
print(l)