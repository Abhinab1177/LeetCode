class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        n=len(s)
        #check for whitespace
        while i<n and s[i]==" ":
            i=i+1
        #Assume + sign
        sign=1
        #check + or - sign
        if i<n and (s[i]=="+" or s[i]=="-"):
            if s[i]=="-":
                sign=-1
            i=i+1
        #check digit to number
        num=0
        while i<n and s[i].isdigit():
            num=num*10+int(s[i])
            i=i+1
        #Apply sign
        num=num*sign
        #check range
        if num<-2**31:
            return -2**31
        if num>2**31-1:
            return 2**31-1
        return num

        
        