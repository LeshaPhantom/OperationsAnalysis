from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


from src.database import get_async_session
from src.operation.models import Operation
from src.operation.schemas import OperationSchema

router = APIRouter(
    prefix="/operation",
    tags=["Операции"]
)
@router.get("")
async def get_operation(operation_type: int, session: Annotated[AsyncSession, Depends(get_async_session)]):
    query = select(Operation).where(Operation.id == operation_type)
    result = await session.execute(query)
    result = [row[0].to_read_model() for row in result.all()]
    return result
@router.post("")
async def post_operation(new_operation: OperationSchema, session: Annotated[AsyncSession, Depends(get_async_session)]):
    stmt = insert(Operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
