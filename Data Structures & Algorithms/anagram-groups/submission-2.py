class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group={}
        # for string in strs: # O(n)
        #     char_list=sorted(string) # O(k log k)
        #     sorted_key="".join(char_list) # O(l)
        #     if sorted_key in group:
        #         group[sorted_key].append(string) # O(1) avg
        #     else:
        #         group[sorted_key]=[string] # O(1) avg
        # # return [res for res in group.values()] # O(v)
        # return list(group.values())
        
        group={}
        for string in strs:
            count=[0]*26
            for char in string:
                index=ord(char)-ord('a')
                count[index]+=1
            key=tuple(count)
            if key in group:
                group[key].append(string)
            else:
                group[key]=[string]
        return list(group.values())
