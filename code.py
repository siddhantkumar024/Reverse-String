class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        f=0
        e=n-1
        while f<e:
            s[f],s[e]=s[e],s[f]
            f+=1
            e-=1
        return s

        
