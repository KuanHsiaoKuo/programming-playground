import sqlite3

# 如果不存在则自动创建并连接
conn = sqlite3.connect('./mytest1.db')

# con.execute("create table lang (id integer primary key, name varchar unique)")
# Successful, con.commit() is called automatically afterwards
with conn:
    conn.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')
j