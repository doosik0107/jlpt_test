import sys
from PyQt5 import QtWidgets

class run(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self._init_menubar()
        self.show()

    def _init_menubar(self):
        menubar = self.menuBar()
        listMenu = menubar.addMenu('목록')
        action = QtWidgets.QAction('1급',self)
        listMenu.addAction(action)
        action = QtWidgets.QAction('2급',self)
        listMenu.addAction(action)
        action = QtWidgets.QAction('3급',self)
        listMenu.addAction(action)


        inputMenu = menubar.addMenu('입력')
        action = QtWidgets.QAction('JLPT',self)
        inputMenu.addAction(action)


        infoMenu = menubar.addMenu('정보')
        action = QtWidgets.QAction('종료',self)
        action.setShortcut("Ctrl+Q")
        action.triggered.connect(QtWidgets.qApp.quit)
        infoMenu.addAction(action)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = run()
    sys.exit(app.exec_())