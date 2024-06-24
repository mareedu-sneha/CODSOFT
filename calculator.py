def switch(choice):
    if choice=="addition":
        add(choice)
    elif choice=="subtraction":
        sub(choice)
    elif choice=="multiplication":
        mul(choice)
    elif choice=="division":
        div(choice)
    elif choice=="modulus":
        mod(choice)
    elif choice=="exit":
        exit(choice)
        
    else:
        print("Please enter a valid input choice..!")
        

def add(choice):
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number:"))
    print(n1+n2)
def sub(choice):
    n1=int(input("Enter the frist number:"))
    n2=int(input("Enter the second number:"))
    print(n1-n2)
def mul(choice):
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number:"))
    print(n1*n2)
def div(choice):
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number:"))
    if(n2==0):
        print("enter any number except zero in number2")
    else:
        print(n1/n2)
def mod(choice):
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number:"))
    print(n1%n2)
def exit(choice):
    print("No operations are performed....")
    print("Exiting....")
    print("Closed...")
choice=input("Enter the operation you want to performe:")
switch(choice)

