# 手写模拟

[人走茶凉le](https://space.bilibili.com/354163879)的软件及其二次开发版本。up主的源代码为Qt版本。

# Qt版本

下载链接：[手写模拟（windows）.zip](https://p74h-my.sharepoint.com/:u:/g/personal/minddance_p74h_onmicrosoft_com/EQthU08XKatJheO1tAAZY8UBMn7yyhQJh6n4OnbmYDgAfQ?e=RRx9W2)

## 贡献者
why20021008（人走茶凉le）编写核心代码，Vincent Zhong（思维悦动）负责文档撰写，Qt版本的注释，并优化变量、函数、属性、方法的命名，去除歧义。

# 使用说明

在右侧release处下载最新的包。然后下载常用的文件夹资源集合包，解压到同一个文件夹下即可运行。

## 开发环境构建

推荐使用VScode，已配置`.vscode`配置文件，使用其他IDE需要自行配置，如果你愿意分享教程，欢迎提出PR！  
目前构建开发环境仅提供Windows系统配置教程，Mac和Linux的可以在下方参考资料中找到，如果你愿意写这两个系统的虚拟环境配置教程，欢迎提出PR！  
Windows的命令行环境推荐`powershell`（下文简称PS），相比于`cmd`，PS支持面向对象等一系列新功能，功能更加强大。  
受限于篇幅，更详细的资料请在下方参考资料查看原文档。

首先需要创建Python虚拟环境，避免本项目与全局环境相互污染。根据Qt for Python文档，执行以下操作。

在本文件夹右键打开终端（或者在终端切换至本目录），构建虚拟环境。
```powershell
py -3 -m venv venv
```
激活虚拟环境
```powershell
venv\Scripts\activate
```

激活后，你的终端提示符会显示虚拟环境的名称。创建完成后，从requirements.txt中安装所需包

```powershell
pip install -r requirements.txt
```

修改完以后打包（虚拟环境中）

```powershell
pyinstaller -F main.py --windowed -i "ui/3d.ico" --add-data "ui/night.png:ui" -n "手写模拟"
```

## 缺陷
原本的run()函数重构为方法后无法使用多线程，期待后人的智慧

## 代码贡献
项目已经设置git action，一旦提交代码到`main`分支，就会自动编译、打包并发布。建议所有的修复bug与添加新功能的工作通过新开分支的方式进行，执行完后合并到主分支。

项目已经设置`gitignore`，会忽略常见的构建产物。

# Electron跨平台版本

🚧正在开发🚧

# 参考资料
[Qt for Python文档](https://doc.qt.io/qtforpython-6/quickstart.html)

[handright使用教程](https://github.com/Gsllchb/Handright/blob/master/docs/tutorial.md)

[Pyinstaller文档](https://pyinstaller.org/en/stable/index.html#)

[GitHub action文档](https://docs.github.com/zh/actions)