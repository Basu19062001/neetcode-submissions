class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for string in strs:
            char_list=sorted(string)
            sorted_key="".join(char_list)
            if sorted_key in group:
                group[sorted_key].append(string)
            else:
                group[sorted_key]=[string]
        return [res for res in group.values()]