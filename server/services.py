from sqlalchemy.orm import Session
from server.schema.task_schema import (
    CreateTask,
    Task,
    ListTask,
    BaseTask,
    BulkTaskAdd,
    BulkTaskOut,
    BulkTaskDelete,
)
from typing import List
from server.models import tasks_model
from fastapi import status
from server.utils.custom_handler import CustomException
from sqlalchemy import delete


def service_create_task(db: Session, task: CreateTask):
    insert_task = tasks_model.Task(**task.model_dump())
    db.add(insert_task)
    db.commit()
    db.refresh(insert_task)
    return insert_task


def service_get_all_task(db: Session):
    res = db.query(tasks_model.Task).filter().all()
    if len(res) == 0:
        raise CustomException(
            status_code=status.HTTP_404_NOT_FOUND, msg="There is no task available"
        )
    tasks = ListTask(tasks=res)
    return tasks


def service_task_by_id(db: Session, id: int):
    res = db.query(tasks_model.Task).filter(tasks_model.Task.id == id).first()
    if res is None:
        raise CustomException(
            status_code=status.HTTP_404_NOT_FOUND, msg="There is no task at that id"
        )
    return res


def service_delete_task_by_id(db: Session, id: int):
    res = db.query(tasks_model.Task).filter(tasks_model.Task.id == id).first()
    if res is None:
        raise CustomException(
            status_code=status.HTTP_404_NOT_FOUND, msg="There is no task at that id"
        )
    db.delete(res)
    db.commit()
    return None


def service_edit_task(db: Session, id: int, task: BaseTask):
    res: Task = service_task_by_id(db, id)
    if task.title is not None:
        res.title = task.title
    if task.is_completed is not None:
        res.is_completed = task.is_completed
    db.commit()
    db.refresh(res)
    return None


def service_bulk_add_tasks(db: Session, tasks: BulkTaskAdd):
    list_of_task = [tasks_model.Task(**task.model_dump()) for task in tasks]
    db.add_all(list_of_task)
    db.commit()
    tasks = BulkTaskOut(tasks=list_of_task)
    return tasks


def service_bulk_task_delete(db: Session, tasks: BulkTaskDelete):
    statement = delete(tasks_model.Task).where(
        tasks_model.Task.id.in_([task.id for task in tasks.tasks])
    )
    db.execute(statement)
    db.commit()
    return None
