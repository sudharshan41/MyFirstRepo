print("simple calculator")
print("select an operation")
print("1.addition\n2.subtraction \n3.multiplication\n4.division\n5.modulus\n6.FloutDivision")
while True:
    operation=int(input("Enter an option>> "))
    num1=float(input("enter num1>>"))
    num2=float(input("enter a num2>>"))

    if operation==1:
        print(num1+num2)
    elif operation==2:
        print(num1-num2)
    elif operation==3:
        print(num1*num2)
    elif operation==4:
        print(num1/num2)
    elif operation==5:
        print(num1%num2)
    elif operation==6:
        print(num1//num2)


    else:
        print("Invalid input.Try again")
        break