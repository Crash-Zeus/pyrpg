#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

# My classes
from classes.engine.Printator import Printator
from classes.engine.Saveator import Saveator
from classes.engine.Fightator import Fightator
from classes.engine.Lantator import Lantator
from classes.engine.Apitator import Apitator

from dotenv import load_dotenv
load_dotenv()
if os.getenv('DEBUG') == 'True':
    import debugpy
    debugpy.listen(('0.0.0.0',5678))
    debugpy.wait_for_client()

class Game:
    """
        Game class
    """

    def __init__(self):
        self.apitator = Apitator()
        self.classes = self.apitator.getClass()
        self.printator = Printator(self.classes)
        self.apitator.login()
        self.printator.start(60, 40)
        # Goes wrong with some console : include kde konsole, fix exist ?
        # Settings.resize()
        self.printator.loading(0, 20)
        self.saveator = Saveator(self.printator, self.classes, self.apitator)
        if self.saveator.loadSave():
            self.showInformation()
        else:
            self.saveator.choseName()
            self.saveator.choseClass()
            self.showInformation()

    def showInformation(self):
        self.printator.showMainTitle(self.saveator)
        self.saveator.updateStats()
        self.mainMenu()

    def mainMenu(self, jump=False):
        if not jump:
            choice = self.printator.showMainMenu()
        else:
            choice = jump
        if choice == 0:
            fightator = Fightator(self.apitator, self.saveator, self.printator)
            fightator.quickBattle()
            self.mainMenu()
        elif choice == 1:
            lan = Lantator(self.printator)
            choice = lan.choice()
            if choice == 'host':
                lan.hoster()
            elif choice == 'join':
                lan.joiner()
            elif choice == 'back':
                self.mainMenu()
        elif choice == 2:
            option = self.printator.showMenuOption()
            if option == 0:
                self.saveator.removeSave()
                self.mainMenu()
            else:
                self.mainMenu()
        elif choice == 3:
            save = self.saveator.save()
            if not save:
                self.mainMenu()
        elif choice == 10:
            self.mainMenu()


if __name__ == "__main__":
    try:
        Game()
    except KeyboardInterrupt:
        exit
