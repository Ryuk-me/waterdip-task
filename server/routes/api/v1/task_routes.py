from fastapi import APIRouter, status, Depends
from fastapi.requests import Request
from typing import Union
from server.schema.task_schema import (
    TaskOut,
    CreateTask,
    ListTask,
    Task,
    BaseTask,
    BulkTaskAdd,
    BulkTaskOut,
    BulkTaskDelete,
)
from server.database import get_db
from sqlalchemy.orm import Session
from server.services import (
    service_create_task,
    service_get_all_task,
    service_task_by_id,
    service_delete_task_by_id,
    service_edit_task,
    service_bulk_add_tasks,
    service_bulk_task_delete,
)

router = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=Union[TaskOut, BulkTaskOut]
)
async def create_task(
    req: Request, task: Union[CreateTask, BulkTaskAdd], db: Session = Depends(get_db)
):
    if task.title is None:
        return service_bulk_add_tasks(db, task.tasks)
    return service_create_task(db, task)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def bulk_delete_task(
    req: Request, task: BulkTaskDelete, db: Session = Depends(get_db)
):
    return service_bulk_task_delete(db, task)


@router.get("/", status_code=status.HTTP_200_OK, response_model=ListTask)
async def get_all_tasks(req: Request, db: Session = Depends(get_db)):
    tasks = service_get_all_task(db)
    return tasks


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Task)
async def get_task(id: str, db: Session = Depends(get_db)):
    return service_task_by_id(db, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: str, db: Session = Depends(get_db)):
    return service_delete_task_by_id(db, id)


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_task(id: str, task: BaseTask, db: Session = Depends(get_db)):
    return service_edit_task(db, id, task)
