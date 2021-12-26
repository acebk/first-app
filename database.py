import sqlite3

def get_all_facts():
    conn=sqlite3.connect('factbook.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM facts""")
    rows = cur.fetchall()
    return rows
