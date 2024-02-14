def arithmetic_arranger(problems, show = True):
    f = ''
    s = ''
    t = ''
    l = ''
    for problem in problems:
        first_row = ''
        second_row = ''
        third_row = ''
        fourth_row = ''
        space = ' '
        p = str(problem).split()
        difference = abs(len(p[0]) - len(p[2]))
        #ERRORS
        if len(problems) > 5:
            print("Error: Too many problems.")
            break
        if p[1] != '+' and p[1] != '-':
            print("Error: Operator must be '+' or '-' .")
            break
        if not p[0].isdigit() or not p[2].isdigit():
            print("Error: Numbers must only contain digits.")
            break
        if max(len(p[0]), len(p[2])) > 4:
            print('Error: Numbers cannot be more than four digits.')
            break
        #OPERATION TYPE, RESULT
        if p[1] == '+':
            result = str(int(p[0]) + int(p[2]))
        else:
            result = str(int(p[0]) - int(p[2]))
        #DEFINE EACH ROW, DEPENDS ON LENGTH OF EACH NUMBER
        if len(p[0]) > len(p[2]):
            first_row += space*2 + p[0]
            second_row += p[1] + space + difference*space + p[2]
            third_row += len(first_row) * '-'
            fourth_row +=(abs(len(result)-len(third_row)))*space + result
            
        else:
            first_row += (difference+2)*space + p[0]
            second_row += p[1] + space + p[2]
            third_row += len(second_row) * '-'
            fourth_row += (len(third_row)-len(result))*space + result
        #SPACES BETWEEN PROBLEMS
        first_row += 4*space
        second_row += 4*space
        third_row += 4*space
        fourth_row += 4*space
        #FINAL STRINGS
        f += first_row
        s += second_row
        t += third_row
        l += fourth_row
    if show is True:
        arranged_problems = f + '\n' + s + '\n' + t + '\n' + l
    else:
        arranged_problems = ''
    return arranged_problems