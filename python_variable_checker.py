import re
from keyword import kwlist # gets reserved keywords list


def variable_check(variable):
    print()
    print("Checking variable name: {}".format(variable))
    variable_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    check = re.search(variable_pattern, variable)

    if check == None:
        print('No valid Variable Syntax!')
        return False
    else:
        if variable in kwlist:
            print('Variable is a reserved word!')
            print('List of reserved words in Python:')
            print(kwlist)
            return False
        else:
            print('Variable name is valid!')
            return True


while True:
    print()
    print("Python Variable Checker")
    print("-"*20)
    print("Check if your Variable Name can be used in Python.")
    print("End the Variable Checker by typing q.")
    variable_name = input("Variable Name >> ")
    if variable_name == "q":
        print("Good bye!")
        quit()
    print(variable_check(variable_name))
