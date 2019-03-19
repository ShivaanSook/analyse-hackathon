def bubble_sort(items):
    
    '''
    Return array of items, sorted in ascending order

	Args:
		items (iterable) : array of items to be sorted.

	Returns:
		   iterable : The given array sorted using the
		   			  "Bubble" sorting method.

	Examples:
		>>> bubble_sort([3,4,15,6,9,10])
		[3, 4, 6, 9, 10, 15]

		>>> bubble_sort([10,40,20,15,99])
		[10, 15, 20, 40, 99]

		>>> bubble_sort([5,3,6,8,1,90])
		[1, 3, 5, 6, 8, 90]

    '''
    
    for x in range(len(items)):
        swapped = False
        
        for y in range(len(items) - x - 1):
            if items[y] > items[y+1]:
                items[y],items[y+1] = items[y+1],items[y]
                swapped = True
            
        if swapped == False: break
    return items

#-------------------------------------------------------------             

def merge_sort(items):
    
    '''
    Return array of items, sorted in ascending order

	Args:
		items (iterable) : array of items to be sorted.

	Returns:
		   iterable : The given array sorted using the
		   			  "Merge" sorting method.

	Examples:
		>>> merge_sort([4,6,3,10,14])
		[3, 4, 6, 10, 14]

		>>> merge_sort([45,3,67,23,7])
		[3, 7, 23, 45, 67]

		>>> merge_sort([10,80,56,34,68])
		[10, 34, 56, 68, 80]

    '''
    if len(items) > 1:
        midpoint = len(items)//2
        left = items[:midpoint]
        right = items[midpoint:]
        
        merge_sort(left)
        merge_sort(right)
        
        x = y = z = 0
        
        while (x < len(left)) and (y < len(right)):
            if left[x] < right[y]: items[z] = left[x]; x += 1; z += 1;
            else: items[z] = right[y]; y += 1; z += 1;
        
        while x < len(left): items[z] = left[x]; x += 1; z += 1;
            
        while y < len(right): items[z] = right[y]; y += 1; z += 1;
            
    return items

#-------------------------------------------------------------       

def quick_sort(items):
    
    '''
    Return array of items, sorted in ascending order

	Args:
		items (iterable) : array of items to be sorted.

	Returns:
		   iterable : The given array sorted using the
		   			  "Merge" sorting method.

	Examples:
		>>> quick_sort([34,56,24,73,45,200])
		[24, 34, 45, 56, 73, 200]

		>>> quick_sort([45,3,67,23,7])
		[3, 7, 23, 45, 67]

		>>> quick_sort([10,80,56,34,68])
		[10, 34, 56, 68, 80]

    '''
    if len(items) > 1:
        pivot = items[-1]
        return quick_sort([x for x in items[:-1] if x < pivot]) + [pivot] + quick_sort([x for x in items[:-1] if x > pivot])
    else: return items

#-------------------------------------------------------------      
