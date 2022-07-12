# Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
#Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of  is not equal to n. 

# Example
# x=1
# y=1
# z=1
# n=2


# All permutations of  are:
# .[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# Print an array of the elements that do not sum to n.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    answer = [[i, j, k ] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
    print(answer)
