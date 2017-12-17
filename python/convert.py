# Python3 将GBK转换成utf-8编码，明天继续实现，把*.java文件 *.porperties文件都转成utf-8
import os
import chardet
import codecs


def ReadFile(filePath, dst, encoding="gbk"):
    with codecs.open(filePath, "r", encoding) as f:
        try:
            WriteFile(dst, f.read(), encoding="utf-8")
            try:
                print(filePath + "  " + encoding + " to utf-8  converted!")
            except Exception:
                print("print error")
        except Exception:
            print(filePath +"  "+ encoding+ "  read error")


def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)


def GBK_2_UTF8(src, dst):
    #     检测编码
    f = open(src, "rb")
    coding = chardet.detect(f.read())["encoding"]
    f.close()
    if coding != "utf-8":
        ReadFile(src, dst, encoding=coding)


# 递归遍历rootdir目录，把目录中的*.java编码由gbk转换为utf-8
def ReadDirectoryFile(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
            # case 1:
        for dirname in dirnames:
            #                     print("folder is:" + os.path.join(parent, dirname))
            ReadDirectoryFile(dirname)
        # case 2
        for filename in filenames:
            #                     print("filename with full path:" + os.path.join(parent, filename))
            if filename.endswith(".java"):
                GBK_2_UTF8(os.path.join(parent, filename),
                           os.path.join(parent, filename))


if __name__ == "__main__":
    src_path = "D:/liuyuqi/twtech/github/q 前端/java-note/src"
    ReadDirectoryFile(src_path)
