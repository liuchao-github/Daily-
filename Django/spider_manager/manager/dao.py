#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/11 0011 上午 11:23

base Info
"""
import pymysql
import re
import sys
import traceback

reload(sys)
sys.setdefaultencoding("utf8")

db = pymysql.connect("127.0.0.1", "root", "liu1991chao", "spider_manager", charset="utf8mb4")
# db = pymysql.connect("127.0.0.1", "root", "1234", "test", charset="utf8mb4")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data

__author__ = 'Administrator'
__version__ = '1.0'


def get_spider_on_date(date):
    sql = """SELECT * FROM manager_spider
              WHERE manager_spider.id IN
              (SELECT DISTINCT spider_id FROM manager_spiderstatus WHERE edit_time LIKE %s)"""
    try:
        cursor.execute(sql, date + "%")
        results = cursor.fetchall()

    except BaseException, e:
        print e
    return results



if __name__ == '__main__':
    get_spider_on_date("2017-09-06")