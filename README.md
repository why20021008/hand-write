# 手写模拟

本项目以GUI交互的形式生成并导出足以媲美真人手写的文档图片。

## 使用

### 界面

![界面](assets/qt界面.png)

### 效果

![效果](assets/效果.png)

### 下载链接

以下任选一个方式下载。

[手写模拟-百度云](https://pan.baidu.com/s/16ReiVqKryIHkT84_qE5v7g?pwd=yn1z)  
提取码：yn1z

[手写模拟-OneDrive](https://1drv.ms/f/c/ce2d233c2ff03eb6/Epk-2WVaIn5DisGzqWhm94IBhVRN6T8sp6qCO_CyVTpuaQ?e=jSkagp)  
可能要魔法

[手写模拟-蓝奏云](https://wwuv.lanzouw.com/b00ocwmfcj)  
密码:1i7

## 开发环境构建

首先需要创建Python虚拟环境，避免本项目与全局环境相互污染。

在本文件夹右键打开终端（或者在终端切换至本目录），构建虚拟环境。

```powershell
python3 -m venv .venv
```

激活虚拟环境
```powershell
.venv\Scripts\activate
```

激活后，你的终端提示符会显示虚拟环境的名称。创建完成后，从requirements.txt中安装所需包

```powershell
pip install -r requirements.txt
```

修改完以后打包（虚拟环境中）

```powershell
pyinstaller -F main.py --windowed -i "ui/3d.ico" --add-data "ui/night.png:ui" -n "手写模拟"
```

## 路线图

🚧开发ing🚧

- [ ] Web前端工程：收集参数后以api的形式发给后端
- [ ] Flask后端工程：收集api中的参数后调用handright库
- [ ] Python托盘图标应用：常驻任务栏右下角
- [ ] 应用打包：打包为一个压缩包或者安装包

可能会加的功能（想做，但是有点过于复杂，不一定能做）

- [ ] 自由排版
- [ ] 手写公式

## 相关链接

[Qt for Python文档](https://doc.qt.io/qtforpython-6/quickstart.html)

[handright使用教程](https://github.com/Gsllchb/Handright/blob/master/docs/tutorial.md)

[Pyinstaller文档](https://pyinstaller.org/en/stable/index.html#)

[GitHub action文档](https://docs.github.com/zh/actions)
