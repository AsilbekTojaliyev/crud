from fastapi import FastAPI
from products_routes import router_products

app = FastAPI(docs_url="/")

app.include_router(router_products)

