# -*- coding: utf-8 -*-
import os


def get_all_files(file_dir, suffix=None):
    """
    :param file_dir: 文件目录
    :param suffix: 文件后缀名
    :return: file_dir目录下所有文件的路径
    """
    assert os.path.isdir(file_dir), '文件夹路径不合法!'
    file_list = []
    for dir_path, _, file_names in os.walk(file_dir):
        for file_name in file_names:
            if suffix:
                if file_name.endswith(suffix):
                    file_list.append(os.path.join(dir_path, file_name))
            else:
                file_list.append(os.path.join(dir_path, file_name))
    return file_list

