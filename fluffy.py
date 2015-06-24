
import colors as c
from utils import ask

intro = c.magenta + '''
Welcome tothe pink fluffy unicorns quiz

lets test your knowledge of what you learned so far.
'''

def q1():
    answer = ask("What color are the unicorns?")
    if answer == "pink":
        return True
    return False

def q2():
    answer = ask("What are the unicorns dancing on?")
    if answer == "rainbows":
        return True
    return False

def q3():
    answer = ask("What are their fur made of?")
    if awnswer.startswith("smile"):
        return True
    return False

questions = [q1,q2,q3]
