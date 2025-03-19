import random

player_health = 50
enemy_health = 50
potions = 3
skip_turn = False


while player_health > 0 and enemy_health > 0:
    print(f"\n🔹 Votre vie : {player_health} | Vie de l'ennemi : {enemy_health} |  Potions : {potions}")

    if not skip_turn:
        choice = input("\nSouhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if choice == "1":
            damage = random.randint(5, 10)
            enemy_health -= damage
            print(f" Vous attaquez l'ennemi et infligez {damage} points de dégâts !")
        elif choice == "2":
            if potions > 0:
                heal = random.randint(15, 50)
                player_health += heal
                potions -= 1
                skip_turn = True
                print(f" Vous utilisez une potion et récupérez {heal} points de vie !")
            else:
                print(" Vous n'avez plus de potions !")
                continue
        else:
            print(" Choix invalide, veuillez entrer 1 ou 2.")
            continue

    skip_turn = False


    if enemy_health <= 0:
        print("\n Félicitations ! Vous avez vaincu l'ennemi !")
        break


    enemy_damage = random.randint(5, 15)
    player_health -= enemy_damage
    print(f" L'ennemi vous attaque et inflige {enemy_damage} points de dégâts !")


    if player_health <= 0:
        print("\n Vous avez été vaincu... Fin de la partie.")
        break
