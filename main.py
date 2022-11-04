import sys
import os
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PIL import Image, ImageFont, ImageQt
from handright import Template, handwrite
from threading import Thread

from ui import *


class mainwindow(QMainWindow, Ui_Form):
    sendmsg = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_Form.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.lineEdit.setText(getfile()))
        self.pushButton_2.clicked.connect(lambda: self.lineEdit_2.setText(getfile()))
        self.pushButton_3.clicked.connect(self.yulan)
        self.pushButton_5.clicked.connect(self.daochu)
        self.pushButton_4.clicked.connect(self.baocun)
        self.pushButton_6.clicked.connect(self.zairu)
        self.sendmsg.connect(self.msg)

    def msg(self):
        QMessageBox.information(self, "完成", "已导出图片到output目录下")

    def baocun(self):
        file_path = savefile()
        if file_path != "":
            file_text = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (
                self.lineEdit_10.text(), self.lineEdit_11.text(), self.lineEdit_12.text(), self.lineEdit.text(),
                self.lineEdit_2.text(), self.lineEdit_7.text(), self.spinBox.text(), self.lineEdit_8.text(),
                self.spinBox_2.text(), self.lineEdit_9.text(), self.spinBox_3.text(), self.spinBox_5.text(),
                self.spinBox_4.text(), self.doubleSpinBox_6.text(), self.lineEdit_3.text(), self.lineEdit_5.text(),
                self.lineEdit_6.text(), self.lineEdit_4.text())
            with open(file=file_path, mode='w', encoding='utf-8') as file:
                file.write(file_text)

    def zairu(self):
        file_path = getfile()
        if file_path != "":
            shuju = []
            if file_path is not None:
                with open(file=file_path, mode='r+', encoding='utf-8') as f:
                    for line in f.readlines():
                        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                        shuju.append(line)
            self.lineEdit_10.setText(shuju[0])
            self.lineEdit_11.setText(shuju[1])
            self.lineEdit_12.setText(shuju[2])
            self.lineEdit.setText(shuju[3])
            self.lineEdit_2.setText(shuju[4])
            self.lineEdit_7.setText(shuju[5])
            self.spinBox.setValue(int(shuju[6]))
            self.lineEdit_8.setText(shuju[7])
            self.spinBox_2.setValue(int(shuju[8]))
            self.lineEdit_9.setText(shuju[9])
            self.spinBox_3.setValue(int(shuju[10]))
            self.spinBox_5.setValue(int(shuju[11]))
            self.spinBox_4.setValue(int(shuju[12]))
            self.doubleSpinBox_6.setValue(float(shuju[13]))
            self.lineEdit_3.setText(shuju[14])
            self.lineEdit_5.setText(shuju[15])
            self.lineEdit_6.setText(shuju[16])
            self.lineEdit_4.setText(shuju[17])

    def yulan(self):
        text = self.textEdit.toPlainText()

        ziti = self.lineEdit.text()
        beijing = self.lineEdit_2.text()
        zspjj = self.lineEdit_7.text()
        zspjj_ = self.spinBox.text()
        zszjj = self.lineEdit_8.text()
        zszjj_ = self.spinBox_2.text()
        ztdx = self.lineEdit_9.text()
        ztdx_ = self.spinBox_3.text()
        spbhwy_ = self.spinBox_5.text()
        szbhwy_ = self.spinBox_4.text()
        bhxz_ = self.doubleSpinBox_6.text()
        bianju_left = self.lineEdit_5.text()
        bianju_right = self.lineEdit_6.text()
        bianju_up = self.lineEdit_3.text()
        bianju_down = self.lineEdit_4.text()
        red = self.lineEdit_10.text()
        green = self.lineEdit_11.text()
        blue = self.lineEdit_12.text()
        if ziti == "" or zspjj == "" or bianju_down == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整")
        elif text == "":
            QMessageBox.information(self, "!!!", "未输入要处理的文字")
        elif not os.path.exists(ziti):
            QMessageBox.information(self, "路径错误", "字体指定的路径不存在")
        elif not os.path.exists(beijing):
            QMessageBox.information(self, "路径错误", "背景指定的路径不存在")
        else:
            def run():
                self.pushButton_3.setEnabled(False)
                template = Template(
                    background=Image.open(beijing),
                    font=ImageFont.truetype(ziti, size=int(ztdx)),
                    line_spacing=int(zszjj) + int(ztdx),
                    fill=(int(red), int(green), int(blue)),  # 字体“颜色”
                    left_margin=int(bianju_left),
                    top_margin=int(bianju_up),
                    right_margin=int(bianju_right) - int(zspjj) * 2,
                    bottom_margin=int(bianju_down),
                    word_spacing=int(zspjj),
                    line_spacing_sigma=int(zszjj_),  # 行间距随机扰动
                    font_size_sigma=int(ztdx_),  # 字体大小随机扰动
                    word_spacing_sigma=int(zspjj_),  # 字间距随机扰动
                    end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
                    perturb_x_sigma=int(spbhwy_),  # 笔画横向偏移随机扰动
                    perturb_y_sigma=int(szbhwy_),  # 笔画纵向偏移随机扰动
                    perturb_theta_sigma=float(bhxz_),  # 笔画旋转偏移随机扰动
                )
                images = handwrite(text, template)
                for i, im in enumerate(images):
                    im = im.convert("RGBA")
                    image = ImageQt.toqpixmap(im)

                    self.label_11.setScaledContents(True)
                    self.label_11.setPixmap(image)
                    self.pushButton_3.setEnabled(True)
                    break

            t = Thread(target=run)
            t.start()

    def daochu(self):

        text = self.textEdit.toPlainText()
        ziti = self.lineEdit.text()
        beijing = self.lineEdit_2.text()
        zspjj = self.lineEdit_7.text()
        zspjj_ = self.spinBox.text()
        zszjj = self.lineEdit_8.text()
        zszjj_ = self.spinBox_2.text()
        ztdx = self.lineEdit_9.text()
        ztdx_ = self.spinBox_3.text()
        spbhwy_ = self.spinBox_5.text()
        szbhwy_ = self.spinBox_4.text()
        bhxz_ = self.doubleSpinBox_6.text()
        bianju_left = self.lineEdit_5.text()
        bianju_right = self.lineEdit_6.text()
        bianju_up = self.lineEdit_3.text()
        bianju_down = self.lineEdit_4.text()
        red = self.lineEdit_10.text()
        green = self.lineEdit_11.text()
        blue = self.lineEdit_12.text()
        if ziti == "" or zspjj == "" or bianju_down == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整")
        elif text == "":
            QMessageBox.information(self, "!!!", "未输入要处理的文字")
        elif not os.path.exists(ziti):
            QMessageBox.information(self, "路径错误", "字体指定的路径不存在")
        elif not os.path.exists(beijing):
            QMessageBox.information(self, "路径错误", "背景指定的路径不存在")
        else:
            if not os.path.exists("./output"):
                os.mkdir("./output")
            self.pushButton_5.setEnabled(False)

            def run():
                template = Template(
                    background=Image.open(beijing),
                    font=ImageFont.truetype(ziti, size=int(ztdx)),
                    line_spacing=int(zszjj) + int(ztdx),
                    fill=(int(red), int(green), int(blue)),  # 字体“颜色”
                    left_margin=int(bianju_left),
                    top_margin=int(bianju_up),
                    right_margin=int(bianju_right) - int(zspjj) * 2,
                    bottom_margin=int(bianju_down),
                    word_spacing=int(zspjj),
                    line_spacing_sigma=int(zszjj_),  # 行间距随机扰动
                    font_size_sigma=int(ztdx_),  # 字体大小随机扰动
                    word_spacing_sigma=int(zspjj_),  # 字间距随机扰动
                    end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
                    perturb_x_sigma=int(spbhwy_),  # 笔画横向偏移随机扰动
                    perturb_y_sigma=int(szbhwy_),  # 笔画纵向偏移随机扰动
                    perturb_theta_sigma=float(bhxz_),  # 笔画旋转偏移随机扰动
                )
                images = handwrite(text, template)
                for i, im in enumerate(images):
                    assert isinstance(im, Image.Image)
                    im.save("./output/{}.png".format(i))
                self.sendmsg.emit()
                self.pushButton_5.setEnabled(True)

            t = Thread(target=run)
            t.start()




def getfile():
    q = QFileDialog.getOpenFileName()
    return q[0]


def savefile():
    q = QFileDialog.getSaveFileName()
    return q[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainwindow()  # 创建自定义ui界面
    ui.show()
    sys.exit(app.exec())
