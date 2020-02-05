# -*- coding: utf-8 -*-
import argparse
from utils.file_tools import get_all_files
from pdf2png import convert


def main(file_dir):
    for file_path in get_all_files(file_dir=file_dir, suffix='pdf'):
        convert(file_path)
    print('convert done.')


def parse_argument():
    parser = argparse.ArgumentParser(description='Distribute Script')
    parser.add_argument('-dir', '--file_dir', dest='file_dir', default=None,
                        help='file dir path. Default: None')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_argument()
    main(file_dir=args.file_dir)
