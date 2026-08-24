class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count={}
        for num in nums:
            if num in freq_count:
                freq_count[num]+=1
            else:
                freq_count[num]=1
        sorted_freq=sorted(freq_count.items(), key=lambda x: x[1], reverse=True)
        return [pair[0] for pair in sorted_freq[:k]]
        # freq_count={}
        # for num in nums:
        #     if num in freq_count:
        #         freq_count[num]+=1
        #     else:
        #         freq_count[num]=1
        # buckets=[[] for _ in range(len(nums)+1)]
        # for key, value in freq_count.items():
        #     buckets[value].append(key)
        # res=[]
        # for indx in range(len(buckets)-1,0,-1):
        #     if buckets[indx]:
        #         for num in buckets[indx]:
        #             if k==len(res):
        #                 break
        #             else:
        #                 res.append(num)

        # return res