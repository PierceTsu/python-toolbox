#!/usr/bin/python
# encoding=utf-8
import os

FILE_DIR = 'E:/WorkSpace/test'
SRC_STR = 'href="http://'
DES_STR = 'href="https://'


def list_files(file_dir):
    """
    :param file_dir: 文件目录
    :return: file_dir目录下所有文件的路径
    """
    file_list = []
    for dir_path, dir_names, file_names in os.walk(file_dir):
        for file_name in file_names:
            if file_name.endswith('.php') or file_name.endswith('.html') or file_name.endswith('.htm') \
                    or file_name.endswith('.tpl') or file_name.endswith('.js') or file_name.endswith('.css')\
                    or file_name.endswith('.json') or file_name.endswith('.svg'):
                file_list.append(os.path.join(dir_path, file_name))
    return file_list


def main():
    count = 0
    file_list = list_files(FILE_DIR)
    for file in file_list:
        # print '|' + file
        f = open(file, 'r+')
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if SRC_STR in line:
                count += 1
            f.write(line.replace(SRC_STR, DES_STR))
        f.close()
    print 'replace: ' + str(count) + ' times!'


if __name__ == '__main__':
    main()
