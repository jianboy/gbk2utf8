# Python3 将GBK转换成utf-8编码，明天继续实现，把*.java文件 *.porperties文件都转成utf-8
import os
import chardet
import codecs


def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)


def GBK_2_UTF8(src, dst):
    #     检测编码，coding可能检测不到编码，有异常
    f = open(src, "rb")
    coding = chardet.detect(f.read())["encoding"]
    f.close()
    if coding != "utf-8":
        with codecs.open(src, "r", encoding) as f:
            try:
                WriteFile(dst, f.read(), coding="utf-8")
                try:
                    print(src + "  " + coding + " to utf-8  converted!")
                except Exception:
                    print("print error")
            except Exception:
                print(src +"  "+ coding+ "  read error")

# 把目录中的*.java编码由gbk转换为utf-8
def ReadDirectoryFile(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for dirname in dirnames:
          	#递归函数，遍历所有子文件夹
            ReadDirectoryFile(dirname)
        for filename in filenames:
            if filename.endswith(".java"):
                GBK_2_UTF8(os.path.join(parent, filename),
                           os.path.join(parent, filename))

if __name__ == "__main__":
    src_path = "D:/liuyuqi/twtech/github/q 前端/java-note/src"
    ReadDirectoryFile(src_path)
