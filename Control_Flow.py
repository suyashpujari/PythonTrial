#if
print("\n---if example---")
a=20
n=int(input("\nEnter number: "))
if a>n:
    print("\n",a,"is greater than",n)
if a==n:
    print("\n",a,"is equal to",n)

#if-else
print("\n---if-else example---")
a=40
if a>n:
    print("\n",a,"is greater than",n)
else:
    print("\n",a,"is smaller than",n)

#elif
print("\n---elif  example---")
m=int(input("\nEnter number: "))
if m>0 :
    print("\n",m,"is a positive number")
elif m==0:
        print("\nYour Entered Number is zero")
else:
    print("\n",m,"is a negative number")

#for loop
print("\n---For loop example---")
list=[1,2,3,4,5,6,7,8,9]
sum=0
for num in list:
    sum=sum+num
print("\nsum:",sum)

#while loop
print("\n---While loop example---")
i = 1
while i < 11:
  print(i)
  i += 1

#Pass
print("\n---Pass example---")
if 10>5:
    pass
print("\n---Pass example end---")


#break
print("\n---Break example---")
for s  in "training":
    if s=='i':
        break
    print(s)

#continue
print("\n---Continue example---")
for s  in "industrial training":
    if s=='n':
        continue
    print(s)