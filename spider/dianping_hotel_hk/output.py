# coding=utf-8

import pymysql
import result_manager
import url_manager
import re
import sys
import traceback

reload(sys)
sys.setdefaultencoding("utf8")

db = pymysql.connect("192.168.1.166", "root", "keystone", "k11data", charset="utf8mb4")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data
print pymysql.paramstyle


def insert(i, n, d, a, w, t, p, s, r):
    try:
        sql = """INSERT INTO dianping_hotel_hk_liuchao(
                     id, name, detail_url, addr, walk, tags, price, star, review_num)
                     VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d')""" % (i, n, d, a, w, t, p, s, r)

        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def downloadShopUrl():
    results = []
    try:
        sql = """SELECT id
                    FROM dianping_hotel_hk_liuchao"""
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        db.rollback()
        print e

    return results


def insert_hotel_shops():
    """
    从dianping_hotel_hk_liuchao中把数据更新到hotel_shops中，
    要在每次准备爬取新的shop前调用一次
    :return:
    """

    sql = """INSERT INTO hotel_shops (
              shopId,shopName,area,walk,star,tag)
              SELECT id,name,addr,walk,star,tags
              FROM dianping_hotel_hk_liuchao d
              WHERE d.id NOT IN (SELECT shopId FROM hotel_shops)"""
    try:
        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def update_hotel_shops(shopId, addr, tel, openTime, checkTime, facs, room_facs, services, info):
    """hotel_shop的部分信息已经由insert_hotel_shops插入，剩下的信息在这里补全"""
    sql = """UPDATE hotel_shops SET addr = '%s',tel = '%s',openTime = '%s',checkTime = '%s',facilities = '%s',roomFac = '%s', service = '%s',info = '%s' WHERE hotel_shops.shopId = '%d'""" % (
        addr, tel, openTime, checkTime, facs, room_facs, services, info, shopId)
    try:
        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def insert_hotel_goods(shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices):
    # 清空原表
    try:
        cursor.execute("truncate hotel_room")
        db.commit()
    except BaseException, e:
        db.rollback()
        print e

    for (s, r, t, b, bf, n, c, p) in zip(shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices):
        sql = """INSERT INTO hotel_room (shopId,roomType,bedType,breakfastInfo,internet,cancelRules,roomPrice)
                  VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%d')""" % (s, t, b, bf, n, c, p)
        try:
            cursor.execute(sql)
            db.commit()
        except BaseException, e:
            db.rollback()
            print e


def insert_hotel_review():
    while (result_manager.has_new_result()):
        res = result_manager.get_new_result()
        shopId = res[0]
        review_id = res[1]
        user_id = res[2]
        reviewStar = res[3]
        room = res[4]
        loc = res[5]
        service = res[6]
        health = res[7]
        fac = res[8]
        comment_txt = res[9]
        create_time = res[10]
        like = res[11]
        reply_num = res[12]

        sql = """INSERT INTO hotel_review (reviewId,memberId,shopId,reviewStar,room,location,service,health,
              facilities,content,creatTime,likes,reply)
              values('%d','%d','%d','%d','%d','%d','%d','%d','%d','%s','%s','%d','%d')""" % \
              (review_id, user_id, shopId, reviewStar, room, loc, service, health, fac, comment_txt, create_time, like,
               reply_num,)
        sql1 = """INSERT INTO hotel_review (reviewId,memberId,shopId,reviewStar,room,location,service,health,
                      facilities,content,creatTime,likes,reply)
                      values(?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        sql2 = """INSERT INTO hotel_review (reviewId,memberId,shopId,reviewStar,room,location,service,health,
                      facilities,content,creatTime,likes,reply)
                      values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        data = (review_id, user_id, shopId, reviewStar, room, loc, service, health, fac,
                comment_txt.replace("'", "").replace('"', ""),
                create_time, like,
                reply_num)
        try:
            cursor.execute(sql2 % data)
            db.commit()
        except BaseException, e:
            db.rollback()
            print e
            # print "review_id", review_id
            # print sql


def add_review_url_crawled(url):
    sql = """INSERT INTO hotel_review_url_crawled (shopId,reviewUrl) VALUES('%s','%s')"""
    u = url
    url_mini = url.split("?")[0]
    try:
        shopId = int(re.sub(r'\D', "", url_mini))
    except BaseException, e:
        print e
        print traceback.format_exc()
        print "add_review_url_crawled(url) ----------------------------------- url:",url
        return

    d = (shopId, url)
    try:
        cursor.execute(sql % d)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def init_old_review_urls():
    sql = """SELECT reviewUrl FROM hotel_review_url_crawled"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        db.rollback()
        print e
    urls = set(results)
    url_manager.old_review_urls = urls


def get_last_old_review_urls():
    sql = """select reviewUrl from hotel_review_url_crawled a
              where not exists
              (select * from hotel_review_url_crawled where shopId=a.shopId and reviewUrl>a.reviewUrl)
              GROUP BY shopId              
              ORDER BY shopId"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except BaseException, e:
        db.rollback()
        print e
        return
        # url_manager.old_review_urls = set(results)
