a=10
b=20
c=30
d=40
li=[a,b,c,d]
n=int(input())
for i in range(0,n):
    x=li.pop()
    li.insert(0,x)
    a,b,c,d=li
    print(a,b,c,d)
    
