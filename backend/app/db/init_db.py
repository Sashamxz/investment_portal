from engine import Base, engine
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create database tables
def init_db() -> None:
    Base.metadata.create_all(bind=engine)


# Dependency
def get_db() -> object | None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
