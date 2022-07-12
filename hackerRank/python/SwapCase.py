# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    final = []
    for i in s:
        if i.islower():
            
            final.append(i.upper())
        elif i.isupper():
            
            final.append(i.lower())
        else:
            
            final.append(i)
    
    f_str = "".join(str(x) for x in final)
    return f_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
