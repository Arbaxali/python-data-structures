def addsum(a,b):
    sum=a+b
    return sum
try:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    sol=addsum(num1,num2)
    print(sol)
except:
    print("enter valid input")
    quit()
print("finished sum")
