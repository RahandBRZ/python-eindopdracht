# Choose a character class
player_class = "Warrior"
 
# Check the character class
match player_class:
    case "Warrior":
        health = 150
        damage = 20
 
    case "Mage":
        health = 80
        damage = 35
 
    case "Archer":
        health = 100
        damage = 25
 
    case "Rogue":
        health = 90
        damage = 30
 
    # Bonus classes
    case "Knight":
        health = 170
        damage = 15
 
    case "Ninja":
        health = 85
        damage = 40
 
    # Unknown character
    case _:
        health = 0
        damage = 0
        print("Unknown character class!")
 
# Print results
if player_class in ["Warrior", "Mage", "Archer", "Rogue", "Knight", "Ninja"]:
    print("Character class:", player_class)
    print("Health:", health)
    print("Damage:", damage)