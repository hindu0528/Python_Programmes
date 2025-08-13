n=int(input("enter number of lines you need to enter:"))
result=[]
for i in range(0,n):
    s=str(input("enter a string"))
    result.append(s)
# for l in result:
#     print(l)

# print(result)
first=result[0]
# list concatination
pairs=[[first]+result[i:i+2] for i in range(1,len(result),2)]
print(pairs)

