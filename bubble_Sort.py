import random
import time

def bubble_sort(l):
    for n in range(len(l)):
        for j in range(0, len(l) - 1 - n):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def main():
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    print(l)
    start = time.time()
    bubble_sort(l)
    end = time.time()
    print(l)
    print(end-start)

main()