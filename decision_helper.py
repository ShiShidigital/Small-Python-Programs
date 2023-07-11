# Program to help me with difficult decisions
from random import choice 
from time import sleep


# def to get one random item out of a list 
def random_item_from_list(list):
    # print("Following list was given:", list)
    list_item = choice(list)
    # print("Following Item was choosen:", list_item)
    return list_item


print()
print("Decision Helper")
print('-' * 20)
print("I will help you to make a decision.\n")


while True:
    print("MENU")
    print("0) End this program.")
    print("1) Yes or No?")
    print("2) Choose an item from a list.")
    print('-'* 20)
    user_input = input("Choose a number from the MENU. > ")


    try:
        user_input = int(user_input)

    except:
        print()
        print("Looks like your input is not a number.\n")
        continue


    if user_input == 0:
        print()
        print("Good Bye!")
        quit()

    elif user_input == 1:
        print()
        list = ["Yes", "No"]
        print("You want to know the answer to a Yes or No question?")
        user_input = input("Please ask your question > ")
        decision = random_item_from_list(list)

        print("Your question is:\n" + user_input)
        sleep(2)
        print("The answer is ...")
        sleep(2)
        print(decision)
        input("\nPress any key to continue\n")

    elif user_input == 2:
        print()
        list = []
        print("You want a choice from a list of items?")
        question = input("What is the question or thema of your request? > ")
        user_list = input("Please give me a comma seperated list of items > ")
        list = user_list.split(',')
        decision = random_item_from_list(list)        

        print("Your question is:\n" + question)
        sleep(2)
        print("Your list has the follwoing items:")
        print(list)
        sleep(2)
        print("The answer is ...")
        sleep(2)
        print(decision)
        input("\nPress any key to continue\n")

    else:
        print()
        print("Please choose a number from the menu.")
        continue