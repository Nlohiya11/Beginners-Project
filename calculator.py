def add(x, y):
    return x + y


def substract(x, y):
    return x-y


def multiplication(x, y):
    return x*y


def division(x, y):
    return x/y


def power(x, y):
    return x**y


calculator = {
    "+": add, "-": substract, "*": multiplication, "/": division, "^": power
}
for function in calculator:
    print(function)
should_continue = True
a = float(input("First number is : "))
while should_continue:
    choice1 = input("Choose any operation from list showing in first screen : ")
    b = float(input("Second number is : "))
    function = calculator[choice1]
    answer = function(a, b)
    print(f"{a} {choice1} {b} = {answer}")
    if input("Do you want to continue calculating? y/n :") == "y":
        if input("do you want to go ahead with the answer or restart the calculator ? y for going with same no/n for "
                 "restarting : ") == "y":
            a = answer
        else:
            a = float(input("First number is : "))
    else:
        print("Thanks for using my calculator")
        should_continue = False
        