# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    inputArr = []
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        student.append(name)
        student.append(score)
        inputArr.append(student)

    sort_list = sorted(inputArr, key=lambda x: x[1], reverse=True)
    last_score = sort_list[-1][1]
    
    lowestScore =[i for i in sort_list if i[1] != last_score]
    
    sec_low_sc = lowestScore[-1][1]
    names = [i[0] for i in lowestScore if i[1] == sec_low_sc]
    names = sorted(names)
    for i in names:
        print(i)
        
