class Solution:
    def encode(self, strs):
        # write your code here
        res=""
        for s in strs:
            res+= str(len(s)) + "#" + s
        return res

    def decode(self, str):
        # write your code here
        res=[]
        i=0
        while i<len(str):
            j=i
            while str[j]!="#":
                j+=1
            length=int(str[i:j])
            i=j+1
            j=i+length
            res.append(str[i:j])
            i=j
        return res