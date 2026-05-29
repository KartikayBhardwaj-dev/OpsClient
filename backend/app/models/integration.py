from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base


class Integration(Base):

    __tablename__ = "integrations"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int]

    provider: Mapped[str] = mapped_column(
        String
    )

    access_token: Mapped[str] = mapped_column(
        String
    )

    refresh_token: Mapped[str] = mapped_column(
        String
    )

    is_active: Mapped[bool] = mapped_column(
        default=True
    )