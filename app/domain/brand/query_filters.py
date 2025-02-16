from pydantic import BaseModel

class RouteBrandsParams(BaseModel):
    detail: bool = True
