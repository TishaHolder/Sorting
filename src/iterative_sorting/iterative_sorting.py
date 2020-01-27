# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    temp = 0
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i

        #1st time through => store the first value as the smallest element we have seen so far
        #i or current index will always be the smallest index on subsequent iterations and used for comparisons 
        #because the indexes before were already determined to be smaller than the current index
        smallest_index = cur_index 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        #if item at arr[j] which the 1st time through will be arr[1] is < arr[smallest_index]
        #arr[smallest_index] the 1st time though is arr[0]
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:               
                smallest_index = j #1st time through=> now the smallest index will be pointing to 1      
            
        # TO-DO: swap  
        #if arr[i] (i is cur_index) != smallest_index (j)
        #
        if cur_index != smallest_index:   
            temp = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):    

    #double loops so that the program can go through each iteration of the array n(the length of the array) times
    #if there are 4 items in an array, the program will iterate through the array a total of 16 times
    #outer loop will execute the inner loop 4 times
    for i in range(0, len(arr) - 1):  
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]: #if item at j is 5 and item at j+1 is 3
                temp = arr[j] #put 5(larger num) in temp
                arr[j] = arr[j + 1] #place the smaller value at j+1 (3) where j was
                arr[j+1] = temp #then put 5(larger value) that was in temp in position j+1
    
    return arr       

    


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr