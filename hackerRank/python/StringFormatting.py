"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
"""

def print_formatted(number):
    width=len(bin(number))-2
    for num in range(1,number+1): 
        for base in ('d', 'o', 'X', 'b'):
            print("{0:{width}{base}}".format(num, base=base, width=width), end=' ')
        print()
    
if __name__ == '__main__':
