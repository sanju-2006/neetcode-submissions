class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                need=len(sub)-sub.count(max(set(sub),key=sub.count))
                if need<=k:
                    res=max(res,len(sub))
        return res