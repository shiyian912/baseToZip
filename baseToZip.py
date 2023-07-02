# -*- coding: utf-8 -*-
import argparse
import base64
import zipfile


def main():
    parser = argparse.ArgumentParser(description='This is a simple base64 encoded zip file restoration tool')
    parser.add_argument('-f', '--file', type=str, required=True)

    args = parser.parse_args()

    restoration(args)


def restoration(args):
    # 经过Base64编码的ZIP文件数据
    base64_encoded_data = open(args.file, 'r').read()

    # 解码Base64数据
    decoded_data = base64.b64decode(base64_encoded_data)

    # 写入解码后的数据到ZIP文件
    with open("restored_file.zip", "wb") as file:
        file.write(decoded_data)

    print("ZIP文件已还原")

    # 如果需要提取ZIP中的文件内容，可以使用zipfile模块
    with zipfile.ZipFile("restored_file.zip", 'r') as zip_ref:
        # 提取所有文件到目标文件夹
        zip_ref.extractall("restore_folder")

    print("ZIP文件已解压缩")


if __name__ == '__main__':
    main()
