# Insertion Sort

'''
my answer
'''

def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        min_ = i
        for j in range(i):
            if arr[j] > arr[i]:
                min_ = j
                arr[i], arr[min_] = arr[min_], arr[i]
    return arr




if __name__ == "__main__":
    arr = [8,4,6,1,5,7,9,3,2,10]
    ins = insertion_sort(arr)
    print(ins)
    
    
'''
answer
'''

# Python program for implementation of Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
                print(arr)
        arr[j + 1] = key
        print(j, key, arr)
  
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 
  
# This code is contributed by Mohit Kumra 