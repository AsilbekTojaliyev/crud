from db import get_db_connection
from functions.files import create_file, delete_file, get_files
from schemas.files import Create_file
from fastapi import APIRouter, Depends

router_files = APIRouter(
    prefix="/files",
    tags=["Files operations"]
)


@router_files.post("/create_file")
def create(form: Create_file = Depends(Create_file)):
    db = get_db_connection()
    return create_file(db, form.new_file, form.product_id)


@router_files.get("/get_files")
def get():
    db = get_db_connection()
    return get_files(db)


@router_files.delete("/delete_file")
def delete(ident: int):
    db = get_db_connection()
    return delete_file(ident, db)
