from sqlite3 import connect
from fastapi import HTTPException


def check_if_exists(ident):
    with connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM products WHERE id=?""", (ident,))
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            raise HTTPException(400, "malumot mavjud emas")


def get_products():
    with connect("data.db") as con:
        c = con.cursor()
        c.execute("""SELECT * FROM products""")
        items = c.fetchall()
        c.close()
        return items


def create_product(name, description):
    with connect("data.db") as con:
        c = con.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS products
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)
                    """)
        c.execute(f"""
                    INSERT INTO products (name, description) VALUES (?, ?)
                    """, (name, description))
        c.close()


def update_product(ident, name, description):
    check_if_exists(ident)
    with connect("data.db") as con:
        c = con.cursor()
        c.execute(f"""
                    UPDATE products 
                    SET name = ?, description = ? 
                    WHERE id = ?""", (name, description, ident))
        c.close()


def delete_product(ident):
    check_if_exists(ident)
    with connect("data.db") as con:
        c = con.cursor()
        c.execute(f"""DELETE FROM products 
        WHERE id = ?""", (ident,))
        c.close()
