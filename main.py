#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import random
import sys
import time
import json
import random
from colorama import Fore, Back, Style

# My classes
from classes.engine.Printator import Printator
from classes.engine.Saveator import Saveator
from classes.engine.Fightator import Fightator
from settings.Settings import Settings
from classes.char.Monster import Monster
from classes.char.Class import Rogue, Warrior, Gunner, Developer, Admin


class Game():

    # use ?
    classes = Settings.loadClass(Settings)
    # In saveator ?
    # charName = None
    # charClass = None
    # me = None
    # charLevel = 1
    # charExp = 0
    # score = 0
    turn = 1
    useSpe = 0

    def __init__(self):
        Settings.resize()
        Printator.__init__(Printator)
        Printator.loading(0, 20)
        if Saveator.__init__(Saveator) == True:
            self.showInformation(self)
        else:
            Saveator.choseName(Saveator)
            Saveator.choseClass(Saveator)
            self.showInformation(self)

    def showInformation(self):
        Printator.showInformations()
        Printator.showMainTitle(Saveator.charName, Saveator.me, Saveator.charLevel)
        Saveator.updateStats(Saveator)
        choice = Printator.showMainMenu(Printator)
        if choice == 0:
            Fightator.quickBattle()
        elif choice == 1:
            print('CAMPAGN')
        elif choice == 2:
            Printator.showMenuOption()
        elif choice == 3:
            print('SAVE')


    def showOptionMenu(self):
        Settings.Addspace(Settings, 100)
        print("-----------")
        print("| OPTIONS |")
        print("-----------")
        options = Settings.options()
        for i in range(len(options)):
            print(str(i) + " -> " + options[i])
        action = input("> ")

        if action == "0":
            self.removeSaveFile(self)
        elif action == "1":
            Settings.Addspace(Settings, 100)
            return self.showMainMenu(self)

    def removeSaveFile(self):
        print(Fore.RED + "/!\ " + Fore.RESET + " WARNING " + Fore.RED + " /!\ ")
        print(
            Fore.RESET
            + "This action will be "
            + Fore.RED
            + "remove"
            + Fore.RESET
            + " the save file"
        )
        confirm = input("Are you sure ? y/n ")
        if confirm == "y":
            if os.path.exists("save/save.json"):
                os.remove("save/save.json")
                print("removing save file success")
                Settings.Addspace(Settings, 5)
                self.showMainMenu(self)
            else:
                print("No save file exist")
                self.showOptionMenu(self)
        else:
            self.showOptionMenu(self)

    def save(self):
        if os.path.exists("save/save.json"):
            print("A save file already exist :")
            save = Settings.loadSave()
            print(save["charName"] + " level " + str(save["charLevel"]))
            print("This action will be replace the save file with your actual game")
            action = input("Continue ? y/n ")
            if action == "y":
                os.remove("save/save.json")
                self.save(self)
            else:
                Settings.Addspace(Settings, 100)
                self.showMainMenu(self)

        else:
            file = open("save/save.json", "a")
            json_data = {
                "charName": "{0}".format(self.charName),
                "charClassId": self.charClass,
                "charClass": self.classes[self.charClass],
                "charLevel": self.charLevel,
                "charExp": self.charExp,
                "score": self.score,
            }
            json.dump(json_data, fp=file, indent=4, sort_keys=False)
            file.close()
            Settings.Addspace(Settings, 100)
            print(Fore.GREEN + "Game saved" + Fore.RESET)
            Settings.Addspace(Settings, 2)
            self.showMainMenu(self)

    def createMonster(self):
        monster = Monster()
        return monster

    def quickBattle(self):
        self.turn = 1
        Settings.Addspace(Settings, 50)
        monster = self.createMonster(self)
        self.showBattleInfo(self, monster)
        self.showActions(self, self.me, monster)

    def showBattleInfo(self, monster):
        Settings.Addspace(Settings, 2)
        print('Turn : ' + str(self.turn))
        Settings.Addspace(Settings, 2)
        print("---------------------------------------------")
        Settings.Addspace(Settings, 2)
        print("You : ")
        print(
            "Hp : {0} / {1} | atk : {2} | def : {3} | acr : {4}".format(
                self.me.hp, self.me.maxHp, self.me.atk, self.me.defc, self.me.acr
            )
        )
        Settings.Addspace(Settings, 2)
        print("---------------------------------------------")
        Settings.Addspace(Settings, 2)
        print(monster.name + " :")
        print(
            "Hp : {0} / {1} | atk : {2} | def : {3} | acr : {4}".format(
                monster.hp, monster.maxHp, monster.atk, monster.defc, monster.acr
            )
        )
        Settings.Addspace(Settings, 2)
        print("---------------------------------------------")
        Settings.Addspace(Settings, 2)

    def showActions(self, me, monster):
        print("0 -> Attak")
        if self.useSpe == 0:
            print("1 -> Special : %s " % self.me.spe['name'])
        print("2 -> Defend (%i %%)" % self.me.defc)
        print("3 -> Escape")
        Settings.Addspace(Settings, 1)
        action = input("> ")
        if action == "0":
            self.attak(self, monster)
        elif action == "1":
            if self.useSpe == 0:
                self.specialSkill(self, monster)
            else:
                self.badEntry(self, monster)
        elif action == "2":
            self.protect(self, monster)
        elif action == "3":
            self.escape(self, monster)
        else:
            self.showActions(self, self.me, monster)

    def badEntry(self, monster):
        Settings.Addspace(Settings, 2)
        print('Bad entry')
        Settings.Addspace(Settings, 2)
        self.showActions(self, self.me, monster)

    def validate(self, me, monster):
        self.showBattleInfo(self, monster)
        self.showActions(self, me, monster)

    def attak(self, target):
        baseHp = target.hp
        hp = Settings.calcAtk(Settings,self.me.atk, target.hp)
        if hp > 0:
            target.hp = hp
            Settings.Addspace(Settings, 2)
            print("Hit ! You hurt " + target.name)
            print("Decrease hp from " + str(baseHp) + " to " + str(target.hp))
            print(Fore.RED + " - " + str(Settings.lastAtk) + " hp" + Fore.RESET)
            Settings.Addspace(Settings, 2)
            self.showBattleInfo(self, target)
            Settings.Addspace(Settings, 2)
            self.loading(0, 10, '')
            self.ennemyAction(self, target)
        else:
            self.win(self, target)

    def protect(self, monster):
        Settings.protect = self.me.defc
        self.ennemyAction(self, monster)

    def specialSkill(self, monster):
        speName = self.me.spe['name']
        speTarget = self.me.spe['target']
        speEffect = self.me.spe['effect']
        speFocus = speEffect['focus']
        speAlt = speEffect['alterate']
        speValue = speEffect['value']

        if speTarget == 'self':
            target = self.me
        else:
            target = monster

        if speFocus == 'atk':
            spe = Settings.calcSpeAtk(Settings, target, speAlt, speValue)
        elif speFocus == 'def':
            spe = Settings.calcSpeDef(Settings, target, speAlt, speValue)
        elif speFocus == 'acr':
            spe = Settings.calcSpeAcr(Settings, target, speAlt, speValue)
        elif speFocus == 'hp':
            spe = Settings.calcSpeHp(Settings, target, speAlt, speValue)
            self.me.hp = spe
            self.useSpe += 1
            Settings.Addspace(Settings, 2)
            print('Your hp increase by ' + Fore.GREEN + str(speValue) + Fore.RESET)
            self.ennemyAction(self, monster)

    
    def escape(self, monster):
        print('Escaping funct')

    def ennemyAction(self, monster):
        Settings.Addspace(Settings, 2)
        print(monster.name + ' playing...')
        self.loading(0, 10, '')
        action = random.randint(1, 3)
        if action == 1:
            self.turn += 1
            print(monster.name + ' attak !')
            Settings.Addspace(self, 2)
            self.monsterAttak(self, monster)
        elif action == 2:
            self.turn += 1
            print(monster.name + ' protect him')
            Settings.Addspace(self, 2)
            self.monsterProtect(self, monster)
        elif action == 3:
            if self.turn in Settings.validateTurns:
                self.turn += 1
                print(monster.name + ' use special spell')
                Settings.Addspace(self, 2)
                self.validate(self, self.me, monster)
            else:
                print(monster.name + ' bad entry')
                self.ennemyAction(self, monster)

    def monsterAttak(self, monster):
        hp = Settings.calcAtk(Settings, monster.atk, self.me.hp)
        if hp > 0:
            print('Hit ! ' + monster.name + ' hurt you')
            print(Fore.RED + ' - ' + str(Settings.lastAtk) + ' hp' + Fore.RESET)
            Settings.Addspace(self, 2)
            self.me.hp = hp
            self.validate(self, self.me, monster)
        else:
            self.gameOver(self, monster)
    
    def monsterProtect(self, monster):
        Settings.protect = monster.defc
        self.validate(self, self.me, monster)

    def win(self, monster):
        self.charExp += monster.xp
        up = Settings.checkLevel(self.charLevel, self.charExp)
        print("Exp win : " + Fore.GREEN + str(monster.xp) + Fore.RESET)
        print("Exp total : " + Fore.GREEN + str(self.charExp) + Fore.RESET)
        if up == True:
            self.charLevel += 1
            Settings.Addspace(Settings, 2)
            print(Fore.GREEN + "Level up !" + Fore.RESET)
            print("Level : " + str(self.charLevel))
            Settings.Addspace(Settings, 2)
            self.showMainMenu(self)
        else:
            Settings.Addspace(Settings, 2)
            self.showMainMenu(self)

    def gameOver(self, monster):
        print(monster.name + ' killed you')
        print(Fore.RED + 'GAME OVER' + Fore.RESET)
        Settings.Addspace(Settings, 4)
        exit

if __name__ == "__main__":
    try:
        Game.__init__(Game)
    except KeyboardInterrupt:
        exit
