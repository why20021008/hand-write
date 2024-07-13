
from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        # 设置窗口对象的名称为"Form"，便于在调试和对象查找时识别。
        Form.setObjectName("Form")
        # 设置窗口为非模态窗口，该窗口打开时，用户仍可以与父窗口或其他窗口交互。
        Form.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        # 启用该窗口，不隐藏
        Form.setEnabled(True)
        # 窗口大小
        Form.resize(848, 592)
        # 大小调整策略
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(848, 592))
        Form.setMaximumSize(QtCore.QSize(848, 592))
        # 设置窗口图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./ui/3d.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        # 设置窗口透明度
        Form.setWindowOpacity(0.98)
        # 设置窗口描述，用于无障碍
        Form.setAccessibleDescription("")
        # 设置窗口的布局方向，汉语言为从左到右，从上到下。
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        # 样式表
        Form.setStyleSheet("font: 10pt 楷体; border-radius: 3px;")

        # 待处理文本编辑器
        self.pending_text = QtWidgets.QTextEdit(Form)
        self.pending_text.setGeometry(QtCore.QRect(430, 30, 411, 221))
        self.pending_text.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pending_text.setAutoFillBackground(False)
        self.pending_text.setStyleSheet("border-radius: 30px;")
        self.pending_text.setObjectName("textEdit")

        # 字体选择路径
        self.font = QtWidgets.QLineEdit(Form)
        self.font.setGeometry(QtCore.QRect(480, 280, 311, 20))
        self.font.setText("")
        self.font.setObjectName("lineEdit")

        # 字体选择按钮
        self.font_selection_button = QtWidgets.QPushButton(Form)
        self.font_selection_button.setGeometry(QtCore.QRect(792, 281, 45, 18))
        self.font_selection_button.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.font_selection_button.setObjectName("pushButton")
        
        # 背景选择按钮
        self.background_selection_button = QtWidgets.QPushButton(Form)
        self.background_selection_button.setGeometry(QtCore.QRect(792, 311, 45, 18))
        self.background_selection_button.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.background_selection_button.setObjectName("pushButton_2")

        # 背景选择路径
        self.background = QtWidgets.QLineEdit(Form)
        self.background.setGeometry(QtCore.QRect(480, 310, 311, 20))
        self.background.setText("")
        self.background.setObjectName("lineEdit_2")
        
        # 上边距文本框
        self.top_margin = QtWidgets.QLineEdit(Form)
        self.top_margin.setGeometry(QtCore.QRect(720, 357, 61, 24))
        self.top_margin.setText("")
        self.top_margin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.top_margin.setObjectName("top_margin")
        
        # 下边距文本框
        self.bottom_margin = QtWidgets.QLineEdit(Form)
        self.bottom_margin.setGeometry(QtCore.QRect(720, 431, 61, 24))
        self.bottom_margin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bottom_margin.setObjectName("lineEdit_4")
        
        # 左边距文本框
        self.left_margin = QtWidgets.QLineEdit(Form)
        self.left_margin.setGeometry(QtCore.QRect(697, 380, 24, 51))
        self.left_margin.setText("")
        self.left_margin.setObjectName("lineEdit_5")

        # 右边距文本框
        self.right_margin = QtWidgets.QLineEdit(Form)
        self.right_margin.setGeometry(QtCore.QRect(780, 380, 24, 51))
        self.right_margin.setObjectName("lineEdit_6")

        # 字水平边距设置框
        self.word_spacing_sigma = QtWidgets.QSpinBox(Form)
        self.word_spacing_sigma.setGeometry(QtCore.QRect(600, 360, 51, 20))
        self.word_spacing_sigma.setObjectName("spinBox")

        # 字水平边距文本框
        self.word_spacing = QtWidgets.QLineEdit(Form)
        self.word_spacing.setGeometry(QtCore.QRect(514, 360, 74, 20))
        self.word_spacing.setObjectName("lineEdit_7")

        # 字竖直边距文本框
        self.line_spacing = QtWidgets.QLineEdit(Form)
        self.line_spacing.setGeometry(QtCore.QRect(514, 400, 74, 20))
        self.line_spacing.setObjectName("lineEdit_8")
        
        # 字竖直边距设置框
        self.line_spacing_sigma = QtWidgets.QSpinBox(Form)
        self.line_spacing_sigma.setGeometry(QtCore.QRect(600, 400, 51, 20))
        self.line_spacing_sigma.setObjectName("spinBox_2")
        
        # 字体大小文本框
        self.font_size = QtWidgets.QLineEdit(Form)
        self.font_size.setGeometry(QtCore.QRect(514, 440, 74, 20))
        self.font_size.setObjectName("lineEdit_9")
        
        # 字体大小设置框
        self.font_size_sigma = QtWidgets.QSpinBox(Form)
        self.font_size_sigma.setGeometry(QtCore.QRect(600, 440, 51, 20))
        self.font_size_sigma.setObjectName("spinBox_3")
        
        # 竖直笔画偏移设置框
        self.perturb_y_sigma = QtWidgets.QSpinBox(Form)
        self.perturb_y_sigma.setGeometry(QtCore.QRect(600, 520, 51, 20))
        self.perturb_y_sigma.setProperty("value", 4)
        self.perturb_y_sigma.setObjectName("spinBox_4")
        
        # 水平笔画偏移设置框
        self.perturb_x_sigma = QtWidgets.QSpinBox(Form)
        self.perturb_x_sigma.setGeometry(QtCore.QRect(600, 480, 51, 20))
        self.perturb_x_sigma.setProperty("value", 4)
        self.perturb_x_sigma.setObjectName("spinBox_5")
        
        # 笔画旋转设置框
        self.perturb_theta_sigma = QtWidgets.QDoubleSpinBox(Form)
        self.perturb_theta_sigma.setGeometry(QtCore.QRect(600, 560, 51, 20))
        self.perturb_theta_sigma.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.perturb_theta_sigma.setSingleStep(0.01)
        self.perturb_theta_sigma.setProperty("value", 0.05)
        self.perturb_theta_sigma.setObjectName("doubleSpinBox_6")

        # 预览按钮
        self.preview_button = QtWidgets.QPushButton(Form)
        self.preview_button.setGeometry(QtCore.QRect(700, 500, 101, 31))
        self.preview_button.setStyleSheet("background-color: rgb(157, 220, 128);")
        self.preview_button.setObjectName("pushButton_3")

        # 导出按钮
        self.export_button = QtWidgets.QPushButton(Form)
        self.export_button.setGeometry(QtCore.QRect(700, 540, 101, 31))
        self.export_button.setStyleSheet("background-color: rgb(157, 220, 128);")
        self.export_button.setObjectName("pushButton_5")

        # 预览区域
        self.preview_area = QtWidgets.QLabel(Form)
        self.preview_area.setGeometry(QtCore.QRect(3, 1, 420, 593))
        self.preview_area.setText("")
        self.preview_area.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.preview_area.setObjectName("label_11")

        # 主界面（除所有按钮、文本框之外的区域）
        self.main_interface = QtWidgets.QListView(Form)
        self.main_interface.setGeometry(QtCore.QRect(-5, -9, 861, 611))
        self.main_interface.setStyleSheet("background-image: url(./ui/night.png); color: rgb(11, 214, 255);")
        self.main_interface.setObjectName("listView")
        
        # 保存按钮
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(600, 334, 51, 23))
        self.save_button.setAutoFillBackground(False)
        self.save_button.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.save_button.setObjectName("pushButton_4")
        
        # 载入按钮
        self.load_utton = QtWidgets.QPushButton(Form)
        self.load_utton.setGeometry(QtCore.QRect(514, 334, 74, 23))
        self.load_utton.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.load_utton.setAutoDefault(False)
        self.load_utton.setObjectName("pushButton_6")
        
        # R文本框
        self.red = QtWidgets.QLineEdit(Form)
        self.red.setGeometry(QtCore.QRect(727, 259, 31, 20))
        self.red.setObjectName("lineEdit_10")
        
        # G文本框
        self.green = QtWidgets.QLineEdit(Form)
        self.green.setGeometry(QtCore.QRect(760, 259, 31, 20))
        self.green.setObjectName("lineEdit_11")
        self.blue = QtWidgets.QLineEdit(Form)
        
        # B文本框
        self.blue.setGeometry(QtCore.QRect(793, 259, 31, 20))
        self.blue.setObjectName("lineEdit_12")
        
        # 显示控件？
        self.main_interface.raise_()
        self.pending_text.raise_()
        self.font.raise_()
        self.font_selection_button.raise_()
        self.background_selection_button.raise_()
        self.background.raise_()
        self.top_margin.raise_()
        self.bottom_margin.raise_()
        self.left_margin.raise_()
        self.right_margin.raise_()
        self.word_spacing_sigma.raise_()
        self.word_spacing.raise_()
        self.line_spacing.raise_()
        self.line_spacing_sigma.raise_()
        self.font_size.raise_()
        self.font_size_sigma.raise_()
        self.perturb_y_sigma.raise_()
        self.perturb_x_sigma.raise_()
        self.perturb_theta_sigma.raise_()
        self.preview_button.raise_()
        self.export_button.raise_()
        self.preview_area.raise_()
        self.save_button.raise_()
        self.load_utton.raise_()
        self.red.raise_()
        self.green.raise_()
        self.blue.raise_()
        self.retranslateUi(Form)
        # self.stroke_rotation_box.setStyleSheet("background-color: rgb(255, 0, 0);")  # 高亮查找特定位置
        QtCore.QMetaObject.connectSlotsByName(Form)

    # 原本为多语言的国际化支持，这里似乎用于重写？
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "手写模拟"))
        self.pending_text.setPlaceholderText(_translate("Form", "本软件主要基于handwrite库开发，仅供学习交流。作者只是一名为手写作业发愁的大学生，想要源码或者想要添加功能、反馈bug的，可以联系作者b站：人走茶凉le"))
        self.font.setAccessibleDescription(_translate("Form", "1111"))
        self.font_selection_button.setText(_translate("Form", "选择"))
        self.background_selection_button.setText(_translate("Form", "选择"))
        self.background.setAccessibleDescription(_translate("Form", "1111"))
        self.preview_button.setText(_translate("Form", "预览"))
        self.export_button.setText(_translate("Form", "导出"))
        self.save_button.setText(_translate("Form", "保存"))
        self.load_utton.setText(_translate("Form", "载入预设"))
        self.red.setText(_translate("Form", "0"))
        self.green.setText(_translate("Form", "0"))
        self.blue.setText(_translate("Form", "0"))
