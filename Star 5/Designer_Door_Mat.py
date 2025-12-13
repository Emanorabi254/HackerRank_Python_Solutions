# Enter your code here. Read input from STDIN. Print output to STDOUT

row, col = map(int, input().split())

# TOP           
for r in range(1,row,2):
    mid =".|." * r
    print(mid.center(col,"-"))
# Mid
print("WELCOME".center(col,"-"))    

# Bottom
for r in range(row-2,0,-2):
    mid = ".|." *r
    print(mid.center(col,"-"))

 

