class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # count_s = {}
        # count_t = {}
        
        # for char in s:
        #     if char in count_s:
        #         count_s[char] += 1
        #     else: count_s[char]=1
        
        # for char in t:
        #     if char in count_t:
        #         count_t[char] += 1
        #     else: count_t[char]=1

        # return count_s == count_t
        if len(s) != len(t):
            return False
        
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else: 
                count[char] = 1
        print(count)
        for char in t:
            if char in count:
                count[char] -= 1
            elif char not in count:
                return False
        print(count)
        # return not all(count.values())
        return all(value == 0 for value in count.values())
        # for val in count.values():
        #     if val == 0:
        #         continue
        #     return False
        # return True