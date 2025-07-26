#calculator
#addition
def addition(num1,num2):
    return num1+num2

#substraction
def substraction(num1,num2):
    return num1-num2

#multipication
def multiplication(num1,num2):
    return num1*num2

#division
def division(num1,num2):
    if num2==0:
        return "invalid number"
    return num1/num2

print("press 1 for Addition")
print("press 2 for Substraction")
print("press 3 for Multiplication")
print("press 4 for Division")

choice=int(input("Enter your operand(1/2/3/4): "))

#taking input from user
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))

if choice==1:
    print("The result is ",addition(num1,num2))

elif choice==2:
    print("The result is ",substraction(num1,num2))

elif choice==3:
    print("The result is ",multiplication(num1,num2))

elif choice==4:
    print("The result is ",division(num1,num2))

else:
    print("invlid choice")
