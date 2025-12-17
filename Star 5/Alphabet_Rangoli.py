import string
def print_rangoli(size):
    char = string.ascii_lowercase
    width = 4*size -3
    line= []
    
    for i in range(size):
        left = char[size-1 : size-i-1: -1]
        right = char[size-i-1: size]
            
        row = "-".join(left+right)
        line.append(row.center(width,"-"))    
    print( "\n".join(line+line[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
