# Recursive Insertion Sort 

'''
my answer
'''

def recursive_insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        min_ = i
        for j in range(i - 1):
            if arr[j] > arr[i]:
                min_ = j
                arr[j], arr[min_] = arr[min_], arr[j]
    return recursive_insertion_sort(arr)        

#if __name__ == "__main__":
    arr = [5,9,10,8,6,4,7,3,1,2]
    ris = recursive_insertion_sort(arr)
    print(ris)






'''
answer
'''

# Recursive Python program for insertion sort 
# Recursive function to sort an array using insertion sort 
  
def insertionSortRecursive(arr,n): 
    # base case 
    if n<=1: 
        return
      
    # Sort first n-1 elements 
    insertionSortRecursive(arr,n-1) 
    '''Insert last element at its correct position 
        in sorted array.'''
    last = arr[n-1] 
    j = n-2
      
      # Move elements of arr[0..i-1], that are 
      # greater than key, to one position ahead 
      # of their current position  
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j] 
        j = j-1
  
    arr[j+1]=last 
      
# A utility function to print an array of size n 
def printArray(arr,n): 
    for i in range(n): 
        print(arr[i])
  
# Driver program to test insertion sort  
arr = [12,11,13,5,6] 
n = len(arr) 
insertionSortRecursive(arr, n) 
printArray(arr, n) 
  
# Contributed by Harsh Valecha 