class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        current = 1

        for i in range(len(nums)):
            prefix.append(current)
            current *= nums[i]
            
        current = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix.append(current)
            current *= nums[i]
        suffix = suffix[::-1]
        
        print(prefix)
        print(suffix)
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])
        
        return ans
