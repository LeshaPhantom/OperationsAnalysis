from sqlalchemy import String, MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.operation.schemas import OperationSchema

metadata = MetaData()
class Base(DeclarativeBase):
    metadata = metadata


# an example mapping using the base
class Operation(Base):
    __tablename__ = "operation"

    id: Mapped[int] = mapped_column(primary_key=True)
    # id операции.

    data_time_operation: Mapped[str] = mapped_column(String(20))
    # Дата и время операции не больше 20 символов. Пример "28.08.2023 14:55:28"

    data_payment: Mapped[str] = mapped_column(String(10))
    # Дата платежа не более 10. Пример "28.08.2023"

    card_number: Mapped[str] = mapped_column(String(5))
    # Номер карты. Пример *0476

    status_operation: Mapped[bool] = mapped_column(default=True)
    # Статус операции. True|False. По умолчанию True. В файле "OK"

    sum_operation: Mapped[str] = mapped_column(String(30))
    # Сумма операций. Ограничение на 30 символов.

    currency_operation: Mapped[str] = mapped_column(String(10))
    # Валюта операции. Желательно сделать выборку.

    sum_payment: Mapped[str] = mapped_column(String(30))
    # Сумма платежа. Ограничение на 30 символов.(неизвестно отличие платежа от операции)

    currency_payment: Mapped[str] = mapped_column(String(10))
    # Валюта платежа. Желательно сделать выборку.

    cashback: Mapped[int]
    # Кэшбэк. Целое число.

    category: Mapped[str] = mapped_column(String(30))
    # Название категории

    mss: Mapped[int]
    # МСС всегда 4 цифры.

    description: Mapped[str] = mapped_column(String(30))
    # Описание операции.

    bonus_cashback: Mapped[str] = mapped_column(String(30))
    # Сумма бонусов (Включая кэшбэк).

    rounding_invest: Mapped[str] = mapped_column(String(30))
    # Округление на инвесткопилку

    rounding_operation: Mapped[int]
    # Сумма операции с округлением

    def to_read_model(self) -> OperationSchema:
        return OperationSchema(
            id=self.id,
            data_time_operation=self.data_time_operation,
            data_payment=self.data_payment,
            card_number=self.card_number,
            status_operation=self.status_operation,
            sum_operation=self.sum_operation,
            currency_operation=self.currency_operation,
            sum_payment=self.sum_payment,
            currency_payment=self.currency_payment,
            cashback=self.cashback,
            category=self.category,
            mss=self.mss,
            description=self.description,
            bonus_cashback=self.bonus_cashback,
            rounding_invest=self.rounding_invest,
            rounding_operation=self.rounding_operation,
        )
