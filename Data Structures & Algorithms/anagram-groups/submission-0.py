class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            fre = [0]*26
            for ch in str:
                fre[ord(ch)-ord('a')] +=1
            key  = tuple(fre)
            if key not in d:
                d[key] = []
            d[key].append(str)
        return list(d.values())
            
        