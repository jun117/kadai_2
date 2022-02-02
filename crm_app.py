import os

from dotenv import load_dotenv
import psycopg2

load_dotenv()

dsn = os.environ.get('SECRET')
conn = psycopg2.connect(dsn)
cur = conn.cursor()

with open('welcome.txt', encoding="utf-8") as f:
    print(f)

"""
要件
　　・ユーザー一覧表示
　　・新規ユーザー追加　
　　・終了する
初めに、Welcome to CRM APPlicationの表示をする

"""
