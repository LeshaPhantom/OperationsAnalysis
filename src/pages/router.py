from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.operation.routers import get_operation

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")

@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/search/{ID_operation}")
def get_search_page(request: Request, operation=Depends(get_operation)):
    return templates.TemplateResponse("search.html", {"request": request, "operations": operation['data']})

@router.get("/search/")
def get_search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})