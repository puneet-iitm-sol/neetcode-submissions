class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s)!=len(t):
            return False
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch2 in t:
            if ch2 not in d:
                return False
            else:
                d[ch2] -= 1
                if d[ch2] == 0:
                    del d[ch2]
        return True


        