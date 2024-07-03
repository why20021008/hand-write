# 手写模拟

[人走茶凉le](https://space.bilibili.com/354163879)的软件及其二次开发版本。up主的源代码为Qt版本。

# Qt版本

## 贡献者
why20021008（人走茶凉le）编写核心代码，Vincent Zhong（思维悦动）负责文档撰写，Qt版本的注释，并优化变量、函数、属性、方法的命名，去除歧义。

## 开发环境构建

推荐使用VScode，已配置`.vscode`配置文件，使用其他IDE需要自行配置，欢迎PR。  
（目前构建开发环境仅提供Windows系统，其他系统欢迎PR）Windows的命令行环境推荐`powershell`（下文简称PS），相比于`cmd`，PS支持面向对象等一系列新功能，功能更加强大。  
如有不明白的，在下方参考资料查看原文档。

首先需要创建Python虚拟环境，避免本项目与全局环境相互污染。根据Qt for Python文档，执行以下操作。

在本文件夹右键打开终端（或者在终端切换至本目录），构建虚拟环境。
```powershell
python -m venv env
```
激活虚拟环境
```powershell
env\Scripts\activate.bat
```

创建完成后，从requirements.txt中安装所需包

```powershell
pip install -r requirements.txt
```

## 踩坑笔记
- [ ] 考虑重构预览和导出，代码重复度较高
- [ ] ObjectName不知道在写什么，也许是Qt design直接做的ui？

# Electron跨平台版本

🚧正在开发🚧

# 参考资料
[Qt for Python文档](https://doc.qt.io/qtforpython-6/quickstart.html)
[handright使用教程](https://github.com/Gsllchb/Handright/blob/master/docs/tutorial.md)