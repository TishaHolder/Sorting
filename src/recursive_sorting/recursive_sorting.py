import math

# TO-DO: complete the helper function below to merge 2 sorted arrays
# merge function - takes two sorted arrays
def merge( arrA, arrB ):
    #elements = len( arrA ) + len( arrB )
    #merged_arr = [0] * elements
    results = [] #array to store the result of merging the two arrays passed in

    # TO-DO
    indexA = 0 #arrA index
    indexB = 0 #arrB index

    #while not at the end of either arrA or arrB
    #this first loop only applies if we are looping through both at the same time
    #if the end of either arrA or arrB is reached the loop will exit
    while indexA < len(arrA) and indexB < len(arrB):
        #if the item in the second array is greater than the item in the first array
        #add the item in the first array (smaller value) to the results arrary
        #increment the array index with the smaller element that was moved to results
        if arrB[indexB] > arrA[indexA]:
            results.append(arrA[indexA])
            indexA = indexA + 1
        else:
            #if the item in the first array was larger
            #add the item in the second array to results and increment the second array index
            results.append(arrB[indexB])
            indexB = indexB + 1

    #if arrB reaches the end before arrA
    #push in all remaining values from arrA to results
    while indexA < len(arrA):
        results.append(arrA[indexA])
        indexA = indexA + 1

    #if arrA reaches the end before arrB
    #push in all remaining values from arrB to results
    while indexB < len(arrB):
        results.append(arrB[indexB])
        indexB = indexB + 1

    return results
    #return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# keep breaking up the array into halves until you have arrays that are empty or have one element
def merge_sort( arr ):
    # TO-DOs
    #every recursive function has a base case and a recursive case
    #recursive case continually calls the function or itself
    #base case ends the recursive calls

    #keep calling merge_sort until the length of the array is 1 or 0
    #base case
    if len(arr) <= 1:
         return arr

    midpoint = math.floor(len(arr)/2)

    # recursive case
    # keep calling merge_sort and breaking each half into halves
    # keep going recursively until arrays are empty or have one element (base case: <= 1)
    leftSide = merge_sort(arr[slice(0, midpoint)]) #midpoint is not inclusive 
    rightSide = merge_sort(arr[slice(midpoint, len(arr))]) #len(arr) is not inclusive

    #once we have those small arrays we merge them back using our merge function
    return merge(leftSide, rightSide)     

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
