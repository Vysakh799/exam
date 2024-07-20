f=open('exam/Q13.txt','r')
t=open('exam/Q16.txt','w')
lines=f.readlines()
for i in lines:
    i.strip()
    t.write(i)