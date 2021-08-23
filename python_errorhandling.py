#overflow error
a=200.76
b=651651161619165116651511115.78
try:
    print("The Addition of a&b ",a**b)
except(OverflowError):
    print("Overflow error occured")

#divide by zero
a=4
b=0
try:
    print("Division by zero ",a/b)
except(ZeroDivisionError):
    print("Divide by zero error is not allowed")

#value error
try:
    b=int(input("Enter the variable to raise the error"))
except(ValueError):
    print("Value Error Occured")

#UnboundLocal Error
try:
    def f():
        a = a + 1
    f()
except (UnboundLocalError):
    print ("UnboundLocal Error Occured")

#Type Error
a='2'
b=2
try:
    print("a+b",a+b)
except(TypeError):
    print("Type Error Occured")    

#Name error
a=10
b=7
try:
    print("Substraction",a-c)
except(NameError):
    print("Name Error Occured")

#IndentationError
def fun():
 pass

try:
    fun()
except IndentationError as i:
    print("IndentationError Occured",i)


#SyntaxError
a = 10000
try:
    if(a > 8000)
     print(a,"is greater than 8000")
except:
    print("SyntaxError Occured")