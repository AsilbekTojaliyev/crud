import os
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from routes.products_routes import router_products
from routes.files import router_files

app = FastAPI(docs_url="/")

app.include_router(router_files)
app.include_router(router_products)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.get('/files/{fileName}')
async def get_file(fileName: str):
    path = f"./files/{fileName}"
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(400, "Not Found")

