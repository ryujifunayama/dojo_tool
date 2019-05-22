for i in range(1,100+1):
    mod_fizz = i % 3
    mod_buzz = i % 5
    if(mod_fizz == 0):
        print("fizz", end="")
    if(mod_buzz == 0):
        print("buzz", end="")
    if(mod_fizz != 0 and mod_buzz != 0):
        print(i, end="")
    print("\n", end="")
