dwarfs = ["Doc", "Dopey", "Bashful", "Grumpy"]

def roll_call_dwarves(dwarfs):
    for dwarf in dwarfs:
        
        print(f'{dwarfs.index(dwarf) + 1}. {dwarf}')
    pass
roll_call_dwarves(dwarfs)

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def summon_captain_planet(calls):
    [print(call.capitalize() + "!" )for call in calls]
    return [call.capitalize() + "!" for call in calls]

summon_captain_planet(planeteer_calls)
#=> ["Earth!", "Wind!", "Fire!", "Water!", "Heart!"]


def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4: 
            print(word)
            print("True")
            return True
        else:
            print(word)
            print("False")
    return False
  
 
        
short_words = ["puff", "go", "two"]
long_planeteer_calls(short_words)
#=> False

assorted_words = ["axe", "earth", "wind", "fire"]
long_planeteer_calls(assorted_words)
#=> True

cheeses = ["cheddar", "gouda", "camembert"]

def find_the_cheese(foods):
    for food in foods:
        if food in cheeses:
            print(f"'{food}' is in the list.")
            return food
        else:
            print(f"'{food}' is not in the list.")


snacks = ["crackers", "gouda", "thyme"]
find_the_cheese(snacks)
#=> "gouda"

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
find_the_cheese(soup)
#=> "cheddar"