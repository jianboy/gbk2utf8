# gbk2utf8
## 功能介绍
之前开发的很多eclipse项目源码设置的是ANSI，即随系统编码，默认GBK编码。那么现在开发的项目源码都是UTF-8编码。很多工具打开都会出现乱码的情况。文件众多，于是开发这个项目，实现gbk文件批量转换为utf-8编码。

在网上找了一些资料，开发语言很多，这里分别用到的三种语言：Python、java、php来实现。

## 使用
1. 配置项目文件夹
python：pip install  os, chardet, codecs

2. java执行 convert.java；php执行php convert.php; python执行python convert.py即可。

## 进度
2017-12-17 python部分完成，对项目所有非utf-8编码的java文件全部转为utf-8编码。
