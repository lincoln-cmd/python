# Heap Sort

'''
my answer
'''

def heap(arr, index, size):
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    
    if arr[left_child] < size and arr[left_child] > arr[largest]:
        largest = left_child
    if arr[right_child] < size and arr[right_child]> arr[largest]:
        largest = right_child
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heap(arr, index, size)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2  - 1, -1, -1):
        heap(arr, i, n)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap(arr, 0, i)
            
    return arr

if __name__ == "__main__":
    arr = [1,10,5,4,9]
    he = heap_sort(arr)
    print(he)
  
    # result = [10,9,5,4,1]



'''
answer
'''

# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# Driver code to test above 
arr = [1,10,5,4,9] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra 