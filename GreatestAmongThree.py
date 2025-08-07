# a=10
# b=20
# c=30
a,b,c=map(int,input("enter three numbers:").split())
if(a>b):
    if(a>c):
        print(a,"is greater")
    else:
        print(c,"is greater")
else:
    if(b>c):
        print(b,"is greater")
    else:
        print(c,"is greater")
