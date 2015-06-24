
import colors as c
from utils import ask

intro = c.magenta + '''
Welcome to my fnaf quiz

lets see what you know about this all of the fnaf games
'''

def q1():
    answer = ask("in fnaf2, how many characters are there?")
    if answer == "11":
        return True
    return False

def q2():
    answer = ask("who killed the children?")
    if answer == " the purple man":
        return True
    return False

def q3():
    answer = ask("What are their fur made of?")
    if answer.startswith("smile"):
        return True
    return False

questions = [q1,q2,q3]
