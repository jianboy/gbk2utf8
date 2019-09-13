package gbk2utf8;

import java.io.File;
import java.io.IOException;
import java.util.Collection;
import org.apache.commons.io.FileUtils;

public class Convert {
	public static void main(String[] args) throws IOException {
		String srcDirPath = "/home/xx/hadoop/xxproj";
		// 转为UTF-8编码格式源码路径。这个路径可以若不存在，会自动建立。
		String utf8DirPath = "/home/xx/hadoop/1";

		// 获取所有txt,xml,java文件
		Collection<File> javaGbkFileCol = FileUtils.listFiles(new File(srcDirPath), new String[] { "txt","xml","java"}, true);

		for (File javaGbkFile : javaGbkFileCol) {
			// UTF8格式文件路径
			String utf8FilePath = utf8DirPath + javaGbkFile.getAbsolutePath().substring(srcDirPath.length());
			// 使用GBK读取数据，然后用UTF-8写入数据
			FileUtils.writeLines(new File(utf8FilePath), "UTF-8", FileUtils.readLines(javaGbkFile, "GBK"));
		}
		System.out.println("finish");
	}
}
