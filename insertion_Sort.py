import random
import time

def insertion_sort(l):
    l_sorted = []
    while(len(l) > 0):
        min_elem = l[0]
        min_index = 0
        for index, elem in enumerate(l):
            if elem < min_elem:
                min_elem = elem
                min_index = index
        l.pop(min_index)
        l_sorted.append(min_elem)
    return l_sorted
    

def main():
    l = []
    for i in range(1000):
        l.append(random.randint(0, 999))
    print(l)
    start = time.time()
    print(insertion_sort(l))
    end = time.time()
    print(end-start)


main()