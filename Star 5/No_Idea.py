# Enter your code here. Read input from STDIN. Print output to STDOUT

n , m= map(int, input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happ= 0

for i in arr:
    
    if i in A:
        happ +=1
    elif i in B:
        happ +=-1
print(happ)
