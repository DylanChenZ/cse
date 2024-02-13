import random

def LNG():
        list = []
        for i in range(7):
            list.append(random.randint(0,9))
            print(list[i])
        s = str(input("give me a number of 7 digit long: "))
        while len(s) != 7:
            s = str(input("give me a number of 7 digit long: "))
        for i in range(7):
            print(s[i], end = ' ')
            print("match") if int(s[i]) == list[i] else print("no match")
        print("you won the lottery") if (all(int(s[i]) == list[i] for i in range(7))) else print("you didn't win")

def NAP():
    print("give me 20 numbers")
    list = []
    for i in range(3):
        list.append(int(input()))
    print("lowest number is: " + str(min(list)))
    print("highest number is " + str(max(list)))
    print("length of list is " + str(len(list)))
    print("the average of list is :" + str(sum(list)/len(list)))


LNG()

NAP()