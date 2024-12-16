import random
from Quest import Quest
from Mobs import Mobs


def ajouter_item_aleatoire(bag, items_disponibles):
    item = random.choice(items_disponibles)
    
    if bag.addItem(item):
        print(f"L'item {item._name} a été ajouté au sac du joueur !")
    else:
        print("Le sac est plein, impossible d'ajouter un nouvel item.")
        print(bag) 
        
        # Proposer l'échange d'un item
        choix = input("Le sac est plein. Voulez-vous échanger un item ? (o/n) : ")
        if choix.lower() == 'o':
            print("Voici les items dans votre sac :")
            for index, current_item in enumerate(bag._lItems):
                print(f"{index + 1}. {current_item._name}")
            
            try:
                # Choisir un item à remplacer
                item_index = int(input(f"Entrez le numéro de l'item à échanger contre {item._name} : ")) - 1
                if 0 <= item_index < len(bag._lItems):
                    old_item = bag._lItems[item_index]
                    bag._lItems[item_index] = item  # Remplacement de l'item
                    print(f"L'item {old_item._name} a été échangé contre {item._name}.")
                else:
                    print("Choix invalide. Aucun échange n'a été effectué.")
            except ValueError:
                print("Entrée invalide. Aucun échange n'a été effectué.")
        else:
            print("Aucun échange effectué. L'item n'a pas été ajouté au sac.")



def combat(joueur1, joueur2, items_disponibles):
    print(f"Combat entre {joueur1._nom} et {joueur2._nom} commence !")
    round = 1

    while joueur1._life > 0 and joueur2._life > 0:
        print(f"# Round {round} #")
        print(f"# PV de {joueur1._nom} : {joueur1._life}")
        print(f"# PV de {joueur2._nom} : {joueur2._life}")

        if joueur1.initiative() > joueur2.initiative():
            print(f"{joueur1._nom} commence !")
            dommage = joueur1.damages()
            joueur2.defense(dommage)

            if joueur2._life <= 0:
                print(f"{joueur2._nom} est tombé au combat !")
                break

            dommage = joueur2.damages()
            joueur1.defense(dommage)

        else:
            print(f"{joueur2._nom} commence !")
            dommage = joueur2.damages()
            joueur1.defense(dommage)

            if joueur1._life <= 0:
                print(f"{joueur1._nom} est tombé au combat !")
                break

            dommage = joueur1.damages()
            joueur2.defense(dommage)

        round += 1

    if joueur1._life <= 0:
        print(f"{joueur2._nom} a gagné le combat !")
        ajouter_item_aleatoire(joueur2.bag, items_disponibles) 
    elif joueur2._life <= 0:
        print(f"{joueur1._nom} a gagné le combat !")
        ajouter_item_aleatoire(joueur1.bag, items_disponibles)  # Ajouter un item au gagnant

def combatPVE(joueur, mob, items_disponibles):
    while joueur._life > 0 and mob._life > 0:
        damage = joueur.damages()
        mob.defense(damage)
        print(f"{joueur._nom} attaque {mob._nom} pour {damage} dégâts !")
        
        if mob._life > 0:
            damage = mob.damages()
            joueur.defense(damage)
            print(f"{mob._nom} attaque {joueur._nom} pour {damage} dégâts !")

    if joueur._life <= 0:
        print(f"{joueur._nom} est mort!")
    if mob._life <= 0:
        print(f"{mob._nom} est mort!")
        ajouter_item_aleatoire(joueur.bag, items_disponibles)  # Ajouter un item au joueur s'il gagne
        mob.reset()


def jouer(joueur1, joueur2, mobs, items_disponibles):
    plateau_taille = 50 
    joueur1.bag.reset()
    joueur2.bag.reset()

    while joueur1._life > 0 and joueur2._life > 0: 
        # Tour de joueur1
        input(f"{joueur1._nom} appuyez sur Entrée pour lancer le dé...")
        de1 = random.randint(1, 6)  # Simule un lancer de dé
        joueur1._position += de1
        print(f"{joueur1._nom} a lancé un {de1} ! Il est maintenant sur la case {joueur1._position}.")

        # Chance de rencontrer un mob
        if random.random() < 0.3:  # 30% de chance de rencontrer un mob
            mob = random.choice(mobs)
            print(f"{joueur1._nom} a rencontré un {mob} !")
            combatPVE(joueur1, mob, items_disponibles)  

        # Tour de joueur2
        input(f"{joueur2._nom} appuyez sur Entrée pour lancer le dé...")
        de2 = random.randint(1, 6)  # Simule un lancer de dé
        joueur2._position += de2
        print(f"{joueur2._nom} a lancé un {de2} ! Il est maintenant sur la case {joueur2._position}.")

        # Chance de rencontrer un mob
        if random.random() < 0.3:  # 30% de chance de rencontrer un mob
            mob = random.choice(mobs)
            mob.reset()
            print(f"{joueur2._nom} a rencontré un {mob} !")
            combatPVE(joueur2, mob, items_disponibles)  # Passer les items disponibles

       
        if joueur1._position == joueur2._position:
            print(f"{joueur1._nom} et {joueur2._nom} sont sur la même case, un combat commence !")
            combat(joueur1, joueur2, items_disponibles)  # Passer les items disponibles


        if joueur1._position >= plateau_taille:
            print(f"{joueur1._nom} a gagné la partie !")
            break
        elif joueur2._position >= plateau_taille:
            print(f"{joueur2._nom} a gagné la partie !")
            break

    print("La partie est terminée !")



