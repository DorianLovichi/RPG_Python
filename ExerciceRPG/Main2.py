from Bag import Bag
from Equipement import Equipment
from Hero import Hero
from Item import Item
from Mobs import Mobs
from Quest import Quest
from Race import Race
from Stat import Stat

class Main:
    def main():
        ### RACE
        stat_elfe = Stat({
            'strength': 5, 'magic': 10, 'agility': 10,
            'speed': 5, 'charisma': 5, 'chance': 5
        })
        elfe = Race('Elfe', stat_elfe)

        stat_human = Stat({
            'strength': 10, 'magic': 10, 'agility': 5,
            'speed': 5, 'charisma': 5, 'chance': 5
        })
        human = Race('Human', stat_human)

        stat_dwarf = Stat({
            'strength': 10, 'magic': 0, 'agility': 10,
            'speed': 5, 'charisma': 5, 'chance': 10
        })
        dwarf = Race('Dwarf', stat_dwarf)

        stat_orc = Stat({
            'strength': 15, 'magic': 0, 'agility': 5,
            'speed': 10, 'charisma': 5, 'chance': 5
        })
        orc = Race('Orc', stat_orc)

        ### CLASS
        stat_wizard = Stat({
            'strength': 0, 'magic': 10, 'agility': 0,
            'speed': 0, 'charisma': 10, 'chance': 10
        })
        wizard = Race('Wizard', stat_wizard)

        stat_warrior = Stat({
            'strength': 10, 'magic': 0, 'agility': 5,
            'speed': 5, 'charisma': 5, 'chance': 5
        })
        warrior = Race('Warrior', stat_warrior)

        ### ITEMS
        stat_sword = Stat({
            'strength': 5, 'magic': 0, 'agility': 5,
            'speed': 5, 'charisma': 0, 'chance': 5
        })
        sword = Equipment({
            'classList': 'warrior', 'place': 'hand',
            'name': 'dragon sword', 'type': 'sword', 'space': 2
        }, stat_sword)

        stat_baton = Stat({
            'strength': 0, 'magic': 10, 'agility': 0,
            'speed': 5, 'charisma': 0, 'chance': 5
        })
        baton = Equipment({
            'classList': 'wizard', 'place': 'hand',
            'name': 'wizard baton', 'type': 'baton', 'space': 2
        }, stat_baton)

        stat_potion = Stat({
            'strength': 0, 'magic': 0, 'agility': 0,
            'speed': 0, 'charisma': 0, 'chance': 0
        })
        potion = Item({
            'name': 'life potion', 'type': 'potion', 'space': 2
        }, stat_potion)

        ### BAG
        my_bag = Bag({
            "sizeMax": 20, "items": [potion, potion]
        })

        ### MOBS
        mechant1 = Mobs({
            'name': 'orc 1', 'race': orc, 'classe': warrior,
            'bag': my_bag, 'equipment': [sword], 'element': 'Fire', 'type': 'soldier'
        })
        mechant2 = Mobs({
            'name': 'orc 2', 'race': orc, 'classe': warrior,
            'bag': my_bag, 'equipment': [sword], 'element': 'Fire', 'type': 'soldier'
        })

        ### HEROES
        hero1 = Hero({
            'name': 'Jean', 'race': elfe, 'classe': wizard,
            'bag': my_bag, 'equipment': [baton], 'element': 'Fire', 'profession': 'chomeur'
        })

        hero2 = Hero({
            'name': 'Pierre', 'race': human, 'classe': warrior,
            'bag': my_bag, 'equipment': [sword], 'element': 'Fire', 'profession': 'chomeur'
        })

        ### SAVE HEROES
        hero1.save()
        hero1.saveXML()

        ### QUEST
        first_quest = Quest({
            'lAvatar': [mechant1, mechant2], 'lvl': 2, 'gift': sword
        })

        # Uncomment to test the quest with hero2
        first_quest = Quest({'lAvatar': [hero2], 'lvl': 2, 'gift': sword})

        # Uncomment to run the quest with hero1
        first_quest.run(hero1)


    if __name__ == "__main__":
        # Execute only if run as a script
        main()

