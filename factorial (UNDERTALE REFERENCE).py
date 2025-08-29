def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
x = int(input("what number do u want he factorial (UNDERTALE REFERENCE!?!?!?) of: "))
# x is the number you inputted
print("the factorial of x is: ", factorial(x))