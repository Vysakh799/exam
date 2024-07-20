l=[1,3,4,11,3,'ABC',8.5]
no=[]
for i in l:
    if type(i)==int or type(i)==float:
        no.append(i)
b=no[0]
for i in no:
    if i>b:
        b=i
        largest=i
print(largest)
