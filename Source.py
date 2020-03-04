'''This project I've created to binary search algorithum ,what is binary search ? Binary search algorithum is fast search alogrithum based on the concept of divide and conquer,so here basically through this alogrithum we are returning  the index of targeted value .'''
def binarysearch(values):
    target=3
    low = 0
    high = len(values)
    while low<=high:
         mid = int((low + high)/2)
         if target==values[mid]:
            return mid
            break 
         if target>values[mid]:
            low = low+1
            continue 
         if target<values[mid]:
            high=high-1
            continue 


values = [1,2,3,4,5,6]
print(binarysearch(values))
