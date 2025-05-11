x,y=map(int,input().split())
z=list(map(int,input().split()))
members=[]
for i in z:
    d=i+y
    if d<=5:
        members.append(d)
print(len(members)//3)        
