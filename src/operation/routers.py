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

new_operation_insert = {'id': 1,
                        'data_time_operation': 'string',
                        'data_payment': 'string',
                        'card_number': 'str',
                        'status_operation': True,
                        'sum_operation': 'string',
                        'currency_operation': 'string',
                        'sum_payment': 'string',
                        'currency_payment': 'string',
                        'cashback': 0,
                        'category': 'string',
                        'mss': 0,
                        'description': 'string',
                        'bonus_cashback': 'string',
                        'rounding_invest': 'string',
                        'rounding_operation': 0
                        }

@router.post("/")
async def post_operation_csv(session: Annotated[AsyncSession, Depends(get_async_session)]):
    stmt = insert(Operation).values(**new_operation_insert)
    print(stmt)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}