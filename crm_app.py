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

    sql = "INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"

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
    # users = all_users()

    while True:
        # users = all_users()

        command = input('Your command>')
        if command == 'S':
            users = all_users()
            for user in users:
                print(f"Name:{user[0]} Age:{user[1]}")

        elif command == 'A':
            name = input(f"New user name>")
            age = input(f"New user age>")
            register_user(name, age)

            print(f"Add new user :{name}")

        elif command == 'X':
            print(f"X:command not found")

        elif command == 'Q':
            print("Bye!")
            break

        else:
            print(f"X:command not found")

if __name__ == '__main__':
    main()
