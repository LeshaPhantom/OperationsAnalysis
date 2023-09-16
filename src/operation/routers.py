from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operation.models import Operation
from src.operation.schemas import OperationSchema

from src.operation.utils import main as dict_operation

router = APIRouter(
    prefix="/operation",
    tags=["Операции"]
)


@router.get("")
async def get_operation(ID_operation: int,
                        session: Annotated[AsyncSession, Depends(get_async_session)]):
    query = select(Operation).where(Operation.id == ID_operation)
    result = await session.execute(query)
    result = [row[0].to_read_model() for row in result.all()]
    return {
        "status": "success",
        "data": result,
        "details": None

    }


@router.post("")
async def post_operation(new_operation: OperationSchema,
                         session: Annotated[AsyncSession, Depends(get_async_session)]):
    stmt = insert(Operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.post("/auto_import")
async def post_operation(session: Annotated[AsyncSession, Depends(get_async_session)]):
    URL = 'src/operation/operationsFiles/operations.csv'
    get_dict_operation = dict_operation(URL)
    for i in range(len(get_dict_operation)):
        value = OperationSchema(**get_dict_operation[i])
        stmt = insert(Operation).values(**value.model_dump())
        await session.execute(stmt)
        await session.commit()
    return {"status": "success"}

