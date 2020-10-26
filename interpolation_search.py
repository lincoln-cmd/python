# Interpolation Search
'''
// The idea of formula is to return higher value of pos
// when element to be searched is closer to arr[hi]. And
// smaller value when closer to arr[lo]
pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

arr[] ==> Array where elements need to be searched
x     ==> Element to be searched
lo    ==> Starting index in arr[]
hi    ==> Ending index in arr[]
'''




'''
my answer
'''


def interpolation_search(arr, x):
    length = len(arr)
    low = 0
    high = length - 1
    
    while arr[low] <= x and arr[high] >= x and low <= high:
        if arr[low] == arr[high]:
            if arr[low] == x:
                return low
            else:
                return -1
            
        
        if arr[low] == x:
            return low
        elif arr[high] == x:
            return high
        else:
            low += 1
            high -= 1
            
        if low >= high:
            return -1
        
    return -1
        
            
            
        
    
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    x = 11
    inter = interpolation_search(arr, x)
    print(inter)







'''
answer
'''


# Python program to implement interpolation search 
  
# If x is present in arr[0..n-1], then returns 
# index of it, else returns -1 
def interpolationSearch(arr, n, x): 
    # Find indexs of two corners 
    lo = 0
    hi = (n - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo; 
            return -1; 
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x: 
            lo = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            hi = pos - 1; 
      
    return -1

if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    n = len(arr)
    x = 16
    inter = interpolationSearch(arr, n, x)
    print(inter)