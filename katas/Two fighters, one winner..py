class Kata():

    def declare_winner(fighter1, fighter2, first_attacker):
        # Code your solution here
        if first_attacker == fighter1.name:
            while True:
                fighter2.health -= fighter1.damage_per_attack
                fighter1.health -= fighter2.damage_per_attack
                if fighter2.health <= 0:
                    return fighter1.name
                elif fighter1.health <= 0:
                    return fighter2.name
        else:
            while True:
                fighter1.health -= fighter2.damage_per_attack
                fighter2.health -= fighter1.damage_per_attack
                if fighter1.health <= 0:
                    return fighter2.name
                elif fighter2.health <= 0:
                    return fighter1.name






