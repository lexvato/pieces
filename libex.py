# My first Library
# Multi, Factorial, Median

# Multiplies two numbers
def multi(a,b): 
    cont = 0
    result = 0
    while cont<b:
        cont += 1
        result+=b
    return result

# Function for factorial
def factorial(factor): # Factor is the number for the factorial
    cont = factor
    result = 1 # Accumulates the result

    while cont>0:
        result = cont * result
        cont -= 1
        
        
    return result

# Calculate median
def median(data):
    result = 0 # Defining the result variable and cleaning it
    lenarr = len(data) # getting the size of the array of data
    
    # Process the sum of data
    for element in data:
        ho = element.strip()
        
        if ho != '':
            ho = int(ho)
            result += ho # Adding each element in result
    
    result = result/lenarr # Calculating the median
    return result

# Reverses a word
def flip(str1):
    strlen = len(str1) # Length of string
    str2 = ""
    
    while strlen>0:
        str2 += str1[strlen-1]
        strlen -= 1
    return str2

# Eliminates blanks
def trimmer(str1, strwrd = " "):
    strlen = len(str1) # Length of string
    str2 = "" # Defines str2 empty
    
    for element in str1:
        if element != strwrd:
            str2 += element
    return str2


# Count Patterns
def patterncheck(str1, pattern):
    counter = 0
    
    for element in str1:
        if element.lower() == pattern:
            counter += 1
    return counter

def fullpatterncheck(str1, pattern):
    counter = 0
    strlen = len(str1) # Length of a string
    ptrlen = len(pattern) # Getting the size of the pattern
    ptrcnt = 0
    
    while counter < strlen:
        patternsearch = str1[counter:counter + ptrlen]
        
        if patternsearch == pattern:
            ptrcnt += 1
            
        counter += 1
        
    return ptrcnt


def palindromecheck(str1):
    strflipped = flip(str1) # Flipping the word 
    if str1 == strflipped:
        return True
    else:
        return False
