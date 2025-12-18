# Enter your code here. Read input from STDIN. Print output to STDOUT

N= int(input())

distnict_set= set()

for i in range(N):

    country_stamp = str(input())
    distnict_set.add(country_stamp)
    
print(len(distnict_set))    
