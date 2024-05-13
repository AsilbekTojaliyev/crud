import os
from fastapi import HTTPException


def check_if_exists(conn, ident):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM products WHERE id=?""", (ident,))
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(400, "Ma'lumot mavjud emas")


def get_files(db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM files""")
    items = cursor.fetchall()
    return [{"id": item[0], "new_file": item[1], "product_id": item[2]} for item in items]


def create_file(db, new_file, product_id):
    uploaded_file_objects = []
    ext = os.path.splitext(new_file.filename)[-1].lower()
    if ext not in [".jpg", ".png", ".mp3", ".mp4", ".gif", ".jpeg"]:
        raise HTTPException(400, "Fayl formati mos kelmadi !!!")

    file_location = f"files/{new_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(new_file.file.read())

    c = db.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS files(id INTEGER PRIMARY KEY AUTOINCREMENT, new_file TEXT, product_id INTEGER)
    """)
    new_db = c.execute("""
    INSERT INTO files (new_file, product_id) VALUES (?, ?)
    """, (new_file.filename, product_id))
    c.execute("""UPDATE products 
    SET image=? WHERE id=?""", (new_file.filename, product_id))
    uploaded_file_objects.append(new_db)
    db.commit()
    raise HTTPException(200, "Success!")


def delete_file(ident, db):
    cursor = db.cursor()
    check_if_exists(db, ident)
    cursor.execute("""DELETE FROM files
            WHERE id = ?""", (ident,))
    db.commit()
    raise HTTPException(200, "Success!")
