no=int(input("Enter a number :"))
for i in range(no):
    b=no%10
    no=no//10
    if b==0:
        pass
    else:
        print(b,end="")