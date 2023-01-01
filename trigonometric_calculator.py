
def calc():
    user = input(str("State your trigonometric identities?"))

    if user == input("sine"):
        b = float(input("Enter value b"))
        c = float(input("Enter value c"))
        return sine_O
    elif user == input("cos"):
        a = float(input("Enter value a"))
        c = float(input("Enter value c"))
        return cos_O
    elif user == input("tan"):
        b = float(input("Enter value b"))
        a = float(input("Enter value a"))
        return tan_O
    else:
        return "Invalid request"


# setting the trigonometric identities formulaic
# setting the logical argument of the calculator
def sine_O (b,c):
    return float(b/c)

def cos_O (a,c):
    return float(a/c)

def tan_O (b,a):
    return float(b/a)
