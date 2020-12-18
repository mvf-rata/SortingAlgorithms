l = [1,2,3,4,5,6,7,8,9,10]
item = 1


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

print(binary_search(l, item))