from fastapi import UploadFile
from pydantic import BaseModel, Field


class Create_file(BaseModel):
    new_file: UploadFile
    product_id: int = Field(..., gt=0)
