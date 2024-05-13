from fastapi import APIRouter, HTTPException
from functions.products_funcs import get_products, get_product_by_id, create_product, update_product, delete_product
from schemas.products_schemas import CreateProduct, UpdateProduct
from db import get_db_connection

router_products = APIRouter(
    prefix="/products",
    tags=["Products operations"]
)


@router_products.get("/get_products")
def get(ident: int = None):
    db = get_db_connection()
    if ident is None:
        return get_products(db)
    return get_product_by_id(db, ident)


@router_products.post("/create_products")
def create(form: CreateProduct):
    db = get_db_connection()
    create_product(db, form)
    raise HTTPException(200, "Success!")


@router_products.put("/update_products")
def update(form: UpdateProduct):
    db = get_db_connection()
    update_product(db, form)
    raise HTTPException(200, "Success!")


@router_products.delete("/delete_products")
def delete(ident: int):
    db = get_db_connection()
    delete_product(db, ident)
    raise HTTPException(200, "Success!")
