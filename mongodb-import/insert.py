# coding=utf-8


# 批量导入json
import json
import pymongo


if __name__ == '__main__':

    conn = pymongo.MongoClient("localhost", 27017)
    db = conn['wb']
    user_collection = db['user']
    f = open("user.json")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        print line,  # 后面跟 ',' 将忽略换行符
        user_collection.insert(json.loads(line))
        line = f.readline()
    f.close()
