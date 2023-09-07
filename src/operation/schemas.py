from pydantic import BaseModel

class OperationSchema(BaseModel):
    id: int
    data_time_operation: str
    data_payment: str
    card_number: str
    status_operation: str
    sum_operation: str
    currency_operation: str
    sum_payment: str
    currency_payment: str
    cashback: str
    category: str
    mss: str
    description: str
    bonus_cashback: str
    rounding_invest: str
    rounding_operation: str

    class Config:
        from_attributes = True


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
