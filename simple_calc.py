print("Hello This is a Simple Calculator")
num1= int (input ("Enter number :"))
operator= (input ("Enter operator (*,/,+,-) :"))
num2= int (input ("Enter number :"))

if operator== "+":
    sum= num1+num2
    print(f"The sum of the numbers is : {sum}")

elif operator== "-":
    diff= num1-num2
    print(f"The difference of the numbers is : {diff}")
    
elif operator== "*":
    mul= num1*num2
    print(f"The product of the numbers is : {mul}")
    
elif operator== "/":
    div= num1/num2
    print(f"The division of the numbers is : {div}")

else:
    print("The operator entered is invalid")
