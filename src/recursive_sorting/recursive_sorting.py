# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # TO-DO
    merged_arr = []  # this new list will be the merged list we return at the end
    # create variables to hold the current indexes and set them to 0
    arrA_index, arrB_index = 0, 0
    # ^ bc the smallest nums will be at the first position of both arrays since theyre SORTED
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        # ^ a while loop that will continue iterating until we used up all the elements in both arrays
        if arrA[arrA_index] < arrB[arrB_index]:
            # ^ on each iteration we compare the elemnts on the top of each array
            merged_arr.append(arrA[arrA_index])
            # ^ append whichever is smaller onto your merged array
            arrA_index += 1
            # ^ increment the index on the array you pulled from so you don't write the same element onto the merged list again
        else:
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1
    if arrA_index == len(arrA):
        # ^ if its the last element left in array A (we know that we already pushed all the array A elements onto the merged array)
        # ^ and if this is the case, there must also be only 1 element left in array B
        # ^ so we push the remaining element of B directly onto Merged Array
        # put that last element LAST on the merged list with extend()method
        merged_arr.extend(arrB[arrB_index:])
    else:
        merged_arr.extend(arrA[arrA_index:])

    return merged_arr


    # test below to make sure they're merging properly
arrA = [1, 3, 5]  # remember we are assuming these are sorted already!
arrB = [2, 4, 6]  # so make your tests sorted lists!!!
print(merge(arrA, arrB))
# works


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:  # check to see if the array has at least 1 element, if it DOES, its sorted
        return arr  # ^ so it will just return the sorted array of length 1
    # from index 0 until the middle #dont forget to use int div //
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])  # from the middle to the end
    # ^ split the list in half and create 2 new variables called left & right
    # ^ called the merge_sort func recursively on each
    # call the merge helper function from above to put the 2 lists back together sorted
    return merge(left, right)


print(merge_sort([2, 12, 8, 6, 14, 3, 1]))  # test


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
