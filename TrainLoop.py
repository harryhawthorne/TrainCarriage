# Determines which carriage problems are unsolvable

# Cartesian product of operations
from itertools import product

# Counter for carriages with no solutions
count = 0

# Loop through every possible train carriage number
for num in range(10000):

    # Prepare string to be 4 digits
    if num < 10:
        num_string = '000' + str(num)
    elif num <100:
        num_string = '00' + str(num)
    elif num <1000:
        num_string = '0' + str(num)
    else:
        num_string = str(num)

    # Get all operation permutations of length 3 (3 operators between 4 numbers)
    perms = [''.join(p) for p in product('+-*/', repeat = 3)]

    # Define a counter for the number of solutions
    numOfSols = 0

    # Loop through all possible arrangements of operations
    for i in range(len(perms)):
        eqn = num_string[0] + perms[i][0] + num_string[1] + perms[i][1] + num_string[2] + perms[i][2] + num_string[3]

        # Create an empty list
        paras = []

        # Store strings of equations with brackets in a list
        # https://math.stackexchange.com/questions/2450961/how-many-ways-are-there-to-put-parentheses-between-n-numbers
        paras.append('(' + eqn + ')')
        paras.append('(' + eqn[:3] + ')' + eqn[3:])
        paras.append(eqn[:2] + '(' + eqn[2:5] + ')' + eqn[5:])
        paras.append(eqn[:4] + '(' + eqn[4:] + ')')
        paras.append('(' + eqn[:3] + ')' + eqn[3] + '(' + eqn[4:7] + ')')
        paras.append('(' + eqn[:5] + ')' + eqn[5:])
        paras.append(eqn[:2] + '(' + eqn[2:7] + ')')
        paras.append('((' + eqn[:3] + ')' + eqn[3:5] + ')' + eqn[5:7])
        paras.append('(' + eqn[:2] + '(' + eqn[2:5] + '))' + eqn[5:7])
        paras.append(eqn[:2] + '(' + eqn[2:4] + '(' + eqn[4:] + '))')
        paras.append(eqn[:2] + '((' + eqn[2:5] + ')' + eqn[5:] + ')')

        # Loop through paras
        for x in range(len(paras)):

            # Try evaluate the string
            try:
                if eval(paras[x]) == 10:
                    numOfSols += 1

            # Exception to prevent divide by zero from ending program
            except ZeroDivisionError:
                pass

    # Count all iterations with no solutions equal to 10
    if numOfSols == 0:
        count += 1
        print(str(num))

print('Total Unsolvable Carriages: ' + str(count))
