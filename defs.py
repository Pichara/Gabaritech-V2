from time import sleep

def linha(): 
    """\n | linha | \n. Apenas"""
    print("\n" + "=+"*30 + "=\n")

def color(x, color):
    """Transformar string em outra cor: Green, Red, Yellow and Blue"""

    original = '\033[0;0m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    color = color.upper()
    if color == "RED":
        return(red + x + original)
    elif color == "GREEN":
        return(green + x + original)
    elif color == "YELLOW":
        return(yellow + x + original)
    elif color == "BLUE":
        return(blue + x + original)
    else:
        print("We haven't this color")

def choices(how_many):
    """It uses by parameters the quantity of phrase that need to be chosen, 
    then put with a lot of tratament issues the options
    Ex: how_many = 3\n
    return: (1) or (2) or (3): """

    ask = "(1):"
    for i in range(how_many - 1):
        ask = ask.replace(":", f" or ({i + 2}):")

    #determining the list to confirm the return
    list_with_choices = []
    for i in range(how_many):
        list_with_choices.append(i + 1)
    
    #inputing the chosen and returning it without errors
    while True:
        try:
            choice = int(input(color(ask, "Yellow")))
            if choice in list_with_choices:
                return choice
            else:
                print(color("Only choice the OPTIONS above", "RED"))
                sleep(1)
                continue
        except:
            print(color("Only NUMBERS please!! Let's Try again...", "RED"))
            sleep(1)
            continue

def find_answer_in_string(x):
    """To know what answer are in the string"""

    if "A" in x:
        return("A")
    if "B" in x:
        return("B")
    if "C" in x:
        return("C")
    if "D" in x:
        return("D")
    if "E" in x:
        return("E")

    