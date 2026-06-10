import datetime
from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dto import Status


class Base(DeclarativeBase): ...


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    status: Mapped[Status] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
    )

    def __repr__(self):
        return f"Task(id={self.id!r}, title={self.title!r}, description={self.description!r}, status={self.status!r}, created_at={self.created_at!r})"
