
import datetime

def decorator_function(original_function):
    """ Decorator that caches result of function calls"""

    dictionaryFunc = original_function.__globals__

    def wrapper_function(*arg, **kwarg):
        
        if not arg in dictionaryFunc:
            dictionaryFunc[arg] = {}

        dictionary = dictionaryFunc[arg]

        dictionary['counter'] = (dictionary['counter'] + 1) % 10 if 'counter' in dictionary else 0

        if (dictionary['counter'] == 0 or (datetime.datetime.now() - dictionary['last_update_time']).total_seconds() > 300):
            
            dictionary['cache'] = original_function(*arg, **kwarg) 
            dictionary['counter'] = 0 
            dictionary['last_update_time'] = datetime.datetime.now()
    
            print ("Cache updated : ", dictionary['cache'])
        else:
            print ("From cache    : ", dictionary['cache'])
        
        return dictionary['cache']

    return wrapper_function

@decorator_function
def Fibonacci(n):
    """ Calculates the nth fibonacci number."""
    if n < 2:
        return n
    else:
     return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == '__main__':

    for i in range (12):
        Fibonacci(6)
        Fibonacci(8)