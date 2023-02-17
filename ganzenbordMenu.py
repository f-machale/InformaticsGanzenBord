import pygame
import random
import time
import subprocess
import sys
from ganzenbordFionn import ganzenbord
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class GanzenbordMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Ganzenbord Start menu'
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox for name input
        self.player0 = QLineEdit(self)
        self.player0.setMaxLength(10)
        self.player0.move(490, 10)
        self.player0.resize(100, 30)

        self.player1 = QLineEdit(self)
        self.player1.setMaxLength(10)
        self.player1.move(490, 45)
        self.player1.resize(100, 30)

        self.player2 = QLineEdit(self)
        self.player2.setMaxLength(10)
        self.player2.move(490, 80)
        self.player2.resize(100, 30)

        self.player3 = QLineEdit(self)
        self.player3.setMaxLength(10)
        self.player3.move(490, 115)
        self.player3.resize(100, 30)

        self.player4 = QLineEdit(self)
        self.player4.setMaxLength(10)
        self.player4.move(490, 150)
        self.player4.resize(100, 30)

        self.player5 = QLineEdit(self)
        self.player5.setMaxLength(10)
        self.player5.move(490, 185)
        self.player5.resize(100, 30)

        # resolution selection
        self.resolution = QComboBox(self)
        self.resolution.addItem("2200x1100px")
        self.resolution.addItem("2000x1000px")
        self.resolution.addItem("1800x900px")
        self.resolution.addItem("1600x800px")
        self.resolution.addItem("1400x700px")
        self.resolution.addItem("1200x600px")
        self.resolution.addItem("1000x500px")
        self.resolution.move(300, 105)
        self.resolution.resize(100, 30)

        self.player0Checked = QCheckBox(self)
        self.player0Checked.move(465, 15)
        self.player0Checked.resize(20, 20)

        self.player1Checked = QCheckBox(self)
        self.player1Checked.move(465, 50)
        self.player1Checked.resize(20, 20)

        self.player2Checked = QCheckBox(self)
        self.player2Checked.move(465, 85)
        self.player2Checked.resize(20, 20)

        self.player3Checked = QCheckBox(self)
        self.player3Checked.move(465, 120)
        self.player3Checked.resize(20, 20)

        self.player4Checked = QCheckBox(self)
        self.player4Checked.move(465, 155)
        self.player4Checked.resize(20, 20)

        self.player5Checked = QCheckBox(self)
        self.player5Checked.move(465, 190)
        self.player5Checked.resize(20, 20)

        # Start the game
        self.startBTN = QPushButton("Start game pls", self)
        self.startBTN.clicked.connect(self.run_script)
        self.startBTN.setToolTip("Dit gaat Ganzenbord starten")
        self.startBTN.move(200, 310)
        self.startBTN.resize(200, 50)

        self.show()

    def run_script(self, selected_res):
        def playerAmmount():
            player0 = self.player0Checked.checkState()
            player1 = self.player1Checked.checkState()
            player2 = self.player2Checked.checkState()
            player3 = self.player3Checked.checkState()
            player4 = self.player4Checked.checkState()
            player5 = self.player5Checked.checkState()
            selected_players = (
                (player0 + player1 + player2 + player3 + player4 + player5) / 2) - 1
            return selected_players

        playerAmmount = int(playerAmmount())
        selected_res = self.resolution.currentIndex()
        ganzenbord(self.player0.text(), self.player1.text(), self.player2.text(),
                   self.player3.text(), self.player4.text(), self.player5.text(), selected_res, playerAmmount)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GanzenbordMenu()
    win.show()
    sys.exit(app.exec_())
