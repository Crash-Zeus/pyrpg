# -*- coding: utf-8 -*-
import os
import time
from colorama import Fore, Back, Style
from settings.Settings import Settings

# Only print & choice class


class Printator():
    """
        Display class
        - Use success function to print
    """

    def __init__(self, classes = None):
        if classes is not None:
            self.classes = classes

    def start(self, col, row):
        print('Recommended resolution of terminal is : ')
        print(' ' + str(col) + ' X ' + str(row))
        input('[press enter to continue]')
        print("""
            .=========================================.
            |                                         |
            |              .::::::::::.               |
            |            .::``::::::::::.             |
            |            :::..:::::::::::             |
            |            ````````::::::::             |
            |    .::::::::::::::::::::::: iiiiiii,    |
            | .:::::::::::::::::::::::::: iiiiiiiii.  |
            | ::::::::::::::::::::::::::: iiiiiiiiii  |
            | ::::::::::::::::::::::::::: iiiiiiiiii  |
            | :::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii  |
            | :::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii  |
            | `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii`  |
            |    `:::::: iiiiiiiiiiiiiiiiiiiiiii`     |
            |            iiiiiiii,,,,,,,,             |
            |            iiiiiiiiiii''iii             |
            |            `iiiiiiiiii..ii`             |
            |              `iiiiiiiiii`               |
            |                                         |
            |    ____        _   _                    |
            |   |  _ \ _   _| |_| |__   ___  _ __     |
            |   | |_) | | | | __| '_ \ / _ \| '_ \    |
            |   |  __/| |_| | |_| | | | (_) | | | |   |
            |   |_|    \__, |\__|_| |_|\___/|_| |_|   |
            |          |___/                          |
            |                                         |
            '========================================='
        """)

    def loading(self, valmin, valmax, mess = ''):
        os.system('setterm -cursor off')
        begin = "["
        close = "]"
        bar = [
            " =     ",
            "  =    ",
            "   =   ",
            "    =  ",
            "     = ",
            "      =",
            "     = ",
            "    =  ",
            "   =   ",
            "  =    ",
        ]
        while valmin != valmax:
            print(
                Fore.WHITE
                + begin
                + Fore.RED
                + bar[valmin % len(bar)]
                + Fore.WHITE
                + close,
                end="\r",
            )
            time.sleep(0.1)
            valmin += 1
        else:
            if mess != '':
                print(Fore.GREEN + mess + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "                        " + Style.RESET_ALL)
        os.system('setterm -cursor on')
        return True

    def logMenu(self):
        self.success('0 -> Signin')
        self.success('1 -> Sigup')
        choice = input('> ')
        if choice == '0':
            return 'signin'
        elif choice == '1':
            return 'signup'
        else:
            return False

    def saveFound(self, save, *action):
        print("Save file found for :")
        print(
            save["charName"]
            + " "
            + self.classes[int(save["charClassId"])]["name"]
            + " level "
            + str(save["charLevel"])
        )
        if action:
            print("This action will be replace the save file with your actual game")
            action = input("Continue ? y/n ")
            if action == 'y':
                return True
            else:
                return False
        else:
            print("Continue with this game ? y/n")
            return True

    def saved(self):
        Settings.Addspace(Settings, 20)
        print(Fore.GREEN + "Game saved" + Fore.RESET)
        Settings.Addspace(Settings, 2)
        return True

    def choseName(self):
        Settings.Addspace(Settings, 2)
        print("- New game -")
        Settings.Addspace(Settings, 2)
        print("Choose your name : ")
        return True

    def confirm(self, param, string):
        confirm = input(
            'Do you really want "'
            + Fore.RED
            + "%s" % param
            + Fore.RESET
            + '"'
            + " %s ? y/n " % string
        )
        if confirm == "y":
            return True
        elif confirm == "n":
            return False
        else:
            return False

    def classChose(self, i, classes):
        print(
            str(i)
            + " -> "
            + Fore.GREEN
            + classes[i]["name"]
            + " - Special spell : "
            + classes[i]["spe"]["name"]
            + Fore.RESET
        )
        return True

    def showInformations(self):
        Settings.Addspace(Settings, 10)
        return True

    def showMainTitle(self, name, me, level):
        print('-------------------------------------------')
        print('|                                         |')
        print('| RPY   --   THE PYTHON ROLE PLAYING GAME |')
        print('|                                         |')
        print('-------------------------------------------')
        Settings.Addspace(Settings, 2)
        print('Name  : ' + name)
        print('Class : ' + me.name)
        print('Level : ' + str(level))
        Settings.Addspace(Settings, 2)
        return True

    def showMainMenu(self, space=False):
        if space != False:
            Settings.Addspace(Settings, 20)
        print("------------")
        print("| MAIN MENU |")
        print("------------")
        Settings.Addspace(Settings, 2)
        for i in range(len(Settings.mainMenu())):
            print(str(i) + " -> " + Settings.mainMenu()[i])
        Settings.Addspace(Settings, 2)

        action = input("> ")

        if action == "0":
            return 0
        elif action == "1":
            return 1
        elif action == "2":
            return 2
        elif action == "3":
            return 3
        elif action == "4":
            exit
        else:
            return 10

    def showMenuOption(self):
        Settings.Addspace(Settings, 20)
        print("-----------")
        print("| OPTIONS |")
        print("-----------")
        options = Settings.options()
        for i in range(len(options)):
            print(str(i) + " -> " + options[i])
        action = input("> ")

        if action == "0":
            return 0
        elif action == "1":
            return 99

    def removeSave(self):
        print(Fore.RED + "/!\ " + Fore.RESET +
              " WARNING " + Fore.RED + " /!\ ")
        print(
            Fore.RESET
            + "This action will be "
            + Fore.RED
            + "remove"
            + Fore.RESET
            + " the save file"
        )
        confirm = input("Are you sure ? y/n ")
        if confirm == 'y':
            return True
        else:
            return False

    def success(self, string, space=0):
        if space != 0:
            Settings.Addspace(Settings, space)
        print(string + Fore.RESET)
        if space != 0:
            Settings.Addspace(Settings, space)
        return True

    def health(self, maxHealth, health):
        healthDashes = 20
        dashConvert = int(maxHealth/healthDashes)
        currentDashes = int(health/dashConvert)
        remainingHealth = healthDashes - currentDashes
        healthDisplay = '█' * currentDashes
        remainingDisplay = ' ' * remainingHealth
        percent = int((health/maxHealth)*100)
        color = Fore.GREEN
        if percent <= 60:
            color = Fore.YELLOW
        if percent <= 30:
            color = Fore.RED
        print("|" + color + healthDisplay + Fore.RESET + remainingDisplay + "| " + str(health) + ' / ' + str(maxHealth))

    def battleInfo(self, turn, me, monster):
        print('Turn : ' + str(turn))
        Settings.Addspace(Settings, 2)
        print("---------------------------------------------")
        print("You : ")
        Printator.health(me.maxHp, me.hp)
        print(
            "atk : {0} | def : {1} | acr : {2}".format(
                me.atk, me.defc, me.acr
            )
        )
        print("---------------------------------------------")
        print(monster.name + " :")
        Printator.health(monster.maxHp, monster.hp)
        print(
            "atk : {0} | def : {1} | acr : {2}".format(
                monster.atk, monster.defc, monster.acr
            )
        )
        print("---------------------------------------------")
        Settings.Addspace(Settings, 1)
        return True

    def showBattleAction(self, useSpe, me, monster):
        print(" 0 -> Attak " + monster.name)
        if useSpe == 0:
            print(" 1 -> Special : %s " % me.spe['name'])
        print(" 2 -> Defend (%i %%)" % me.defc)
        print(" 3 -> Escape")
        print(" 4 -> pass")
        Settings.Addspace(Settings, 1)
        action = input("> ")
        if action == "0":
            return 'attak'
        elif action == "1":
            if useSpe == 0:
                return 'spe'
            else:
                Settings.Addspace(Settings, 1)
                Printator.success('Bad entry')
                Settings.Addspace(Settings, 1)
                return False
        elif action == "2":
            return 'protect'
        elif action == "3":
            return 'escape'
        elif action == "4":
            return 'pass'
        else:
            return False

    def attak(self, atk, target):
        Settings.Addspace(Settings, 2)
        print("Hit ! Hurt " + target.name)
        print("Decrease hp to " + str(target.hp))
        print(Fore.RED + " - " + str(atk) + " hp" + Fore.RESET)
        return True

    def useSpell(self, caster, spell, focus, target, alt, power, perso=False):
        Settings.Addspace(Settings, 2)
        if perso == True:
            print(caster + ' use "' + spell + '" on ' + caster + '!')
        else:
            print(caster.name + ' use "' + spell + '" on ' + target.name + '!')
        print(Fore.YELLOW + alt + ' ' + str(power) + ' ' + focus + Fore.RESET)
        Settings.Addspace(Settings, 2)
        return True

    def lanMenu(self):
        Settings.Addspace(Settings, 30)
        print('0 -> Create lan')
        print('1 -> Join lan')
        print('2 -> Back')
        choice = input('> ')
        if choice == '0':
            return 'host'
        elif choice == '1':
            return 'join'
        elif choice == '2':
            return 'back'
        else:
            return False