"""test1"""

def main():
    """test1"""
    grade1 = float(input())
    if 0 <= grade1 < 1:
        print("I'm so sad")
    elif 1 <= grade1 < 2:
        print("%.2f" %(4 - grade1))
    else:
        print("I'm so happy")
main()
