# Binary Search

'''
my answer
'''

def binary_search(arr, x):
    length = len(arr)
    mid = length // 2
    
    while mid >= 1:
        if arr[mid] < x:
            mid += mid // 2
        elif arr[mid] > x:
            mid -= mid // 2
        else:
            return mid
        

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    x = 6
    bina = binary_search(arr, x)
    print(bina)
    
    
    
'''
my answer2
'''
def binary_search(arr, x):
    length = len(arr)
    left = 0
    right = length - 1
    
    mid = length // 2
    
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        left = mid + 1
        right = length
        arr = arr[left:right]
        print(arr, mid)
        return binary_search(arr, x)
    elif arr[mid] > x:
        left = 0
        rigth = mid - 1
        arr = arr[left:right]
        return binary_search(arr, x)
    else:
        return -1
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    x = 7
    bina = binary_search(arr, x)
    print(bina)
    
    
'''
my answer3
'''
def binary_search(arr, left, right, x):
    
    if right > left:
#        length = len(arr)
#        mid = length // 2
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, right, x)
        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)
    return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    left = 0
    right = len(arr) - 1
    x = 1
    bina = binary_search(arr, left, right, x)
    print(bina)
    
    
    
'''
my answer4
'''

def binary_search(arr, left, right, x):
    while left < right and arr[left] <= x and arr[right] >= x:
        if arr[left] == x:
            return left
        elif arr[right] == x:
            return right
        else:
            left += 1
            right -= 1
            return binary_search(arr, left, right, x)
    return -1
        
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    left = 0
    right = len(arr) - 1
    x = 3
    bina = binary_search(arr, left, right, x)
    print(bina)
    
    
    
############################################################################
############################################################################
############################################################################   
    
    
    
    
'''
answer1
'''
# Python3 Program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 
    
    
    

'''
answer2
'''
# Python3 code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1
  
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")