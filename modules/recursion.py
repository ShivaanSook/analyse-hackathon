def sum_array(array):
    
    '''
    Return the sum of all the items in the array.
	
	Args:
		array (iterable) : An iterable object consisting of uniform data types.

	Returns:
		   int or float : The numerical return type depends on the type 
		   				  of elements in the array.

	Examples:
		>>> sum_array([1,2,3,4,5])
		15

		>>> sum_array([1,2.5,3])
		6.5
	
    '''
    if len(array) == 0:
            return 0
    else:
            return array[-1] + sum_array(array[:-1])


#-------------------------------------------------------------

def fibonacci(n):
    
    '''
    Return the n'th term in the fibonacci sequence
	
	Args:
		n (int) : The integer position of the desired term
				  within the Fibonacci sequence.

	Returns:
		   int : The n'th term in the Fibonacci sequence.

	Examples:
		>>> fibonacci(0)
		0
		>>> fibonacci(1)
		0
		>>> fibonacci(5)
		3
    '''
    if n > 2:
        return fibonacci(n-2) + fibonacci(n-1)
    elif n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return 0


#-------------------------------------------------------------      

def factorial(n):
    
    '''
    Return n!
	
	Args:
		n (int) : The integer to find the desired factorial value.

	Returns:
		   int : The factorial based on argument n.

	Examples:
		>>> factorial(0)
		0
		>>> factorial(3)
		6
		>>> factorial(5)
		120
    '''
	if n == 1:
		return n
	elif n == 0:
		return 0
	else:
		return n * factorial(n-1) 

#-------------------------------------------------------------  

def reverse(word):
    
    '''
    Return the given word in reverse.

	Args:
		word (str) : The desired word to be reversed.

	Returns:
		   str : The given word in reverse.

	Examples:
		>>> reverse('abcde')
		'edcba'
		>>> reverse('tom')
		'mot'
		>>> reverse('honey')
		'yenoh'
    '''

    if len(word) == 0:
            return word
    else:
            return word[-1] + reverse(word[:-1])          

#-------------------------------------------------------------             