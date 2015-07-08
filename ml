#!/usr/bin/env python3
import colors as c
from utils import ask
print(c.clear)
print(c.yellow + 'welcome to  the awesome MadLib quiz')


text = '''
once my pet {animal} was running around my {a_place_in_your_house}
with a {explosive_thing} straped to {his_or_her} back and then i lit the 
{same explosive you chose before.'''


words = {
    "animal" :{},
    "a place in your house" :{},
    "explosive thing" :{},
    "his or her" :{},
    "same exsplosive you chose before" :{}
}

answers = {}
for key in words:
    
    answer = ask("Enter " + key)







