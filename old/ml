#!/usr/bin/env python3
import colors as c
from utils import ask

text = '''My Crazy Pet

once my pet {animal} was running around my {a place in your house}
with a {explosive thing} straped to {his or her} back and then i lit the 
{same explosive you chose before} and went flying out of my front door
and then exploded in my neighbors front yard. The End''' 


words = {
    "animal" : None,
    "a place in your house" : None,
    "explosive thing" : None,
    "his or her" : None,
    "same explosive you chose before" : None,
}

for key in words:
    words[key] = c.red + ask(key.rstrip('0123456789') + ': ') + c.reset

print(c.clear + text.format(**words))







