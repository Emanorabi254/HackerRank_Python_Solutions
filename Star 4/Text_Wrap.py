"""
Sample Input 

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""


import textwrap

def wrap(string, max_width):
    # Wrapp the text
    Wrapper = textwrap.TextWrapper(width=max_width)
    paragraphs_List = Wrapper.wrap(text=string)
    
    return "\n".join(paragraphs_List)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
