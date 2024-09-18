import random

def game_over():
    print("Game over\n")
    print("This is the end of your playthrough")
    respawn = input("If you would like to play again please type restart and hit enter")
    if respawn == "restart":
        start_adventure()
def space():
    input()
def enemy_list():
    enemy = input("Type the name of the enemy you would like to know more about \nZombie\nLion\nBear\n")
    if enemy == "Zombie":
        print("A zombie has 10 health, deals from 1-2 damage, has a speed of 5, and is rarely found alone as they often travel in groups")
        input()
    elif enemy == "Lion":
        print("A lion has 15 health, deals from 2-3 damage, has a speed of 25, and can be found in groups or alone.")
    elif enemy == "Bear":
        print("A bear has 25 health deals form 3-5 damage, has a speed of 10 and is usually found alone.")
    space()
def buy_items(health_pot, mana_pot, gold):
    answer = ""
    while answer != "e":
        answer = input(f"You have {health_pot} health potions and {mana_pot} mana potions. What items would you like to buy. You have {gold} gold remaining\n(h)Health Potion\n(m)Mana Potion\n(e)Exit Shop")
        if answer == "h":
            if gold > 14:
                health_pot += 1
                gold -= 15
        elif answer == "m":
            if gold > 9:
                mana_pot += 1
                gold -= 10
def enemy_attack(hero_health, enemy_min_damage, enemy_max_damage):
    hero_health = hero_health - random.randint(enemy_min_damage, enemy_max_damage)
    return hero_health
undead = "zombies"
def choose_action(mana, valid_action, charge, mana_pot, health_pot, speed, enemy_speed):
    while valid_action == False:
        answer = int(input(f"You have {mana} mana. Light blast costs 1 mana, Light Ray costs 5 mana, and your Ultimate Attack costs 10 mana.You can rest to regain 3 mana \n1.Light blast\n2.Light Ray\n3.Ultimate\n4.Rest\n5.Use Item"))
        print(f"Ultimate has {charge} out of 3 charges")
        if answer == 1:
            if mana > 0:
                valid_action == True
                return answer
        elif answer == 2:
            if mana > 4:
                valid_action == True
                return answer
        elif answer == 3:
            if charge > 2:
                if mana > 9:
                    valid_action == True
                    return answer
        elif answer == 4:
            valid_action == True
            return answer
        elif answer == 5:
            potion = input(f"You have {health_pot} health potions and {mana_pot} mana potions. What items would you like to use. \n(h)Health Potion\n(m)Mana Potion")
            if potion == "Health Potion":
                if health_pot > 0:
                    valid_action == True
                    return answer
            elif potion == "Mana Potion":
                if mana_pot > 0:
                    valid_action == True
                    answer = 6
                    return answer
        if valid_action == False:
                print("You cannot choose that action.")
                space()
def fight_enemy(enemy, enemy_max_damage, enemy_min_damage, enemy_hp, enemy_number, mana_pot, health_pot, speed, enemy_speed):
    enemy_dead = False
    mana = 10
    hero_health = 25
    hero_dead = False
    valid_action = False
    charge = 0

    print(f"{enemy_number} {enemy} attack you.")
    while enemy_dead == False:
        choice = choose_action(mana,valid_action,charge, mana_pot, health_pot, speed, enemy_speed)
        #Light Blast attack
        if choice == 1:
            hit = random.randint(1,100)
            if hit > enemy_speed:
                enemy_hp = enemy_hp - random.randint(1,3)
                mana -= 1
                charge += 1
            else:
                print(f"The {enemy} dodged your attack")
                charge += 1
                mana -= 1
        #Light Ray enemy_attack
        elif choice == 2:
            hit = random.randint(1,100)
            if hit > (enemy_speed / 2):
                enemy_hp = enemy_hp - random.randint(4,6)
            else:
                print(f"The {enemy} dodged your attack")
            mana -= 5
            charge += 1
        #Ultimate Attack
        elif choice == 3:
            charge = 0
            enemy_hp = enemy_hp - random.randint(20, 25)
            mana -= 10
        #Resting
        elif choice == 4:
            mana += 4
            hero_health += random.randint(1,3)
        elif choice == 5:
            hero_health += 15
        elif choice == 6:
            mana += 15

        #Checking if the enemy is dead
        if enemy_hp < 1:
            if enemy_number > 1:
                enemy_number -= 1
                print(f"You've killed the first {enemy}")
                enemy_hp = 10
            else:
                enemy_dead = True
                print("Congraulations, you killed the zombie")

        #Enemy attack
        elif enemy_hp > 0:
            print(f"The {enemy} has {enemy_hp} health left")
            print(f"The {enemy} attacks you")
            for i in range(0, 2):
                hit = random.randint(1, 100)
                if hit > speed:
                    hero_health = enemy_attack(hero_health, enemy_min_damage, enemy_max_damage)
                else:
                    print("You dodged the attack")
            print(f"You have {hero_health} health left")
            space()
        if hero_health < 1:
            hero_dead = True
            enemy_dead = True
        if mana > 10:
            mana = 10
    return hero_dead
def start_adventure():
    enemy_max_damage = 0
    enemy_min_damage = 0
    enemy_dead = False
    hero_health = 15
    gold = 50
    Var1 = input("Hello, This is a choose your own adventure game. if you would like to start, Type Start and hit enter")
    if Var1 == "Start":
        stage = input("Where would you like to start. \nTutorial\nStage 1")
        if stage == "Tutorial":
            print("Ok, you will now be asked to fight a zombie. To select an action, type the number in front of the action you would like to take.")
            space()
            dead = fight_enemy(undead, 2, 1, 10, 2, 0, 0, 25 , 5)
            if dead == False:
                print("You have successfully defeated the zombie")
                print("Whenever the option bestiary shows up, you can select that action to see the stats of all of the different enemies")
                space()
                print("The game starts in a small town shop")
                print("You will start with 50 gold to buy items")
                gold = 50
                space()
                print("To use an item during battle, take the Use Item action and type in the name of the item you want to use. Make sure to type it exactly how it is spelled in the menu.")
                space()
                print("This shop is selling potions. A health potion restores 15 health and costs 15 gold and a mana potion restores 15 mana and costs 10 gold. To buy a item, select that item if you have enough gold.")
                space()
                health_pot = 0
                mana_pot = 0
                buy_items(health_pot, mana_pot, gold)
                dead = fight_enemy(undead, 2, 1, 10, 2, mana_pot, health_pot, 5, 10)
        elif stage == "Stage 1":
            print("You start in a small town that has a small shop you decide to go to")
            space()
            gold = 50
            health_pot = 0
            mana_pot = 0
            buy_items(health_pot,mana_pot, gold)
            beast = False
            while beast == False:
                direction = input("You find yourself leaving the town. The path splits in two directions, one leading to the forest where you could run into bears and the other leading to the plains where you could run into lions. Where would you like to go.\n(f)Forest\n(p)Plains\n(b)Bestiary")
                if direction == "f":
                    print("You enter the forest")
                    beast = True
                    growl = input(print("As you are walking along a path through the forest you hear a growling noise up a head. Do you continue along the path or risk heading into the woods.\n(p)Path\n(w)Woods)"))
                    if  growl == "p":
                        print("You are walking along the path and come across a bear. He charges at you and you are forced to fight")
                elif direction == "p":
                    print("You enter the plains")
                    beast = True
                elif direction == "b":
                    enemy_list()
        else:
            game_over()
start_adventure()
