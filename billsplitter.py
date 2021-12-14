from random import random, choice


def init_friends(n,x=0):
    global friends
    friends = {}
    friend = ''
    for n in (range(n_friends)):
        friend = input()
        friends[friend] = x

def set_friends_bill(x):
    global friends
    for friend in friends:
        friends[friend] = float(x)

print()
print("Enter the number of friends joining (including you):")
n_friends = int(input())
if n_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    init_friends(n_friends)
    n = 0
    print("Enter the total bill value:")
    bill_total = float(input())
    split = float(bill_total / n_friends)
    print('Do you want to use the "who is lucky?" feature? Write Yes/No:')
    lucky = str(input())
    if lucky == "Yes":
        lucky_one = choice(list(friends.keys()))
        print(lucky_one, "is the lucky one!")
        topay = "{:.2f}".format((bill_total / (n_friends - 1)))
        for friend in friends:
            if friend == lucky_one:
                friends[friend]=0
            else:
                friends[friend]=float(topay)
        print(friends)
    elif lucky == "No":
        print("No one is going to be lucky")
        set_friends_bill("{:.2f}".format(split))
        print(friends)
