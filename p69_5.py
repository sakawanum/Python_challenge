"""
def flo(string):
    try:
        string = float(string)
            print(string)
        except ValueError:
            print(Invalid input.)
"""


#答え
def convert(string):
    try:
        return float(string)
    except ValueError:
        print("could not convert the string to a float.")
c = convert("55.0")
print(c)
