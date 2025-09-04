def shutdown(y):
    '''would you like to shutdown ur device (50/50 chance the pc gets shutdown either that or u get 360 no scoped)'''
    if y=="yes":
        print("self destruct sequence intiated")
    else:
        print("aight ur getting 360 no scoped now")
print(shutdown.__doc__)
y = input("yes or no? ")
print(shutdown(y))