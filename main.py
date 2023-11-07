import random

lists = []

# with open("dauletsuper.txt", 'r') as files:
#     for line in files:
#         words = line.strip().split()
#         lists.extend(words)


def task_1():
    for x in lists:
        print(x)


# task_1()

def task_2():
    random_string = random.randint(1, len(lists) - 1)
    print(f'{lists[random_string]}\n{random_string}')


# task_2()

def task_3():
    count = 0
    for i in lists:
        if i.istitle():
            count += 1
    print(count)


# task_3()


def task_4():
    count = 0
    with open('boring_file.txt', 'r') as fil:
        for line in fil:
            words = line.strip().split()
            if words and words[0].lower() == 'd':
                count += 1
                print(f"{words}\n{count}")

task_4()
