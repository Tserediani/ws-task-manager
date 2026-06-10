import datetime
from pydantic import BaseModel
from enum import StrEnum


class Status(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskBase(BaseModel):
    title: str
    description: str


class TaskCreate(TaskBase):
    status: Status = Status.TODO


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: Status | None = None


class TaskResponse(TaskBase):
    id: int
    status: Status
    created_at: datetime.datetime
