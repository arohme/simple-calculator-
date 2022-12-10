x=float(input("first number"))
y=float(input("second number"))
print("1-addition")
print("2-substraction")
print("3-division")
print("4-multiply")
choice=int(input("choose what you want "))
if choice==1:
    print(x+y)
elif choice==2:
    print(x-y)
elif choice==3:
    print(x/y)
elif choice==4:
    print(x*y)
else:
    print("invalid choice")
