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

    sql = f"INSERT INTO users (name,age)VALUES('{name}',{age})"
    cur.execute(sql)
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


def main():
    init_db()
    users = all_users()
    command = input('Your command>')
    if command == 'S':
        print(f"Name:{users[0][0]} Age:{users[0][1]}")
        print(f"Name:{users[1][0]} Age:{users[1][1]}")
        print(f"Name:{users[2][0]} Age:{users[2][1]}")


"""
    
        d = open("schema.sql", "r")
        print(d.read())
        d.close()
"""

"""
    name = 'Bob'
    age = 20

    register_user(name,age)
"""

if __name__ == '__main__':
    main()
