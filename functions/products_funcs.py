from fastapi import HTTPException


def check_if_exists(conn, ident):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM products WHERE id=?""", (ident,))
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(400, "malumot mavjud emas")


def get_product_by_id(conn, ident):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM products WHERE id = ?""", (ident,))
    item = cursor.fetchone()
    return [{"id": item[0], "name": item[1], "description": item[2], "image": item[3], "price": item[4]}]


def get_products(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM products""")
    items = cursor.fetchall()
    return [{"id": item[0], "name": item[1], "description": item[2], "image": item[3], "price": item[4]} for item in items]


def create_product(conn, form):
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS products
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), description TEXT,
                    image TEXT, price DOUBLE)""")
    cursor.execute("""
                    INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)
                    """, (form.name, form.description, form.image, form.price))
    conn.commit()


def update_product(conn, form):
    cursor = conn.cursor()
    check_if_exists(conn, form.id)
    cursor.execute("""
                    UPDATE products
                    SET name = ?, description = ?, image = ?, price = ? WHERE id = ?
                    """, (form.name, form.description, form.image, form.price, form.id))
    conn.commit()


def delete_product(conn, ident):
    cursor = conn.cursor()
    check_if_exists(conn, ident)
    cursor.execute("""DELETE FROM products
            WHERE id = ?""", (ident,))
    conn.commit()
