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