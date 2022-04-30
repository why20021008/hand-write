import sys
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PIL import Image, ImageFont, ImageQt
from handright import Template, handwrite
import night


def getfile():
    q = QFileDialog.getOpenFileName()
    return q[0]


def savefile():
    q = QFileDialog.getSaveFileName()
    return q[0]


class mainwindow(QMainWindow, Ui_Form):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_Form.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.lineEdit.setText(getfile()))
        self.pushButton_2.clicked.connect(lambda: self.lineEdit_2.setText(getfile()))
        self.pushButton_3.clicked.connect(self.preview)
        self.pushButton_5.clicked.connect(self.output)
        self.pushButton_4.clicked.connect(self.save)
        self.pushButton_6.clicked.connect(self.load)

    def save(self):
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

    def load(self):
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

    def preview(self):
        text = self.textEdit.toPlainText()
        font = self.lineEdit.text()
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
        EdgeDistance_left = self.lineEdit_5.text()
        EdgeDistance_right = self.lineEdit_6.text()
        EdgeDistance_up = self.lineEdit_3.text()
        EdgeDistance_down = self.lineEdit_4.text()
        red = self.lineEdit_10.text()
        green = self.lineEdit_11.text()
        blue = self.lineEdit_12.text()
        if text == "" or font == "" or zspjj == "" or EdgeDistance_down == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整", QMessageBox.Yes)
        else:
            template = Template(
                background=Image.open(beijing),
                font=ImageFont.truetype(font, size=int(ztdx)),
                line_spacing=int(zszjj) + int(ztdx),
                fill=(int(red), int(green), int(blue)),  # 字体“颜色”
                left_margin=int(EdgeDistance_left),
                top_margin=int(EdgeDistance_up),
                right_margin=int(EdgeDistance_right) - int(zspjj) * 2,
                bottom_margin=int(EdgeDistance_down),
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

    def output(self):
        text = self.textEdit.toPlainText()
        font = self.lineEdit.text()
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
        EdgeDistance_left = self.lineEdit_5.text()
        EdgeDistance_right = self.lineEdit_6.text()
        EdgeDistance_up = self.lineEdit_3.text()
        EdgeDistance_down = self.lineEdit_4.text()
        red = self.lineEdit_10.text()
        green = self.lineEdit_11.text()
        blue = self.lineEdit_12.text()
        if text == "" or font == "" or zspjj == "" or EdgeDistance_down == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整", QMessageBox.Yes)
        else:
            template = Template(
                background=Image.open(beijing),
                font=ImageFont.truetype(font, size=int(ztdx)),
                line_spacing=int(zszjj) + int(ztdx),
                fill=(int(red), int(green), int(blue)),  # 字体“颜色”
                left_margin=int(EdgeDistance_left),
                top_margin=int(EdgeDistance_up),
                right_margin=int(EdgeDistance_right) - int(zspjj) * 2,
                bottom_margin=int(EdgeDistance_down),
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


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ui = mainwindow()  # 创建自定义ui界面
    ui.show()
    sys.exit(app.exec_())

