def cube(number):
    return number*number*number
def by_three(number):
    if number %3==0:
        return cube(number)
    else:
        return False
number1 = int(input("please enter a number that is divisible by three: "))
print("the number you entered cubed is:")
print(by_three(number1))