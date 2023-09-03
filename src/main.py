from fastapi import FastAPI

from src.operation.routers import router as router_operation

app = FastAPI(
    title='Мой Свагер'
)

app.include_router(router_operation)
