from __future__ import annotations

from pydantic import BaseModel
from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.engine import Base


class InvestmentBase(BaseModel):
    amount: float


class Investment(InvestmentBase, Base):
    __tablename__ = "investments"

    id_ = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="investments")


class InvestmentCreate(BaseModel):
    amount: float
