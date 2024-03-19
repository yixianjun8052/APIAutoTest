import pymysql

from Common.handle_conf import conf


class HandleDB(object):

    def __init__(self):
        self.conn = pymysql.Connection(
            user=conf.get('mysql', 'user'),
            password=conf.get('mysql', 'password'),
            host=conf.get('mysql', 'host'),
            port=conf.getint('mysql', 'port'),
            database=conf.get('mysql', 'database'),
            charset=conf.get('mysql', 'charset'),
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def execute_sql(self, sql):
        # 返回结果条数。1
        self.cur.execute(sql)

    def get_all_data(self, sql):
        """
        查询所有数据
        :param sql: 查询sql
        :return: 有数据则返回字典的列表，无数据则返回空元组
        """
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_one_data(self, sql):
        """
        查询一条数据
        :param sql: 查询sql
        :return: 有数据则返回字典，无数据则返回 None
        """
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def update(self, sql):
        """
        对数据库进行增、删、改的操作：执行完 sql 语句后，要提交。
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        self.conn.commit()

    def get_counts(self, sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def close_db(self):
        self.cur.close()
        self.conn.close()

    def __del__(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db = HandleDB()
    # sql = 'select * from member limit 5;'
    # sql = 'select leave_amount from future.member where id=4874;'
    sql = 'select status from loan where id=55468;'
    # sql = "select * from future.member where mobile_phone=18600001322;"
    result = db.get_all_data(sql)
    print(result, type(result))
    result = db.get_one_data(sql)
    # print(result, type(result), result['leave_amount'], result['reg_time'])
    print(result, type(result), result['status'])
    # if result['leave_amount'] == 0.00:
    #     print(result['reg_time'])
    # sql2 = 'select cast(leave_amount as char) as leave_amount from future.member where id=4874;'
    # result2 = db.get_one_data(sql2)
    # print(result2, result2['leave_amount'], type(result2['leave_amount']))

    # from decimal import Decimal
    # print(round(db.get_one_data(sql)['leave_amount'] + Decimal(0.1), 2))

    # sql3 = 'select count(*) as count from future.financelog;'
    # result3 = db.get_one_data(sql3)
    # print(result3, type(result3), result3['count'])
