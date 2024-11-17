def calculator():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    c = str(input("Enter operator:"))
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)
    else:
        print("invalid operator")

calculator()


