import random
import time

def selection_sort(l):
    for index in range(len(l)):
        min_index = index
        for i in range(min_index + 1, len(l)):
            if l[min_index] > l[i]:
                min_index = i

        cache = l[index]
        l[index] = l[min_index]
        l[min_index] = cache

    return l


def main():
    l = []
    for n in range(9999):
        l.append(random.randint(0, 999))
    print(l)
    start = time.time()
    print(selection_sort(l))
    end = time.time()
    print('The sorting took: {} seconds.'.format((end - start)))

main()