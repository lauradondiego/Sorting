# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        # assume i is the smallest value [index 0]
        lowest_index = i # holds the index position of the lowest value
        # setting the min value to the i position
        # TO-DO: find next smallest element
        for j in range(i + 1, len(arr)):
            # j is the index that starts right after i
            # so now you are comparing [i and j] directly to the right
            if arr[j] < arr[lowest_index]:
                # look at j and compare it to [i(aka the cur_index)]
                # if j is lower than i, then the smallest index is lower
                lowest_index = j
                # ^ then reset the smallest index to that j index
        if i != lowest_index:
            # if we find an item that has a lower value than lowest_index
            arr[i], arr[lowest_index] = arr[lowest_index], arr[i]
            # then we need to swap

    return arr


print(selection_sort([3, 8, 4, 12, 1, 92]))  # test
# works

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    sorted = False
    # ^ sorted variable = false bc the list is not sorted now
    # ^ we will use this variable again inside the loop, to break us out when the list has been sorted
    while not sorted:
        # ^ means while sorted variable = False (line 17)
        sorted = True
        # ^ swapped variable = false will break us out of the loop is sorted
        for i in range(len(arr) - 1):
            # ^ the -1 is because there is no number after the last one to compare, therefore you cant perform a comparison on the last number of the list
            if arr[i] > arr[i+1]:
                sorted = False
                # if item to the left is > than item to right, SWAP THEM and say sorted variable = FALSE
                # then FLIP those two items -> below
                arr[i], arr[i + 1] = arr[i+1], arr[i]
                # ^ this is literally swapping the positions of the larger w the smaller

    return arr


print(bubble_sort([4, 6, 12, 1, 5, 32]))  # test
# works


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
