from monster_class import *

# function('input') == 'what you want out'
#
# def make_dough(wheat):
#     return 'dough'
#
# print(make_dough('wheat') == 'dough')


#
# Behaviours of monsters (methods)
# - As a user I should be able to create a monster from Monster()
monster_example = Monster()

print("- Monsters should sleep --> respond back with 'zzzzz'")
print(monster_example.sleep() == 'zzzzz')
print('------------------')

print("- Monsters should eat --> something including 'Nom nom'")
print(monster_example.eat() == 'Nom nom')
print('------------------')

# - Monsters should scare_attack ---> something including 'RAAAAAHHHHH!'
print(monster_example.scare_attack == 'RAAAAAHHHHH!')
print('------------------')

# monster should be able to hide --> should return "You can't see me go back to sleep"



# - Should be able to have a skill added to list of skills
print(monster_example.add_skill('stealth') == 'stealth ' in monster_example.skills)
print('------------------')


# Looks of a monster (attributes)

print("Should have a name that is a string")
print(type(monster_example.name) == str) # check if its string
print('------------------')

# - Should have a name (str)

# We are now having a new setup
print("When we create a monster with a name 'Ringo' We get a monster with that name as an attribute")
monster_ringo = Monster('Ringo')
print(monster_ringo.name == 'Ringo')
print('------------------')

# Should have a list of skills
print(type(monster_ringo.skills) == list)
print('------------------')

# A monster should have an age as an integer

# When we create a monster with the age of 2000 years old we should get a monster with that age.
