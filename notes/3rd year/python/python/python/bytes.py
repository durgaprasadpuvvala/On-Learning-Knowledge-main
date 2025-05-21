class Test:
    def ispoweroftwo(self,n):#
        while n!=1:#25!=1
            if n%2!=0:
                return "No"
            n=n//2#25
        return "Yes"
            
#driver code
obj=Test()
n=int(input())
print(obj.ispoweroftwo(n))