<?php
//解决eclipse编码GBK转换为utf-8编码问题
//项目文件放在src文件夹
//访问：http://others.yoqi.me/convert.php
function listDir($dir)
{
	echo "start!";
    if(is_dir($dir))
    {
        if ($dh = opendir($dir)) 
        {
            while (($file = readdir($dh)) !== false)
            {
                if((is_dir($dir."/".$file)) && $file!="." && $file!="..")
                {
                	//进入子文件夹
                    rename($dir."/".$file,$dir."/".mb_convert_encoding($file,"GBK", "UTF-8"));
                    listDir($dir."/".$file."/");
                }
                else
                {
                    if($file!="." && $file!="..")
                    {
                         rename($dir."/".$file,$dir."/".mb_convert_encoding($file,"GBK", "UTF-8"));
						 echo $dir."/".$file;
                    }
                }
            }
            closedir($dh);
        }
    }
	echo "finish!";
}
//开始运行

listDir("E:/web/iis/teleport");

?>