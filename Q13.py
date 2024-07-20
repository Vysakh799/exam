f=open("exam/Q13.txt",'r')
lines=f.readlines()
print("No of lines :",len(lines))
count=0
cap=0
sm=0
words=0
word=[]
for i in lines:
    i.strip()
    word.append(i.split(" "))
    for j in i:
        j.strip()
        if j==" " or j=="\n":
            pass
        else:
            count+=1
        if j.isupper():
            cap+=1
        if j.islower():
            sm+=1
for i in word:
    for j in i:
        words+=1
print("Total number of words :",words)
print("Total number of letters :",count)
print("Total number of capital letters:",cap)
print("Total number of small letters :",sm)
