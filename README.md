# 🚀快速开始
## 1.安装miniconda
一般来说都是windows 64bit 系统，不懂的话无脑下载就行
清华源miniconda Windows 64bit下载地址：
https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda-3.10.1-Windows-x86_64.exe

下载后安装，可以参考以下教程：
https://blog.csdn.net/ming12131342/article/details/140233867

## 2.创建环境和运行代码
```
conda create -n wbAuto python=3.10
conda activate wbAuto
git clone https://github.com/Demifiend217/wbAutoTools.git
cd wbAutoTools
pip install -r requirements.txt
python test.py
```

## 3.修改发布内容、发布标签、定时发布时间
```
# 微博内容
WEIBO_CONTENT = "copilot万岁！o(*￣▽￣*)ブ"

# 微博标签（示例）。将你想要的标签放在这个列表中，程序会把它们格式化为 #标签# 并拼接到正文前面
TAGS = ["茶几5mini不好用", "还得是克劳德酱w"]

# 定时发布时间
SCHEDULED_TIME = "2025-11-06 22:57:45"
```

# 🔔注意
1.默认使用谷歌浏览器\
2.打开网页需要进行登录操作，这个过程无法自动实现（毕竟要人机验证）\
3.

# （；´д｀）ゞ未来计划
1.头条文章发布功能实现
2.上传图片功能实现
3.基于pyqt的可视化界面




