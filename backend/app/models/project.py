from decimal import Decimal

from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship

from app.db.engine import Base


class ProjectBase(BaseModel):
    name: str
    min_investment: Decimal
    investment_target: Decimal


class ProjectCreate(BaseModel):
    name: str
    target_investment: float


class ProjectInfo(BaseModel):
    total_investment: float
    percentage_completed: float


class Project(ProjectBase, Base):
    __tablename__ = "projects"

    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    target_investment = Column(Float)
    total_investment = Column(Float, default=0.0)
    investments = relationship("Investment", back_populates="project")
