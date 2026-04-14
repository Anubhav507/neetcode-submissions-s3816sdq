class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        set1 = set(nums)
        if len(set1) == len(nums):
            return False
        else:
            return True
        