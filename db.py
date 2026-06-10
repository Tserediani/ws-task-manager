from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from typing import Generator


from models import Base

engine = create_engine("sqlite:///database.db")
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

Base.metadata.create_all(bind=engine)


def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
