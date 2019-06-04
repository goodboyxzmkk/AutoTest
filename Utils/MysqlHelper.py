import pymysql

from Public import ConfigManage

config = ConfigManage.get_default_configdic()


class MySql:
    def __init__(self, database):
        self.host = config['mysql.config']['host']
        self.port = config['mysql.config']['port']
        self.user = config['mysql.config']['user']
        self.password = config['mysql.config']['pwd']
        self.database = database

    def _GetConnect(self):

        '''得到连接信息，返回conn.cursor()'''
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                    database=self.database,
                                    charset="utf8")
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 定义游标
        # cur = self.conn.cursor()  # sqlserver连接
        if not cur:
            raise NameError('连接数据库失败')
        else:
            return cur

    def ExecQuery(self, sql):
        '''
        查询模块，传入查询语句，返回查询结果
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        '''
        cur = self._GetConnect()
        cur.execute(sql)  # 查询SQL语句
        reslist = cur.fetchall()  # 查询结果
        self.conn.close()  # 关闭连接
        return reslist

    def ExecNotQuery(self, sql):
        '''
        执行非查询语句
        '''
        cur = self._GetConnect()
        cur.execute(sql)
        self.conn.commit()  # update/delete/insert必须要这一步
        self.conn.close()

    # def CheckDB(self, testDB):
    #     db = config['mysql.config']['database']
    #     for value in db.values():
    #         print(value)
    #         if value != testDB:
    #             return False
    #     return True


if __name__ == '__main__':
    host = '59.111.124.211'
    port = 33161
    user = 'root'
    pwd = 'zhMysql6567'
    db = 'ychgoods'
    sql = "select *from Gds_GoodsClass where id='a9e100e9-1293-cc24-f107-3f46496d8a8a';"
    a = MySql(db)
    result = a.ExecQuery(sql)
    print(result)
    print(result[0]['ID'])
