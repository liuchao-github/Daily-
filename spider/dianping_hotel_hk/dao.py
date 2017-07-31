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


def insert(i, n, d, a, w, t, p, s, r, pu):
    try:
        sql = """INSERT INTO hotel_shop_list(
                     id, name, detail_url, addr, walk, tags, price, star, review_num, picUrl)
                     VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d', '%s')""" % (
        i, n, d, a, w, t, p, s, r, pu)

        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def downloadShopUrl():
    results = []
    try:
        sql = """SELECT id
                    FROM hotel_shop_list"""
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
              shopId,shopName,area,walk,star,tag,picUrl)
              SELECT id,name,addr,walk,star,tags,picUrl
              FROM hotel_shop_list d
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


# def insert_hotel_goods(shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices):
#     # 清空原表
#     try:
#         cursor.execute("truncate hotel_room")
#         db.commit()
#     except BaseException, e:
#         db.rollback()
#         print e
#
#     for (s, r, t, b, bf, n, c, p) in zip(shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices):
#         sql = """INSERT INTO hotel_room (shopId,roomType,bedType,breakfastInfo,internet,cancelRules,roomPrice)
#                   VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%d')""" % (s, t, b, bf, n, c, p)
#         try:
#             cursor.execute(sql)
#             db.commit()
#         except BaseException, e:
#             db.rollback()
#             print e

def insert_hotel_rooms(room_info_list,query_time):
    for room_info in room_info_list:
        room = room_info["roomInfo"]

        try:
            sql = """INSERT INTO hotel_room (roomId,shopId,roomType,query_time,roomPrice_0,roomPrice_1,roomPrice_2,roomPrice_3,roomPrice_4)
                  VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                    room[0], room[1], room[2], query_time, room[3], room[4], room[5], room[6], room[7])

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


def insert_new_review_url(urls):
    sql = """INSERT INTO hotel_new_review_url (shopId,reviewUrl) VALUES('%s','%s')"""
    for u in urls:
        url_mini = u.split("?")[0]
        try:
            shopId = int(re.sub(r'\D', "", url_mini))
        except BaseException, e:
            print e
            print traceback.format_exc()

            return

        d = (shopId, u)
        try:
            cursor.execute(sql % d)
            db.commit()
        except BaseException, e:
            db.rollback()
            print e


# def init_old_review_urls():
#     sql = """SELECT reviewUrl FROM hotel_new_review_url"""
#     try:
#         cursor.execute(sql)
#         results = cursor.fetchall()
#     except BaseException, e:
#         db.rollback()
#         print e
#     urls = set(results)
#     url_manager.old_review_urls = urls


def select_new_review_urls():
    sql = """SELECT reviewUrl FROM hotel_new_review_url"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except BaseException, e:
        db.rollback()
        print e
        return
        # url_manager.old_review_urls = set(results)


def insert_ip(data):
    sql = """INSERT INTO ip (country,Ipaddress,post)
            VALUES
            ('lc','%s','%s')"""
    try:
        ip = data[0]
        port = data[1]
        cursor.execute(sql % (ip, port))
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def select_ip():
    sql = """SELECT Ipaddress,post
              FROM ip
              WHERE country = 'lc' """

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except BaseException, e:
        db.rollback()
        print e
        return
