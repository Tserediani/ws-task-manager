from fastapi import APIRouter, Query, status, HTTPException
from typing import Annotated
from dto import Status, TaskResponse, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
def get_tasks(
    task_status: Annotated[Status | None, Query()] = None,
) -> list[TaskResponse]:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=f"{task_status=}"
    )


@router.get("/{task_id}")
def get_task(task_id: int) -> TaskResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=f"{task_id=}"
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(to_create: TaskCreate) -> TaskResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=f"{to_create=}"
    )


@router.put("/{task_id}")
def update_status(task_id: int, to_update: TaskUpdate) -> TaskResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=f"{task_id=}, {to_update=}"
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=f"{task_id=}"
    )
