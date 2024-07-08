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
        self.font_selection_button.clicked.connect(lambda: self.handwrite_font.setText(getfile()))
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
                self.red.text(), self.green.text(), self.blue.text(), self.handwrite_font.text(),
                self.background_selection_path.text(), self.word_horizontal_margin_edit.text(), self.word_horizontal_margin_box.text(), self.word_vertical_margin_edit.text(),
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
            self.red.setText(data[0])
            self.green.setText(data[1])
            self.blue.setText(data[2])
            self.handwrite_font.setText(data[3])
            self.background_selection_path.setText(data[4])
            self.word_horizontal_margin_edit.setText(data[5])
            self.word_horizontal_margin_box.setValue(int(data[6]))
            self.word_vertical_margin_edit.setText(data[7])
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
        text = self.pending_text.toPlainText()
        font = self.handwrite_font.text()
        beijing = self.background_selection_path.text()
        # 字水平间距
        zspjj = self.word_horizontal_margin_edit.text()
        zspjj_ = self.word_horizontal_margin_box.text()
        zszjj = self.word_vertical_margin_edit.text()
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
        red = self.red.text()
        green = self.green.text()
        blue = self.blue.text()
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

        待处理文字 = self.pending_text.toPlainText()
        字体 = self.handwrite_font.text()
        背景 = self.background_selection_path.text()
        字水平间距 = self.word_horizontal_margin_edit.text()
        字水平间距干扰 = self.word_horizontal_margin_box.text()
        字竖直间距 = self.word_vertical_margin_edit.text()
        字竖直间距干扰 = self.word_vertical_margin_box.text()
        字体大小 = self.font_size_edit.text()
        字体大小干扰 = self.font_size_box.text()
        笔画水平干扰 = self.horizontal_stroke_offset.text()
        笔画竖直干扰 = self.vertical_stroke_offset.text()
        笔画旋转干扰 = self.stroke_rotation_box.text()
        左边距 = self.left_margin_edit.text()
        右边距 = self.right_margin_edit.text()
        上边距 = self.top_margin_edit.text()
        下边距 = self.bottom_margin_edit.text()
        红色 = self.red.text()
        绿色 = self.green.text()
        蓝色 = self.blue.text()
        if 字体 == "" or 字水平间距 == "" or 下边距 == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整")
        elif 待处理文字 == "":
            QMessageBox.information(self, "!!!", "未输入要处理的文字")
        elif not os.path.exists(字体):
            QMessageBox.information(self, "路径错误", "字体指定的路径不存在")
        elif not os.path.exists(背景):
            QMessageBox.information(self, "路径错误", "背景指定的路径不存在")
        else:
            if not os.path.exists("./output"):
                os.mkdir("./output")
            self.export_button.setEnabled(False)

            def run():
                template = Template(
                    background=Image.open(背景),
                    font=ImageFont.truetype(字体, size=int(字体大小)),
                    line_spacing=int(字竖直间距) + int(字体大小),
                    fill=(int(红色), int(绿色), int(蓝色)),  # 字体“颜色”
                    left_margin=int(左边距),
                    top_margin=int(上边距),
                    right_margin=int(右边距) - int(字水平间距) * 2,
                    bottom_margin=int(下边距),
                    word_spacing=int(字水平间距),
                    line_spacing_sigma=int(字竖直间距干扰),  # 行间距随机扰动
                    font_size_sigma=int(字体大小干扰),  # 字体大小随机扰动
                    word_spacing_sigma=int(字水平间距干扰),  # 字间距随机扰动
                    end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
                    perturb_x_sigma=int(笔画水平干扰),  # 笔画横向偏移随机扰动
                    perturb_y_sigma=int(笔画竖直干扰),  # 笔画纵向偏移随机扰动
                    perturb_theta_sigma=float(笔画旋转干扰),  # 笔画旋转偏移随机扰动
                )
                images = handwrite(待处理文字, template)
                for i, im in enumerate(images):
                    assert isinstance(im, Image.Image)
                    im.save("./output/{}.png".format(i))
                self.sendmsg.emit()
                self.export_button.setEnabled(True)

            t = Thread(target=run)
            t.start()

    def check(self):
        '''检查是否合规'''
        pass
    def do_run(self):
        '''运行handright代码'''
        try:
            if not os.path.exists("./output"):
                os.mkdir("./output")
            # 处理过程中导出按钮不可用，防止二次导出。
            self.export_button.setEnabled(False)
            template = Template(
                background=Image.open(self.background_selection_path.text())
                font= ImageFont.truetype(self.handwrite_font.text(), size=int(self.font_size_edit.text())),
                line_spacing=int(self.word_vertical_margin_edit.text()) + int(self.font_size_edit.text()),
                fill=(int(self.red.text()), int(self.green.text()), int(self.blue.text())),  # 字体“颜色”
                left_margin=int(self.left_margin_edit.text()),
                top_margin=int(self.top_margin_edit.text()),
                right_margin=int(self.right_margin_edit.text()) - int(self.word_horizontal_margin_edit.text()) * 2,
                bottom_margin=int(self.bottom_margin_edit.text()),
                word_spacing=int(self.word_horizontal_margin_edit.text()),
                line_spacing_sigma=int(self.word_vertical_margin_box.text()),  # 行间距随机扰动
                font_size_sigma=int(self.font_size_box.text()),  # 字体大小随机扰动
                word_spacing_sigma=int(self.word_horizontal_margin_box.text()),  # 字间距随机扰动
                end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
                perturb_x_sigma=int(self.horizontal_stroke_offset.text()),  # 笔画横向偏移随机扰动
                perturb_y_sigma=int(self.vertical_stroke_offset.text()),  # 笔画纵向偏移随机扰动
                perturb_theta_sigma=float(self.stroke_rotation_box.text())  # 笔画旋转偏移随机扰动
            )
            images = handwrite(self.pending_text, template)
            return images
        except:
            pass
        pass
        



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
