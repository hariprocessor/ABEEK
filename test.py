import random
import sys

freshman = 200
desire = 5
department = 30
freshman_data = []
department_data = []
final_match = []
arranged = []

# input data
for i in range(department) :
    final_match.append([])

for i in range(freshman) :
    input = raw_input("Enter input : ")
    freshman_data.append(map(int, input.split(' ')))

for i in range(department) :
    input = raw_input("Enter department data : ")
    department_data = map(int, input.split(' '))

# sample data
for i in range(freshman) :
    freshman_data.append(random.sample(range(30), desire))

for i in range(department) :
    if i < 20 :
        department_data.append(6)
    else :
        department_data.append(8)

# algorithm
for i in range(desire) :
    for j in range(department) :
        for k in range(freshman) :
            if freshman_data[k][i] == j and len(final_match[j]) < department_data[j] and not k in arranged :
                arranged.append(k)
                final_match[j].append(k)

for i in range(department) :
    for j in range(freshman) :
        if not j in arranged and len(final_match[i]) < department_data[i] :
            arranged.append(j)
            final_match[i].append(j)

# print result
for i in range(department) :
    sys.stdout.write("%d department : "%i)
    for j in range(len(final_match[i])) :
        sys.stdout.write("%d "%final_match[i][j])
    sys.stdout.write("\n")

                
