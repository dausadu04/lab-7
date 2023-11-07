import random
import re

lists = []

with open("dauletsuper.txt", 'r') as files:
    for line in files:
        words = line.strip().split()
        lists.extend(words)


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
    with open('boring_file.txt', 'r') as file:
        for i in file:
            i = i.strip().split()
            for j in i:
                if j and j[0].lower() == 'd':
                    count += 1
                    print(f"{j}\n{count}")


# task_4()


def task_5():
    count = 0
    with open('boring_file.txt', 'r') as file:
        for i in file:
            i = i.strip().split()
            for j in i:
                if j and j[-1].lower() == 'f':
                    count += 1
                    print(f"{j}")

        print(count)


# task_5()

def task_6():
    count = 0
    with open('chatgpt_text.txt', 'r') as file:
        for i in file:
            i = i.strip().split()
            for j in i:
                if j == 'all' or j == 'none':
                    count += 1
        print(count)


# task_6()


def task_6_2():
    with open('chatgpt_text.txt', 'r') as file:
        file = file.read()
        count_all = file.count(' all ')
        count_none = file.count(' none ')
        counts = count_none + count_all
    print(counts)


# task_6_2()

def task_7():
    checked = set()
    lists = []
    with open('chatgpt_text.txt', 'r') as file:
        for line in file:
            words = line.strip().split()
            lists.extend(words)

    for i in lists:
        i = i.strip()
        count = lists.count(i)
        if (i, count) not in checked:
            checked.add((i, count))
    print(checked)


# task_7()

def task_8():
    max_length = 0
    with open('chatgpt_text.txt', 'r') as file:
        for i in file:
            i = i.strip().split()
            for j in i:
                if max_length < len(j):
                    max_length = len(j)
                    word = j
    print(f"{max_length}\n{word}")


# task_8()

def task_8_2():
    lists = []

    with open('chatgpt_text.txt', 'r') as file:
        for i in file:
            i = i.strip().split()
            lists.extend(i)
    print(max(lists, key=len))


# task_8_2()

def task_9():
    with open('gay boy', 'r+') as file:
        content = file.read()
        content = content.replace('b', 'j')

        file.seek(0)
        file.write(content)
        file.truncate()

        print(content)


# task_9()

def task_10():
    # gay boy is {I am a joy.}
    checked = set()
    with open('gay boy', 'r') as file:
        lines = file.read()
        for i in lines:
            i = i.split()
            for j in i:
                j = j.lower().strip()
                for k in j:
                    if k not in checked:
                        count = i.count(k)
                        if count == 0:
                            count += 1
                        checked.add((k, count))
    print(checked)


# task_10()
