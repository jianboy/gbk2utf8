package cwj.bbb;

import java.io.*;
import java.util.Collection;

import org.apache.commons.io.FileUtils;
/*
 * 批量把文本文档的GBK编码转化为UTF-8
 * 使用用commons-io.jar实现文件的读取和写入
 * */

public class EncodeTest1 {
	public static void main(String[] args) throws IOException {
		String srcDirPath = "/home/cwjy1202/hadoop/旅游领域/旅游类测试文档/地方文化";
		// 转为UTF-8编码格式源码路径。这个路径可以若不存在，会自动建立。
		String utf8DirPath = "/home/cwjy1202/hadoop/旅游领域/旅游类测试文档/地方文化1";

		// 获取所有txt文件
		Collection<File> javaGbkFileCol = FileUtils.listFiles(new File(srcDirPath), new String[] { "txt" }, true);

		for (File javaGbkFile : javaGbkFileCol) {
			// UTF8格式文件路径
			String utf8FilePath = utf8DirPath + javaGbkFile.getAbsolutePath().substring(srcDirPath.length());
			// 使用GBK读取数据，然后用UTF-8写入数据
			FileUtils.writeLines(new File(utf8FilePath), "UTF-8", FileUtils.readLines(javaGbkFile, "GBK"));
		}

	}
}