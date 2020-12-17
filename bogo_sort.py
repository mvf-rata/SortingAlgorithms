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
def main():
    l = []
    for i in range(0, 10):
        l.append(random.randint(0, 999))
    print(l)
    start = time.time()
    bogo_sort(l)
    end = time.time()
    print(l)
    print('The sorting took: {} seconds.'.format((end - start)))

main()
