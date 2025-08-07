#output formatting
a=2.534
print("value up to two decimals {:0.2f}".format(a))

#Example 2: using sep and end paramter
company="tantude.com"
print("hindu",end="@")
print(company)
print("hindu","tantude","com",sep=".")
print("My date of Birth:",end="")
print("05","06","2004",sep="-")

#using f string format
name="hindu"
age=21
print(f"my name is {name} and age is {age}")
#using % operator
n=int(input("enter a number"))
sum=5+n
print("%d"%sum)

