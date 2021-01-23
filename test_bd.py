import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        # conn = mysql.connector.connect(host='127.0.0.1',
        #                                database='app_db',
        #                                user='db_user',
        #                                password='db_user_pass')
        conn1 = mysql.connector.connect(host='localhost',
                                        user='db_user',
                                        password='db_user_pass')
        if conn1.is_connected():
            print('conn1 is connected to MySQL database')
            # my_cursor = conn1.cursor()
            # my_cursor.execute("SHOW DATABASES")
            # my_cursor.execute("CREATE DATABASE test_database")
            # for x in my_cursor:
            #     print(x)
            return conn1

    except Error as e:
        print(e)


def create_bd(conn2=mysql.connector.connect()):
    if conn2.is_connected():
        print('conn1 is connected to MySQL database')
        my_cursor = conn2.cursor()
        my_cursor.execute("SHOW DATABASES")
        for x in my_cursor:
            print(x)
        # my_cursor = conn.cursor()
        # my_cursor.exeсute("CREATE DATABASE my_database")


if __name__ == '__main__':
    conn3 = connect()
    create_bd(conn3)
