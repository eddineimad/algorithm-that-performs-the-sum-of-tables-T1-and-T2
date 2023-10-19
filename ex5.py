t1=[]
t2=[]
T=[]
n=int(input("Type the size n of the first and second table"))
for i in range (0,n) :
    m=int(input("Type the number for the first table"))
    t1.append(m)
for i in range (0,n) :
    p=int(input("Type the number for the second table"))
    t2.append(p)
for i in range (0,n) :
    S=t1[i]+t2[i]
    T.append(s)
print("The sum of tables T1 and T2 is:",T)