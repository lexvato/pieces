import libex as app

Menu = """
Available functions
------------------------
1) Multiply two numbers
2) Calculate the factorial
3) Calculate the median
4) Reverse a word
5) Eliminate blank spaces in sentences
6) Check for patterns in sentences
7) Check if a word is a palindrome or not
"""
print(Menu)

option = int(input("Please choose a function to run:"))



if option == 1:
    a = input("Write a number to multiply:")
    b = input("Write the multiplier number:")
    a = int(a)
    b = float(b)
    
    print("Result:",app.multi(a,b))
    
elif option == 2:
    factor = input("Write a number:")
    factor = int(factor)
    print("Factorial is:",app.factorial(factor))

elif option == 3:
    data = input("Type any quantity of numbers seperated by a space:")
    print("Median:",app.median(data))
    
elif option == 4:
    str1 = input("Write a word:")
    print("Flipped word:",app.flip(str1))
    
elif option == 5:
    str1 = input("Write words with a lot of spaces between them:")
    #pattern = input("Pattern:")
    print("Clean string:",app.trimmer(str1)) # remember to write ,pattern next to str1
    
elif option == 6:
    str1 = input("Write a sentence:")
    pattern = input("Pattern to search for:")
    print("Patterns found:",app.fullpatterncheck(str1, pattern))

elif option == 7:
    str1 = input("Write a word:")
    result = app.palindromecheck(str1)
    
    if result:
        print("Its a Palindrome!")
    
    else:
        print("Its not a Palindrome :(")