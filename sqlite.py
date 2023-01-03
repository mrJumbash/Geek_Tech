import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products(product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def add_products(conn, list1):
    try:
        for product in list1:
            if len(product)<=3:
                insert_product(conn, product)
            print('Done')
    except sqlite3.Error as e:
        print(e)



def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
#
def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_cheap_products(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_product_by_like(conn, selection):
    try:
        sql = """SELECT * FROM products WHERE product_title LIKE '%?%'"""
        cursor = conn.cursor()
        cursor.execute(sql, (selection, ))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
#SsS
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''

database = 'hw.db'
connection = create_connection(database)
product_list = [('Soup', 22.1, 65), ('Kids Soup', 18.9), ('Potato', 23.5, 100), ('Carrot', 31.6, 200)]
# add_products(connection, product_list)
if connection is not None:
    # create_table(connection, sql_create_products_table)
    # insert_product(connection, ('Eggs', 12.2, 100))
    # insert_product(connection, ('Bread', 25, 50))
    # insert_product(connection, ('Butter', 75, 25))
    # insert_product(connection, ('Rice', 75, 30))
    # insert_product(connection, ('Bubblegum', 5, 500))
    # insert_product(connection, ('Tomato', 25.4, 120))
    # insert_product(connection, ('Water', 18.5, 60))
    # insert_product(connection, ('Lemon', 100, 40))
    # select_cheap_products(connection)
    # select_all_products(connection)
    select_product_by_like(connection, 'Soap')
    print('Done')
    connection.close()
