import random
import time

def generate_sorted_data(size):
    """
    This function generates random intgers between 1 and 100 of size dtermined by user input and uses 
    insertion sort to sort the data
    """
    #Generates random integers of size inputed by user
    array = []
    for _ in range(size):
        array.append(random.randint(1, 100))
    
    # Sort the array using insertion sort
    if len(array) <= 1:
        print(array)
    else:
        idx=0
        for idx in range(1, len(array)):  
            value = array[idx]     
            subidx = idx - 1                  

            while subidx >= 0 and array[subidx] > value:
                array[subidx + 1] = array[subidx]  
                subidx = subidx - 1
            array[subidx + 1] = value

        return array
    

def binary_search(sorted_array, target1, start=0, end=None):
    """
    This function does a binary search to locate and return a target value.
    """
    if end is None:
        end = len(sorted_array) - 1
    # Uses binary search to find target
    if start > end:
        return None
    mid = (start + end) // 2
    if sorted_array[mid] == target1:
        return mid 
    elif sorted_array[mid] < target1:
        return binary_search(sorted_array, target1, mid + 1, end)
    else:
        return binary_search(sorted_array, target1, start, mid - 1)
    
def merge_sort(large_data):
    """
    This function uses recursion merge sort to sort the arra large_data.
    """
    if len(large_data) <= 1:
        return large_data
    else:
        even = []
        odd =[]
        for index in range(len(large_data)):
            if index % 2 == 0:
                even.append(large_data[index])
            else:
                odd.append(large_data[index])
        evenidx = merge_sort(even)
        oddidx = merge_sort(odd)

    sorted_array = [] 
    even_index = 0 
    odd_index = 0  
   
    while even_index < len(evenidx) and odd_index < len(oddidx):
        # Compare and add the smaller one to the sorted list
        if evenidx[even_index] < oddidx[odd_index]:
            sorted_array.append(evenidx[even_index])
            even_index += 1 
        else:
            sorted_array.append(oddidx[odd_index])
            odd_index += 1  
    # Add remaining elements 
    while even_index < len(evenidx):
        sorted_array.append(evenidx[even_index])
        even_index += 1

    while odd_index < len(oddidx):
        sorted_array.append(oddidx[odd_index])
        odd_index += 1 

    return sorted_array
 
     
def linear_search(large_data, target):
    """
    This function uses linear search to locate a target value.
    """
    for index in range(len(large_data)):
        if target == large_data[index]:
            return index
    return -1 

def timer(large_data):
    """
    This function measures and prints the time taken to perform linear and binary search on
    a dataset.
    """
    target = 72
    sorted_array = merge_sort(large_data)
    
     # Measure time for linear search
    start = time.perf_counter()
    linear_result = linear_search(sorted_array, target)
    end = time.perf_counter()
    elapsed_linear_time = end - start
    print(f"Linear_time: {elapsed_linear_time}")

    # Measure time for binary search 
    start = time.perf_counter()
    binary_result = binary_search(sorted_array, target)
    end = time.perf_counter()
    elapsed_binary_time = end - start
    print(f"binary_time: {elapsed_binary_time}")

def main():
    """
      This function asks the user for the size of the data and a target value. 
      It then generates and sorts the data using both insertion sort and merge sort. 
      The function searches for the target value using both binary search and linear search. 
      Finally, it measures and prints the elapsed time for both binary and linear searches.
    """  

    # Input size of the array
    size = int(input("Enter size of the array: "))
    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]

    # Generate and sort the data with insertion
    sorted_array = generate_sorted_data(size)
    print(sorted_array)
    
    # Input target and locate index of target
    target1 = int(input("Enter the target value you are looking for: "))
    result_index = binary_search(sorted_array, target1)
    print(result_index)
    
    # Sorts data using merge sort
    mergesort1 =  merge_sort(large_data[:10])
    mergesort = merge_sort(large_data)
    print(mergesort1)
    print(mergesort)

    #Gives elapsed time of binary and linear search
    timer(large_data)


if __name__ == "__main__":
    main()


# Additional Question for Reflection:
"""
How does the choice of sorting algorithm impact the performance of searching algorithms? 

The choice of sorting algorithm impacts search performance by determining how quickly data can be organized for searches that use sort like
binary search. Faster sorting methods, such as merge sort, allow quicker sorting than insertion sort, increasing overall search speed.

Discuss why binary search is faster than linear search on large, sorted data and how efficient sorting methods enhance overall performance.

Binary search is faster than linear search because it splits a sorted data in half and discard the other half as it surely doesn't have
the targeted value we are looking for while for linera search we will have to compare the target value with every next values in the data until
we find the target value. Linear search has O(n) complexity while binary uses O(logn) complexity which is faster than linear search.
Efficient sorting methods enhance overall performance by reducing the time needed to sort and search for a value.

"""