from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, Query, status, HTTPException, Depends
from typing import Annotated
from dto import Status, TaskResponse, TaskCreate, TaskUpdate

from db import get_session
from models import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    session: Annotated[Session, Depends(get_session)],
    task_status: Annotated[Status | None, Query()] = None,
):
    stmt = select(Task)
    if task_status is not None:
        stmt = stmt.where(Task.status == task_status)
    return session.execute(stmt).scalars().all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, session: Annotated[Session, Depends(get_session)]):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id `{task_id}` not found.",
        )
    return task


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskResponse)
def create_task(
    to_create: TaskCreate, session: Annotated[Session, Depends(get_session)]
):
    task = Task(
        title=to_create.title,
        description=to_create.description,
        status=to_create.status,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_status(
    task_id: int,
    to_update: TaskUpdate,
    session: Annotated[Session, Depends(get_session)],
):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id `{task_id}` not found.",
        )
    for field, value in to_update.model_dump(exclude_unset=True).items():
        setattr(task, field, value)

    session.commit()
    session.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    session: Annotated[Session, Depends(get_session)],
):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id `{task_id}` not found.",
        )
    session.delete(task)
    session.commit()
