class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            result+=str(len(word))+"#"+word
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            dash=s.find("#",i)
            n=int(s[i:dash])
            result.append(s[dash+1:dash+1+n])
            i=dash+1+n
        return result
