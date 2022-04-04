import sys
from ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()  # 创建主窗口
    ui = Ui_Form()  # 创建自定义ui界面

    ui.setupUi(MainWindow)  # 将自定义ui界面设置到主窗口
    MainWindow.show()
    sys.exit(app.exec_())