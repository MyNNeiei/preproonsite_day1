'''test1'''

def main():
    '''test1'''
    num1 = int(input())
    num2 = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    total = num1 - num2
    result = total % 3
    print("Now you have" / "", num1 / "left")
    if result == 0:
        total-10*snack1
        print("Snack number 1:", (10*snack1))
    elif result == 1:
        total-15*snack1
        print("Snack number 1:", (15*snack1))
    elif result == 2:
        total-20*snack1
        print("Snack number 1:", (20*snack1))
    else: 
        
main()