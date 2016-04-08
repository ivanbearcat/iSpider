# iSpider

爬取多玩图库中的搞笑gif

## 依赖
__selenium__  
pip install selenium

__requests__  
pip install selenium

__PhantomJS__  
到Phantomjs的官方网站http://phantomjs.org/download.html  下载“Download\phantomjs-1.9.0-windows.zip”。随后打开这个压缩包，将phantomjs.exe这一个文件解压到系统路径所能找到的地方，比如“C:\Python27\Scripts”。

## 配置
manager.py:  
设置gif_dir，gif的存放目录  
worker.py:  
设置manager_host，manager的ip地址

## 运行
无先后顺序，无参数，直接运行manager.py和worker.py
ss
