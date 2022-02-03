import os

from dotenv import load_dotenv

import psycopg2

load_dotenv()
"""
要件
　　・ユーザー一覧表示
　　・新規ユーザー追加　
　　・終了する
初めに、Welcome to CRM APPlicationの表示をする

"""


def init_db():
    # DBに情報を取得　
    dsn = os.environ.get('DATABASE_URL')
    # DBに接続　　
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # SQLを用意　
    with open('schema.sql', encoding="utf-8") as f:
        sql = f.read()
        cur.execute(sql)
    # 実行状態を保存　
    conn.commit()
    # コネクションを閉じる
    conn.close()


def register_user(name, age):
    dsn = os.environ.get('DATABASE_URL')

    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    sql = f"INSERT INTO users (name,age)VALUES(%(name)s,%(age)s)"
    cur.execute(sql, {'name': name, 'age': age})
    conn.commit()

    conn.close()


def all_users():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # すべてのユーザー情報を取得
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    conn.close()
    return users


def welcome_print():
    d = open("welcome.txt", "r")
    print(d.read())
    d.close()


def main():
    init_db()
    welcome_print()
    users = all_users()

    if input('Your command>') == 'S':
        print(f"Name:{users[0][0]} Age:{users[0][1]}")
        print(f"Name:{users[1][0]} Age:{users[1][1]}")
        print(f"Name:{users[2][0]} Age:{users[2][1]}")
    else:
        print("No data")

    if input('Your command>') == 'A':
        name = 'Kazuma'
        age = 35
        register_user(name, age)
        print(f"NEW user name >{users[3][0]}")
        print(f"NEW usSer age >{users[3][1]}")
        print(f"Add new user :{name}")
    else:
        print("No data")
    if input('Your command>') == 'S':
        register_user(name, age)
        print(f"Name:{users[0][0]} Age:{users[0][1]}")
        print(f"Name:{users[1][0]} Age:{users[1][1]}")
        print(f"Name:{users[2][0]} Age:{users[2][1]}")
        print(f"Name:{users[3][0]} Age:{users[3][1]}")
    else:
        print("No data")
    if input('Your command>') == 'X':
        print(f"X:command not found")
    else:
        print("No data")
    if input('Your command>') == 'Q':
        print("Bye!")
    else:
        input("No data")


if __name__ == '__main__':
    main()
