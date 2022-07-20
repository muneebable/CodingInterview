# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be NxM (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.


"""
Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------


"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
if __name__ == '__main__':
    N = int(input().split(' ')[0])
    M = N*3
    final_strings = [] 

    dot_danda = 1
    for i in range(math.floor(N/2)):
        dot_danda_str = '.|.' * dot_danda
        dot_danda_count = dot_danda* 3
        dash_count = int((M-dot_danda_count)/2)
        dash = '-' * dash_count
        final_srt = dash+dot_danda_str+dash
        final_strings.append(final_srt)
        print(final_srt)
        
        
        dot_danda = dot_danda+2
    
    WELCOME_DASH_count = int((M-7)/2)
    WELCOME_DASH = '-' * WELCOME_DASH_count
    welcome = 'WELCOME'
    print(WELCOME_DASH+welcome+WELCOME_DASH)
    
    for x in final_strings[::-1]:
        print(x)
