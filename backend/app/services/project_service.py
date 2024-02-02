from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.project import Project, ProjectCreate, ProjectInfo


def create_project(db: Session, project: ProjectCreate) -> Project:
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_project_info(db: Session, project_id: int) -> ProjectInfo:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    total_investment = project.total_investment
    target_investment = project.target_investment
    percentage_completed = (total_investment / target_investment) * 100

    project_info = ProjectInfo(
        total_investment=total_investment,
        percentage_completed=percentage_completed,
    )

    return project_info
