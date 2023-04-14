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

        # Load and display image 
        self.imageLogo = QLabel(self)
        self.pixmap = QPixmap("photosOne/GanzenbordIcon.png")
        self.imageLogo.setPixmap(self.pixmap)
        self.imageLogo.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.imageLogo.move(275, 20)

        # Create textbox for name input
        self.playerText = QLabel(self)
        self.playerText.setText("Player names:")
        self.playerText.move(11, 10)

        self.player0 = QLineEdit(self)
        self.player0.setMaxLength(10)
        self.player0.move(11, 40)
        self.player0.resize(100, 30)

        self.player1 = QLineEdit(self)
        self.player1.setMaxLength(10)
        self.player1.move(11, 75)
        self.player1.resize(100, 30)

        self.player2 = QLineEdit(self)
        self.player2.setMaxLength(10)
        self.player2.move(11, 110)
        self.player2.resize(100, 30)

        self.player3 = QLineEdit(self)
        self.player3.setMaxLength(10)
        self.player3.move(11, 145)
        self.player3.resize(100, 30)

        self.player4 = QLineEdit(self)
        self.player4.setMaxLength(10)
        self.player4.move(11, 180)
        self.player4.resize(100, 30)

        self.player5 = QLineEdit(self)
        self.player5.setMaxLength(10)
        self.player5.move(11, 215)
        self.player5.resize(100, 30)

        # Player selection
        self.selectionText = QLabel(self)
        self.selectionText.setText("Select each player:")
        self.selectionText.move(120, 10)

        self.player0Checked = QCheckBox(self)
        self.player0Checked.move(120, 45)
        self.player0Checked.resize(20, 20)

        self.player1Checked = QCheckBox(self)
        self.player1Checked.move(120, 80)
        self.player1Checked.resize(20, 20)

        self.player2Checked = QCheckBox(self)
        self.player2Checked.move(120, 115)
        self.player2Checked.resize(20, 20)

        self.player3Checked = QCheckBox(self)
        self.player3Checked.move(120, 150)
        self.player3Checked.resize(20, 20)

        self.player4Checked = QCheckBox(self)
        self.player4Checked.move(120, 185)
        self.player4Checked.resize(20, 20)

        self.player5Checked = QCheckBox(self)
        self.player5Checked.move(120, 220)
        self.player5Checked.resize(20, 20)
        
        # resolution selection
        self.resolutionText = QLabel(self)
        self.resolutionText.setText("Select desired Resolution:")
        self.resolutionText.move(11, 260)
        self.resolutionText.adjustSize()

        self.resolution = QComboBox(self)
        self.resolution.addItem("2200x1100px")
        self.resolution.addItem("2000x1000px")
        self.resolution.addItem("1800x900px")
        self.resolution.addItem("1600x800px")
        self.resolution.addItem("1400x700px")
        self.resolution.addItem("1200x600px")
        self.resolution.addItem("1000x500px")
        self.resolution.move(11, 280)
        self.resolution.resize(100, 30)

        # Start the game
        self.startBTN = QPushButton("Start the game", self)
        self.startBTN.clicked.connect(self.run_script)
        self.startBTN.setToolTip("Dit gaat Ganzenbord starten")
        self.startBTN.move(11, 330)
        self.startBTN.resize(580, 60)

        self.show()

    #Function to start the game
    def run_script(self, selected_res):
        #Function to check if a player was selected 
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
