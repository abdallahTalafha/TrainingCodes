print('Welcome to my magnificent calculator!')
print("To use the calculator enter 1st number followd by an opiration symbol{+,-,*,/,^,%}, followed by the second number.")
num1 = float(input("Enter 1st number: "))
Operation = input("Enter Operation: ")
num2 = float(input("Enter 2nd number: "))

def calculator(num1,Operation,num2):
    if Operation == '+':
        print(num1+num2)
    elif Operation == '-':
        print(num1-num2)
    elif Operation == '*':
        print(num1*num2)
    elif Operation == '/':
        print(num1/num2)  
    elif Operation == '^':
        print(num1^num2) 
    elif Operation == '%':
        print(num1%num2)   
    else:
        print('Wrong Input') 

calculator(num1,Operation,num2)    