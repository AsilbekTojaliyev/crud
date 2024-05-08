from fastapi import APIRouter, HTTPException
from products_funcs import create_product, update_product, delete_product, get_products

router_products = APIRouter(
    prefix="/products",
    tags=["Products operations"]
)


@router_products.get("/get_products")
def get_all():
    return get_products()


@router_products.post("/create_products")
def create(name: str, description: str):
    create_product(name, description)
    raise HTTPException(200, "Amaliyot muvaffaqiyatli amalga oshirildi !!!")


@router_products.put("/update_products")
def update(ident: int, name: str, description: str):
    update_product(ident, name, description)
    raise HTTPException(200, "Amaliyot muvaffaqiyatli amalga oshirildi !!!")


@router_products.delete("/delete_products")
def delete(ident: int):
    delete_product(ident)
    raise HTTPException(200, "amaliyot muvaffaqiyatli")