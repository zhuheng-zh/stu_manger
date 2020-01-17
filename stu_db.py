
import pymysql
class Database:
    def __init__(self):
        # 连接数据库

        self.db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             database='st_manager',
                             charset='utf8')

        # 生成游标对象 (操作数据库,执行sql语句,获取结果)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库连接
        self.cur.close()
        self.db.close()

    def register(self, host, password):
        sql = "select host from login where host=%s;"
        if self.cur.execute(sql, host):
            return False

        else:
            try:
                sql = "insert into login (host,password) values (%s,%s);"
                self.cur.execute(sql, [host, password])
                self.db.commit()

            except Exception as e:
                print(e)

                self.db.rollback()
            return True


    def login(self, host, password):
        sql = "select id from login where host=%s and password=%s;"
        if self.cur.execute(sql, [host, password]):
            return True
        else:
            return False

if __name__ == '__main__':
    db = Database()
    db.close()

