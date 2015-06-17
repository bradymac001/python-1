
'''This is my utility room which means im smart and epic.'''

import colors as c

def ask(question):
    print(c.red + question + c.reset)
    answer = input('>' + c.base3).lower().strip()
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear) 
    name = ask("What is ur name?") 





