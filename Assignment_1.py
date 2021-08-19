# 1) Reverse a String and print it on console "Python Skills"
print("\n---Answer 1---")
str="Python Skills"
print("\nOriginal string: ",str)
print("\nReversed string: ",str[::-1])

# 2) Assign String to x variable in DD-MM-YYYY format extract and print Year from String.
print("\n---Answer 2---")
import datetime
date = "19-08-2021" 
format = "%d-%m-%Y"
dt_object = datetime.datetime.strptime(date, format)
print("\nYear using function : ", dt_object.year)
print("\nYear using slice operator:",date[6:])

# 3) In a small company, the average salary of three employees is Rs1000 per week. If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn? Solve by using java programm
print("\n---Answer 3---")
#import os.path,subprocess
#output = subprocess.check_output("java average", stderr=subprocess.PIPE)
#print(output)
avg=1000
e1=1100
e2=500
e3=(avg*3)-(e1+e2)
print("\nFirst employee salary = ",e1,"\nSecond employee salary =",e2,"\nThird employee salary = ",e3,"\nAverage =",avg)
# 4) Write Program - convert a percentage to a fraction (To convert a percentage into fraction let say 30% to a fraction)
print("\n---Answer 4---")
percent=30
n=percent
d=100
num=n/10
den=d/10
print("\nConversion of 30 percent into fraction is equal to : ",int(num),"/",int(den))

# 5) Write Program - A train 340 m long is running at a speed of 45 km/hr. what time will it take to cross a 160 m long tunnel?
print("\n---Answer 5---")
train_length=340
tunnel_length=160
#Total distance to be travelled by train
distance=train_length+tunnel_length
print("Total distance to be travelled by train:",distance,"meter")
#Conversion of km per hour into m per seconds
speed=(45*5)/18
print("Speed=",speed,"m/sec")
time=distance/speed
print("Time taken by train to cross the tunnel=",time,"sec")
