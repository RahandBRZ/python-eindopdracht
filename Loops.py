# Beginwaarden
monster_health = 150
player_damage = 25
aantal_aanvallen = 0
# Val het monster aan zolang het health heeft
while monster_health > 0:
    monster_health -= player_damage
    aantal_aanvallen += 1 
    # Health mag niet on 0
    if monster_health < 0:
        monster_health = 0
        # Print de overgebleven health
    print("Monster health:", monster_health)

# Print het aantal aanvallen
print("Het monster is verslagen!")
print("Aantal aanvallen:", aantal_aanvallen)