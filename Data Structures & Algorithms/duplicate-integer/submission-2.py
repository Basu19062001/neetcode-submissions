class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # num_len = len(nums)
        # if num_len < 2:
        #     return False
        
        # for i in range(num_len):
        #     for j in range(i+1, num_len):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        is_seen = set()
        if len(nums) < 2:
            return False
        
        for num in nums:
            if num in is_seen:
                return True
            is_seen.add(num)
        return False