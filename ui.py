# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageFont, ImageQt
from handright import Template, handwrite
import img
import tkinter as tk
from tkinter import filedialog, dialog
import os


def getfile():
    root = tk.Tk()
    root.withdraw()
    Filepath = filedialog.askopenfilename()
    return Filepath


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(848, 592)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(848, 592))
        Form.setMaximumSize(QtCore.QSize(848, 592))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../ps/图标/火绒.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.95)
        Form.setAccessibleDescription("")
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(430, 30, 411, 221))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(570, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(480, 280, 311, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 280, 31, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(792, 279, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(792, 309, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(450, 310, 31, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 310, 311, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(720, 357, 61, 24))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(720, 431, 61, 24))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(697, 380, 24, 51))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(780, 380, 24, 51))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(730, 390, 41, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(440, 330, 71, 78))
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(600, 360, 51, 20))
        self.spinBox.setObjectName("spinBox")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(514, 360, 74, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(514, 400, 74, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(600, 400, 51, 20))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(440, 370, 71, 78))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(440, 410, 71, 78))
        self.label_7.setObjectName("label_7")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(514, 440, 74, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.spinBox_3 = QtWidgets.QSpinBox(Form)
        self.spinBox_3.setGeometry(QtCore.QRect(600, 440, 51, 20))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(Form)
        self.spinBox_4.setGeometry(QtCore.QRect(600, 520, 51, 20))
        self.spinBox_4.setProperty("value", 4)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(Form)
        self.spinBox_5.setGeometry(QtCore.QRect(600, 480, 51, 20))
        self.spinBox_5.setProperty("value", 4)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(440, 450, 81, 78))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(440, 530, 71, 78))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(440, 490, 91, 78))
        self.label_10.setObjectName("label_10")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(600, 560, 51, 20))
        self.doubleSpinBox_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_6.setSingleStep(0.01)
        self.doubleSpinBox_6.setProperty("value", 0.05)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 500, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 540, 101, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(3, 1, 420, 593))
        self.label_11.setText("")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setObjectName("label_11")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(-5, -9, 861, 611))
        self.listView.setStyleSheet("background-image: url(:/新前缀/Desktop Screenshot 2022.03.30 - 20.06.33.02.png);")
        self.listView.setObjectName("listView")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(514, 334, 74, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(599, 334, 51, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(450, 334, 31, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(727, 259, 31, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(760, 259, 31, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(793, 259, 31, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(673, 260, 51, 21))
        self.label_13.setObjectName("label_13")
        self.listView.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.spinBox.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_8.raise_()
        self.spinBox_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEdit_9.raise_()
        self.spinBox_3.raise_()
        self.spinBox_4.raise_()
        self.spinBox_5.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.doubleSpinBox_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.label_11.raise_()
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.label_12.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_12.raise_()
        self.label_13.raise_()
        self.pushButton.clicked.connect(lambda: self.lineEdit.setText(getfile()))
        self.pushButton_2.clicked.connect(lambda: self.lineEdit_2.setText(getfile()))
        self.pushButton_3.clicked.connect(self.yulan)
        self.pushButton_5.clicked.connect(self.daochu)
        self.pushButton_4.clicked.connect(self.baocun)
        self.pushButton_6.clicked.connect(self.zairu)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def baocun(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(title=u'保存文件', filetypes=[("Text file", ".txt")])
        file_text = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (
        self.lineEdit_10.text(), self.lineEdit_11.text(), self.lineEdit_12.text(), self.lineEdit.text(),
        self.lineEdit_2.text(), self.lineEdit_7.text(), self.spinBox.text(), self.lineEdit_8.text(),
        self.spinBox_2.text(), self.lineEdit_9.text(), self.spinBox_3.text(), self.spinBox_5.text(),
        self.spinBox_4.text(), self.doubleSpinBox_6.text(), self.lineEdit_3.text(), self.lineEdit_5.text(),
        self.lineEdit_6.text(), self.lineEdit_4.text())
        with open(file=file_path, mode='w', encoding='utf-8') as file:
            file.write(file_text)


    def zairu(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title=u'选择文件')
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
            break

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
            im.save("./{}.png".format(i))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "手写模拟"))
        self.textEdit.setPlaceholderText(
            _translate("Form", "本软件主要基于handwrite库开发，仅供学习交流。作者只是一名为手写作业发愁的大学生，想要源码或者想要添加功能、反馈bug的，可以联系作者b站：人走茶凉le"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#00aaff;\">待处理文本</span></p></body></html>"))
        self.lineEdit.setAccessibleDescription(_translate("Form", "1111"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">字体：</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "选择"))
        self.pushButton_2.setText(_translate("Form", "选择"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">背景：</span></p></body></html>"))
        self.lineEdit_2.setAccessibleDescription(_translate("Form", "1111"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#0261f9;\">边距</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "字水平间距："))
        self.label_6.setText(_translate("Form", "字竖直间距："))
        self.label_7.setText(_translate("Form", "字体大小："))
        self.label_8.setText(_translate("Form", "水平笔画位移："))
        self.label_9.setText(_translate("Form", "笔画旋转："))
        self.label_10.setText(_translate("Form", "竖直笔画位移："))
        self.pushButton_3.setText(_translate("Form", "预览"))
        self.pushButton_5.setText(_translate("Form", "导出"))
        self.pushButton_4.setText(_translate("Form", "保存"))
        self.pushButton_6.setText(_translate("Form", "载入"))
        self.label_12.setText(_translate("Form",
                                         "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">预设</span></p></body></html>"))
        self.lineEdit_10.setText(_translate("Form", "0"))
        self.lineEdit_11.setText(_translate("Form", "0"))
        self.lineEdit_12.setText(_translate("Form", "0"))
        self.label_13.setText(_translate("Form",
                                         "<html><head/><body><p><span style=\" font-weight:600;\">文字RGB</span></p></body></html>"))
