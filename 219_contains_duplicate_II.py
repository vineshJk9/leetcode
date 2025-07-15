class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        arr_set = set()
        if k==0:
            return False
        for i in range(len(nums)):
            if i > k:
                arr_set.remove(nums[(i-k)-1])
            if nums[i] in arr_set:
                return True
            arr_set.add(nums[i])
        return False