
def calc():
    user = input(str("State your trigonometric identities?"))

    if user == "sine":
        b = float(input("Enter value b: "))
        c = float(input("Enter value c: "))
        return sine_O (b,c)
    elif user == "cos":
        a = float(input("Enter value a: "))
        c = float(input("Enter value c: "))
        return cos_O (a,c)
    elif user == "tan":
        b = float(input("Enter value b: "))
        a = float(input("Enter value a: "))
        return tan_O (b,a)
    
    return "Invalid request"


# setting the trigonometric identities formulaic
# setting the logical argument of the calculator
def sine_O (b,c):
    return float(b/c)

def cos_O (a,c):
    return float(a/c)

def tan_O (b,a):
    return float(b/a)

print(calc())
