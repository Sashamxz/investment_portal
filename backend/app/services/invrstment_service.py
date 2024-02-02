from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.investment import Investment, InvestmentCreate
from app.models.project import Project


def create_investment(
    db: Session,
    project_id: int,
    investment: InvestmentCreate,
) -> Investment:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    new_investment = Investment(**investment.dict(), project_id=project_id)
    project.total_investment += new_investment.amount

    db.add(new_investment)
    db.commit()
    db.refresh(new_investment)

    return new_investment
