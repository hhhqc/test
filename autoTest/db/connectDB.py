import psycopg2

class dbUtil():
    def coonDB(self):
        ## 连接到一个给定的数据库
        self.conn = psycopg2.connect(database="zy", user="pg", password="4d565964-24d1-4c97-a586-1b5a7e229f5d", host="120.24.173.173", port="5432")
        ## 建立游标，用来执行数据库操作
        self.cur = self.conn.cursor()

    def Select(self,sql):
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows


    def closeDB(self):
        ## 关闭游标
        self.cur.close()
        ## 关闭数据库连接
        self.conn.close()