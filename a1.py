# Assignment 1
# a1.py
import sys


def five_x_cubed_plus_two(num):  # function that returns 5(x^3)+2
    return 5 * (num ** 3) + 2


def triple_up(lst):  # return nested list group by 3 elements f([1,2,3,4]) = [[1,2,3],[4]]
    new_lst = []
    last_lst = []
    mod = len(lst) % 3
    if mod == 0:
        for i in range(0, len(lst), 3):
            new_lst.append([lst[i], lst[i + 1], lst[i + 2]])
    else:
        for i in range(0, len(lst) - mod, 3):
            new_lst.append([lst[i], lst[i + 1], lst[i + 2]])
        for j in range(len(lst) - mod, len(lst), 1):
            last_lst.append(lst[j])
        new_lst.append(last_lst)
    return new_lst


def mystery_code(string):  # ord index 97 to 122 for lower, 65 to 90 for upper
    # new_string = string
    string = list(string)
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                string[i] = string[i].lower()
                index = ord(string[i]) + 21
                if index > 122:
                    index = ord(string[i]) - 5
            else:
                string[i] = string[i].upper()
                index = ord(string[i]) + 21
                if index > 90:
                    index = ord(string[i]) - 5
            string[i] = chr(index)
    string = ''.join(string)
    return string


def future_tense(lst):
    word_lst = {'ate': 'will eat', 'am': 'will be', 'today': 'tomorrow', 'yesterday': 'tomorrow', 'is': 'will be',
                'now': 'tomorrow'}
    for i in range(len(lst)):
        if lst[i].lower() in word_lst:
            if i == 0:
                lst[i] = word_lst[lst[i].lower()].capitalize()
                lst[i][0].upper()
            else:
                lst[i] = word_lst[lst[i]]

    lst1 = ' '.join(lst)
    lst1 = lst1.split(' ')
    return lst1


if __name__ == '__main__':
    #sys.stdout = open("/Users/tianyizhang/EE514/a1examplesPlus.txt", "w")
    #print('five_x_cubed_plus_two(3)=', five_x_cubed_plus_two(3))
    a = future_tense(['Yesterday', 'I', 'ate', 'pasta', 'and', 'today', 'I', 'am', 'having', 'soup'])

    b = future_tense(['Life', 'is', 'good', 'now'])
    print(a,b)
