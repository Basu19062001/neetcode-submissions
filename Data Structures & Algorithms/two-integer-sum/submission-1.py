class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return -1
        
        # target - i = complement
        is_seen={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in is_seen:
                return [is_seen[complement], i]
            is_seen[nums[i]]=i
        return -1