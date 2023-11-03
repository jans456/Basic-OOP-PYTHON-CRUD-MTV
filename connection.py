import pymysql

def get_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='pbo1',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection