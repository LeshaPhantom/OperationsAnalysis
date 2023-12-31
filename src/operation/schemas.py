import decimal
from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, field_validator


class OperationSchema(BaseModel):
    data_time_operation: datetime
    data_payment: date
    card_number: str
    status_operation:  bool
    sum_operation: decimal.Decimal
    currency_operation: str
    sum_payment: decimal.Decimal
    currency_payment: str
    cashback: int
    category: str
    mss: int
    description: str
    bonus_cashback: decimal.Decimal
    rounding_invest: decimal.Decimal
    rounding_operation: decimal.Decimal

    class Config:
        from_attributes = True

    @field_validator('cashback', 'mss', mode='before')
    @classmethod
    def validator(cls, v):
        if v == '':
            return 0
        return v

key = [
        'data_time_operation',
        'data_payment',
        'card_number',
        'status_operation',
        'sum_operation',
        'currency_operation',
        'sum_payment',
        'currency_payment',
        'cashback',
        'category',
        'mss',
        'description',
        'bonus_cashback',
        'rounding_invest',
        'rounding_operation',
    ]
