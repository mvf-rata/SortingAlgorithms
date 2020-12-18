import random
import time

def bogo_sort(l):
    while not is_sorted(l):
        random.shuffle(l)
    return
    
def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i +1]:
            return False
    return True
    

def binary_search(l, item):
    begin_l = 0
    end_l = len(l) - 1

    while begin_l <= end_l:
        mid_l = (begin_l + end_l) // 2
        mid_value = l[mid_l]
        if mid_value == item:
            return mid_l
        elif item < mid_l:
            end_l = mid_l -1
        else:
            begin_l = mid_l + 1
    


def get_list():
    global l
    global item
    l = []
    print('This is a bogo sorter with a binary search.\nPls choose random numbers.\nAnd keep your list small.\n')
    n = int(input('enter number of elements in list: '))

    for i in range(0, n):
        print('enter the {} number: '.format(i+1))
        num = int(input())
        l.append(num)
    print('your entered list is: ', l)
    item = int(input('choose a number from your list: '))


def main():
    get_list()
    print('starting bogo sort...')
    bogo_sort(l)
    print(l)
    print('starting binary search...')
    print('Your number is at index: ',binary_search(l, item))

main()