from fastapi import FastAPI

from src.operation.routers import router as router_operation

# import csv

app = FastAPI(
    title='Мой Свагер'
)

app.include_router(router_operation)


#     with open('src/operations/operationsFiles/operations.csv') as f:
#     reader = csv.reader(f)
#     headers = next(reader)
#     print('Headers: ', headers)
#     operations = list(reader)
#     print(operations)
