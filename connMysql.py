import pymysql

host = "127.0.0.1"
port = 3306
username = "root"
password = "root"
database = "crew1"


class ConnMysql(object):

    def __init__(self):
        self.conn = pymysql.Connect(host=host, port=port, user=username, password=password, database=database)
        self.cursor = self.conn.cursor()

    def exAndCom(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def innsert(self, **kwargs):
        id_ = kwargs.get("id")
        name = kwargs.get("name")
        detail = kwargs.get("detail")
        path = kwargs.get("path")
        sql = str.format("insert into info1(id, name, detail, path) value ({0}, {1}, {2}, {3})", id_, name, detail, path)
        self.exAndCom(sql)

    def delete(self, id_):
        sql = str.format("delete from info1 where id = {0}", id_)
        self.exAndCom(sql)

    def update(self, **kwargs):
        sql = "update info1 set "
        if kwargs.get("id") is None:
            return
        i = 0
        for k, v in kwargs.items():
            i += 1
            if k != "id":
                if i == len(kwargs):
                    sql = str.format("{0}{1}={2}", sql, k, v)
                else:
                    sql = str.format("{0}{1}={2},", sql, k, v)
        sql += str.format(" where id={0}", kwargs.get("id"))
        self.exAndCom(sql)

    def query(self, **kwargs):
        sql = "select * from info1"
        if len(kwargs) > 0:
            flag = True
            sql += " where"
            for k, v in kwargs.items():
                if flag:
                    flag = False
                    sql = str.format(" {0} {1}={2}", sql, k, v)
                else:
                    sql = str.format("{0} and {1} = {2}", sql, k, v)
        self.cursor.execute(sql)
        return self.cursor


def main():
    map = {
        "id": 1,
        "name": 2,
        "detail": 23,
        "path": 234
    }
    mapU = {
        "id": 1,
        "name": 222,
        "detail": 222,
        "path": 222
    }
    conn = ConnMysql()
    conn.innsert(**map)
    conn.update(**mapU)
    print("--------add after----------")
    for c in conn.query():
        print(c)
    conn.delete(1)
    print("--------delete after-------")
    for c in conn.query():
        print(c)


if __name__ == '__main__':
    main()

