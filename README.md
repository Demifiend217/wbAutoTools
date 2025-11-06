# 快速开始
## 安装miniconda
一般来说都是windows 64bit 系统，不懂的话无脑下载就行
清华源miniconda Windows 64bit下载地址：
https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda-3.10.1-Windows-x86_64.exe

下载后安装，可以参考以下教程：
https://blog.csdn.net/ming12131342/article/details/140233867

## 创建环境和运行代码
```
conda create -n wbAuto python=3.10
conda activate wbAuto
git clone https://github.com/Demifiend217/wbAutoTools.git
cd wbAutoTools
pip install -r requirements.txt
python test.py
```

## 修改发布时间和发布内容
```
# 微博内容直接修改test字段
WEIBO_CONTENT = "test"

# 定时发布时间，注意格式：2025-11-06 22:57:45
SCHEDULED_TIME = "2025-11-06 22:57:45"
```

# 注意
1.默认使用谷歌浏览器\
2.打开网页需要进行登录操作，这个过程无法自动实现（毕竟要人机验证）\
3.tag功能未测试\

