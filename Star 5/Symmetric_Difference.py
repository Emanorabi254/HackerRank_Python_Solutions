# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
set_M= set(map(int,input().split()))

_ = input()
set_N= set(map(int,input().split()))

Intersect = set_M.intersection(set_N)

diff_M_N= set_M.difference(Intersect)
diff_N_M= set_N.difference(Intersect)

diff_symmetric= diff_M_N.union(diff_N_M)

for element in sorted(diff_symmetric):
    print(element)
