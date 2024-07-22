for i in range(1,6):
    for j in range(i):
        print((i+j)%2,end=" ")
    print()


for i in range(1,5):
    for j in range(i):
        if i%2==0:
            if j%2==0:
                print(0,end="")
            else:
                print(1,end="")
        else:
            if j%2==0:
                print(1,end="")
            else:
                print(0,end="")
    print()


# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1   