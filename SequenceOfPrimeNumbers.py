n=int(input("enter n value:"))
for num in range(2,n+1):
    is_Prime=True
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            is_Prime=False
            break
    if(is_Prime):
        print(num,end=",")