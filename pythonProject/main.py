import random

def motv():
    a = int(input())
    b = int(input())
    print(a) if a >= b else print(b)

def calc_average(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    avg = total / 5
    return avg

def determine_grade(score):
    if score >= 90 and score <= 100:
        grade = 'A'
        return grade
    elif score >= 80 and score <= 89:
        grade = 'B'
        return grade
    elif score >= 70 and score <= 79:
        grade = 'C'
        return grade
    elif score >= 60 and score <= 69:
        grade = 'D'
        return grade
    else:
        grade = 'F'
        return grade

def taag():
    score1 = int(input())
    score2 = int(input())
    score3 = int(input())
    score4 = int(input())
    score5 = int(input())

    findAvg = calc_average(score1, score2, score3, score4, score5)
    letterGrade = determine_grade(findAvg)

    print('Score\t\t Numeric Grade   Letter Grade')
    print('------------------------------------------------')
    print('Score 1:\t', score1, '\t\t', determine_grade(score1))
    print('Score 2:\t', score2, '\t\t', determine_grade(score2))
    print('Score 3:\t', score3, '\t\t', determine_grade(score3))
    print('Score 4:\t', score4, '\t\t', determine_grade(score4))
    print('Score 5:\t', score5, '\t\t', determine_grade(score5))

    print('Your final average is: ', findAvg, ',', 'This is your letter   grade: ', letterGrade)


def repeat():
    print("tie, try again")
    rpc()

def rpc():
    possible = ["rock", "paper", "scissor"]
    choice = str(input("give me a input in rock or paper or scissor: ")).lower()
    try:
        choice = possible.index(choice)
    except:
        print("not valid choice")
        rpc()
        return
    comp = random.randint(0,2)
    print("robot pick " + possible[comp])
    result = int((comp - choice)%3)
    print("You win") if result == 2 else print("You lose") if result == 1 else repeat()

rpc()

motv()

taag()
