import time
import random
import sys
sys.setrecursionlimit(10000)


def bubble_sort(list):
    # calculate the length of list as n
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


def selection_sort(list):
    # calculate the length of the list as n
    for i in range(len(list)-1):
        min = i
        for j in range(i, len(list)):
            if list[min] > list[j]:
                min = j
        temp = list[min]
        list[min] = list[i]
        list[i] = temp
    return list


def merge_sort(list):
    # calculate the length of the list as n
    if len(list) <= 1:
        return list
    # middle of the list
    mid = len(list)//2
    left_list = merge_sort(list[:mid])
    right_list = merge_sort(list[mid:])
    return merge(left_list, right_list)


def merge(left, right):
    output = []
    # create two counters for two lists as lc and rc
    lc, rc = 0, 0
    while lc < len(left) and rc < len(right):
        if left[lc] < right[rc]:
            output.append(left[lc])
            lc += 1
        else:
            output.append(right[rc])
            rc += 1
        # add the unfinished part of left or right into the output
    output.extend(left[lc:])
    output.extend(right[rc:])
    return output


def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        left = []
        right = []
        # we use the first element as the pivot
        for i in range(1, len(list)):
            if list[i] > list[0]:
                right.append(list[i])
            else:
                left.append(list[i])
    return(quick_sort(left) + list[:1] + quick_sort(right))


def classic_quick_sort(list):
    partition(list, 0, len(list)-1)
    return list


def partition(list, lb, rb):
    if rb-lb <= 1:  # one element only or an empty list
        return
    else:
        # take the most right element as the pivot
        pivot = rb
        # create new bounds
        left = lb
        right = rb-1
        # compare the elements with the pivot from the left2right first
        left2right = True
        while left <= right:
            if left2right:
                if list[left] > list[pivot]:
                    # swap the values of left and pivot
                    temp = list[pivot]
                    list[pivot] = list[left]
                    list[left] = temp
                    # set new pivot as left
                    pivot = left
                    left2right = False  # compare from right to left
                left += 1
            else:
                if list[right] < list[pivot]:
                    # swap the values of right and pivot
                    temp = list[pivot]
                    list[pivot] = list[right]
                    list[right] = temp
                    # set new pivot as right
                    pivot = right
                    left2right = True
                right -= 1

        partition(list, lb, pivot-1)
        partition(list, pivot, rb)


def binary_search(element, list, lower, upper):
    if upper >= lower:
        mid = lower + (upper-lower)//2
        if list[mid] == element:
            return True
        if list[mid] < element:
            lower = mid+1
            return binary_search(element, list, lower, upper)
        if list[mid] > element:
            upper = mid-1
            return binary_search(element, list, lower, upper)
    else:
        return -1


def binary_search_iterartion(element, list):
    lower = 0
    upper = len(list)-1
    while lower <= upper:
        mid = lower + (upper - lower) // 2
        if list[mid] == element:
            return True
        if list[mid] < element:
            lower = mid
        if list[mid] > element:
            upper = mid
    else:
        return -1


def main():
    f = open('numbers.txt', 'r')
    line = f.read()
    list = line.split(' ')
    list = [int(x) for x in list]
    # # # # Bubble sort algorithm
    # start = time.time()
    # bubble_sort(list)
    # end = time.time()
    # print("The elapsed time is Bubble sort " + str(end-start))
    # # selection sort algorithm
    # start = time.time()
    # selection_sort(list)
    # end = time.time()
    # print("The elapsed time is Selection sort " + str(end-start))
    # # Merge sort algorithm
    # start = time.time()
    # merge_sort(list)
    # end = time.time()
    # print("The elapsed time is Merge sort " + str(end-start))
    # # # Quick sort not in place algorithm
    # start = time.time()
    # quick_sort(list)
    # end = time.time()
    # print("The elapsed time is Quick sort not-in-place " + str(end-start))
    # # # # Quick sort  in place algorithm
    start = time.time()
    classic_quick_sort(list)
    end = time.time()
    print("The elapsed time is Quick sort in-place " + str(end-start))
    # Binary search
    print(binary_search(100, list, 0, len(list)-1))
    # Binary search iteration
    print(binary_search_iterartion(100, list))


if __name__ == '__main__':
    main()
