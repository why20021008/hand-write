import sys
import os
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PIL import Image, ImageFont, ImageQt
from handright import Template, handwrite
from threading import Thread

from ui import *


class mainwindow(QMainWindow, Ui_Form):
    sendmsg = Signal()

    def __init__(self):
        QMainWindow.__init__(self)
        # Ui_Form.__init__(self)
        self.setupUi(self)
        # 按钮发送信号
        self.font_selection_button.clicked.connect(lambda: self.font_selection_path.setText(getfile()))
        self.background_selection_button.clicked.connect(lambda: self.background_selection_path.setText(getfile()))
        self.preview_button.clicked.connect(self.preview)
        self.export_button.clicked.connect(self.export)
        self.save_button.clicked.connect(self.save)
        self.load_utton.clicked.connect(self.load)
        self.sendmsg.connect(self.msg)
    # 导出完成消息窗
    def msg(self):
        QMessageBox.information(self, "完成", "已导出图片到output目录下")

    # 保存
    def save(self):
        file_path = savefile()
        if file_path != "":
            file_text = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (
                self.r_edit.text(), self.g_edit.text(), self.b_edit.text(), self.font_selection_path.text(),
                self.background_selection_path.text(), self.word_horizontal_margin_edit.text(), self.spinBox.text(), self.lineEdit_8.text(),
                self.word_vertical_margin_box.text(), self.font_size_edit.text(), self.font_size_box.text(), self.horizontal_stroke_offset.text(),
                self.vertical_stroke_offset.text(), self.stroke_rotation_box.text(), self.top_margin_edit.text(), self.left_margin_edit.text(),
                self.right_margin_edit.text(), self.bottom_margin_edit.text())
            with open(file=file_path, mode='w', encoding='utf-8') as file:
                file.write(file_text)
    # 载入
    def load(self):
        file_path = getfile()
        if file_path != "":
            data = []
            if file_path is not None:
                with open(file=file_path, mode='r+', encoding='utf-8') as f:
                    for line in f.readlines():
                        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                        data.append(line)
            self.r_edit.setText(data[0])
            self.g_edit.setText(data[1])
            self.b_edit.setText(data[2])
            self.font_selection_path.setText(data[3])
            self.background_selection_path.setText(data[4])
            self.word_horizontal_margin_edit.setText(data[5])
            self.spinBox.setValue(int(data[6]))
            self.lineEdit_8.setText(data[7])
            self.word_vertical_margin_box.setValue(int(data[8]))
            self.font_size_edit.setText(data[9])
            self.font_size_box.setValue(int(data[10]))
            self.horizontal_stroke_offset.setValue(int(data[11]))
            self.vertical_stroke_offset.setValue(int(data[12]))
            self.stroke_rotation_box.setValue(float(data[13]))
            self.top_margin_edit.setText(data[14])
            self.left_margin_edit.setText(data[15])
            self.right_margin_edit.setText(data[16])
            self.bottom_margin_edit.setText(data[17])
    # 预览
    def preview(self):
        text = self.pending_text_editor.toPlainText()
        font = self.font_selection_path.text()
        beijing = self.background_selection_path.text()
        # 字水平间距
        zspjj = self.word_horizontal_margin_edit.text()
        zspjj_ = self.spinBox.text()
        zszjj = self.lineEdit_8.text()
        zszjj_ = self.word_vertical_margin_box.text()
        # 字体大小
        ztdx = self.font_size_edit.text()
        ztdx_ = self.font_size_box.text()
        # 水平笔画位移 Stroke horizontal shifting
        spbhwy_ = self.horizontal_stroke_offset.text()
        # 竖直笔画位移 Stroke vertical shifting
        szbhwy_ = self.vertical_stroke_offset.text()
        # 笔画旋转 	Stroke rotating
        bhxz_ = self.stroke_rotation_box.text()
        # 边距
        bianju_left = self.left_margin_edit.text()
        bianju_right = self.right_margin_edit.text()
        bianju_up = self.top_margin_edit.text()
        bianju_down = self.bottom_margin_edit.text()
        red = self.r_edit.text()
        green = self.g_edit.text()
        blue = self.b_edit.text()
        if font == "" or zspjj == "" or bianju_down == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整")
        elif text == "":
            QMessageBox.information(self, "!!!", "未输入要处理的文字")
        elif not os.path.exists(font):
            QMessageBox.information(self, "路径错误", "字体指定的路径不存在")
        elif not os.path.exists(beijing):
            QMessageBox.information(self, "路径错误", "背景指定的路径不存在")
        else:
            def run():
                self.preview_button.setEnabled(False)
                template = Template(
                    background=Image.open(beijing),
                    font=ImageFont.truetype(font, size=int(ztdx)),
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

                    self.preview_area.setScaledContents(True)
                    self.preview_area.setPixmap(image)
                    self.preview_button.setEnabled(True)
                    break

            t = Thread(target=run)
            t.start()

    # 导出
    def export(self):

        text = self.pending_text_editor.toPlainText()
        font = self.font_selection_path.text()
        background = self.background_selection_path.text()
        zspjj = self.word_horizontal_margin_edit.text()
        zspjj_ = self.spinBox.text()
        zszjj = self.lineEdit_8.text()
        zszjj_ = self.word_vertical_margin_box.text()
        ztdx = self.font_size_edit.text()
        ztdx_ = self.font_size_box.text()
        spbhwy_ = self.horizontal_stroke_offset.text()
        szbhwy_ = self.vertical_stroke_offset.text()
        bhxz_ = self.stroke_rotation_box.text()
        bianju_left = self.left_margin_edit.text()
        bianju_right = self.right_margin_edit.text()
        bianju_up = self.top_margin_edit.text()
        bianju_down = self.bottom_margin_edit.text()
        red = self.r_edit.text()
        green = self.g_edit.text()
        blue = self.b_edit.text()
        if font == "" or zspjj == "" or bianju_down == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整")
        elif text == "":
            QMessageBox.information(self, "!!!", "未输入要处理的文字")
        elif not os.path.exists(font):
            QMessageBox.information(self, "路径错误", "字体指定的路径不存在")
        elif not os.path.exists(background):
            QMessageBox.information(self, "路径错误", "背景指定的路径不存在")
        else:
            if not os.path.exists("./output"):
                os.mkdir("./output")
            self.export_button.setEnabled(False)

            def run():
                template = Template(
                    background=Image.open(background),
                    font=ImageFont.truetype(font, size=int(ztdx)),
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
                self.export_button.setEnabled(True)

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
