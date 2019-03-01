# window下Python3.6+Qyqt5+eric6搭建 

如果已经安装多了anaconda3，它已经自带了 PyQt5，只需要安装eric6即可，

安装步骤：

1. 安装前首先在Notebook中进行测试，查看PyQt5是否安装成功，测试代码：

```
import sys

from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

widget.resize(360, 360)

widget.setWindowTitle("hello, pyqt5")

widget.show()

sys.exit(app.exec_())

```

如果有界面弹出，则说明安装成功，如果没有安装成果则需要在Anaconda Prompt进行安装，只需要输入：pip install PyQt5 进行安装。

2. 安装Eric6准备：安装好PyQt5以后，在Anaconda Prompt中进行安装Qscintilla：pip install Qscintilla ；然后同样在Anaconda Prompt中进行PyQt5 tools的安装：pip install PyQt5-tools

3. 安装Eric6：下载[Eric6地址](http://eric-ide.python-projects.org/eric-download.html)，下载获取安装包以后进行解压用Python对install.py进行解析，即可完成安装，解析命令：

   ```
   python install.py install
   ```

安装完成后会在：***\Anaconda3\Lib\site-packages中生成一个eric6文件，然后安装以上的方法在eric6所在的

文件夹，用Python对eric6.py进行解析就可以打开Eric6，进行GUI开发。

 