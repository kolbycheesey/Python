import sys

first = 1
second = 1
ans = 1

def calc():
    while(True):
        first = float(input("First number: "))
        op = int(input("What operation would you like to do:\n1. *\n2. / \n3. - \n4. +\n"))
        second = float(input("\nSecond number: "))
        ##ans = options[op]
        if(op == 1):
            ans = first * second
            print("\nAnswer to ",first, "*",second, " is: ", ans)
        elif(op == 2):
            ans = first / second
            print("\nAnswer to ",first, "/",second, " is: ", ans)
        elif(op == 3):
            ans = first - second
            print("\nAnswer to ",first, "-",second, " is: ", ans)
        elif(op == 4):
            ans = first + second
            print("\nAnswer to ",first, "+",second, " is: ", ans)
        else:
            print("\n\nYou didn't pick a correct option try again!!!\n\n")
        
        quit = input("Do you want to quit? Y/N: ")
        if(quit == 'Y' or quit == 'y'):
            return
    

if __name__ == '__main__':
    print('\nWelcome to the Calculator!\n')
    calc()