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
        self.font_selection_button.clicked.connect(lambda: self.font.setText(getfile()))
        self.background_selection_button.clicked.connect(lambda: self.background.setText(getfile()))
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
                self.red.text(), self.green.text(), self.blue.text(), self.font.text(),
                self.background.text(), self.word_spacing.text(), self.word_spacing_sigma.text(), self.line_spacing.text(),
                self.line_spacing_sigma.text(), self.font_size.text(), self.font_size_sigma.text(), self.perturb_x_sigma.text(),
                self.perturb_y_sigma.text(), self.perturb_theta_sigma.text(), self.top_margin.text(), self.left_margin.text(),
                self.right_margin.text(), self.bottom_margin.text())
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
            self.font.setText(data[3])
            self.background.setText(data[4])
            self.word_spacing.setText(data[5])
            self.word_spacing_sigma.setValue(int(data[6]))
            self.line_spacing.setText(data[7])
            self.line_spacing_sigma.setValue(int(data[8]))
            self.font_size.setText(data[9])
            self.font_size_sigma.setValue(int(data[10]))
            self.perturb_x_sigma.setValue(int(data[11]))
            self.perturb_y_sigma.setValue(int(data[12]))
            self.perturb_theta_sigma.setValue(float(data[13]))
            self.top_margin.setText(data[14])
            self.left_margin.setText(data[15])
            self.right_margin.setText(data[16])
            self.bottom_margin.setText(data[17])


    # 预览
    def preview(self):
        if self.font.text() == "" or self.word_spacing.text() == "" or self.bottom_margin.text() == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整")
        elif self.pending_text.toPlainText() == "":
            QMessageBox.information(self, "!!!", "未输入要处理的文字")
        elif not os.path.exists(self.font.text()):
            QMessageBox.information(self, "路径错误", "字体指定的路径不存在")
        elif not os.path.exists(self.background.text()):
            QMessageBox.information(self, "路径错误", "背景指定的路径不存在")
        else:
            # 按钮变灰，防止二次导出
            self.preview_button.setEnabled(False)
            images = self.run()
            for i, im in enumerate(images):
                im = im.convert("RGBA")
                image = ImageQt.toqpixmap(im)
                self.preview_area.setScaledContents(True)
                self.preview_area.setPixmap(image)
                # 恢复导出按钮
                self.preview_button.setEnabled(True)
                break
            


    # 导出
    def export(self):
        print(self.get_template())
        if self.font.text() == "" or self.word_spacing.text() == "" or self.bottom_margin.text() == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整")
        elif self.pending_text.toPlainText() == "":
            QMessageBox.information(self, "!!!", "未输入要处理的文字")
        elif not os.path.exists(self.font.text()):
            QMessageBox.information(self, "路径错误", "字体指定的路径不存在")
        elif not os.path.exists(self.background.text()):
            QMessageBox.information(self, "路径错误", "背景指定的路径不存在")
        else:
            if not os.path.exists("./output"):
                os.mkdir("./output")
            # 处理过程中导出按钮不可用，防止二次导出。
            self.export_button.setEnabled(False)
            images = self.run()
            for i, im in enumerate(images):
                assert isinstance(im, Image.Image)
                im.save("./output/{}.png".format(i))
            self.sendmsg.emit()
            # 恢复导出按钮
            self.export_button.setEnabled(True)


    def check(self):
        '''检查是否合规'''
        pass


    def get_template(self):
        template = Template(
            # 背景
            background=Image.open(self.background.text()),
            # 字体
            font=ImageFont.truetype(self.font.text(), size=int(self.font_size.text())),
            # 行距
            line_spacing=int(self.line_spacing.text()) + int(self.font_size.text()),
            # 字体“颜色”
            fill=(int(self.red.text()), int(self.green.text()), int(self.blue.text())),
            # 左边距
            left_margin=int(self.left_margin.text()),
            # 上边距
            top_margin=int(self.top_margin.text()),
            # 右边距
            right_margin=int(self.right_margin.text()),
            # 下边距
            bottom_margin=int(self.bottom_margin.text()),
            # 字间距
            word_spacing=int(self.word_spacing.text()),
            # 行间距随机扰动
            line_spacing_sigma=int(self.line_spacing_sigma.text()),
            # 字体大小随机扰动
            font_size_sigma=int(self.font_size_sigma.text()),
            # 字间距随机扰动
            word_spacing_sigma=int(self.word_spacing_sigma.text()),
            # 特定字符提前换行，防止出现在行尾
            start_chars="“（[<",
            # 防止特定字符因排版算法的自动换行而出现在行首
            end_chars="，。",
            # 笔画横向偏移随机扰动
            perturb_x_sigma=int(self.perturb_x_sigma.text()),
            # 笔画纵向偏移随机扰动
            perturb_y_sigma=int(self.perturb_y_sigma.text()),
            # 笔画旋转偏移随机扰动
            perturb_theta_sigma=float(self.perturb_theta_sigma.text()),
        )
        return template
    

    def run(self):
        '''运行handright代码'''
        try:
            if not os.path.exists("./output"):
                os.mkdir("./output")
            template = self.get_template()
            images = handwrite(self.pending_text.toPlainText(), template)
            return images
        except:
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
