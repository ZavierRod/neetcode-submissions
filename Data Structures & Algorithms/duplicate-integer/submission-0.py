class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set(nums)

        return len(nums) != len(ans)