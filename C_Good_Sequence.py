n = int(input())
a=list(map(int,input().split()))
c=set(a)
b={}
for num in a:
    if num in b:
        b[num] += 1
    else:
        b[num] = 1
ans=0
for i,j in b.items():
    if i!=j:
        if i<j:
            ans+=j-i
        else:
            ans+=j


print(ans)