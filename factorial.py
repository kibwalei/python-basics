print("This code prints the factorial of a number")
number= int(input("Enter a number : "))
factorial=1
if number < 0:
    print("There are no factorials fpr negative numbers")
elif number==0:
    print("The factorial for 0 is 1")
else:
    for x in range(1,number+1):
        factorial=factorial*x
        
        
    print(f"The factorial for {number} is {factorial}")