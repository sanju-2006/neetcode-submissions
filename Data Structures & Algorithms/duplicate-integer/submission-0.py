class Solution(object):
    def hasDuplicate(self, nums):
        return len(set(nums)) != len(nums)