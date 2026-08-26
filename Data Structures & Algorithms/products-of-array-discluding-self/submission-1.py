class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res=[]
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             product *= nums[j]
        #     res.append(product)
        # return res

        res=[1]*len(nums)
        left_prod=1
        right_prod=1
        #left product 
        for i in range(len(nums)):
            res[i] = left_prod
            left_prod *= nums[i]
        #right product
        for j in range(len(nums)-1,-1, -1):
            res[j] *= right_prod
            right_prod *= nums[j]
            
        return res