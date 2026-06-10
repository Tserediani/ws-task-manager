from fastapi import APIRouter, Query, status, HTTPException

from typing import Annotated, Any

router = APIRouter(prefix="/tasks")


@router.get("/")
def get_tasks(task_status: Annotated[Any | None, Query()] = None):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.get("/{task_id}")
def get_task(task_id: int) -> Any:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(to_create: Any) -> Any:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.put("/{task_id}")
def update_status(task_id: int, to_update: Any) -> Any:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
