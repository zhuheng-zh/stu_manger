import database_model
class control:
    def __init__(self):
        self.d1=database_model.Database()

    def register(self, host, password):
        sql = "select host from login where host=%s;"
        if self.d1.cur.execute(sql, host):
            return False

        else:
            try:
                sql = "insert into login (host,password) values (%s,%s);"
                self.d1.cur.execute(sql, [host, password])
                self.d1.db.commit()

            except Exception as e:
                print(e)

                self.d1.db.rollback()
            return True


    def login(self, host, paaaword):
        sql = "select id from login where host=%s and password=%s;"
        if self.d1.cur.execute(sql, [host, paaaword]):
            return True
        else:
            return False





