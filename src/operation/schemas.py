from pydantic import BaseModel

class OperationReadSchema(BaseModel):
    id: int
    data_time_operation: str
    data_payment: str
    card_number: str
    status_operation: bool
    sum_operation: str
    currency_operation: str
    sum_payment: str
    currency_payment: str
    cashback: int
    category: str
    mss: int
    description: str
    bonus_cashback: str
    rounding_invest: str
    rounding_operation: int

    class Config:
        from_attributes = True

class MytestSchema(BaseModel):
    id: int
    name: int

    class Config:
        from_attributes = True
