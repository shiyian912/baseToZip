# baseToZip
一个简单的将经过base64编码的zip文件还原工具，使用python编写

使用方法：

将base64字符串保存到txt文件中，例如base64.txt

使用命令`python baseToZip.py -f base64.txt`

使用命令后，会出现restored_file.zip文件和restore_folder目录
restored_file.zip是还原后的zip文件，restore_folder是restored_file.zip解压后的目录。
