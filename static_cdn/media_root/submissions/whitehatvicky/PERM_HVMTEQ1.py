n=int(input())
x=[]
for i in input().split(' '):
    x.append(int(i))
u=[]
y=[]
for i in  x:
    if i not in y:
        y.append(i)
for i in range(n-1):
    if x[i+1]>x[i] and  [x[i+1],x[i]] not in u:
        u.append([x[i+1],x[i]])
print(len(y)-1)

