def fact(n):
    if(n==1 or n==0):
        return 1
    result=n*fact(n-1)
    return result
print(fact(3))