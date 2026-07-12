class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l,r=0, len(num) -1
        while num[l]+num[r]!=target:
            if num[l]+num[r]<target:
                l+=1
            else:
                r-=1
        return[l+1,r+1]  