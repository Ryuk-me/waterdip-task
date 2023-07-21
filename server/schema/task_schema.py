from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class CreateTask(BaseModel):
    title: str
    model_config = ConfigDict(json_schema_extra={"title": "string"})


class BaseTask(BaseModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskOut(BaseModel):
    id: int
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        from_attributes=True,
        populate_by_name=True,
    )


class Task(BaseTask, TaskOut):
    pass


class BulkTaskDelete(BaseModel):
    tasks: List[TaskOut]


class BulkTaskAdd(BaseTask):
    tasks: List[BaseTask]


class BulkTaskOut(BaseModel):
    tasks: List[TaskOut]


class ListTask(BaseModel):
    tasks: List[Task]
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        from_attributes=True,
        populate_by_name=True,
        json_schema_extra={
            "tasks": [{"id": "string", "title": "string", "is_completed": False}]
        },
    )
